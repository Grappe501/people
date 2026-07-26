#!/usr/bin/env node
/**
 * H-drive validation for People Intake.
 * Documentation tooling only — not application code.
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(__dirname, "..");
const reportPath = path.join(root, "reports", "PEOPLE_H_DRIVE_VALIDATION_REPORT.md");

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

const resolvedRoot = path.resolve(root);
const rootLower = resolvedRoot.toLowerCase();
const expected = "h:\\people";

note("# People Intake — H-Drive Validation Report");
note("");
note(`Generated: ${new Date().toISOString()}`);
note("");
note("## Results");
note("");

if (!rootLower.startsWith("h:\\people")) {
  fail(`Project root does not resolve under H:\\people. Resolved: ${resolvedRoot}`);
} else {
  pass(`Project root resolves to ${resolvedRoot}`);
}

if (rootLower.startsWith("c:\\")) {
  fail("Refusing to operate: root resolves to C:\\");
}

const requiredDirs = [
  ".tmp",
  ".cache",
  ".npm-cache",
  ".test-output",
  ".local-storage",
  ".netlify",
  "docs",
  "contracts",
  "scripts",
  "reports",
  "develop_notes",
  "diagrams",
];

for (const d of requiredDirs) {
  const p = path.join(root, d);
  if (fs.existsSync(p)) pass(`Required directory exists: ${d}`);
  else fail(`Missing required directory: ${d}`);
}

const envChecks = [
  ["TEMP", process.env.TEMP],
  ["TMP", process.env.TMP],
  ["TMPDIR", process.env.TMPDIR],
  ["npm_config_cache", process.env.npm_config_cache],
];

for (const [name, value] of envChecks) {
  if (!value) {
    warn(`${name} is not set in this process`);
    continue;
  }
  const v = path.resolve(value).toLowerCase();
  if (v.startsWith("c:\\")) {
    fail(`Controlled path ${name} resolves to C:\\ (${value})`);
  } else if (!v.startsWith("h:\\people")) {
    warn(`${name}=${value} is not under H:\\people`);
  } else {
    pass(`${name} points under H:\\people (${value})`);
  }
}

warn(
  "Windows/Cursor/Node/browsers may still write OS or profile files outside project control on C:\\. This validator only checks controlled project paths."
);

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
