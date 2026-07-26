/**
 * DOC-0 inventory rebuild — PEOPLE-DOC-FOUNDATION-AND-INVENTORY-1.0
 * Schema aligned to Cursor-ready DOC-0 specification.
 */
import fs from "fs";
import path from "path";
import crypto from "crypto";

const ROOT = "H:\\people";

function write(rel, contents) {
  const full = path.join(ROOT, rel);
  fs.mkdirSync(path.dirname(full), { recursive: true });
  fs.writeFileSync(full, contents.endsWith("\n") ? contents : contents + "\n", "utf8");
}

function walkMd(dir, acc = []) {
  if (!fs.existsSync(dir)) return acc;
  for (const ent of fs.readdirSync(dir, { withFileTypes: true })) {
    if (["node_modules", ".git", "dist", "build", ".next", ".netlify", "coverage", ".tmp", ".npm-cache", ".cache"].includes(ent.name))
      continue;
    const p = path.join(dir, ent.name);
    if (ent.isDirectory()) walkMd(p, acc);
    else if (ent.name.endsWith(".md")) acc.push(p);
  }
  return acc;
}

function rel(p) {
  return path.relative(ROOT, p).split(path.sep).join("/");
}

function sha256(abs) {
  try {
    return crypto.createHash("sha256").update(fs.readFileSync(abs)).digest("hex");
  } catch {
    return null;
  }
}

function mtimeIso(abs) {
  try {
    return fs.statSync(abs).mtime.toISOString();
  } catch {
    return null;
  }
}

function classify(fileRel) {
  const base = path.basename(fileRel, ".md");
  let volume_number = null;
  let document_type = "unknown";
  let status = "DRAFT";
  let authority_level = 7;
  let is_canonical = false;
  let notes = "";

  if (fileRel.includes("PROJECT_CONSTITUTION")) {
    volume_number = 0;
    document_type = "volume";
    status = "APPROVED";
    authority_level = 1;
    is_canonical = true;
  } else if (fileRel.startsWith("docs/00_governance/") || fileRel.startsWith("docs/01_product/")) {
    volume_number = 1;
    document_type = "volume";
    status = "APPROVED";
    authority_level = 2;
    is_canonical = true;
    if (fileRel.includes("DOCUMENTATION_LIBRARY")) {
      document_type = "standard";
      authority_level = 4;
    }
  } else if (fileRel.startsWith("docs/02_workflows/") || fileRel.startsWith("docs/03_ux/")) {
    volume_number = 2;
    document_type = "volume";
    status = "APPROVED";
    authority_level = 2;
    is_canonical = true;
  } else if (fileRel.startsWith("docs/04_data/") || fileRel.includes("IMAGE_STORAGE") || fileRel.includes("PRIVACY_AND_RETENTION")) {
    volume_number = 3;
    document_type = "volume";
    status = "APPROVED";
    authority_level = 2;
    is_canonical = true;
  } else if (fileRel.startsWith("docs/05_security/") || fileRel.startsWith("docs/06_engineering/")) {
    volume_number = 4;
    document_type = "volume";
    status = "APPROVED";
    authority_level = 2;
    is_canonical = true;
  } else if (fileRel.startsWith("docs/07_quality/")) {
    volume_number = 5;
    document_type = "volume";
    status = "PARTIAL";
    authority_level = 2;
    notes = "Quality/ops package incomplete — freeze blocker OD-B12";
  } else if (
    fileRel.startsWith("reports/") &&
    (fileRel.includes("ARCHITECTURE") ||
      fileRel.includes("CONTRADICTION") ||
      fileRel.includes("TERMINOLOGY") ||
      fileRel.includes("RISK") ||
      fileRel.includes("OPEN_DECISIONS") ||
      fileRel.includes("SCORECARD") ||
      fileRel.includes("FREEZE"))
  ) {
    volume_number = 6;
    document_type = "report";
    status = "APPROVED";
    authority_level = 3;
    is_canonical = true;
  } else if (fileRel.includes("DESIGN_FREEZE_REPORT")) {
    volume_number = 6;
    document_type = "report";
    status = "APPROVED";
    authority_level = 3;
    is_canonical = true;
    notes = "Freeze DENIED";
  } else if (fileRel.startsWith("docs/08_implementation/")) {
    volume_number = 7;
    document_type = fileRel.includes("ORCHESTRATION") ? "volume" : "standard";
    status = "APPROVED";
    authority_level = 3;
    is_canonical = true;
  } else if (fileRel.startsWith("docs/09_technical_specifications/") || fileRel.includes("volume-08")) {
    volume_number = 8;
    document_type = "working_note";
    status = "DRAFT";
    authority_level = 5;
    notes = "DRAFT_BOOTSTRAP — formalize in DOC-1";
  } else if (fileRel.startsWith("docs/10_database_specifications/") || fileRel.includes("volume-09")) {
    volume_number = 9;
    document_type = "working_note";
    status = "DRAFT";
    authority_level = 5;
    notes = "DRAFT_BOOTSTRAP — formalize in DOC-2";
  } else if (fileRel.startsWith("docs/11_api_specifications/") || fileRel.includes("volume-10")) {
    volume_number = 10;
    document_type = "working_note";
    status = "DRAFT";
    authority_level = 5;
    notes = "DRAFT_BOOTSTRAP — formalize in DOC-3";
  } else if (fileRel.startsWith("docs/12_ui_specifications/") || fileRel.includes("volume-11")) {
    volume_number = 11;
    document_type = "working_note";
    status = "DRAFT";
    authority_level = 5;
    notes = "DRAFT_BOOTSTRAP — formalize in DOC-4";
  } else if (fileRel.startsWith("docs/13_component_library/") || fileRel.includes("volume-12")) {
    volume_number = 12;
    document_type = "working_note";
    status = "DRAFT";
    authority_level = 5;
    notes = "DRAFT_BOOTSTRAP — formalize in DOC-5";
  } else if (fileRel.startsWith("docs/15_platform_standards/") || fileRel.includes("volume-13")) {
    volume_number = 13;
    document_type = "working_note";
    status = "DRAFT";
    authority_level = 5;
    notes = "DRAFT_BOOTSTRAP — formalize in DOC-6";
  } else if (fileRel.startsWith("docs/14_engineering_catalogs/") || fileRel.startsWith("docs/catalogs/")) {
    document_type = "catalog";
    status = "DRAFT";
    authority_level = 5;
    notes = "Catalog foundation / bootstrap";
  } else if (fileRel.startsWith("docs/16_implementation_packages/") || fileRel.startsWith("docs/implementation-packages/")) {
    document_type = "implementation_package";
    status = "DRAFT";
    authority_level = 5;
  } else if (fileRel.startsWith("docs/traceability/")) {
    document_type = "standard";
    status = "DRAFT";
    authority_level = 4;
  } else if (fileRel.startsWith("docs/volumes/")) {
    document_type = "working_note";
    status = "DRAFT";
    authority_level = 6;
    notes = "Canonical volume pointer README — content remains in equivalent approved paths";
    const m = fileRel.match(/volume-(\d{2})/);
    if (m) volume_number = parseInt(m[1], 10);
  } else if (fileRel.startsWith("develop_notes/")) {
    document_type = fileRel.includes("DECISION") || fileRel.includes("OPEN_DECISIONS") ? "decision" : fileRel.includes("CONTRADICTION") ? "risk" : "working_note";
    status = "DRAFT";
    authority_level = 6;
  } else if (fileRel === "README.md" || fileRel === "docs/README.md" || fileRel === "docs/DOCUMENTATION_MASTER_INDEX.md") {
    document_type = "standard";
    status = "DRAFT";
    authority_level = 4;
    volume_number = 1;
  } else if (fileRel.startsWith("reports/")) {
    document_type = "report";
    status = "APPROVED";
    authority_level = 3;
  }

  // Contradiction attachments
  const contradictionHints = {
    PEOPLE_INTAKE_FIELD_DICTIONARY: ["PEOPLE-CON-0001"],
    PEOPLE_INTAKE_FORM_BEHAVIOR_SPEC: ["PEOPLE-CON-0001"],
    PEOPLE_INTAKE_GLOSSARY: ["PEOPLE-CON-0002"],
    PEOPLE_INTAKE_MATCHING_WORKFLOW: ["PEOPLE-CON-0004"],
    PEOPLE_INTAKE_MATCHING_ENGINE_SPEC: ["PEOPLE-CON-0004"],
    PEOPLE_INTAKE_STATE_MACHINES: ["PEOPLE-CON-0006", "PEOPLE-CON-0007"],
    PEOPLE_INTAKE_API_CONTRACTS: ["PEOPLE-CON-0009"],
    PEOPLE_INTAKE_AUTHORIZATION_MATRIX: ["PEOPLE-CON-0011"],
    PEOPLE_INTAKE_QUEUE_AND_CLAIMING: ["PEOPLE-CON-0013"],
    PEOPLE_INTAKE_MASTER_BUILD_PLAN: ["PEOPLE-CON-0007", "PEOPLE-CON-0014"],
    PEOPLE_INTAKE_DESIGN_FREEZE_REPORT: ["PEOPLE-CON-0015"],
  };

  return {
    volume_number,
    document_type,
    status,
    authority_level,
    is_canonical,
    notes,
    known_contradiction_ids: contradictionHints[base] || [],
  };
}

const mdFiles = [
  ...walkMd(path.join(ROOT, "docs")),
  ...walkMd(path.join(ROOT, "reports")),
  ...walkMd(path.join(ROOT, "develop_notes")),
];
if (fs.existsSync(path.join(ROOT, "README.md"))) mdFiles.push(path.join(ROOT, "README.md"));

const documents = [];
let i = 1;
const hashMap = new Map();

for (const abs of mdFiles.sort((a, b) => rel(a).localeCompare(rel(b)))) {
  const current_path = rel(abs);
  const c = classify(current_path);
  const content_hash = sha256(abs);
  const document_id = `PEOPLE-DOC-${String(i).padStart(4, "0")}`;
  i++;

  if (content_hash) {
    if (!hashMap.has(content_hash)) hashMap.set(content_hash, []);
    hashMap.get(content_hash).push(document_id);
  }

  documents.push({
    document_id,
    title: path.basename(current_path, ".md").replace(/_/g, " "),
    current_path,
    canonical_path: current_path,
    document_type: c.document_type,
    volume_number: c.volume_number,
    status: c.status,
    authority_level: c.authority_level,
    source_origin: "existing_project_artifact",
    is_canonical: c.is_canonical,
    is_duplicate: false,
    supersedes_document_ids: [],
    superseded_by_document_id: null,
    related_document_ids: [],
    known_contradiction_ids: c.known_contradiction_ids,
    open_decision_ids: [],
    last_modified: mtimeIso(abs),
    content_hash,
    notes: c.notes,
  });
}

// Mark exact hash duplicates
for (const [, ids] of hashMap) {
  if (ids.length > 1) {
    for (const id of ids) {
      const d = documents.find((x) => x.document_id === id);
      if (d) {
        d.is_duplicate = true;
        d.notes = (d.notes ? d.notes + "; " : "") + `Exact content hash shared with ${ids.filter((x) => x !== id).join(",")}`;
      }
    }
  }
}

const byStatus = {};
for (const d of documents) byStatus[d.status] = (byStatus[d.status] || 0) + 1;

const inventory = {
  schema_version: "1.0",
  registry_id: "PEOPLE-DOCUMENT-INVENTORY-1.0",
  generated_at: new Date().toISOString(),
  project_root: "H:\\people",
  script_id: "PEOPLE-DOC-FOUNDATION-AND-INVENTORY-1.0",
  build_mode: "DOCUMENTATION_AND_SPECIFICATION_ONLY",
  production_code: "PROHIBITED",
  structure_note:
    "Approved Volumes 0–7 content remains under docs/00_*…docs/08_* and reports/. docs/volumes/* are pointers. Bootstrap docs/09_*…docs/16_* are DRAFT pending DOC-1…DOC-12. No git mv performed — movement unsafe for link/history stability.",
  total_documents: documents.length,
  status_counts: byStatus,
  documents,
};

write("data/documentation/document_inventory.json", JSON.stringify(inventory, null, 2));

// Schema
write(
  "contracts/documentation/document_inventory.schema.json",
  JSON.stringify(
    {
      $schema: "https://json-schema.org/draft/2020-12/schema",
      $id: "https://people.local/schemas/document_inventory.schema.json",
      title: "People Intake Document Inventory",
      type: "object",
      required: ["schema_version", "registry_id", "generated_at", "project_root", "documents"],
      properties: {
        schema_version: { type: "string" },
        registry_id: { type: "string" },
        generated_at: { type: "string" },
        project_root: { type: "string", const: "H:\\people" },
        documents: {
          type: "array",
          items: {
            type: "object",
            required: [
              "document_id",
              "title",
              "current_path",
              "canonical_path",
              "document_type",
              "status",
              "authority_level",
              "is_canonical",
              "is_duplicate",
            ],
            properties: {
              document_id: { type: "string", pattern: "^PEOPLE-DOC-\\d{4}$" },
              title: { type: "string" },
              current_path: { type: "string" },
              canonical_path: { type: "string" },
              document_type: {
                type: "string",
                enum: [
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
                ],
              },
              volume_number: { type: ["integer", "null"], minimum: 0 },
              status: {
                type: "string",
                enum: [
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
                ],
              },
              authority_level: { type: "integer", minimum: 1, maximum: 7 },
              source_origin: { type: "string" },
              is_canonical: { type: "boolean" },
              is_duplicate: { type: "boolean" },
              supersedes_document_ids: { type: "array", items: { type: "string" } },
              superseded_by_document_id: { type: ["string", "null"] },
              related_document_ids: { type: "array", items: { type: "string" } },
              known_contradiction_ids: { type: "array", items: { type: "string" } },
              open_decision_ids: { type: "array", items: { type: "string" } },
              last_modified: { type: ["string", "null"] },
              content_hash: { type: ["string", "null"] },
              notes: { type: "string" },
            },
          },
        },
      },
    },
    null,
    2
  )
);

// Terminology expanded
const terms = [
  ["PEOPLE-TERM-0001", "People Intake", "Secure paper-to-database intake application for volunteer sheets", "1"],
  ["PEOPLE-TERM-0002", "Canonical People Domain", "Shared identity domain across ecosystem applications", "3/13"],
  ["PEOPLE-TERM-0003", "Canonical Person", "Shared trusted identity record; not the raw intake entry", "0/3"],
  ["PEOPLE-TERM-0004", "Batch", "Collection of pages from one capture effort", "2/3"],
  ["PEOPLE-TERM-0005", "Page", "One captured source sheet image; primary queue unit; up to supported entries", "0/2"],
  ["PEOPLE-TERM-0006", "Entry", "One independently tracked person-intake row from a page", "0/3"],
  ["PEOPLE-TERM-0007", "Entry Field", "A single transcribed attribute on an entry", "3"],
  ["PEOPLE-TERM-0008", "Source Image", "Private original photograph/scan of a page", "3"],
  ["PEOPLE-TERM-0009", "Source Evidence", "Original artifacts and raw transcription preserved for explanation", "0"],
  ["PEOPLE-TERM-0010", "Raw Transcription", "Exactly what the operator typed from the sheet", "3"],
  ["PEOPLE-TERM-0011", "Normalized Value", "Cleaned comparison form; raw retained", "3"],
  ["PEOPLE-TERM-0012", "Field Condition", "BLANK/UNREADABLE/etc. metadata on a field", "3"],
  ["PEOPLE-TERM-0013", "Claim", "Temporary expiring assignment of queue work; not permanent ownership", "2"],
  ["PEOPLE-TERM-0014", "Queue", "Shared multi-user work list", "2"],
  ["PEOPLE-TERM-0015", "Draft", "Unsubmitted transcription under an active claim", "2"],
  ["PEOPLE-TERM-0016", "Submission", "Page submit after transcription validation", "2"],
  ["PEOPLE-TERM-0017", "Match Evaluation", "Process/run producing candidates and tiers", "3"],
  ["PEOPLE-TERM-0018", "Match Candidate", "Scored possible canonical person for an entry", "3"],
  ["PEOPLE-TERM-0019", "Match Signal", "Explainable reason contributing to a candidate score", "3"],
  ["PEOPLE-TERM-0020", "Match Resolution", "Final LINK/CREATE/DEFER/RETURN/NO_ACTION determination", "3"],
  ["PEOPLE-TERM-0021", "Promotion", "Controlled link/contribute of intake entry to canonical domain", "0/3"],
  ["PEOPLE-TERM-0022", "Person Attribute", "Canonical attribute with provenance", "3"],
  ["PEOPLE-TERM-0023", "Provenance", "Trail of origin for a value or decision", "0/3"],
  ["PEOPLE-TERM-0024", "Audit Event", "Durable business-history record; distinct from operational logs", "0/4"],
  ["PEOPLE-TERM-0025", "Background Job", "Async recoverable work unit", "4"],
  ["PEOPLE-TERM-0026", "Idempotency Key", "Safe replay token for critical writes", "4"],
  ["PEOPLE-TERM-0027", "Correlation ID", "Request/trace identifier across logs and audits", "4"],
  ["PEOPLE-TERM-0028", "Reviewer", "Role resolving uncertain matches", "2"],
  ["PEOPLE-TERM-0029", "Data Entry User", "Role claiming pages and transcribing entries", "2"],
  ["PEOPLE-TERM-0030", "Uploader", "Role capturing/uploading batches", "2"],
  ["PEOPLE-TERM-0031", "Administrator", "Role managing users, exceptions, overrides", "2"],
  ["PEOPLE-TERM-0032", "Owner", "Role governing policy and high-risk configuration", "2"],
  ["PEOPLE-TERM-0033", "UNKNOWN", "Tri-state value when Yes/No not indicated; NEVER means NO", "0"],
];

const terminology = {
  schema_version: "1.0",
  registry_id: "PEOPLE-TERMINOLOGY-INVENTORY-1.0",
  generated_at: new Date().toISOString(),
  semantic_locks: {
    unknown_is_not_no: true,
    page_is_queue_unit: true,
    entry_is_independent_row: true,
    canonical_person_not_owned_by_silent_intake_writes: true,
    promotion_is_controlled: true,
    claim_is_temporary: true,
    audit_event_not_operational_log: true,
  },
  terms: terms.map(([term_id, canonical_term, definition, owning_volume]) => ({
    term_id,
    canonical_term,
    definition,
    allowed_abbreviations: [],
    disallowed_or_deprecated_terms: canonical_term === "UNKNOWN" ? ["treating blank as NO"] : [],
    owning_volume,
    related_terms: [],
    notes: "",
  })),
};

write("data/documentation/terminology_inventory.json", JSON.stringify(terminology, null, 2));

console.log(
  JSON.stringify(
    {
      total: inventory.total_documents,
      status_counts: byStatus,
      hash_duplicate_groups: [...hashMap.values()].filter((x) => x.length > 1).length,
    },
    null,
    2
  )
);
