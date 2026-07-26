/**
 * Validate Volume 13 canonical platform standards packaging.
 * Ensures documentation-only posture (no application implementation).
 */
import crypto from "crypto";
import fs from "fs";
import path from "path";

const ROOT = "H:\\people";
const failures = [];
let warnings = 0;

function fail(msg) {
  failures.push(msg);
}
function warn(msg) {
  warnings++;
  console.log("WARN:", msg);
}
function abs(rel) {
  return path.join(ROOT, rel);
}
function exists(rel) {
  return fs.existsSync(abs(rel));
}
function read(rel) {
  return fs.readFileSync(abs(rel), "utf8");
}
function readJson(rel) {
  return JSON.parse(read(rel));
}

const VOL =
  "docs/volumes/volume-13-platform-standards/VOLUME_13_CANONICAL_PLATFORM_STANDARDS.md";
const REG = "data/documentation/volume_13_platform_registry.json";
const SCHEMA = "contracts/documentation/platform_standards_registry.schema.json";
const POINTER =
  "docs/15_platform_standards/VOLUME_13_CANONICAL_PLATFORM_STANDARDS.md";

console.log("People Volume 13 Validation\n");

for (const rel of [VOL, REG, SCHEMA, POINTER]) {
  if (!exists(rel)) fail(`Missing required file: ${rel}`);
}

if (failures.length) {
  console.log("FAIL");
  for (const f of failures) console.log(" -", f);
  process.exit(1);
}

const volText = read(VOL);
const sha = crypto.createHash("sha256").update(volText, "utf8").digest("hex");
const reg = readJson(REG);

const requiredChecks = [
  ["document id", "PEOPLE-VOLUME-13-CANONICAL-PLATFORM-STANDARDS-1.0"],
  ["project root", "H:\\people"],
  ["locked decision 1", "Documentation-first development"],
  ["locked decision 6", "Canonical identity ownership remains outside People Intake"],
  ["locked decision 18", "Every implementation package must end with validation and documentation updates"],
  ["domain layer", "Business rules belong in the domain layer"],
  ["Volume 9 authority", "The database schema defined in Volume 9 is authoritative"],
  ["Volume 10 authority", "Volume 10 defines the canonical API"],
  ["next catalog", "PEOPLE-STATE-MACHINE-CATALOG-1.0"],
  ["no app code posture", "No application source code"],
  ["readiness", "100%"],
];

for (const [label, needle] of requiredChecks) {
  if (!volText.includes(needle)) fail(`Canonical volume missing ${label}: ${needle}`);
}

if (reg.contentSha256 !== sha) {
  fail(`Platform registry SHA mismatch (file=${sha} registry=${reg.contentSha256})`);
}
if (reg.lockedDecisionCount !== 18) fail("lockedDecisionCount must be 18");
if (reg.standardAreaCount !== 14) fail("standardAreaCount must be 14");
if (!Array.isArray(reg.nextGoverningDocuments) || reg.nextGoverningDocuments.length !== 6) {
  fail("Expected exactly 6 nextGoverningDocuments");
}
if (reg.overallReadinessPercent !== 100) fail("overallReadinessPercent must be 100");

for (const d of reg.lockedDecisions) {
  if (!volText.includes(d)) fail(`Locked decision not documented: ${d}`);
}
for (const a of reg.standardAreas) {
  if (!volText.includes(a)) fail(`Standard area not documented: ${a}`);
}

const pointer = read(POINTER);
if (!pointer.includes("volume-13-platform-standards/VOLUME_13_CANONICAL_PLATFORM_STANDARDS.md")) {
  fail("Legacy pointer does not reference canonical Volume 13 path");
}

for (const forbidden of ["src", "app", "pages", "components", "prisma", "migrations"]) {
  if (exists(forbidden) && fs.readdirSync(abs(forbidden)).length) {
    fail(`${forbidden}/ must remain empty/absent during Volume 13 documentation build`);
  }
}

console.log(`Volume SHA-256: ${sha}`);
console.log(`Standard areas: ${reg.standardAreas.length}`);
console.log(`Locked decisions: ${reg.lockedDecisions.length}`);
console.log(`Next governing documents: ${reg.nextGoverningDocuments.length}`);
console.log(`Warnings: ${warnings}`);

if (failures.length) {
  console.log("\nFAIL");
  for (const f of failures) console.log(" -", f);
  process.exit(1);
}

console.log("\nPASS");
process.exit(0);
