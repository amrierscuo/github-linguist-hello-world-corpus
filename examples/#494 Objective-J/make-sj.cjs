const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { spawnSync } = require('node:child_process');
const tools = path.resolve(process.argv[2] || '.tools');
const source = path.resolve(process.argv[3] || 'hello.j');
const destination = path.resolve(process.argv[4] || 'hello.sj');
const scratch = fs.mkdtempSync(path.join(tools, 'corpus-objj-static-'));
const compiled = path.join(scratch, 'hello.js');
const result = spawnSync(process.execPath, [
  path.join(tools, 'node_modules/objj-transpiler/bin/objjc.js'), source, '-o', compiled,
], { encoding: 'utf8' });
assert.equal(result.status, 0, result.stderr);
const runtime = require(path.join(tools, 'node_modules/objj-runtime'));
const executable = new runtime.Executable(fs.readFileSync(compiled, 'utf8'), [], 'hello.sj');
fs.writeFileSync(destination, executable.toMarkedString());
console.log('PASS: official compiler output serialized by Objective-J Executable.toMarkedString');
