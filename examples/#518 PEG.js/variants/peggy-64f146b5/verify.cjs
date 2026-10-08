const fs = require("node:fs");
const assert = require("node:assert/strict");
const peggy = require("peggy");
const parser = peggy.generate(fs.readFileSync("hello.peggy", "utf8"));
assert.equal(parser.parse("Hello, World!"), "Hello, World!");
assert.throws(() => parser.parse("Goodbye"));
console.log(parser.parse("Hello, World!"));
