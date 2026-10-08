const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
(async()=>{
const postcss=require(path.resolve(process.argv[2],'node_modules/postcss'));
const sugarss=require(path.resolve(process.argv[2],'node_modules/sugarss'));
const result=await postcss([]).process(fs.readFileSync('hello.sss','utf8'),{parser:sugarss,from:'hello.sss'});
let values=[];result.root.walkDecls('content',d=>values.push(d.value));assert.deepEqual(values,['"Hello, World!"']);
fs.writeFileSync(path.join(process.argv[3],'hello.css'),result.css);console.log(result.css);console.log('PASS: authentic SugarSS parser and PostCSS CSS serialization');
})().catch(e=>{console.error(e);process.exitCode=1});
