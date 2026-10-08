const fs = require("node:fs");
const assert = require("node:assert/strict");
const {pathToFileURL} = require("node:url");
const {JSDOM} = require("jsdom");
const dom = new JSDOM("<!doctype html><body></body>");
global.window = dom.window; global.document = dom.window.document;
(async () => {
  const {default: mermaid} = await import(pathToFileURL(require.resolve("mermaid")).href);
  mermaid.initialize({startOnLoad: false});
  const diagram = await mermaid.mermaidAPI.getDiagramFromText(fs.readFileSync("hello.mermaid", "utf8"));
  const vertices = diagram.db.getVertices();
  const node = vertices instanceof Map ? vertices.get("greeting") : vertices.greeting;
  assert.equal(node.text, "Hello, World!");
  console.log(node.text);
})().catch(error => {console.error(error); process.exitCode = 1;}).finally(() => dom.window.close());
