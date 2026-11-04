# #029 AngelScript

`hello.as` defines `void main()` and calls `print()` registered by the host of the official `asrun` runner. `print` is a function of the demonstrative host, not an intrinsic function of any AngelScript integration.

Prerequisite: the sample runner in `/sdk/samples/asrun/` from the AngelScript 2.38.0 SDK, built with a C++ compiler together with the engine and required add-ons. The locally built Linux runner ran under Ubuntu WSL. Its version and hash are recorded in the log. The binary is not included in the corpus.

```sh
asrun hello.as
```

Expected output exact:

```text
Hello, World!
```

The test performed includes filling in bytecode of the source by the engine and calling `main()` in VM. Invoke `asrun` without print file version and use with exit 255: that code belongs to the information command, while the execution of the example ends with exit 0.

Toolchain: **AngelScript SDK 2.38.0; runner ufficiale asrun compilato con GNU C++ su Ubuntu WSL x86_64**.

Status: **Sintassi e semantica verificate.**

Evidence: [log dei comandi e SHA-256 dei sorgenti](verification/toolchain.json). The log keeps exit code, stdout and stderr; the machine paths are normalized.

Primary sources:

- [Documentazione / sorgente ufficiale 1](https://www.angelcode.com/angelscript/sdk/docs/manual/doc_samples_asrun.html)
- [Documentazione / sorgente ufficiale 2](https://github.com/anjo76/angelscript/releases/tag/v2.38.0)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.as` | [hello.as](hello.as) verified |
| `.angelscript` | [hello.angelscript](variants/ext-angelscript-2e616e67656c736372697074/hello.angelscript) created; verification pending |
