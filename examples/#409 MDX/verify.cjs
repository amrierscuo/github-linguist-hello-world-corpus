const fs = require("node:fs");
const assert = require("node:assert/strict");
const {pathToFileURL} = require("node:url");
(async () => {
  const {evaluate} = await import(pathToFileURL(require.resolve("@mdx-js/mdx")).href);
  const React = require("react");
  const runtime = require("react/jsx-runtime");
  const {renderToStaticMarkup} = require("react-dom/server");
  const content = await evaluate(fs.readFileSync("hello.mdx", "utf8"), {...runtime, development: false});
  const html = renderToStaticMarkup(React.createElement(content.default));
  assert.equal(html, "<h1>Hello, World!</h1>");
  console.log("Hello, World!");
})().catch(error => {console.error(error); process.exitCode = 1;});
