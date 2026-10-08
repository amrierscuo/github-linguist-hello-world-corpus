const fs = require("node:fs");
const assert = require("node:assert/strict");
const mask = require("maskjs");
const ast = mask.parse(fs.readFileSync("hello.mask", "utf8"));
const html = mask.render(ast, {target: "World"});
assert.equal(html, "<p>Hello, World!</p>");
console.log("Hello, World!");
