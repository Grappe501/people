/**
 * Validate Volume 10 API specification packaging.
 * Ensures documentation-only posture (no handlers/framework code).
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
  "docs/volumes/volume-10-api-specifications/VOLUME_10_API_SPECIFICATIONS.md";
const ENDPOINT_REG = "data/documentation/volume_10_endpoint_registry.json";
const SCHEMA = "contracts/documentation/api_endpoint_registry.schema.json";
const POINTER = "docs/11_api_specifications/VOLUME_10_API_SPECIFICATIONS.md";

console.log("People Volume 10 Validation\n");

for (const rel of [VOL, ENDPOINT_REG, SCHEMA, POINTER]) {
  if (!exists(rel)) fail(`Missing required file: ${rel}`);
}

if (failures.length) {
  console.log("FAIL");
  for (const f of failures) console.log(" -", f);
  process.exit(1);
}

const volText = read(VOL);
const sha = crypto.createHash("sha256").update(volText, "utf8").digest("hex");
const reg = readJson(ENDPOINT_REG);

const requiredChecks = [
  ["document id", "PEOPLE-VOLUME-10-API-SPECIFICATIONS-1.0"],
  ["api prefix", "/api/v1/"],
  ["API-PRINCIPLE-001", "API-PRINCIPLE-001 — Contract Before Code"],
  ["session", "GET /api/v1/session"],
  ["claim", "POST /api/v1/queue/{id}/claim"],
  ["submit", "POST /api/v1/pages/{id}/submit"],
  ["match resolutions", "POST /api/v1/match-resolutions"],
  ["promotions", "POST /api/v1/promotions"],
  ["CLAIM_ALREADY_HELD", "CLAIM_ALREADY_HELD"],
  ["STALE_VERSION", "STALE_VERSION"],
  ["canonical ops", "findCandidates()"],
  ["Volume 11 next", "PEOPLE-VOLUME-11-USER-INTERFACE-SPECIFICATIONS-1.0"],
  ["no handlers posture", "No route handlers"],
];

for (const [label, needle] of requiredChecks) {
  if (!volText.includes(needle)) fail(`Canonical volume missing ${label}: ${needle}`);
}

for (let i = 1; i <= 5; i++) {
  const id = `API-PRINCIPLE-${String(i).padStart(3, "0")}`;
  if (!volText.includes(id)) fail(`Missing principle ${id}`);
}

if (reg.contentSha256 !== sha) {
  fail(`Endpoint registry SHA mismatch (file=${sha} registry=${reg.contentSha256})`);
}
if (reg.apiPrefix !== "/api/v1/") fail("apiPrefix must be /api/v1/");
if (reg.lockedDecisionCount !== 20) fail("lockedDecisionCount must be 20");
if (!Array.isArray(reg.endpoints) || reg.endpoints.length < 40) {
  fail(`Expected >=40 endpoints, found ${reg.endpoints?.length}`);
}
if (reg.endpointCount !== reg.endpoints.length) {
  fail("endpointCount does not match endpoints array length");
}

for (const ep of reg.endpoints) {
  const marker = `${ep.method} ${ep.path}`;
  if (!volText.includes(marker)) fail(`Endpoint not documented: ${marker}`);
}

for (const code of reg.errorCodes || []) {
  if (!volText.includes(code)) fail(`Error code not in volume: ${code}`);
}

const pointer = read(POINTER);
if (!pointer.includes("volume-10-api-specifications/VOLUME_10_API_SPECIFICATIONS.md")) {
  fail("Legacy pointer does not reference canonical Volume 10 path");
}

// Documentation-only posture
if (exists("src") && fs.readdirSync(abs("src")).length) {
  fail("src/ must remain empty/absent during Volume 10 documentation build");
}
if (exists("api") && fs.readdirSync(abs("api")).length) {
  fail("api/ must remain empty/absent during Volume 10 documentation build");
}
if (exists("netlify/functions") && fs.readdirSync(abs("netlify/functions")).length) {
  fail("netlify/functions/ must remain empty/absent during Volume 10 documentation build");
}

console.log(`Volume SHA-256: ${sha}`);
console.log(`Endpoints: ${reg.endpoints.length}`);
console.log(`Error codes: ${reg.errorCodes.length}`);
console.log(`Principles: ${reg.principles.length}`);
console.log(`Warnings: ${warnings}`);

if (failures.length) {
  console.log("\nFAIL");
  for (const f of failures) console.log(" -", f);
  process.exit(1);
}

console.log("\nPASS");
process.exit(0);
