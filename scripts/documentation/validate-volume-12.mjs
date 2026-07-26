/**
 * Validate Volume 12 component library packaging.
 * Ensures documentation-only posture (no React/CSS/Storybook).
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
  "docs/volumes/volume-12-component-library/VOLUME_12_COMPONENT_LIBRARY_AND_DESIGN_SYSTEM.md";
const COMP_REG = "data/documentation/volume_12_component_registry.json";
const SCHEMA = "contracts/documentation/component_registry.schema.json";
const POINTER =
  "docs/13_component_library/VOLUME_12_COMPONENT_LIBRARY_AND_DESIGN_SYSTEM.md";

console.log("People Volume 12 Validation\n");

for (const rel of [VOL, COMP_REG, SCHEMA, POINTER]) {
  if (!exists(rel)) fail(`Missing required file: ${rel}`);
}

if (failures.length) {
  console.log("FAIL");
  for (const f of failures) console.log(" -", f);
  process.exit(1);
}

const volText = read(VOL);
const sha = crypto.createHash("sha256").update(volText, "utf8").digest("hex");
const reg = readJson(COMP_REG);

const requiredChecks = [
  ["document id", "PEOPLE-VOLUME-12-COMPONENT-LIBRARY-AND-DESIGN-SYSTEM-1.0"],
  ["DESIGN-PRINCIPLE-001", "DESIGN-PRINCIPLE-001 — Clarity Before Decoration"],
  ["PreferenceControl", "PreferenceControl"],
  ["Unknown lock", "Unknown is never silently converted to No"],
  ["EntryGrid", "EntryGrid"],
  ["CandidateCard", "CandidateCard"],
  ["WCAG", "WCAG 2.2 AA"],
  ["COMP-DEC-001", "COMP-DEC-001"],
  ["COMP-DEC-025", "COMP-DEC-025"],
  ["Volume 13 next", "PEOPLE-VOLUME-13-CANONICAL-PLATFORM-STANDARDS-1.0"],
  ["no React posture", "No React components"],
];

for (const [label, needle] of requiredChecks) {
  if (!volText.includes(needle)) fail(`Canonical volume missing ${label}: ${needle}`);
}

for (let i = 1; i <= 10; i++) {
  const id = `DESIGN-PRINCIPLE-${String(i).padStart(3, "0")}`;
  if (!volText.includes(id)) fail(`Missing principle ${id}`);
}
for (let i = 1; i <= 25; i++) {
  const id = `COMP-DEC-${String(i).padStart(3, "0")}`;
  if (!volText.includes(id)) fail(`Missing deferred decision ${id}`);
}

if (reg.contentSha256 !== sha) {
  fail(`Component registry SHA mismatch (file=${sha} registry=${reg.contentSha256})`);
}
if (reg.lockedDecisionCount !== 50) fail("lockedDecisionCount must be 50");
if (!Array.isArray(reg.components) || reg.components.length < 80) {
  fail(`Expected >=80 components, found ${reg.components?.length}`);
}
if (reg.componentCount !== reg.components.length) {
  fail("componentCount does not match components array length");
}

for (const c of reg.components) {
  if (!volText.includes(c.componentName)) fail(`Component not documented: ${c.componentName}`);
}

const pointer = read(POINTER);
if (!pointer.includes("volume-12-component-library/VOLUME_12_COMPONENT_LIBRARY_AND_DESIGN_SYSTEM.md")) {
  fail("Legacy pointer does not reference canonical Volume 12 path");
}

for (const forbidden of ["components", "src", "app", "pages"]) {
  if (exists(forbidden) && fs.readdirSync(abs(forbidden)).length) {
    fail(`${forbidden}/ must remain empty/absent during Volume 12 documentation build`);
  }
}

console.log(`Volume SHA-256: ${sha}`);
console.log(`Components: ${reg.components.length}`);
console.log(`Principles: ${reg.principles.length}`);
console.log(`Deferred decisions: ${reg.deferredDecisions.length}`);
console.log(`Warnings: ${warnings}`);

if (failures.length) {
  console.log("\nFAIL");
  for (const f of failures) console.log(" -", f);
  process.exit(1);
}

console.log("\nPASS");
process.exit(0);
