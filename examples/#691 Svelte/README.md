# #691 Svelte

Voce canonica `Svelte`, tipo `markup`, language_id `928734530`.

Compilare e renderizzare una componente Svelte5 con parametro name.

## Toolchain e riproduzione

Official svelte compiler/parser and server renderer — 5.57.2. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Compiler e server renderer Svelte originali, versione precisa nel log.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
npm install --prefix .tools svelte; node verify.cjs .tools build
```

Risultato atteso: Hello, World! nel risultato conforme, secondo lÃ¢â‚¬â„¢ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il compilatore emette ESM reale e server.render produce World e Reader corretti. Il goal eÌâ‚¬ SSR; il browser non eÌâ‚¬ necessario.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://svelte.dev/docs/svelte/svelte-server](https://svelte.dev/docs/svelte/svelte-server)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.svelte` | [Greeting.svelte](Greeting.svelte) verificato |
