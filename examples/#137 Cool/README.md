# #137 Cool

Voce canonica: `Cool`, tipo `programming`, `language_id: 68`.

Define the Main class of Cool language, inherit IO and print greetings through out_string and String.concat.

## Toolchain and reproduction

Required native toolchain unavailable or not configured, unavailable version / not verified. Test environment: **Windows x64**.

Requires Stanford's Cool reference compiler and its compatible SPIM/trap handler runtime. The exact command of the runtime depends on the wrapper provided by the distribution and must be recorded in future verification.

Comando/procedura from the example directory, except the build directory explicitly indicated:

```text
coolc -o hello hello.cl; eseguire hello con il wrapper/SPIM della stessa distribuzione Cool
```

Expected result: Cool typecheck/codegen successful; runtime MIPS/SPIM emette Hello, World! followed by newline.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Cool qui è Classroom Object-Oriented Language. Main.main restituisce Object; out_string restituisce SELF_TYPE compatibile. Le stringhe sono concatenate dal metodo String.concat. Non sono stati usati lexer/compiler inventati o equivalenti in un altro linguaggio.

Remaining requirements:

- Stanford Cool coolc and compatible SPIM runtime are unavailable.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain versions and SHA-256 values for the artifacts. The `path_normalization` property documents
local route replacements. `<corpus>` identifies the relative files included in
final corpus, which were first verified in the staging directory.
sources remain those identified by checksums. The only offspring of availability
instruments do not attest parsing or execution.
in the work directory and are not included in the corpus.

## Primary sources

- [https://web.stanford.edu/class/cs143/materials/cool-manual.pdf](https://web.stanford.edu/class/cs143/materials/cool-manual.pdf)
- [https://web.stanford.edu/class/cs143/](https://web.stanford.edu/class/cs143/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cl` | [hello.cl](hello.cl) created; verification pending |
