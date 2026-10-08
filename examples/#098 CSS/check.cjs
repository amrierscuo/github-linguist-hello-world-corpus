const fs = require('node:fs');
const assert = require('node:assert/strict');
const csstree = require('css-tree');
const errors = [];
const tree = csstree.parse(fs.readFileSync('hello.css', 'utf8'), { positions: true, onParseError: e => errors.push(e.message) });
assert.deepEqual(errors, []);
const rules = tree.children.toArray();
assert.equal(rules.length, 1);
assert.equal(csstree.generate(rules[0].prelude), '.hello::before');
const declarations = rules[0].block.children.toArray();
assert.equal(declarations.length, 2);
for (const declaration of declarations) {
  assert.equal(csstree.lexer.matchProperty(declaration.property, declaration.value).error, null);
}
assert.equal(declarations[0].property, 'content');
assert.equal(declarations[0].value.children.first.type, 'String');
assert.equal(declarations[0].value.children.first.value, 'Hello, World!');
console.log('CSS Tree: selector, content string and declaration grammar PASS; zero parse errors.');
