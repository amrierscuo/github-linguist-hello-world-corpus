const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const { spawnSync } = require('node:child_process');
const { Blockchain, createShardAccount } = require('@ton/sandbox');
const { toNano } = require('@ton/core');
const { require: tsRequire } = require('tsx/cjs/api');

(async () => {
  const temporary = fs.mkdtempSync(path.join(__dirname, '.tact-build-'));
  try {
    for (const file of ['hello.tact', 'tact.config.json']) {
      fs.copyFileSync(file, path.join(temporary, file));
    }
    const compilerPackage = require.resolve('@tact-lang/compiler/package.json');
    const compiler = path.join(path.dirname(compilerPackage), 'bin', 'tact.js');
    const build = spawnSync(process.execPath, [compiler, '--config', 'tact.config.json'], {
      cwd: temporary, encoding: 'utf8',
    });
    assert.equal(build.status, 0, build.stderr + build.stdout);
    console.log('Tact ' + require(compilerPackage).version);
    console.log('Compilation PASS');
    const wrapperFile = path.join(temporary, 'build', 'Greeting_Greeting.ts');
    const { Greeting } = tsRequire(wrapperFile, __filename);
    const contract = await Greeting.fromInit();
    assert(contract.init, 'Compiler-generated wrapper must provide StateInit');
    const blockchain = await Blockchain.create();
    blockchain.now = 1700000000;
    blockchain.verbosity = { print: false, blockchainLogs: false, vmLogs: 'vm_logs', debugLogs: false };
    await blockchain.setShardAccount(contract.address, createShardAccount({
      address: contract.address, ...contract.init, balance: toNano('1'),
    }));
    const execution = await blockchain.runGetMethod(contract.address, 'greeting');
    assert.equal(execution.exitCode, 0, 'TVM getter must succeed');
    assert.equal(execution.stackReader.readString(), 'Hello, World!');
    const greeting = await blockchain.openContract(contract).getGreeting();
    assert.equal(greeting, 'Hello, World!');
    console.log('Compiled code hash ' + contract.init.code.hash().toString('hex'));
    console.log('TVM exit code ' + execution.exitCode);
    console.log('TVM gas used ' + execution.gasUsed);
    console.log(greeting);
    console.log('Compilation and offline TON Sandbox execution PASS');
  } finally {
    const resolved = fs.realpathSync(temporary);
    assert(resolved.startsWith(fs.realpathSync(__dirname) + path.sep)
      && path.basename(resolved).startsWith('.tact-build-'), 'Unsafe temporary path');
    fs.rmSync(temporary, { recursive: true, force: true });
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
