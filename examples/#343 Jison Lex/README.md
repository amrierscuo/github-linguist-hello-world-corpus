# #343 Jison Lex

Voce canonica `Jison Lex`, tipo `programming`, language_id `406395330`.

Generare uno scanner Jison Lex e verificare token e lexeme del saluto.

## Toolchain e riproduzione

Official Jison Lex lexer generator — jison-lex 0.3.4. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

jison-lex 0.3.4 ufficiale e Node.js 22.20.0. hello.jisonlex è una specifica scanner autonoma, senza grammatica parser.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
npm install --prefix .tools jison-lex@0.3.4; node verify.cjs .tools
```

Risultato atteso: Token/lexeme corretti e PASS.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il vero scanner genera HELLO, COMMA, WORLD, BANG con i valori testuali previsti; la ricostruzione rende Hello, World!. Un carattere ? produce INVALID. La voce distinta Jison contiene invece anche la grammatica.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://github.com/zaach/jison-lex](https://github.com/zaach/jison-lex)
- [https://github.com/zaach/jison](https://github.com/zaach/jison)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.jisonlex` | [hello.jisonlex](hello.jisonlex) verificato |
