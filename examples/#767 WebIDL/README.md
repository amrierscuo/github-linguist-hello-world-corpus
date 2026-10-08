# #767 WebIDL

Voce canonica `WebIDL`, tipo `programming`, language_id `395`.

Contratto WebIDL originale: enum GreetingText con valore `Hello, World!` e namespace Greeting esposto a Window, con metodo hello() che restituisce tale enum.

## Toolchain e riproduzione

webidl2 / Node.js 22.20.0 — 24.5.0. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Node.js 22.20.0 e webidl2, versione nel log. `<prefisso-npm>/node_modules/webidl2` deve essere il pacchetto originale.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
node verify.cjs <prefisso-npm>
```

Risultato atteso: Hello, World! e PASS per enum e firma del contratto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

webidl2 esegue parsing e validazione. Il driver controlla enum, valore, namespace e tipo restituito. La semantica dichiarata è il contratto IDL verificato; nessuna implementazione di binding browser viene affermata.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://webidl.spec.whatwg.org/](https://webidl.spec.whatwg.org/)
- [https://github.com/w3c/webidl2.js](https://github.com/w3c/webidl2.js)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.webidl` | [hello.webidl](hello.webidl) verificato |
