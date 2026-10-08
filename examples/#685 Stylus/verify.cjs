const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const stylus=require(path.resolve(process.argv[2],'node_modules/stylus'));
const css=stylus.render(fs.readFileSync('hello.styl','utf8'),{filename:'hello.styl'});
assert.ok(css.includes('.greeting::before')&&css.includes('content: "Hello, World!"'));
fs.writeFileSync(path.join(process.argv[3],'hello.css'),css);console.log(css);console.log('PASS: authentic Stylus compiler emits CSS content declaration');
