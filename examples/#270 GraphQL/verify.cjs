const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {buildSchema, parse, validate, graphql} = require(path.resolve(process.argv[2], 'node_modules/graphql'));
(async () => {
  const schema = buildSchema(fs.readFileSync('schema.graphql', 'utf8'));
  const query = fs.readFileSync('hello.graphql', 'utf8');
  assert.deepEqual(validate(schema, parse(query)), []);
  const rootValue = {greeting: ({name}) => `Hello, ${name}!`};
  const result = await graphql({schema, source: query, rootValue, variableValues: {name: 'World'}});
  assert.equal(result.errors, undefined);
  assert.equal(result.data.greeting, 'Hello, World!');
  const control = await graphql({schema, source: query, rootValue, variableValues: {name: 'Reader'}});
  assert.equal(control.data.greeting, 'Hello, Reader!');
  const invalid = await graphql({schema, source: query, rootValue, variableValues: {name: null}});
  assert.ok(invalid.errors.length > 0);
  console.log(result.data.greeting);
  console.log('PASS: official GraphQL parse, validation, execution and variable controls');
})().catch(error => { console.error(error); process.exitCode = 1; });
