# 0454: NASL: `.inc`

## Latest recorded verification

**Syntax and behavior verified** for `.inc`. Original NASL parsed and display() emitted the exact greeting through Greenbone GLib message logging on stderr using a disposable Unix-socket Redis knowledge base. TCP was disabled; no vulnerability scans, probe scripts or remote targets were used. [Recorded evidence](../../verification/native_20261105_batch_main.json).

Ruolo: Include NASL con funzione di saluto e caller separato.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Authentic Greenbone OpenVAS NASL interpreter, openvas-nasl 22.7.9; ; Copyright (C) 2002 - 2004 Tenable Network Security; Copyright (C) 2022 Greenbone Networks GmbH. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
NASL originale: caricare driver.nasl senza target di rete
```

Expected result: Hello, World!

Status before this check: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `driver.nasl`: `85f71558fcc4f5b8cf802078a9b0fb30a5e098b45fc02923e14718fea9a30b3f`
- `hello.inc`: `5bfffc3e2878a4a9f76d701681774a11956f300a40f657a451fe903e4fa482be`

Primary sources:

- https://github.com/greenbone/openvas-scanner
