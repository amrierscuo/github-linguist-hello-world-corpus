# #674 Solidity

Fill out a Solidity contract with pure function that returns greeting.

Canonical type `programming`, language_id `237469032`.

Suggested toolchain: Solidity solc0.8.37 + eth-tester0.14.0b1 / PyEVM0.12.1b1 in-memory EVM.

From the example directory:

```sh
mkdir -p build
node verify.cjs build/contract.json
python verify_evm.py build/contract.json
```

Expected result: Original compiler produces bytecode; local in-memory EVM call returns ABI string Hello, World!; stdout greeting and newline.

The compilation is distinct from the execution. Accounts or transactions on blockchain networks are not created.

Recorded status: syntax verified; behavior verified. Toolchain: Original Solidity solc0.8.37 or Vyper0.4.3 compiler + eth-tester0.14.0b1/PyEVM0.12.1b1 in-memory EVM. [Log](verification/result.json).

Sources:

- [Solidity](https://docs.soliditylang.org/en/latest/)

Install the dependencies in a separate directory:

```sh
npm install solc
```

Install the dependencies in a separate directory:

```sh
python -m pip install eth-tester[py-evm] vyper==0.4.3
```

The full check deployed to in-memory PyEVM, sent a local transaction and called greeting. It decoded the string value from the ABI and compared it with Hello, World!. No external blockchain network was used.

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sol` | [Hello.sol](Hello.sol) verified |
