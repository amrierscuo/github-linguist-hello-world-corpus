# #525 Papyrus

Voce canonica `Papyrus`, tipo `programming`, language_id `277`.

Greetings in the Papyrus log when an original one receives OnInit.

## Toolchain and reproduction

Required genuine compiler/runtime, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Requires Creation Kit Papyrus compiler, standard script Quest/Debug and runtime Skyrim with active logging.

Comando/procedura from the directory of the example, unless explicit indications:

```text
PapyrusCompiler CorpusGreeting.psc -f=TESV_Papyrus_Flags.flg -i=/path/to/SkyrimScripts -o=build; collegare a una quest di prova e attivare OnInit nel gioco locale.
```

Expected result: The conformed result contains Hello, World!, according to the framework described.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Original source; compiler and runtime host not available. Event and call Debug.Trace are executable in its host.

Remaining requirements:

- Required PapyrusCompiler compiler/interpreter and matching host libraries are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://ck.uesp.net/wiki/Trace_-_Debug](https://ck.uesp.net/wiki/Trace_-_Debug)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.psc` | [CorpusGreeting.psc](CorpusGreeting.psc) created; verification pending |
