# #275 HAProxy

Voce canonica `HAProxy`, tipo `data`, language_id `366607477`.

Serve greeting as a local HTTP response built by HAProxy without backend.

## Toolchain and reproduction

HAProxy native configuration parser and HTTP engine, HAProxy version 2.8.16-0ubuntu0.24.04.3 2026/06/19 - https://haproxy.org/. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

HAProxy 2.8.16 from the Ubuntu package extracted locally, with liblua5.4. verify.py requires prefix with usr/sbin/haproxy and bookcases. The only bind is 127.0.0.1: 18881; if the door is occupied the test fails.

Comando/procedura from the directory of the example, unless explicit indications:

```text
haproxy -c -f haproxy.cfg; python3 verify.py <prefix-pacchetti-haproxy> haproxy.cfg
```

Expected result: HTTP 200; body Hello, World!; PASS; finished process.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

La prova prima usa il parser -c, poi avvia un processo privato in foreground, effettua una richiesta locale e lo termina in finally. Verifica HTTP 200, Content-Type text/plain e body esatto.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.haproxy.org/download/2.8/doc/configuration.txt](https://www.haproxy.org/download/2.8/doc/configuration.txt)
- [https://www.haproxy.org/](https://www.haproxy.org/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cfg` | [haproxy.cfg](haproxy.cfg) verified |
