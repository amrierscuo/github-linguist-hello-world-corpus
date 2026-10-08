# #042 Astro

Voce canonica: `Astro`, tipo `markup`, `language_id: 578209015`.

Calcolare il saluto nel frontmatter Astro e renderizzare un documento HTML con h1 Hello, World!.

## Toolchain e riproduzione

Official Astro CLI static builder — 5.14.1; compiler 2.13.1. Ambiente della prova: **Windows x64**.

Da questa directory: npm --prefix .tools install --save-exact astro@5.14.1 @astrojs/compiler@2.13.1. Il verificatore riceve la directory che contiene node_modules. In alternativa npm install e npm run build preparano il progetto Astro descritto da package.json.

Comando/procedura dalla directory dell’esempio:

```text
node verify.mjs .tools src/pages/index.astro --syntax-only; node verify.mjs .tools src/pages/index.astro
```

Risultato atteso: Transform del compilatore ufficiale senza errori; runtime atteso: HTML contenente <h1>Hello, World!</h1> (rendering pending).

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **in attesa**.

Il transform ufficiale riesce. L’import del modulo compilato fallisce perché createMetadata non è esportata dal runtime installato. Nessuna semantica positiva è dichiarata. La normalizzazione del filename passato al compilatore usa slash POSIX per evitare escape Windows nel modulo generato; i byte .astro restano identici.

Requisiti residui:

- Official compiler transform succeeds, but the compiled module requires createMetadata which the installed Astro runtime does not export; rendered HTML remains pending.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain e SHA-256 degli artefatti. `path_normalization` descrive le sostituzioni dei
percorsi della macchina; i byte dei sorgenti restano quelli identificati dai checksum.
Se il log registra solo disponibilità degli strumenti, nessun parsing o runtime è attestato.
Gli strumenti, le dipendenze e i prodotti di verifica restano nella directory di lavoro.

## Fonti primarie

- [https://docs.astro.build/en/basics/astro-components/](https://docs.astro.build/en/basics/astro-components/)
- [https://docs.astro.build/en/reference/container-reference/](https://docs.astro.build/en/reference/container-reference/)
- [https://github.com/withastro/compiler](https://github.com/withastro/compiler)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.astro` | [index.astro](src/pages/index.astro) sintassi verificata |
