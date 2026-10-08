const fs=require('fs');
const assert=require('assert/strict');
const w=require('wollok-ts');
const files=['greeting.wlk','hello.wpg'].map(name=>({name,content:fs.readFileSync(name,'utf8')}));
for(const file of files){const ast=w.parse.File(file.name).tryParse(file.content);assert(!ast.hasProblems);}
const environment=w.buildEnvironment(files);
const interpreter=w.interpret(environment,w.natives());
const lines=[];
interpreter.evaluation.console={log:(text)=>lines.push(text)};
interpreter.run('hello.hello');
assert.deepEqual(lines,['Hello, World!']);
console.log(lines[0]);
console.log('PASS: original Wollok parser/linker/interpreter executes object greeting and console println');
