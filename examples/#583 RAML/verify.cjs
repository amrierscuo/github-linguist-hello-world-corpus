const assert = require("node:assert/strict");
const parser = require("raml-1-parser");
(async () => {
 const api = await parser.loadApi("hello.raml");
 assert.equal(api.errors().length, 0);
 const body = api.resources()[0].methods()[0].responses()[0].body()[0];
 const example = body.example();
 const value = typeof example.value === "function" ? example.value() : example;
 assert.equal(value, "Hello, World!");
 console.log(value);
})().catch(error => {console.error(error); process.exitCode = 1;});
