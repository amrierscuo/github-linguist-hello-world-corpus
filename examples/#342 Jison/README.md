# #342 Jison

Voce canonica `Jison`, tipo `programming`, language_id `284531423`.

Generare un parser Jison per una piccola grammatica del saluto e provarlo su input validi e invalidi.

## Toolchain e riproduzione

Official Jison grammar compiler/parser generator — jison 0.4.18. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Jison 0.4.18 e Node.js 22.20.0. hello.jison include scanner, start symbol e azione semantica; il JavaScript generato resta in build.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
npm install --prefix .tools jison@0.4.18; node verify.cjs .tools build
```

Risultato atteso: Parser generato; input accettati/rifiutati come previsto; risultato Hello, World!.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il generator autentico compila la grammatica e il parser realmente generato legge Hello, World!, una variante con spazi e rifiuta Reader. Il risultato è composto dai valori lessicali Hello e World.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://github.com/zaach/jison](https://github.com/zaach/jison)
- [https://gerhobbelt.github.io/jison/docs/](https://gerhobbelt.github.io/jison/docs/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.jison` | [hello.jison](hello.jison) verificato |
