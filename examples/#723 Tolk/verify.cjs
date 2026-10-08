const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const { runTolkCompiler, getTolkCompilerVersion } = require('@ton/tolk-js');
const { Blockchain, createShardAccount } = require('@ton/sandbox');
const { Cell, beginCell, contractAddress, toNano } = require('@ton/core');

(async () => {
  console.log('Tolk ' + await getTolkCompilerVersion());
  const result = await runTolkCompiler({
    entrypointFileName: 'hello.tolk',
    fsReadCallback: file => fs.readFileSync(file, 'utf8'),
  });
  assert.equal(result.status, 'ok', result.message);
  const code = Cell.fromBase64(result.codeBoc64);
  const data = beginCell().endCell();
  const address = contractAddress(0, { code, data });
  const blockchain = await Blockchain.create();
  blockchain.now = 1700000000;
  blockchain.verbosity = { print: false, blockchainLogs: false, vmLogs: 'vm_logs', debugLogs: false };
  await blockchain.setShardAccount(address, createShardAccount({
    address, code, data, balance: toNano('1'),
  }));
  const execution = await blockchain.runGetMethod(address, 'greeting');
  assert.equal(execution.exitCode, 0, 'TVM getter must succeed');
  const greeting = execution.stackReader.readString();
  assert.equal(greeting, 'Hello, World!');
  if (process.argv[2]) {
    fs.mkdirSync(path.dirname(process.argv[2]), { recursive: true });
    fs.writeFileSync(process.argv[2], JSON.stringify(result, null, 2) + '\n');
  }
  console.log('Compiled code hash ' + code.hash().toString('hex'));
  console.log('TVM exit code ' + execution.exitCode);
  console.log('TVM gas used ' + execution.gasUsed);
  console.log(greeting);
  console.log('Compilation and offline TON Sandbox execution PASS');
})().catch(error => { console.error(error); process.exitCode = 1; });
