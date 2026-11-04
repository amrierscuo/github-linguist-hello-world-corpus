# #209 Filebench WML

Voce canonica `Filebench WML`, tipo `programming`, language_id `111`.

Use the echo command of the Workload Model Language Filebench to issue greetings, without I/O. workload

## Toolchain and reproduction

Required authentic toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64**.

The example does not create data files or worker processes and does not change system parameters.

Comando/procedura from the directory of the example, unless explicit indications:

```text
filebench -f hello.f
```

Expected result: WML file accepted; Filebench output containing Hello, World!.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Greeting is a subject of the WML echo command; the proof of the true parser/runtime. is missing

Remaining requirements:

- Filebench WML parser/runtime is unavailable.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sources verified in staging. The only available probe do not attest parsing
or execution. Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://github.com/filebench/filebench/wiki/Workload-model-language](https://github.com/filebench/filebench/wiki/Workload-model-language)
- [https://github.com/filebench/filebench](https://github.com/filebench/filebench)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.f` | [hello.f](hello.f) created; verification pending |
