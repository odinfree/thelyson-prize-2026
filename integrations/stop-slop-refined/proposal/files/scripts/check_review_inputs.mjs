import { createHash } from "node:crypto";
import { readFile, realpath, stat } from "node:fs/promises";
import path from "node:path";
import process from "node:process";
import { fileURLToPath } from "node:url";

export class ReviewInputError extends Error {
  constructor(code, message) {
    super(message);
    this.name = "ReviewInputError";
    this.code = code;
  }
}

function reject(code, message) {
  throw new ReviewInputError(code, message);
}

function nonemptyString(value) {
  return typeof value === "string" && value.trim().length > 0;
}

function validateManifest(manifest) {
  if (!manifest || Array.isArray(manifest) || typeof manifest !== "object") {
    reject("INVALID_MANIFEST", "manifest must be an object");
  }
  if (manifest.version !== 1 || !nonemptyString(manifest.review_id)) {
    reject("INVALID_MANIFEST", "version must be 1 and review_id must be a non-empty string");
  }
  if (!Array.isArray(manifest.inputs) || manifest.inputs.length === 0) {
    reject("INVALID_MANIFEST", "inputs must be a non-empty array");
  }
  const ids = new Set();
  const roles = new Set();
  for (const [index, input] of manifest.inputs.entries()) {
    const label = `input ${index + 1}`;
    if (!input || Array.isArray(input) || typeof input !== "object") {
      reject("INVALID_MANIFEST", `${label} must be an object`);
    }
    if (!nonemptyString(input.id) || ids.has(input.id)) {
      reject("INVALID_MANIFEST", `${label} needs a unique non-empty id`);
    }
    ids.add(input.id);
    if (!["source", "candidate", "context"].includes(input.role)) {
      reject("INVALID_MANIFEST", `${label} has an invalid role`);
    }
    roles.add(input.role);
    if (typeof input.sha256 !== "string" || !/^[a-f0-9]{64}$/.test(input.sha256)) {
      reject("INVALID_MANIFEST", `${label} needs a lowercase 64-character SHA-256`);
    }
    if (!nonemptyString(input.path) || input.path.includes("\0")) {
      reject("INVALID_MANIFEST", `${label} needs a non-empty path without NUL`);
    }
    // Require portable relative paths, before reading any declared input.
    if (path.posix.isAbsolute(input.path) || path.win32.isAbsolute(input.path) ||
        /^[A-Za-z]:/.test(input.path) || input.path.includes("\\") ||
        input.path.split("/").includes("..")) {
      reject("PATH_ESCAPE", `${label} path must be relative, without backslashes or '..'`);
    }
  }
  if (!roles.has("source") || !roles.has("candidate")) {
    reject("INVALID_MANIFEST", "inputs require at least one source and one candidate role");
  }
}

function withinRoot(root, filename) {
  const relative = path.relative(root, filename);
  return relative !== ".." && !relative.startsWith(`..${path.sep}`) && !path.isAbsolute(relative);
}

/** Checks only the declared inputs' bytes. Use a stable, trusted filesystem snapshot. */
export async function checkReviewInputs(manifest, rootPath) {
  validateManifest(manifest);
  if (!nonemptyString(rootPath)) reject("INVALID_ROOT", "root must be a directory path");
  let root;
  try {
    root = await realpath(rootPath);
    if (!(await stat(root)).isDirectory()) throw new Error("not a directory");
  } catch {
    reject("INVALID_ROOT", "root must resolve to an existing directory");
  }
  const checked = [];
  for (const input of manifest.inputs) {
    let filename;
    try {
      filename = await realpath(path.resolve(root, input.path));
    } catch {
      reject("INVALID_FILE", `input ${input.id} is missing or cannot be resolved`);
    }
    if (!withinRoot(root, filename)) {
      reject("PATH_ESCAPE", `input ${input.id} resolves outside root`);
    }
    let bytes;
    try {
      if (!(await stat(filename)).isFile()) throw new Error("not a regular file");
      bytes = await readFile(filename);
    } catch {
      reject("INVALID_FILE", `input ${input.id} is not a readable regular file`);
    }
    const actual = createHash("sha256").update(bytes).digest("hex");
    if (actual !== input.sha256) {
      reject("STALE_INPUT", `input ${input.id} (${input.role}) has changed bytes`);
    }
    checked.push({ id: input.id, role: input.role, path: input.path, sha256: actual });
  }
  return { status: "declared_inputs_match", review_id: manifest.review_id, checked };
}

const usage = "usage: node scripts/check_review_inputs.mjs --manifest review.json --root /path/to/inputs";

export async function main(args) {
  if (args.length === 1 && args[0] === "--help") {
    console.log(usage);
    return 0;
  }
  try {
    const options = new Map();
    if (args.length !== 4) reject("USAGE", usage);
    for (let i = 0; i < args.length; i += 2) {
      if (!["--manifest", "--root"].includes(args[i]) || options.has(args[i]) ||
          !args[i + 1] || args[i + 1].startsWith("--")) reject("USAGE", usage);
      options.set(args[i], args[i + 1]);
    }
    let manifest;
    try {
      manifest = JSON.parse(await readFile(options.get("--manifest"), "utf8"));
    } catch {
      reject("INVALID_MANIFEST", "manifest must be a readable JSON file");
    }
    const result = await checkReviewInputs(manifest, options.get("--root"));
    console.log(JSON.stringify(result, null, 2));
    return 0;
  } catch (error) {
    console.error(JSON.stringify({ status: "rejected", code: error.code ?? "ERROR", message: error.message }));
    return 1;
  }
}

// Node normally resolves module symlinks but leaves argv[1] as the invoked alias.
const entrypoint = process.argv[1] ? await realpath(path.resolve(process.argv[1])).catch(() => null) : null;
if (entrypoint === await realpath(fileURLToPath(import.meta.url))) {
  process.exitCode = await main(process.argv.slice(2));
}
