/**
 * Validate Volume 11 UI specification packaging.
 * Ensures documentation-only posture (no React/CSS/route implementation).
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
  "docs/volumes/volume-11-ui-specifications/VOLUME_11_USER_INTERFACE_SPECIFICATIONS.md";
const SCREEN_REG = "data/documentation/volume_11_screen_registry.json";
const SCHEMA = "contracts/documentation/ui_screen_registry.schema.json";
const POINTER =
  "docs/12_ui_specifications/VOLUME_11_USER_INTERFACE_SPECIFICATIONS.md";

console.log("People Volume 11 Validation\n");

for (const rel of [VOL, SCREEN_REG, SCHEMA, POINTER]) {
  if (!exists(rel)) fail(`Missing required file: ${rel}`);
}

if (failures.length) {
  console.log("FAIL");
  for (const f of failures) console.log(" -", f);
  process.exit(1);
}

const volText = read(VOL);
const sha = crypto.createHash("sha256").update(volText, "utf8").digest("hex");
const reg = readJson(SCREEN_REG);

const requiredChecks = [
  ["document id", "PEOPLE-VOLUME-11-USER-INTERFACE-SPECIFICATIONS-1.0"],
  ["workspaces", "Capture\nTranscribe\nMatch\nManage"],
  ["Unknown default", "Unknown is the safe default"],
  ["autosave", "Autosave is required"],
  ["WCAG", "WCAG 2.2 AA"],
  ["Transcription Workspace", "Transcription Workspace"],
  ["Match Review Screen", "Match Review Screen"],
  ["UI-DEC-001", "UI-DEC-001"],
  ["UI-DEC-018", "UI-DEC-018"],
  ["Volume 12 next", "PEOPLE-VOLUME-12-COMPONENT-LIBRARY-AND-DESIGN-SYSTEM-1.0"],
  ["no React posture", "No React components"],
];

for (const [label, needle] of requiredChecks) {
  if (!volText.includes(needle)) fail(`Canonical volume missing ${label}: ${needle}`);
}

for (const ws of ["Capture", "Transcribe", "Match", "Manage"]) {
  if (!volText.includes(ws)) fail(`Missing workspace ${ws}`);
}

for (let i = 1; i <= 18; i++) {
  const id = `UI-DEC-${String(i).padStart(3, "0")}`;
  if (!volText.includes(id)) fail(`Missing deferred decision ${id}`);
}

if (reg.contentSha256 !== sha) {
  fail(`Screen registry SHA mismatch (file=${sha} registry=${reg.contentSha256})`);
}
if (reg.lockedDecisionCount !== 40) fail("lockedDecisionCount must be 40");
if (!Array.isArray(reg.screens) || reg.screens.length < 50) {
  fail(`Expected >=50 screens, found ${reg.screens?.length}`);
}
if (reg.screenCount !== reg.screens.length) {
  fail("screenCount does not match screens array length");
}
if (!Array.isArray(reg.workspaces) || reg.workspaces.length !== 4) {
  fail("workspaces must list Capture, Transcribe, Match, Manage");
}

for (const s of reg.screens) {
  if (!volText.includes(s.screenName)) fail(`Screen not documented: ${s.screenName}`);
}

const pointer = read(POINTER);
if (!pointer.includes("volume-11-ui-specifications/VOLUME_11_USER_INTERFACE_SPECIFICATIONS.md")) {
  fail("Legacy pointer does not reference canonical Volume 11 path");
}

// Documentation-only posture
for (const forbidden of ["components", "src", "app", "pages"]) {
  if (exists(forbidden) && fs.readdirSync(abs(forbidden)).length) {
    fail(`${forbidden}/ must remain empty/absent during Volume 11 documentation build`);
  }
}

console.log(`Volume SHA-256: ${sha}`);
console.log(`Screens: ${reg.screens.length}`);
console.log(`Workspaces: ${reg.workspaces.join(", ")}`);
console.log(`Deferred decisions: ${reg.deferredDecisions.length}`);
console.log(`Warnings: ${warnings}`);

if (failures.length) {
  console.log("\nFAIL");
  for (const f of failures) console.log(" -", f);
  process.exit(1);
}

console.log("\nPASS");
process.exit(0);
