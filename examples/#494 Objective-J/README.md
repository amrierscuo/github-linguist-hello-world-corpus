# #494 Objective-J

Voce canonica e ordine originali di reference/languages.yml.

Fill and invoke an original Objective-J method.

## Toolchain and reproduction

obj-transpiler 1.0.0-10; objj-runtime 0.4.6; Node.js 22.20.0. Test performed on Windows x64.

From the example folder, install isolated dependencies and check:

```text
npm --prefix .tools install --save-exact objj-transpiler@1.0.0-10 objj-runtime@0.4.6
node verify.cjs .tools hello.j
```

## Status and evidence

Artefatto created; syntax verified; behavior verified.

The original compiler produces JavaScript, evaluated with the class functions and dispatches of the original Objective-J runtime.The checker invokes main and controls the issued message.This procedure only prevents the runtime Windows loader file, keeping compiler and native dispatcher.

Expected result: Hello, World!.

Log reale: [verification/result.json](verification/result.json) con comandi, versioni, exit code, stdout/stderr e SHA-256. Nessun accesso a servizi cloud o database remoti.

## Primary sources

- [https://www.cappuccino.dev/learn/objective-j.html](https://www.cappuccino.dev/learn/objective-j.html)
- [https://github.com/mrcarlberg/objj-runtime](https://github.com/mrcarlberg/objj-runtime)

## Extension coverage

Suffix checks are recorded separately.

| Extension | File and status |
| --- | --- |
| `.j` | [hello.j](hello.j) syntax and behavior verified |
| `.sj` | [hello.sj](variants/sj-c6e9356b/hello.sj) syntax and behavior verified |
