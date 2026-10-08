const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const api=require(path.resolve(process.argv[2],'node_modules/webidl2'));
const tree=api.parse(fs.readFileSync('hello.webidl','utf8'));
assert.deepEqual(api.validate(tree),[]);
const enumeration=tree.find(x=>x.type==='enum');assert.equal(enumeration.name,'GreetingText');assert.equal(enumeration.values[0].value,'Hello, World!');
const space=tree.find(x=>x.type==='namespace');assert.equal(space.name,'Greeting');assert.equal(space.members[0].idlType.idlType,'GreetingText');
console.log(enumeration.values[0].value);console.log('PASS: genuine WebIDL parser/validator and enum-return contract; no generated browser binding execution');
