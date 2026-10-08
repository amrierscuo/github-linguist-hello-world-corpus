const fs = require("node:fs");
const assert = require("node:assert/strict");
const solc = require("solc");
const input = {language:"Solidity",sources:{"Hello.sol":{content:fs.readFileSync("Hello.sol","utf8")}},settings:{outputSelection:{"*":{"*":["abi","evm.bytecode.object"]}}}};
const result = JSON.parse(solc.compile(JSON.stringify(input)));
assert.equal((result.errors||[]).filter(e=>e.severity==="error").length,0);
assert.ok(result.contracts["Hello.sol"].Hello.evm.bytecode.object.length>0);
console.log("PASS: original Solidity compiler produced bytecode");
if (process.argv[2]) fs.writeFileSync(process.argv[2], JSON.stringify(result.contracts["Hello.sol"].Hello));
