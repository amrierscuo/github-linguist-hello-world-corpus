# #759 Vyper

Fill Vyper and perform the pure greeting function in an isolated EVM.

Canonical type `programming`, language_id `1055641948`.

Suggested toolchain: Vyper0.4.3 + eth-tester0.14.0b1 / PyEVM0.12.1b1 in-memory EVM.

From the example directory:

```sh
python verify.py
```

Expected result: Original Vyper compiler produces ABI/bytecode; in-memory EVM returns ABI string Hello, World!.

The expected execution is in memory, without external blockchain.

Recorded status: syntax verified; behavior verified. Toolchain: Original Solidity solc0.8.37 or Vyper0.4.3 compiler + eth-tester0.14.0b1/PyEVM0.12.1b1 in-memory EVM. [Log](verification/result.json).

Sources:

- [Vyper](https://docs.vyperlang.org/en/stable/)

Install the dependencies in a separate directory:

```sh
python -m pip install vyper==0.4.3
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
| `.vy` | [hello.vy](hello.vy) verified |
