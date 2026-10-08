const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const solc = require('solc');
const { createEVM } = require('@ethereumjs/evm');

(async () => {
  const input = {
    language: 'Yul',
    sources: { 'hello.yul': { content: fs.readFileSync('hello.yul', 'utf8') } },
    settings: {
      evmVersion: 'prague',
      optimizer: { enabled: false },
      outputSelection: { '*': { '*': ['evm.bytecode.object'] } },
    },
  };
  const output = JSON.parse(solc.compile(JSON.stringify(input)));
  assert(!(output.errors || []).some(x => x.severity === 'error'),
    JSON.stringify(output.errors));
  const bytecode = output.contracts['hello.yul'].Greeting.evm.bytecode.object;
  assert(bytecode.length > 0, 'Compiler must emit bytecode');
  const evm = await createEVM();
  const result = await evm.runCode({
    code: Buffer.from(bytecode, 'hex'), gasLimit: 100000n,
  });
  assert.equal(result.exceptionError, undefined, 'EVM execution must succeed');
  assert.equal(result.returnValue.length, 13, 'RETURN must return exactly 13 bytes');
  const greeting = Buffer.from(result.returnValue).toString('utf8');
  assert.equal(greeting, 'Hello, World!');
  if (process.argv[2]) {
    fs.mkdirSync(path.dirname(process.argv[2]), { recursive: true });
    fs.writeFileSync(process.argv[2], JSON.stringify(output, null, 2) + '\n');
  }
  console.log('Solc ' + solc.version());
  console.log('EthereumJS EVM hardfork ' + evm.common.hardfork());
  console.log('Bytecode ' + bytecode);
  console.log('Return bytes ' + Buffer.from(result.returnValue).toString('hex'));
  console.log('Gas used ' + result.executionGasUsed);
  console.log(greeting);
  console.log('Compilation and offline EVM execution PASS');
})().catch(error => { console.error(error); process.exitCode = 1; });
