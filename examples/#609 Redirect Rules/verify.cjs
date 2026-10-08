const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
(async()=>{
const parser=require(path.resolve(process.argv[2],'node_modules/@netlify/redirect-parser'));
console.log('EXPORTS:',Object.keys(parser));
const result=await parser.parseAllRedirects({redirectsFiles:[path.resolve('_redirects')],configRedirects:[],minimal:true});
console.log(JSON.stringify(result,null,2));
assert.equal(result.errors.length,0);
assert.equal(result.redirects.length,1);
const rule=result.redirects[0];assert.equal(rule.from,'/hello');assert.equal(rule.to,'/hello.txt');assert.equal(rule.status,200);
assert.equal(fs.readFileSync(rule.to.slice(1),'utf8'),'Hello, World!\n');
console.log('PASS: official Netlify parser and local target data; hosting execution pending outside this scope');
})().catch(e=>{console.error(e);process.exitCode=1});
