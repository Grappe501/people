/**
 * Validate Catalogs 0–9 (Master through Traceability foundation).
 * Documentation-only posture — no application implementation.
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
function sha(text) {
  return crypto.createHash("sha256").update(text, "utf8").digest("hex");
}

const CATS = [
  ["0", "docs/catalogs/catalog-00-master-registry/CATALOG_00_MASTER_REGISTRY.md", "data/documentation/catalog_00_master_registry.json", "contracts/documentation/catalog_master_registry.schema.json", "docs/14_engineering_catalogs/CATALOG_00_MASTER_REGISTRY.md", "catalog-00-master-registry/CATALOG_00_MASTER_REGISTRY.md"],
  ["1", "docs/catalogs/catalog-01-state-machines/CATALOG_01_STATE_MACHINES.md", "data/documentation/catalog_01_state_machine_registry.json", "contracts/documentation/state_machine_catalog_registry.schema.json", "docs/14_engineering_catalogs/CATALOG_01_STATE_MACHINES.md", "catalog-01-state-machines/CATALOG_01_STATE_MACHINES.md"],
  ["2", "docs/catalogs/catalog-02-errors/CATALOG_02_ERRORS.md", "data/documentation/catalog_02_error_registry.json", "contracts/documentation/error_catalog_registry.schema.json", "docs/14_engineering_catalogs/CATALOG_02_ERRORS.md", "catalog-02-errors/CATALOG_02_ERRORS.md"],
  ["3", "docs/catalogs/catalog-03-audit-events/CATALOG_03_AUDIT_EVENTS.md", "data/documentation/catalog_03_audit_event_registry.json", "contracts/documentation/audit_event_catalog_registry.schema.json", "docs/14_engineering_catalogs/CATALOG_03_AUDIT_EVENTS.md", "catalog-03-audit-events/CATALOG_03_AUDIT_EVENTS.md"],
  ["4", "docs/catalogs/catalog-04-configuration/CATALOG_04_CONFIGURATION.md", "data/documentation/catalog_04_configuration_registry.json", "contracts/documentation/configuration_catalog_registry.schema.json", "docs/14_engineering_catalogs/CATALOG_04_CONFIGURATION.md", "catalog-04-configuration/CATALOG_04_CONFIGURATION.md"],
  ["5", "docs/catalogs/catalog-05-permissions/CATALOG_05_PERMISSIONS.md", "data/documentation/catalog_05_permissions_registry.json", "contracts/documentation/permissions_catalog_registry.schema.json", "docs/14_engineering_catalogs/CATALOG_05_PERMISSIONS.md", "catalog-05-permissions/CATALOG_05_PERMISSIONS.md"],
  ["6", "docs/catalogs/catalog-06-notifications/CATALOG_06_NOTIFICATIONS.md", "data/documentation/catalog_06_notifications_registry.json", "contracts/documentation/notifications_catalog_registry.schema.json", "docs/14_engineering_catalogs/CATALOG_06_NOTIFICATIONS.md", "catalog-06-notifications/CATALOG_06_NOTIFICATIONS.md"],
  ["7", "docs/catalogs/catalog-07-background-jobs/CATALOG_07_BACKGROUND_JOBS.md", "data/documentation/catalog_07_background_jobs_registry.json", "contracts/documentation/background_jobs_catalog_registry.schema.json", "docs/14_engineering_catalogs/CATALOG_07_BACKGROUND_JOBS.md", "catalog-07-background-jobs/CATALOG_07_BACKGROUND_JOBS.md"],
  ["8", "docs/catalogs/catalog-08-data-retention/CATALOG_08_DATA_RETENTION.md", "data/documentation/catalog_08_data_retention_registry.json", "contracts/documentation/data_retention_catalog_registry.schema.json", "docs/14_engineering_catalogs/CATALOG_08_DATA_RETENTION.md", "catalog-08-data-retention/CATALOG_08_DATA_RETENTION.md"],
  ["9", "docs/catalogs/catalog-09-traceability/CATALOG_09_TRACEABILITY.md", "data/documentation/catalog_09_traceability_registry.json", "contracts/documentation/traceability_catalog_registry.schema.json", "docs/14_engineering_catalogs/CATALOG_09_TRACEABILITY.md", "catalog-09-traceability/CATALOG_09_TRACEABILITY.md"],
];

console.log("People Catalog Library Validation (0–9)\n");

for (const [, master, reg, schema, pointer] of CATS) {
  for (const rel of [master, reg, schema, pointer]) {
    if (!exists(rel)) fail(`Missing required file: ${rel}`);
  }
}

if (failures.length) {
  console.log("FAIL");
  for (const f of failures) console.log(" -", f);
  process.exit(1);
}

const texts = CATS.map(([, master]) => read(master));
const regs = CATS.map(([, , reg]) => readJson(reg));

const checks0 = [
  ["traceability catalog", "PEOPLE-CATALOG-09-TRACEABILITY-1.0"],
  ["library complete", "PEOPLE-CATALOG-LIBRARY-COMPLETE"],
  ["traceability foundation", "PEOPLE-CATALOG-09-TRACEABILITY-1.0 | Cross-Volume Traceability Matrix | DESIGN COMPLETE (foundation)"],
  ["retention foundation", "PEOPLE-CATALOG-08-DATA-RETENTION-1.0 | Data Classification and Retention Catalog | DESIGN COMPLETE (foundation)"],
  ["canonical value rule", "Implementation may not create undocumented enum values"],
];
for (const [label, needle] of checks0) {
  if (!texts[0].includes(needle)) fail(`Catalog 0 missing ${label}: ${needle}`);
}

const checks8 = [
  ["document id", "PEOPLE-CATALOG-08-DATA-RETENTION-1.0"],
  ["foundation scope", "Foundation Scope"],
  ["principle", "RETAIN-PRINCIPLE-001"],
  ["classification", "SYSTEM_SECRET"],
  ["state", "LEGAL_HOLD"],
  ["seeded audit", "RETAIN-AUDIT-001"],
  ["seeded secret", "RETAIN-SECRET-001"],
  ["next traceability", "PEOPLE-CATALOG-09-TRACEABILITY-1.0"],
];
for (const [label, needle] of checks8) {
  if (!texts[8].includes(needle)) fail(`Catalog 8 missing ${label}: ${needle}`);
}

const checks9 = [
  ["document id", "PEOPLE-CATALOG-09-TRACEABILITY-1.0"],
  ["foundation scope", "Foundation Scope"],
  ["principle", "TRACE-PRINCIPLE-001"],
  ["seed 001", "TRACE-SEED-001"],
  ["seed 010", "TRACE-SEED-010"],
  ["permission link", "PAGE_CLAIM"],
  ["error link", "CLAIM_ALREADY_HELD"],
  ["audit link", "CLAIM_ACQUIRED"],
  ["library complete", "PEOPLE-CATALOG-LIBRARY-COMPLETE"],
  ["next is-101", "PEOPLE-IS-101-TECHNOLOGY-DECISION-SPECIFICATION-1.0"],
];
for (const [label, needle] of checks9) {
  if (!texts[9].includes(needle)) fail(`Catalog 9 missing ${label}: ${needle}`);
}

for (let i = 0; i < CATS.length; i++) {
  if (regs[i].contentSha256 !== sha(texts[i])) fail(`Catalog ${i} SHA mismatch`);
}

if (regs[0].catalogCount !== 10) fail("catalogCount must be 10");
if (regs[0].nextCatalogId !== "PEOPLE-CATALOG-LIBRARY-COMPLETE") {
  fail("Catalog 0 nextCatalogId must be PEOPLE-CATALOG-LIBRARY-COMPLETE");
}
const retentionEntry = regs[0].catalogs.find((c) => c.catalogId === "PEOPLE-CATALOG-08-DATA-RETENTION-1.0");
if (!retentionEntry || retentionEntry.status !== "DESIGN_COMPLETE") {
  fail("Catalog 0 inventory must mark PEOPLE-CATALOG-08-DATA-RETENTION-1.0 DESIGN_COMPLETE");
}
const traceEntry = regs[0].catalogs.find((c) => c.catalogId === "PEOPLE-CATALOG-09-TRACEABILITY-1.0");
if (!traceEntry || traceEntry.status !== "DESIGN_COMPLETE") {
  fail("Catalog 0 inventory must mark PEOPLE-CATALOG-09-TRACEABILITY-1.0 DESIGN_COMPLETE");
}

if (regs[1].machineCount !== 23) fail("machineCount must be 23");
if (regs[2].errorEntryCount !== 154) fail("errorEntryCount must be 154");
if (regs[3].seededEventCount !== 6) fail("seededEventCount must be 6");
if (regs[4].seededConfigCount !== 59) fail("Catalog 4 seededConfigCount must be 59");
if (regs[5].seededPermissionCount !== 18) fail("Catalog 5 seededPermissionCount must be 18");
if (regs[6].seededNotificationCount !== 9) fail("Catalog 6 seededNotificationCount must be 9");
if (regs[7].seededJobCount !== 13) fail("Catalog 7 seededJobCount must be 13");
if (regs[7].nextCatalogId !== "PEOPLE-CATALOG-08-DATA-RETENTION-1.0") {
  fail("Catalog 7 nextCatalogId must be PEOPLE-CATALOG-08-DATA-RETENTION-1.0");
}

if (regs[8].scope !== "FOUNDATION_CONTRACT_WITH_SEEDED_RETENTION_RULES") {
  fail("Catalog 8 scope must be FOUNDATION_CONTRACT_WITH_SEEDED_RETENTION_RULES");
}
if (regs[8].principleCount !== 10) fail("Catalog 8 principleCount must be 10");
if (regs[8].classificationCount !== 5) fail("Catalog 8 classificationCount must be 5");
if (regs[8].domainCount !== 22) fail("Catalog 8 domainCount must be 22");
if (regs[8].retentionStateCount !== 5) fail("Catalog 8 retentionStateCount must be 5");
if (regs[8].seededRetentionCount !== 4) fail("Catalog 8 seededRetentionCount must be 4");
if (regs[8].lockedDecisionCount !== 15) fail("Catalog 8 lockedDecisionCount must be 15");
if (regs[8].nextCatalogId !== "PEOPLE-CATALOG-09-TRACEABILITY-1.0") {
  fail("Catalog 8 nextCatalogId must be PEOPLE-CATALOG-09-TRACEABILITY-1.0");
}

if (regs[9].scope !== "FOUNDATION_CONTRACT_WITH_SEEDED_MATRIX_ROWS") {
  fail("Catalog 9 scope must be FOUNDATION_CONTRACT_WITH_SEEDED_MATRIX_ROWS");
}
if (regs[9].principleCount !== 10) fail("Catalog 9 principleCount must be 10");
if (regs[9].linkNodeCount !== 16) fail("Catalog 9 linkNodeCount must be 16");
if (regs[9].seededRowCount !== 10) fail("Catalog 9 seededRowCount must be 10");
if (regs[9].lockedDecisionCount !== 15) fail("Catalog 9 lockedDecisionCount must be 15");
if (regs[9].nextCatalogId !== "PEOPLE-CATALOG-LIBRARY-COMPLETE") {
  fail("Catalog 9 nextCatalogId must be PEOPLE-CATALOG-LIBRARY-COMPLETE");
}

for (const m of regs[1].machines) {
  if (!texts[1].includes(m.machineId)) fail(`Machine not documented: ${m.machineId}`);
}
for (const eid of regs[2].errorEntryIds) {
  if (!texts[2].includes(eid)) fail(`Error entry not documented: ${eid}`);
}
for (const ev of regs[3].seededEvents) {
  if (!texts[3].includes(ev.eventId) || !texts[3].includes(ev.canonicalName)) {
    fail(`Seeded audit event not documented: ${ev.eventId}`);
  }
}
for (const cfg of regs[4].seededConfigs) {
  if (!texts[4].includes(cfg.configId) || !texts[4].includes(cfg.configurationKey)) {
    fail(`Seeded config not documented: ${cfg.configId}`);
  }
}
for (const p of regs[5].seededPermissions) {
  if (!texts[5].includes(p.permissionId) || !texts[5].includes(p.permissionKey)) {
    fail(`Seeded permission not documented: ${p.permissionId}`);
  }
}
for (const n of regs[6].seededNotifications) {
  if (!texts[6].includes(n.notificationId) || !texts[6].includes(n.canonicalName)) {
    fail(`Seeded notification not documented: ${n.notificationId}`);
  }
}
for (const j of regs[7].seededJobs) {
  if (!texts[7].includes(j.jobId) || !texts[7].includes(j.canonicalName)) {
    fail(`Seeded job not documented: ${j.jobId}`);
  }
}
for (const r of regs[8].seededRetentionRules) {
  if (!texts[8].includes(r.retentionId) || !texts[8].includes(r.label)) {
    fail(`Seeded retention rule not documented: ${r.retentionId}`);
  }
}
for (const row of regs[9].seededRows) {
  if (!texts[9].includes(row.traceRowId) || !texts[9].includes(row.requirementId)) {
    fail(`Seeded trace row not documented: ${row.traceRowId}`);
  }
}
for (const c of regs[0].catalogs) {
  if (!texts[0].includes(c.catalogId)) fail(`Catalog inventory missing: ${c.catalogId}`);
}

for (const [, , , , pointer, needle] of CATS) {
  if (!read(pointer).includes(needle)) {
    fail(`${pointer} does not reference canonical path`);
  }
}

for (const forbidden of ["src", "app", "pages", "components", "prisma", "migrations"]) {
  if (exists(forbidden) && fs.readdirSync(abs(forbidden)).length) {
    fail(`${forbidden}/ must remain empty/absent during catalog documentation build`);
  }
}

for (let i = 0; i < CATS.length; i++) {
  console.log(`Catalog ${i} SHA-256: ${regs[i].contentSha256}`);
}
console.log(`Catalogs inventoried: ${regs[0].catalogs.length}`);
console.log(`Seeded retention rules: ${regs[8].seededRetentionRules.length}`);
console.log(`Seeded trace rows: ${regs[9].seededRows.length}`);
console.log(`Warnings: ${warnings}`);

if (failures.length) {
  console.log("\nFAIL");
  for (const f of failures) console.log(" -", f);
  process.exit(1);
}

console.log("\nPASS");
process.exit(0);
