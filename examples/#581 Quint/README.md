# #581 Quint

Verificare con Quint una espressione pura che restituisce il saluto.

Tipo canonico `programming`, language_id `562056483`.

Toolchain prevista: Quint CLI.

Dalla cartella dell’esempio:

```sh
quint typecheck hello.qnt
quint test hello.qnt
```

Risultato atteso: typecheck riuscito e greetingTest passa.

Quint è un linguaggio di specifica: la semantica consiste nel valutare il test della stringa, senza pretendere I/O di console.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Node.js 22.20.0 + original Quint CLI. [Log](verification/result.json). 

Fonti:

- [Quint language](https://github.com/quint-co/quint/blob/main/docs/content/docs/lang.md)
- [Quint CLI](https://github.com/quint-co/quint/blob/main/docs/content/docs/quint.md)

Preparazione delle dipendenze in una cartella dedicata:

```sh
npm install @informalsystems/quint
```

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.qnt` | [hello.qnt](hello.qnt) verificato |
