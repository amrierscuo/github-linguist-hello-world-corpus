const fs = require('node:fs');
const assert = require('node:assert/strict');
const { Liquid } = require('liquidjs');
(async () => {
 const engine = new Liquid({strictVariables: false});
 const source = fs.readFileSync('hello.liquid', 'utf8');
 const ast = engine.parse(source);
 const greeting = await engine.render(ast, {name: 'World'});
 assert.equal(greeting, 'Hello, World!\n');
 assert.equal(await engine.render(ast, {name: '<World>'}), 'Hello, &lt;World&gt;!\n');
 assert.equal(await engine.render(ast, {}), 'Hello, World!\n');
 process.stdout.write(greeting);
})().catch(e => { console.error(e); process.exitCode = 1; });
