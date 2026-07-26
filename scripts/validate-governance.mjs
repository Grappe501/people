#!/usr/bin/env node
/**
 * Governance documentation validator for People Intake.
 * Documentation tooling only — not application code.
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, "..");
const reportPath = path.join(root, "reports", "PEOPLE_GOVERNANCE_VALIDATION_REPORT.md");

const lines = [];
const failures = [];
const warnings = [];

function note(msg) {
  lines.push(msg);
}
function fail(msg) {
  failures.push(msg);
  lines.push(`- FAIL: ${msg}`);
}
function warn(msg) {
  warnings.push(msg);
  lines.push(`- WARNING: ${msg}`);
}
function pass(msg) {
  lines.push(`- PASS: ${msg}`);
}

function exists(rel) {
  return fs.existsSync(path.join(root, rel));
}

function read(rel) {
  return fs.readFileSync(path.join(root, rel), "utf8");
}

function parseJson(rel) {
  try {
    return JSON.parse(read(rel));
  } catch (err) {
    fail(`JSON parse failed for ${rel}: ${err.message}`);
    return null;
  }
}

note("# People Intake — Governance Validation Report");
note("");
note(`Generated: ${new Date().toISOString()}`);
note("");
note("## Results");
note("");

const rootLower = path.resolve(root).toLowerCase();
if (!rootLower.startsWith("h:\\people")) {
  fail(`Root is not H:\\people (resolved ${path.resolve(root)})`);
} else {
  pass("Root is under H:\\people");
}

const requiredDirs = [
  "docs/00_governance",
  "docs/01_product",
  "docs/02_workflows",
  "docs/03_ux",
  "docs/04_data",
  "docs/05_security",
  "docs/06_engineering",
  "docs/07_quality",
  "docs/08_implementation",
  "contracts/documentation",
  "contracts/governance",
  "contracts/schemas",
  "scripts",
  "reports",
  "develop_notes",
  "diagrams",
];

for (const d of requiredDirs) {
  if (exists(d)) pass(`Directory exists: ${d}`);
  else fail(`Missing directory: ${d}`);
}

const requiredDocs = [
  "docs/00_governance/PEOPLE_INTAKE_MASTER_BUILD_PLAN.md",
  "docs/01_product/PEOPLE_INTAKE_PRODUCT_CHARTER.md",
  "docs/00_governance/PEOPLE_INTAKE_SCOPE_AND_BOUNDARIES.md",
  "docs/00_governance/PEOPLE_INTAKE_H_DRIVE_PROTOCOL.md",
  "docs/00_governance/PEOPLE_INTAKE_DESIGN_BEFORE_CODE_PROTOCOL.md",
  "docs/00_governance/PEOPLE_INTAKE_SOURCE_OF_TRUTH_REGISTRY.md",
  "docs/00_governance/PEOPLE_INTAKE_DECISION_LOG.md",
  "docs/00_governance/PEOPLE_INTAKE_GLOSSARY.md",
  "docs/08_implementation/PEOPLE_INTAKE_CURSOR_EXECUTION_PROTOCOL.md",
  "docs/08_implementation/PEOPLE_INTAKE_BUILD_GATES.md",
  "docs/08_implementation/PEOPLE_INTAKE_PROGRESS_LEDGER.md",
  "README.md",
  "develop_notes/PEOPLE_GOVERNANCE_FOUNDATION_CLOSEOUT.md",
  "develop_notes/NEXT_CURSOR_BUILD.md",
];

for (const doc of requiredDocs) {
  if (exists(doc)) pass(`Document exists: ${doc}`);
  else fail(`Missing document: ${doc}`);
}

const headingChecks = [
  ["docs/00_governance/PEOPLE_INTAKE_MASTER_BUILD_PLAN.md", ["Governing Vision", "H-Drive", "Design Freeze", "Definition of Done"]],
  ["docs/00_governance/PEOPLE_INTAKE_H_DRIVE_PROTOCOL.md", ["Authorized Root", "Prohibited Drive", "Permanent Rule"]],
  ["docs/00_governance/PEOPLE_INTAKE_DESIGN_BEFORE_CODE_PROTOCOL.md", ["Design Sequence", "Prohibited Before Design Freeze"]],
  ["docs/08_implementation/PEOPLE_INTAKE_CURSOR_EXECUTION_PROTOCOL.md", ["Hard Stops", "Start-of-Run"]],
  ["docs/08_implementation/PEOPLE_INTAKE_BUILD_GATES.md", ["Gate G-1", "Gate G-10"]],
];

for (const [rel, headings] of headingChecks) {
  if (!exists(rel)) continue;
  const text = read(rel);
  for (const h of headings) {
    if (text.includes(h)) pass(`${rel} contains heading/marker: ${h}`);
    else fail(`${rel} missing required heading/marker: ${h}`);
  }
}

const active = parseJson("contracts/governance/active-build.json");
if (active) {
  if (active.applicationCodeAuthorized === false) pass("active-build prohibits application code");
  else fail("active-build must set applicationCodeAuthorized=false");
  if (active.databaseChangesAuthorized === false) pass("active-build prohibits database changes");
  else fail("active-build must set databaseChangesAuthorized=false");
  if (active.nextRecommendedBuild === "PEOPLE-WORKFLOW-UX-DESIGN-1.0") {
    pass("nextRecommendedBuild is PEOPLE-WORKFLOW-UX-DESIGN-1.0");
  } else {
    fail(`Unexpected nextRecommendedBuild: ${active.nextRecommendedBuild}`);
  }
  if (String(active.projectRoot).toLowerCase().includes("h:\\people") || String(active.projectRoot).toLowerCase().includes("h:/people")) {
    pass("active-build projectRoot is H:\\people");
  } else {
    fail(`active-build projectRoot unexpected: ${active.projectRoot}`);
  }
}

const phaseReg = parseJson("contracts/governance/build-phase-registry.json");
if (phaseReg && Array.isArray(phaseReg.phases)) {
  pass(`build-phase-registry has ${phaseReg.phases.length} phases`);
} else if (phaseReg) {
  fail("build-phase-registry missing phases array");
}

const schemas = [
  "contracts/schemas/governance-document.schema.json",
  "contracts/schemas/decision-record.schema.json",
  "contracts/schemas/build-phase.schema.json",
];
for (const s of schemas) {
  if (parseJson(s)) pass(`Schema parses: ${s}`);
}

const index = parseJson("contracts/documentation/documentation-index.json");
if (index) {
  if (!Array.isArray(index.documents) || index.documents.length !== 60) {
    fail(`documentation-index must list 60 documents (found ${index.documents?.length})`);
  } else {
    pass("documentation-index lists 60 documents");
  }
  for (const doc of index.documents || []) {
    if (doc.status === "draft_complete" || doc.status === "approved" || doc.status === "frozen") {
      if (!exists(doc.path)) fail(`Indexed complete doc missing file: ${doc.path}`);
      else pass(`Indexed complete doc exists: ${doc.path}`);
    }
  }
}

if (exists("docs/00_governance/PEOPLE_INTAKE_DECISION_LOG.md")) {
  const decisionText = read("docs/00_governance/PEOPLE_INTAKE_DECISION_LOG.md");
  const ids = [...decisionText.matchAll(/### (D-\d{3})/g)].map((m) => m[1]);
  const unique = new Set(ids);
  if (ids.length < 20) fail(`Expected at least 20 seeded decisions, found ${ids.length}`);
  else pass(`Seeded decisions found: ${ids.length}`);
  if (unique.size !== ids.length) fail("Duplicate decision IDs detected");
  else pass("Decision IDs are unique");
}

const prohibited = [
  "src",
  "app",
  "pages",
  "api",
  "prisma",
  "migrations",
  "components",
  "public",
  "netlify/functions",
];
for (const p of prohibited) {
  if (exists(p)) fail(`Prohibited implementation path exists: ${p}`);
  else pass(`Prohibited path absent: ${p}`);
}

const result =
  failures.length === 0
    ? warnings.length
      ? "PASS_WITH_WARNINGS"
      : "PASS"
    : "FAIL";

note("");
note(`## Final Result: ${result}`);
note("");
note(`Failures: ${failures.length}`);
note(`Warnings: ${warnings.length}`);

fs.mkdirSync(path.dirname(reportPath), { recursive: true });
fs.writeFileSync(reportPath, lines.join("\n") + "\n", "utf8");
console.log(lines.join("\n"));
process.exit(failures.length ? 1 : 0);
