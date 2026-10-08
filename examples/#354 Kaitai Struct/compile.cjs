const fs=require('node:fs'),path=require('node:path');
const compiler=require(path.resolve(process.argv[2],'node_modules/kaitai-struct-compiler'));
const yaml=require(path.resolve(process.argv[2],'node_modules/js-yaml'));
console.log('Official Kaitai compiler '+compiler.version);
compiler.compile('python',yaml.load(fs.readFileSync('greeting.ksy','utf8')),null,false).then(files=>{
  fs.mkdirSync(process.argv[3],{recursive:true});
  for(const [name,source] of Object.entries(files)) fs.writeFileSync(path.join(process.argv[3],name),source);
  console.log('PASS: genuine Kaitai compiler produced '+Object.keys(files).join(', '));
}).catch(error=>{console.error(error);process.exitCode=1;});
