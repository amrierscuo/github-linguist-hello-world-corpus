# #117 Circom

Fill out a Circom circuit whose 13 public output signals are ASCII bytes of Hello, World!, and calculate the witness.

Canonical type: `programming`; `language_id`: `1042332086`.

Suggested toolchain: Circom 2.x and Node.js for witness generator WASM. The actual version, when available, is in the log.

From the example folder, depending on the PATH:

```sh
mkdir -p build
circom hello.circom --r1cs --wasm -o build
node build/hello_js/generate_witness.js build/hello_js/hello.wasm input.json build/hello.wtns
```

Expected result: witness with constant initial one and `[72,101,108,108,111,44,32,87,111,114,108,100,33]` output; decode vector Hello, World!.

Greeting is represented as data of the circuit, not as a console print. <== assigns the values and generates the constraints. Calculation of the witness and proof zero knowledge are different steps; this example does not require a trusted setup.

Recorded status: syntax verified; behavior verified. Tried toolchain: Circom 2.2.3 linux/amd64 + Node.js 22.20.0 witness calculator. See [log](verification/verification.log).

Primary sources or original references of the project:

- [Circom — segnali e vincoli](https://docs.circom.io/circom-language/signals/)
- [Circom — implementazione originale](https://github.com/iden3/circom)

Automatic verification included: `node verify.cjs build/hello_js`.

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.circom` | [hello.circom](hello.circom) verified |
