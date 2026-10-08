const fs = require("node:fs");
const assert = require("node:assert/strict");
const {pathToFileURL} = require("node:url");
(async () => {
  const {Edge} = await import(pathToFileURL(require.resolve("edge.js")).href);
  const engine = new Edge();
  const html = await engine.renderRaw(fs.readFileSync("hello.edge", "utf8"), {target: "World"});
  assert.equal(html, "Hello, World!");
  console.log(html);
})().catch(e => {console.error(e); process.exitCode = 1;});
