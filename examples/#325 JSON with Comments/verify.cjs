const fs = require("node:fs");
const assert = require("node:assert/strict");
const jsonc = require("jsonc-parser");
const errors = [];
const value = jsonc.parse(fs.readFileSync("hello.jsonc", "utf8"), errors, {allowTrailingComma: false});
assert.deepEqual(errors, []);
assert.deepEqual(value, {greeting: "Hello, World!"});
console.log(value.greeting);
