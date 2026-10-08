const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const { spawnSync } = require('node:child_process');

const tools = path.resolve(process.argv[2] || '.tools');
const source = path.resolve(process.argv[3] || 'hello.j');
let code;
if (source.endsWith('.sj')) {
  const runtime = require(path.join(tools, 'node_modules/objj-runtime'));
  const url = new global.CFURL('file:///corpus/hello.sj');
  const parent = runtime.StaticResource.resourceAtURL(new global.CFURL('file:///corpus/'), true);
  const resource = new runtime.StaticResource(url, parent, false, true);
  resource.write(fs.readFileSync(source, 'utf8'));
  code = new runtime.FileExecutable(url).code();
  console.log('PASS: original Objective-J runtime decoded the Static-J archive');
} else {
  const scratch = fs.mkdtempSync(path.join(tools, 'corpus-objj-'));
  const output = path.join(scratch, 'hello.js');
  const compilation = spawnSync(process.execPath, [
    path.join(tools, 'node_modules/objj-transpiler/bin/objjc.js'), source, '-o', output,
  ], { encoding: 'utf8' });
  process.stdout.write(compilation.stdout || '');
  process.stderr.write(compilation.stderr || '');
  assert.equal(compilation.status, 0, 'Original Objective-J compiler failed');
  code = fs.readFileSync(output, 'utf8');
}
// The original runtime exports its class/message dispatch functions globally.
// Evaluating compiled code bypasses the runtime's broken Windows file loader.
require(path.join(tools, 'node_modules/objj-runtime'));
vm.runInThisContext(code, { filename: source });
assert.equal(global.Greeting.name, 'Greeting');
assert.equal(typeof global.main, 'function');
const messages = [];
const log = console.log;
try {
  console.log = (...args) => messages.push(args.join(' '));
  global.main([]);
} finally { console.log = log; }
assert.deepEqual(messages, ['Hello, World!']);
messages.forEach(message => log(message));
log('PASS: original Objective-J class method dispatched through the native runtime');
