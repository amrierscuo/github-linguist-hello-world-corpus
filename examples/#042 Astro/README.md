# #042 Astro

Voce canonica e ordine originali di reference/languages.yml.

Calcolare il saluto nel frontmatter Astro e renderizzare un documento HTML con h1 Hello, World!.

## Toolchain e riproduzione

Astro 5.14.1; Node.js 22.20.0. Prova eseguita su Windows x64. Le versioni effettive sono nel log.

Dalla cartella dell'esempio, installare dipendenze isolate e verificare:

```text
npm --prefix .tools install --save-exact astro@5.14.1
node verify.mjs .tools src/pages/index.astro
```

## Stato ed evidenza

Artefatto creato; sintassi verificata; semantica verificata.

Il builder ufficiale Astro compila e renderizza il sorgente originale. Il frontmatter calcola il saluto e il file HTML prodotto contiene il titolo h1 atteso. Il vecchio container incompatibile è sostituito con la normale build statica.

Risultato atteso: Hello, World!; per Astro è il contenuto di un h1 nel documento HTML.

Log reale: [verification/native.json](verification/native.json) con comandi, versioni, exit code, stdout/stderr e SHA-256. Nessun accesso a servizi cloud o database remoti.

## Fonti primarie

- [https://docs.astro.build/en/reference/cli-reference/](https://docs.astro.build/en/reference/cli-reference/)
- [https://docs.astro.build/en/basics/astro-components/](https://docs.astro.build/en/basics/astro-components/)

## Copertura delle estensioni

Le verifiche dei suffissi sono registrate separatamente.

| Estensione | File e stato |
| --- | --- |
| `.astro` | [index.astro](src/pages/index.astro) sintassi e semantica verificate |
