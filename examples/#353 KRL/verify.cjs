const fs=require('node:fs'), path=require('node:path'), assert=require('node:assert/strict');
const parse=require(path.resolve(process.argv[2],'node_modules/krl-parser'));
const ast=parse(fs.readFileSync('hello.krl','utf8'));
assert.ok(ast);
fs.mkdirSync(process.argv[3],{recursive:true});
fs.writeFileSync(path.join(process.argv[3],'ast.json'),JSON.stringify(ast,null,2));
console.log('PASS: authoritative Picolab KRL parser accepted original ruleset');
