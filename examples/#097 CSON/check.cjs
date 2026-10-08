const fs = require('node:fs');
const assert = require('node:assert/strict');
const cson = require('cson-parser');
const parsed = cson.parse(fs.readFileSync('hello.cson', 'utf8'));
assert.deepEqual(parsed, { greeting: 'Hello, World!' });
console.log(parsed.greeting);
console.log('CSON parser: exact object assertion PASS.');
