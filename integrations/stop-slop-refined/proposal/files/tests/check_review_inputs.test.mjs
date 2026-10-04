import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { execFileSync, spawnSync } from "node:child_process";
import { cp, mkdtemp, readFile, rm, symlink, writeFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";
import { checkReviewInputs } from "../scripts/check_review_inputs.mjs";

const here = path.dirname(fileURLToPath(import.meta.url));
const fixtures = path.join(here, "fixtures", "review-inputs");
const cli = path.resolve(here, "../scripts/check_review_inputs.mjs");
const load = async name => JSON.parse(await readFile(path.join(fixtures, name), "utf8"));

async function sandbox(t) {
  const temporary = await mkdtemp(path.join(os.tmpdir(), "stop-slop-input-test-"));
  t.after(() => rm(temporary, { recursive: true, force: true }));
  const root = path.join(temporary, "inputs");
  await cp(fixtures, root, { recursive: true });
  return { root, temporary, manifest: await load("unchanged.json") };
}

test("unchanged declared source, candidate and context pass without approving prose", async () => {
  const result = await checkReviewInputs(await load("unchanged.json"), fixtures);
  assert.equal(result.status, "declared_inputs_match");
  assert.deepEqual(result.checked.map(x => x.role), ["source", "candidate", "context"]);
  assert.equal(Object.hasOwn(result, "approved"), false);
});

for (const [name, code] of [
  ["stale-candidate.json", "STALE_INPUT"],
  ["stale-context.json", "STALE_INPUT"],
  ["missing-role.json", "INVALID_MANIFEST"],
  ["invalid-file.json", "INVALID_FILE"],
]) {
  test(`public fixture ${name} is rejected`, async () => {
    await assert.rejects(checkReviewInputs(await load(name), fixtures), { code });
  });
}

test("changing only source invalidates the check", async t => {
  const { root, manifest } = await sandbox(t);
  await writeFile(path.join(root, "source.txt"), "Dispatches close at noon.\n");
  await assert.rejects(checkReviewInputs(manifest, root), { code: "STALE_INPUT" });
});

test("line endings are bytes, not normalized text", async t => {
  const { root, manifest } = await sandbox(t);
  const filename = path.join(root, "candidate.txt");
  await writeFile(filename, (await readFile(filename, "utf8")).replaceAll("\n", "\r\n"));
  await assert.rejects(checkReviewInputs(manifest, root), { code: "STALE_INPUT" });
});

test("context is optional, while source and candidate remain required", async () => {
  const manifest = await load("unchanged.json");
  manifest.inputs = manifest.inputs.filter(x => x.role !== "context");
  assert.equal((await checkReviewInputs(manifest, fixtures)).checked.length, 2);
  manifest.inputs = manifest.inputs.filter(x => x.role !== "source");
  await assert.rejects(checkReviewInputs(manifest, fixtures), { code: "INVALID_MANIFEST" });
});

test("duplicate IDs, invalid hashes, unknown roles and absent paths fail before reuse", async () => {
  for (const change of [
    m => { m.inputs[1].id = m.inputs[0].id; },
    m => { m.inputs[1].sha256 = "not-a-hash"; },
    m => { m.inputs[1].role = "approval"; },
    m => { delete m.inputs[1].path; },
  ]) {
    const manifest = await load("unchanged.json");
    change(manifest);
    await assert.rejects(checkReviewInputs(manifest, fixtures), { code: "INVALID_MANIFEST" });
  }
});

test("malformed shapes fail closed", async () => {
  for (const manifest of [null, [], {}, { version: 2, review_id: "r", inputs: [] },
    { version: 1, review_id: "r", inputs: [null] }]) {
    await assert.rejects(checkReviewInputs(manifest, fixtures), { code: "INVALID_MANIFEST" });
  }
});

test("missing file and non-directory root are rejected", async () => {
  const manifest = await load("unchanged.json");
  manifest.inputs[1].path = "absent.txt";
  await assert.rejects(checkReviewInputs(manifest, fixtures), { code: "INVALID_FILE" });
  await assert.rejects(checkReviewInputs(manifest, path.join(fixtures, "source.txt")), { code: "INVALID_ROOT" });
});

test("lexical absolute and traversal paths are refused", async () => {
  for (const filename of ["../outside.txt", "nested/../source.txt", "/etc/passwd", "C:\\outside.txt", "C:outside.txt"]) {
    const manifest = await load("unchanged.json");
    manifest.inputs[1].path = filename;
    await assert.rejects(checkReviewInputs(manifest, fixtures), { code: "PATH_ESCAPE" });
  }
});

test("a symlink escaping root fails even with a matching content hash", async t => {
  const { root, temporary, manifest } = await sandbox(t);
  const external = path.join(temporary, "outside.txt");
  const bytes = Buffer.from("Outside the declared input root.\n");
  await writeFile(external, bytes);
  await symlink(external, path.join(root, "escape.txt"));
  manifest.inputs[1].path = "escape.txt";
  manifest.inputs[1].sha256 = createHash("sha256").update(bytes).digest("hex");
  await assert.rejects(checkReviewInputs(manifest, root), { code: "PATH_ESCAPE" });
});

test("CLI reports matching inputs and stale failure with different exit codes", () => {
  const good = JSON.parse(execFileSync(process.execPath, [cli, "--manifest", path.join(fixtures, "unchanged.json"), "--root", fixtures], { encoding: "utf8" }));
  assert.equal(good.status, "declared_inputs_match");
  const bad = spawnSync(process.execPath, [cli, "--manifest", path.join(fixtures, "stale-context.json"), "--root", fixtures], { encoding: "utf8" });
  assert.equal(bad.status, 1);
  assert.equal(JSON.parse(bad.stderr).code, "STALE_INPUT");
  assert.equal(bad.stdout, "");
});

test("CLI rejects malformed JSON and duplicate flags", async t => {
  const { root } = await sandbox(t);
  const invalid = path.join(root, "broken.json");
  await writeFile(invalid, "{");
  const badJson = spawnSync(process.execPath, [cli, "--manifest", invalid, "--root", root], { encoding: "utf8" });
  assert.equal(badJson.status, 1);
  assert.equal(JSON.parse(badJson.stderr).code, "INVALID_MANIFEST");
  const badFlags = spawnSync(process.execPath, [cli, "--root", root, "--root", root], { encoding: "utf8" });
  assert.equal(badFlags.status, 1);
  assert.equal(JSON.parse(badFlags.stderr).code, "USAGE");
});

for (const [name, expectedStatus, code] of [
  ["unchanged.json", 0, null],
  ["stale-candidate.json", 1, "STALE_INPUT"],
  ["malformed.json", 1, "INVALID_MANIFEST"],
]) {
  test(`symlink CLI invocation checks ${name}, with and without preserved main symlink`, async t => {
    const { root, temporary } = await sandbox(t);
    const alias = path.join(temporary, "checker-alias.mjs");
    await symlink(cli, alias);
    if (name === "malformed.json") await writeFile(path.join(root, name), "{");
    for (const flags of [[], ["--preserve-symlinks-main"]]) {
      const result = spawnSync(process.execPath, [...flags, alias, "--manifest", path.join(root, name), "--root", root], { encoding: "utf8" });
      assert.equal(result.status, expectedStatus);
      if (expectedStatus === 0) {
        assert.equal(JSON.parse(result.stdout).status, "declared_inputs_match");
        assert.equal(result.stderr, "");
      } else {
        assert.equal(JSON.parse(result.stderr).code, code);
        assert.equal(result.stdout, "");
      }
    }
  });
}
