/**
 * Validate Volume 9 database specification packaging.
 * Ensures documentation-only posture (no migrations/Prisma in this build).
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
  "docs/volumes/volume-09-database-specifications/VOLUME_09_DATABASE_SPECIFICATIONS.md";
const TABLE_REG = "data/documentation/volume_09_table_registry.json";
const DEC_REG = "data/documentation/volume_09_decision_registry.json";
const SCHEMA = "contracts/documentation/database_table_registry.schema.json";
const POINTER =
  "docs/10_database_specifications/VOLUME_09_DATABASE_SPECIFICATIONS.md";

const FORBIDDEN_IMPL = [
  "prisma/schema.prisma",
  "migrations",
  "src",
];

console.log("People Volume 9 Validation\n");

for (const rel of [VOL, TABLE_REG, DEC_REG, SCHEMA, POINTER]) {
  if (!exists(rel)) fail(`Missing required file: ${rel}`);
}

if (failures.length) {
  console.log("FAIL");
  for (const f of failures) console.log(" -", f);
  process.exit(1);
}

const volText = read(VOL);
const sha = crypto.createHash("sha256").update(volText, "utf8").digest("hex");
const tableReg = readJson(TABLE_REG);
const decReg = readJson(DEC_REG);

const requiredChecks = [
  ["document id", "PEOPLE-VOLUME-09-DATABASE-SPECIFICATIONS-1.0"],
  ["DB-PRINCIPLE-001", "DB-PRINCIPLE-001 — Evidence Before Interpretation"],
  ["DB-PRINCIPLE-003", "Canonical Separation"],
  ["UNKNOWN preference", "No default may convert missing preference to `NO`"],
  ["application_users", "application_users"],
  ["intake_entries", "intake_entries"],
  ["promotion_requests", "promotion_requests"],
  ["audit_events", "audit_events"],
  ["append-only", "# 67. Required Append-Only Tables"],
  ["locked decisions", "# 84. Locked Decisions"],
  ["Volume 10 next", "PEOPLE-VOLUME-10-API-SPECIFICATIONS-1.0"],
  ["no migrations posture", "No SQL migrations"],
];

for (const [label, needle] of requiredChecks) {
  if (!volText.includes(needle)) fail(`Canonical volume missing ${label}: ${needle}`);
}

for (let i = 1; i <= 10; i++) {
  const id = `DB-PRINCIPLE-${String(i).padStart(3, "0")}`;
  if (!volText.includes(id)) fail(`Missing principle ${id}`);
}
for (let i = 1; i <= 15; i++) {
  const id = `DB-DEC-${String(i).padStart(3, "0")}`;
  if (!volText.includes(id)) fail(`Missing deferred decision ${id}`);
}

if (tableReg.contentSha256 !== sha) {
  fail(`Table registry SHA mismatch (file=${sha} registry=${tableReg.contentSha256})`);
}
if (decReg.contentSha256 !== sha) {
  fail(`Decision registry SHA mismatch (file=${sha} registry=${decReg.contentSha256})`);
}

if (tableReg.lockedDecisionCount !== 40) fail("lockedDecisionCount must be 40");
if (!Array.isArray(tableReg.tables) || tableReg.tables.length < 40) {
  fail(`Expected >=40 tables, found ${tableReg.tables?.length}`);
}
if (tableReg.principles?.length !== 10) fail("principles must list 10 DB-PRINCIPLE-* ids");
if (tableReg.deferredDecisions?.length !== 15) fail("deferredDecisions must list 15 DB-DEC-* ids");

for (const t of tableReg.tables) {
  if (!t.mentioned) fail(`Registry marks ${t.tableName} as not mentioned`);
  if (!volText.includes(t.tableName)) fail(`Table ${t.tableName} not found in volume text`);
}

const pointer = read(POINTER);
if (!pointer.includes("volume-09-database-specifications/VOLUME_09_DATABASE_SPECIFICATIONS.md")) {
  fail("Legacy pointer does not reference canonical Volume 9 path");
}

// Documentation-only posture: no new implementation artifacts introduced by this volume
if (exists("prisma/schema.prisma")) {
  fail("prisma/schema.prisma must not exist during Volume 9 documentation build");
}
if (exists("migrations") && fs.readdirSync(abs("migrations")).length) {
  fail("migrations/ must remain empty/absent during Volume 9 documentation build");
}

console.log(`Volume SHA-256: ${sha}`);
console.log(`Tables: ${tableReg.tables.length}`);
console.log(`Append-only: ${tableReg.appendOnlyCount}`);
console.log(`Principles: ${tableReg.principles.length}`);
console.log(`Deferred decisions: ${tableReg.deferredDecisions.length}`);
console.log(`Warnings: ${warnings}`);

if (failures.length) {
  console.log("\nFAIL");
  for (const f of failures) console.log(" -", f);
  process.exit(1);
}

console.log("\nPASS");
process.exit(0);
