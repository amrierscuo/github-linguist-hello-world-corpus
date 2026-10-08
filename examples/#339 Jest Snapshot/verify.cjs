const assert = require("node:assert/strict");
const path = require("node:path");
const {SnapshotState} = require("jest-snapshot");
const state = new SnapshotState(path.resolve("greeting.test.js.snap"), {updateSnapshot: "none"});
const result = state.match({testName: "greeting", received: "Hello, World!"});
assert.equal(result.pass, true);
console.log("Hello, World!");
