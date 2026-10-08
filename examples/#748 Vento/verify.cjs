const fs = require("node:fs");
const assert = require("node:assert/strict");
(async () => {
 const {pathToFileURL} = require("node:url");
 const path = require("node:path");
 const roots = [...module.paths, ...require("node:module").globalPaths];
 const base = roots.find(root => fs.existsSync(path.join(root, "ventojs", "package.json")));
 assert.ok(base, "install ventojs before verification");
 const {default: vento} = await import(pathToFileURL(path.join(base,"ventojs","mod.js")).href);
 const engine = vento();
 const result = await engine.runString(fs.readFileSync("hello.vto","utf8"), {target:"World"});
 assert.equal(result.content, "Hello, World!\n");
 console.log(result.content.trimEnd());
})().catch(error=>{console.error(error);process.exitCode=1;});
