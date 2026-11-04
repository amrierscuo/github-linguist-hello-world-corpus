# #210 Filterscript

Voce canonica `Filterscript`, tipo `programming`, language_id `112`.

Describe an Android FilterScript kernel that writes the ASCII character corresponding to each U8 allocation index of thirteen items.

## Toolchain and reproduction

Required authentic toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64**.

Requires a historical Android toolchain with llvm-rs-cc and a compatible RenderScript/FilterScript runtime. RenderScript is deprecated; the current toolchain here is not configured.

Comando/procedura from the directory of the example, unless explicit indications:

```text
Progetto Android con SDK/Build Tools storici che supportano FilterScript: compilare hello.fs; invocare ScriptC_hello.forEach_root su allocation U8 lunga 13 e copiarne i byte sul lato Java
```

Expected result: Kernel compiled; allocation equal to Hello, World!.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

The root kernel returns real ASCII values for x= 0..12. It is not compiled as a simple C to attest FilterScript; that control would ignore language restrictions and runtime.

Remaining requirements:

- Historical Android FilterScript compiler/SDK runtime and compatible device/emulator are unavailable.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sources verified in staging. The only available probe do not attest parsing
or execution. Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://developer.android.com/guide/topics/renderscript/compute](https://developer.android.com/guide/topics/renderscript/compute)
- [https://source.android.com/docs/core/architecture/graphics/renderscript](https://source.android.com/docs/core/architecture/graphics/renderscript)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.fs` | [hello.fs](hello.fs) created; verification pending |
