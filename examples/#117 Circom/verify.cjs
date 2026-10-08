const fs = require("node:fs");
const path = require("node:path");
const assert = require("node:assert/strict");

(async () => {
  const generated = path.resolve(process.argv[2] || "build/hello_js");
  const calculator = await require(path.join(generated, "witness_calculator.js"))(
    fs.readFileSync(path.join(generated, "hello.wasm")));
  const witness = await calculator.calculateWitness(JSON.parse(fs.readFileSync("input.json", "utf8")), true);
  assert.deepEqual(witness.map(Number), [1, 72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]);
  const text = Buffer.from(witness.slice(1).map(Number)).toString("ascii");
  assert.equal(text, "Hello, World!");
  console.log(text);
})().catch(error => { console.error(error); process.exitCode = 1; });
