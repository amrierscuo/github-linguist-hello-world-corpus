# #021 Adblock Filter List

Voce canonica: `Adblock Filter List`, tipo `data`, `language_id: 884614762`.
`hello.txt` is an original list of Adblock Plus 2.0.
`example.org/ads/` and allows `hello-world.png` by means of a rule of exception.
This is the equivalent of greeting: to allow the resource of greeting.

## Toolchain and reproduction

verified su Windows x64 con Node.js **22.20.0** e motore ufficiale
**adblockpluscore 0.11.1**. From the directory of this example:

```powershell
npm --prefix .tools install --no-audit --no-fund --save-exact adblockpluscore@0.11.1
node verify.cjs .tools/node_modules hello.txt
```

The first command prepares a local dependence; `verify.cjs` imports the parser and
the engine matcher. It does not replace the grammar with a parser of the corpus.
Expected result: five correct decisions, blocked banner image, image
allowed greeting, scripts and requests outside percorso/dominio without correspondence —
e `PASS: 2 active filters; 5 engine decisions; invalid-option rejected`.

## Status and evidence

Artifact created; syntax **verified**; behavior **verified** in ABP engine.
Negative control: the parser refuses an existing option. The list file
includes header and comments; the verification counts exactly two active filters.
The test is about the local matcher; it does not charge a site or install an extension.
No residual requirement for declared verification.

Log: [adblockpluscore.json](verification/adblockpluscore.json), con comandi, output,
versions and SHA-256 of artifacts.
normalized according to `path_normalization`; sources and results remain unchanged.

## Official sources

- [Sintassi dei filtri, eccezioni e opzione image](https://help.adblockplus.org/adblock-plus-help-center/how-to-write-filters).
- [Motore adblockpluscore](https://github.com/adblockplus/adblockpluscore).

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.txt` | [hello.txt](hello.txt) verified |
