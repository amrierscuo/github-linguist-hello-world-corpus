const fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
(async()=>{
const wabt=await require(path.resolve(process.argv[2],'node_modules/wabt'))();
const module=wabt.parseWat('hello.wat',fs.readFileSync('hello.wat','utf8'));module.resolveNames();module.validate();
const binary=module.toBinary({log:false,write_debug_names:true}).buffer;fs.writeFileSync(path.join(process.argv[3],'hello.wasm'),binary);
const {instance}=await WebAssembly.instantiate(binary);const api=instance.exports;
const message=new TextDecoder().decode(new Uint8Array(api.memory.buffer,api.pointer(),api.length()));assert.equal(message,'Hello, World!');
console.log(message);console.log('PASS: authentic WABT compiler/validator and native WebAssembly instantiation/exports');module.destroy();
})().catch(e=>{console.error(e);process.exitCode=1});
