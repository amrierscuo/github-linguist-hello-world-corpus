const fs = require("node:fs");
const assert = require("node:assert/strict");
const overpy = require("overpy");
(async () => {
    const result = await overpy.compile(fs.readFileSync("hello.opy", "utf8"), "en-US");
    assert.ok(result.result.includes("Hello, World!"));
    assert.ok(result.result.includes("Big Message"));
    console.log("Hello, World!");
})().catch(error => { console.error(error); process.exitCode = 1; });
