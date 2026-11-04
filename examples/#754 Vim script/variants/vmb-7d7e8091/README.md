# 0754: `.vmb`

Authentic Vimball produced by the original Vimball plugin; .vmb and .vba are supported suffixes of the same textual serialization.

Origin: produttore/serializzatore original executed, as recorded in the log.

Artefatto principale: `hello.vmb`.

Control provided:

```text
vim --version
vim -Nu NONE -i NONE -n -es -S make.vim
```

Expected result: Vimball generated with original payload; later isolated extraction and CorpusGreeting must return Hello, World!.

State: created; syntax not verified; behavior not verified.

Toolchain osservata: VIM - Vi IMproved 9.1 (2024 Jan 02, compiled Aug 24 2026 22:13:04).

Real ambition: Original MkVimball generator produces the real text archive with original payload. The batch extraction attempt ends before the final check: no parser/estrazione/esecuzione outcome is declared.

Log: `verification/result.json`; SHA-256 of each sorgente/supporto of the variant, commands, exit code and actual output. Build/cache remain under `work/verify_extensions_561_836`.

Blocker: Vimball extraction and import were not verified. The Vim batch command exits before writing the check result.

Primary sources:

- [https://vimhelp.org/pi_vimball.txt.html](https://vimhelp.org/pi_vimball.txt.html)
