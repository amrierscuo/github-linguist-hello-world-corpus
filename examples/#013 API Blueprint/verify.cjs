// Drafter is the actual API Blueprint parser. This script checks its AST.
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const drafter = require(path.resolve(process.argv[2]));
const source = fs.readFileSync(path.join(__dirname, 'hello.apib'), 'utf8');
const diagnostics = drafter.validateSync(source, {requireBlueprintName: true});
assert.equal(diagnostics, null, 'Drafter returned diagnostics');
const result = drafter.parseSync(source, {requireBlueprintName: true});
function collect(node, element, found = []) {
  if (node && typeof node === 'object') {
    if (node.element === element) found.push(node);
    for (const child of Object.values(node)) {
      if (Array.isArray(child)) child.forEach(value => collect(value, element, found));
      else if (child && typeof child === 'object') collect(child, element, found);
    }
  }
  return found;
}
const resources = collect(result, 'resource');
assert.equal(resources.length, 1);
assert.equal(resources[0].attributes.href.content, '/hello');
const requests = collect(resources[0], 'httpRequest');
assert.equal(requests.length, 1);
assert.equal(requests[0].attributes.method.content, 'GET');
const responses = collect(resources[0], 'httpResponse');
assert.equal(responses.length, 1);
assert.equal(responses[0].attributes.statusCode.content, '200');
const bodies = collect(responses[0], 'asset');
assert.equal(bodies.length, 1);
assert.equal(bodies[0].attributes.contentType.content, 'text/plain');
assert.equal(bodies[0].content, 'Hello, World!\n');
console.log('Drafter: valid, no warnings');
console.log('AST: GET /hello -> 200 text/plain; body = Hello, World! + LF');
