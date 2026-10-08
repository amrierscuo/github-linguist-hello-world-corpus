const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const compiler=require(path.resolve(process.argv[2],'node_modules/@riotjs/compiler'));
const render=require(path.resolve(process.argv[2],'node_modules/@riotjs/ssr')).default;
(async()=>{
const result=compiler.compile(fs.readFileSync('corpus-greeting.riot','utf8'),{file:'corpus-greeting.riot'});
assert.equal(result.meta.tagName,'corpus-greeting');
const generated=path.join(process.argv[3],'greeting.mjs');fs.writeFileSync(generated,result.code);
const component=(await import(require('node:url').pathToFileURL(generated))).default;
const output=render('corpus-greeting',component,{name:'World'});
console.log(output);assert.ok(output.includes('<p>Hello, World!</p>'));
assert.ok(render('corpus-greeting',component,{name:'Reader'}).includes('<p>Hello, Reader!</p>'));
console.log('PASS: authentic Riot compiler plus official server rendering, parameter control');
})().catch(e=>{console.error(e);process.exitCode=1});
