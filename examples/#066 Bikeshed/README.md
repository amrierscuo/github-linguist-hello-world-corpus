# #066 Bikeshed

Specifica minima indipendente che genera la sezione Greeting con il paragrafo Hello, World!.

## Riproduzione

Bikeshed 7.1.3 e Python 3.13.9. Installare Bikeshed in un ambiente Python isolato, come da [manuale ufficiale](https://speced.github.io/bikeshed/).

```sh
bikeshed --die-on=everything spec hello.bs hello.html
```

Il documento usa il valore generale `Status: DREAM` senza `Group`. Il generatore deve terminare senza errori o warning. Nell'HTML generato, `#greeting` identifica il titolo Greeting e il paragrafo successivo contiene esattamente Hello, World!.

## Prova

Sintassi e semantica verificate il 2026-10-08T23:35:51.294764+00:00: [log nativo](verification/finish_native.json), comandi, versioni, SHA-256 e valori estratti dall'output HTML reale. L'output generato e le dipendenze restano fuori dal corpus.

## Fonti primarie

- [Bikeshed manual](https://speced.github.io/bikeshed/)
- [Bikeshed repository](https://github.com/speced/bikeshed)

## Copertura delle estensioni

Le verifiche dei suffissi sono registrate separatamente.

| Estensione | File e stato |
| --- | --- |
| `.bs` | [hello.bs](hello.bs) sintassi e semantica verificate |
