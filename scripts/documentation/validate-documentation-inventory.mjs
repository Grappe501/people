/**
 * Validate documentation inventory — DOC-0 Cursor-ready spec.
 */
import fs from "fs";
import path from "path";

const ROOT = "H:\\people";
let documentsChecked = 0;
let canonicalDocs = 0;
let plannedDocs = 0;
let duplicateIds = 0;
let duplicatePaths = 0;
let missingFiles = 0;
let invalidRecords = 0;
let warnings = 0;
const failures = [];

function fail(msg) {
  failures.push(msg);
  invalidRecords++;
}
function warn(msg) {
  warnings++;
  console.log("WARN:", msg);
}

function exists(rel) {
  return fs.existsSync(path.join(ROOT, rel));
}

function parseJson(rel) {
  try {
    return JSON.parse(fs.readFileSync(path.join(ROOT, rel), "utf8"));
  } catch (e) {
    fail(`JSON parse ${rel}: ${e.message}`);
    return null;
  }
}

function underPeople(rel) {
  const resolved = path.resolve(ROOT, rel);
  const root = path.resolve(ROOT);
  return resolved.toLowerCase().startsWith(root.toLowerCase());
}

console.log("People Documentation Inventory Validation\n");

if (!exists("data/documentation/document_inventory.json")) {
  fail("document_inventory.json missing");
}

const inv = parseJson("data/documentation/document_inventory.json");
const STATUS = new Set([
  "PLANNED",
  "PARTIAL",
  "DRAFT",
  "READY_FOR_REVIEW",
  "APPROVED",
  "FROZEN",
  "SUPERSEDED",
  "DUPLICATE",
  "ARCHIVED",
  "UNKNOWN",
]);
const TYPES = new Set([
  "volume",
  "standard",
  "catalog",
  "register",
  "report",
  "runbook",
  "decision",
  "risk",
  "diagram",
  "template",
  "working_note",
  "implementation_package",
  "unknown",
]);

if (inv) {
  if (inv.project_root !== "H:\\people") fail(`project_root invalid: ${inv.project_root}`);
  if (inv.production_code && inv.production_code !== "PROHIBITED") fail("production_code must be PROHIBITED");
  if (!Array.isArray(inv.documents)) fail("documents must be array");
  else {
    const ids = new Set();
    const paths = new Set();
    const hashes = new Map();
    for (const d of inv.documents) {
      documentsChecked++;
      if (!d.document_id || !/^PEOPLE-DOC-\d{4}$/.test(d.document_id)) fail(`bad document_id: ${d.document_id}`);
      if (ids.has(d.document_id)) {
        duplicateIds++;
        fail(`duplicate document_id ${d.document_id}`);
      }
      ids.add(d.document_id);
      if (!TYPES.has(d.document_type)) fail(`${d.document_id} bad type ${d.document_type}`);
      if (!STATUS.has(d.status)) fail(`${d.document_id} bad status ${d.status}`);
      if (typeof d.authority_level !== "number" || d.authority_level < 1 || d.authority_level > 7)
        fail(`${d.document_id} bad authority_level`);
      if (d.volume_number != null && (d.volume_number < 0 || !Number.isInteger(d.volume_number)))
        fail(`${d.document_id} bad volume_number`);
      if (!underPeople(d.current_path) || !underPeople(d.canonical_path))
        fail(`${d.document_id} path escapes H:\\people`);
      if (paths.has(d.canonical_path)) {
        duplicatePaths++;
        fail(`duplicate canonical_path ${d.canonical_path}`);
      }
      paths.add(d.canonical_path);
      if (d.status === "PLANNED") {
        plannedDocs++;
      } else if (!exists(d.current_path)) {
        missingFiles++;
        fail(`missing file ${d.current_path}`);
      }
      if (d.is_canonical) canonicalDocs++;
      if (d.content_hash) {
        if (!hashes.has(d.content_hash)) hashes.set(d.content_hash, []);
        hashes.get(d.content_hash).push(d.document_id);
      }
      if (d.last_modified && Number.isNaN(Date.parse(d.last_modified)))
        fail(`${d.document_id} bad last_modified`);
    }
    for (const [h, list] of hashes) {
      if (list.length > 1) warn(`Exact hash duplicate group: ${list.join(", ")}`);
    }
  }
}

const term = parseJson("data/documentation/terminology_inventory.json");
let terminologyEntries = 0;
if (term?.terms) {
  terminologyEntries = term.terms.length;
  const required = ["Batch", "Page", "Entry", "Claim", "Promotion", "Canonical Person", "UNKNOWN", "Audit Event"];
  const have = new Set(term.terms.map((t) => t.canonical_term));
  for (const t of required) if (!have.has(t)) fail(`terminology missing ${t}`);
  if (!term.semantic_locks?.unknown_is_not_no) fail("semantic lock unknown_is_not_no required");
}

const map = parseJson("data/documentation/design_source_map.json");
let sourceMapEntries = 0;
if (map?.domains) sourceMapEntries = Object.keys(map.domains).length;

const requiredArts = [
  "docs/README.md",
  "docs/DOCUMENTATION_MASTER_INDEX.md",
  "docs/traceability/DESIGN_SOURCE_MAP.md",
  "docs/catalogs/terminology/TERMINOLOGY_MATRIX.md",
  "docs/catalogs/identifiers/IDENTIFIER_STANDARD.md",
  "develop_notes/PEOPLE_DOCUMENTATION_PROGRESS_LEDGER.md",
  "develop_notes/PEOPLE_OPEN_DECISIONS_REGISTER.md",
  "develop_notes/PEOPLE_CONTRADICTION_REGISTER.md",
  "develop_notes/PEOPLE_DOCUMENTATION_CHANGELOG.md",
  "develop_notes/PEOPLE_LATEST_CURSOR_REPORT.md",
  "contracts/documentation/document_inventory.schema.json",
];
for (const r of requiredArts) {
  if (!exists(r)) fail(`missing required artifact ${r}`);
}

for (const p of ["src", "app", "prisma", "migrations"]) {
  if (exists(p)) fail(`forbidden app path present: ${p}`);
}

const result = failures.length ? "FAIL" : warnings ? "PASS_WITH_WARNINGS" : "PASS";

console.log(`Documents checked: ${documentsChecked}`);
console.log(`Canonical documents: ${canonicalDocs}`);
console.log(`Planned documents: ${plannedDocs}`);
console.log(`Duplicate IDs: ${duplicateIds}`);
console.log(`Duplicate paths: ${duplicatePaths}`);
console.log(`Missing files: ${missingFiles}`);
console.log(`Invalid records: ${invalidRecords}`);
console.log(`Terminology entries: ${terminologyEntries}`);
console.log(`Source-map entries: ${sourceMapEntries}`);
console.log(`Warnings: ${warnings}`);
console.log(`Result: ${result}`);
if (failures.length) {
  console.log("\nFailures:");
  for (const f of failures) console.log("-", f);
}
process.exit(failures.length ? 1 : 0);
