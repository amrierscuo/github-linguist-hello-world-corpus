const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const modules = path.resolve(process.argv[2] || '.tools/node_modules');
const { Program, ProgramManagerBase, PrivateKey } =
  require(path.join(modules, '@provablehq/wasm/dist/mainnet/index.cjs'));
const source = fs.readFileSync(process.argv[3] || 'hello.aleo', 'utf8');
(async () => {
  const program = Program.fromString(source);
  assert.equal(program.id(), 'corpus_hello_world.aleo');
  assert.deepEqual(program.getFunctions(), ['greeting']);
  assert.deepEqual(program.getFunctionInputs('greeting'), []);
  console.log('PASS: official SnarkVM WASM parser accepted program and function signature');
  let rejected = false;
  try { Program.fromString(source.replace('cast ', 'unknown_instruction ')); }
  catch { rejected = true; }
  assert.ok(rejected, 'Parser must reject unknown instruction');
  console.log('PASS: unknown-instruction negative control rejected');
  if (process.argv.includes('--syntax-only')) return;
  // Ephemeral local key: never printed and never used for a transaction.
  const key = new PrivateKey();
  const response = await ProgramManagerBase.executeFunctionOffline(
    key, source, 'greeting', [], false, false,
    undefined, undefined, undefined, undefined, undefined, 1
  );
  const outputs = response.getOutputs();
  const expected = '[72u8, 101u8, 108u8, 108u8, 111u8, 44u8, 32u8, 87u8, 111u8, 114u8, 108u8, 100u8, 33u8]';
  assert.deepEqual(outputs, [expected]);
  console.log(JSON.stringify({outputs}));
  console.log('PASS: official VM output equals the 13 ASCII bytes of Hello, World!');
})().catch(error => { console.error(String(error)); process.exitCode = 1; });
