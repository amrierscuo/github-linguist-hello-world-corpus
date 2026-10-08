# #068 BitBake .inc

Include require applicato a hello_1.0.bb. La variante originale del corpus conserva i byte identificati dai checksum.

## Toolchain e verifica

BitBake branch 2.10 (runtime 2.9.1), Python 3.12.3 e en_US.UTF-8. Copiare i file della variante nel layer temporaneo del campione principale. Per .bbappend, BBFILES deve scoprire anche ${LAYERDIR}/*.bbappend. Usare un filesystem Linux con socket Unix; i dettagli della locale privata sono nel README principale.

```text
Nel layer temporaneo configurato: bitbake -p; bitbake hello -c build
```

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

La toolchain originale ha controllato questa specifica variante. Il task BitBake o l’eseguibile m68k produce Hello, World! e termina con exit 0. Gli esiti non derivano solo dall’uguaglianza con il campione principale.

Prova: [finish_variants.json](../../verification/finish_variants.json), con comandi, UTC, versioni, exit code, output e hash. Il log registra ogni variante separatamente.

## Sorgenti verificati

- [hello.inc](hello.inc) SHA-256 `31709e6870ef89ffb69a3790ccd5c43ba96214f70b9234d0bbc2e2445b07463a`.
- [hello_1.0.bb](hello_1.0.bb) SHA-256 `2ab4132b085ecb869ec91fdbf42ece05941581dacf1911d1f09261f99ade74d3`.

## Fonti primarie

- https://docs.yoctoproject.org/bitbake/2.10/bitbake-user-manual/bitbake-user-manual-hello.html
- https://github.com/openembedded/bitbake/tree/2.10
- https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml
- https://docs.yoctoproject.org/bitbake/dev/bitbake-user-manual/bitbake-user-manual-metadata.html
