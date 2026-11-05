# #454 NASL

## Latest recorded verification

**Syntax and behavior verified** on November 5, 2026.

Original NASL parsed and display() emitted the exact greeting through Greenbone GLib message logging on stderr using a disposable Unix-socket Redis knowledge base. TCP was disabled; no vulnerability scans, probe scripts or remote targets were used.

[Native commands, versions, outputs and SHA-256](verification/native_20261105_batch_main.json). [Earlier evidence](verification/native.json).

## Extension results

- `.nasl`: syntax and behavior verified.
- `.inc`: syntax and behavior verified.

<details>
<summary>Original instructions and earlier status</summary>

Voce canonica `NASL`, tipo `programming`, language_id `171666519`.

Only perform greeting display in a local NASL script.

## Toolchain and reproduction

Authentic Greenbone OpenVAS NASL interpreter, openvas-nasl 22.7.9; Copyright (C) 2002 - 2004 Tenable Network Security; Copyright (C) 2022 Greenbone Networks GmbH. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

He interprets Greenbone OpenVAS NASL 22.7.9 extracted locally with native libraries.

Comando/procedura from the directory of the example, unless explicit indications:

```text
openvas-nasl -X hello.nasl
```

Expected result: Hello, World!

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

The authentic tool part, but the Redis context is missing: parsing/esecuzione are not attested.

Remaining requirements:

- The genuine Greenbone runtime requires a local Redis KB context that is not configured; execution remains pending.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://github.com/greenbone/openvas-scanner](https://github.com/greenbone/openvas-scanner)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.nasl` | [hello.nasl](hello.nasl), [driver.nasl](variants/inc-dd126fb7/driver.nasl) syntax and behavior verified |
| `.inc` | [hello.inc](variants/inc-dd126fb7/hello.inc) syntax and behavior verified |

</details>
