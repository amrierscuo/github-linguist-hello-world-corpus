const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
(async()=>{
const prefix=path.resolve(process.argv[2]);const dir=path.resolve(process.argv[3]);
const compiler=require(path.join(prefix,'node_modules/svelte/compiler'));
const output=compiler.compile(fs.readFileSync('Greeting.svelte','utf8'),{generate:'server',filename:'Greeting.svelte'});
const generated=path.join(dir,'Greeting.mjs');fs.writeFileSync(generated,output.js.code);
const link=path.join(dir,'node_modules');if(!fs.existsSync(link))fs.symlinkSync(path.join(prefix,'node_modules'),link,'junction');
const component=(await import(require('node:url').pathToFileURL(generated))).default;
const server=await import(require('node:url').pathToFileURL(path.join(prefix,'node_modules/svelte/src/server/index.js')));
const world=server.render(component,{props:{name:'World'}}).body;
const reader=server.render(component,{props:{name:'Reader'}}).body;
console.log(world);assert.ok(world.includes('<p>Hello, World!</p>'));assert.ok(reader.includes('<p>Hello, Reader!</p>'));
console.log('PASS: official Svelte compiler and SSR render with parameter control');
})().catch(e=>{console.error(e);process.exitCode=1});
