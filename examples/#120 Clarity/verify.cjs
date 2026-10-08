const fs = require("node:fs");
const assert = require("node:assert/strict");
const {getSDK} = require("@stacks/clarinet-sdk");
const {Cl} = require("@stacks/transactions");

(async () => {
  const simnet = await getSDK();
  await simnet.initEmptySession(null);
  simnet.setEpoch("3.0");
  // Standard publicly documented simulation address, not an external account.
  const sender = "ST1PQHQKV0RJXZFY1DGX8MNSNYVE3VGZJSRTPGZGM";
  simnet.deployer = sender;
  const deployment = simnet.deployContract("hello", fs.readFileSync("hello.clar", "utf8"), {clarityVersion: 3}, sender);
  assert.equal(Cl.prettyPrint(deployment.result), "true");
  const answer = simnet.callReadOnlyFn(sender + ".hello", "greeting", [], sender);
  assert.equal(Cl.prettyPrint(answer.result), '"Hello, World!"');
  console.log("Clarity local read-only result: Hello, World!");
})().catch(error => { console.error(error); process.exitCode = 1; });
