# #183 Ecere Projects

Describe a project Ecere console with an eC source that prints Hello, World!.

Canonical type `data`, language_id `98`.

Suggested toolchain: Ecere SDK with Ecere IDE, ecereCOM and epj2make.

From the example directory:

```sh
epj2make greeting.epj
make
./greeting
```

Expected result: accepted project and console program that print `Hello, World!` followed by newline.

The .epj retains the documented structure of the 0.2 version; the support source is eC. The read-only JSON does not test the project format or linking Ecere.

Initial state: created; syntax and behavioral verification pending. native toolchain not yet performed: syntax and behavior verifications remain pending.

Sources of linguaggio/formato and original implementations:

- [Ecere — progetto console originale](https://github.com/ecere/ecere-sdk/blob/master/samples/eC/HelloWorld/HelloWorld.epj)
- [Ecere SDK](https://github.com/ecere/ecere-sdk)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.epj` | [greeting.epj](greeting.epj) created; verification pending |
