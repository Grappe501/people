/**
 * Validate Volume 8 technical domain specification packaging.
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
  "docs/volumes/volume-08-technical-specifications/VOLUME_08_TECHNICAL_DOMAIN_SPECIFICATIONS.md";
const DOMAIN_REG = "data/documentation/volume_08_domain_registry.json";
const RULE_REG = "data/documentation/volume_08_rule_registry.json";
const SCHEMA = "contracts/documentation/domain_specification.schema.json";
const POINTER =
  "docs/09_technical_specifications/VOLUME_08_TECHNICAL_DOMAIN_SPECIFICATIONS.md";

console.log("People Volume 8 Validation\n");

for (const rel of [VOL, DOMAIN_REG, RULE_REG, SCHEMA, POINTER]) {
  if (!exists(rel)) fail(`Missing required file: ${rel}`);
}

if (failures.length) {
  console.log("FAIL");
  for (const f of failures) console.log(" -", f);
  process.exit(1);
}

const volText = read(VOL);
const sha = crypto.createHash("sha256").update(volText, "utf8").digest("hex");
const domainReg = readJson(DOMAIN_REG);
const ruleReg = readJson(RULE_REG);

const requiredChecks = [
  ["document id", "PEOPLE-VOLUME-08-TECHNICAL-DOMAIN-SPECIFICATIONS-1.0"],
  ["PEOPLE-INV-002", "PEOPLE-INV-002 — Unknown Is Not No"],
  ["AUTH-RULE-001", "People Intake must not allow anonymous access to protected records"],
  ["AMBIGUOUS", "AMBIGUOUS"],
  ["PROMOTION-RULE-010", "Unknown preferences must not overwrite known canonical preferences"],
  ["Scenario A", "Clean New Person"],
  ["Volume 9", "PEOPLE-VOLUME-09-DATABASE-SPECIFICATIONS-1.0"],
  ["Locked decisions header", "# 55. Locked Decisions"],
];

for (const [label, needle] of requiredChecks) {
  if (!volText.includes(needle)) fail(`Canonical volume missing ${label}: ${needle}`);
}

const globalInv = Array.from({ length: 15 }, (_, i) => `PEOPLE-INV-${String(i + 1).padStart(3, "0")}`);
for (const id of globalInv) {
  if (!volText.includes(id)) fail(`Missing global invariant ${id}`);
}

if (domainReg.contentSha256 !== sha) {
  fail(`Domain registry SHA mismatch (file=${sha} registry=${domainReg.contentSha256})`);
}
if (ruleReg.contentSha256 !== sha) {
  fail(`Rule registry SHA mismatch (file=${sha} registry=${ruleReg.contentSha256})`);
}

if (domainReg.documentId !== "PEOPLE-VOLUME-08-TECHNICAL-DOMAIN-SPECIFICATIONS-1.0") {
  fail("domain registry documentId incorrect");
}
if (domainReg.lockedDecisionCount !== 40) fail("lockedDecisionCount must be 40");
if (!Array.isArray(domainReg.domains) || domainReg.domains.length !== 28) {
  fail(`Expected 28 domains, found ${domainReg.domains?.length}`);
}
if (!Array.isArray(domainReg.globalInvariants) || domainReg.globalInvariants.length !== 15) {
  fail("globalInvariants must list 15 PEOPLE-INV-* ids");
}

const idRe = /([A-Z][A-Z0-9]+-(?:RULE|INV)-\d{3})/g;
const fromVol = new Set([...volText.matchAll(idRe)].map((m) => m[1]));
const fromRules = new Set(ruleReg.rules || []);
const fromInvs = new Set(ruleReg.invariants || []);

for (const id of fromRules) {
  if (!fromVol.has(id)) fail(`Rule registry lists ${id} not found in volume text`);
}
for (const id of fromInvs) {
  if (!fromVol.has(id)) fail(`Invariant registry lists ${id} not found in volume text`);
}

const pointer = read(POINTER);
if (!pointer.includes("volume-08-technical-specifications/VOLUME_08_TECHNICAL_DOMAIN_SPECIFICATIONS.md")) {
  fail("Legacy pointer does not reference canonical Volume 8 path");
}

if ((ruleReg.rules?.length || 0) < 200) {
  warn(`Rule count seems low: ${ruleReg.rules?.length}`);
}

console.log(`Volume SHA-256: ${sha}`);
console.log(`Rules: ${ruleReg.rules.length}`);
console.log(`Invariants: ${ruleReg.invariants.length}`);
console.log(`Domains: ${domainReg.domains.length}`);
console.log(`Warnings: ${warnings}`);

if (failures.length) {
  console.log("\nFAIL");
  for (const f of failures) console.log(" -", f);
  process.exit(1);
}

console.log("\nPASS");
process.exit(0);
