# #625 Rouge

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Eseguire Rouge e stampare Hello, World!.

È il linguaggio Clojure su Ruby identificato dalla voce canonica .rg. Il driver chiama Rouge.repl e il parser/evaluatore autentico valuta puts e str.

## Toolchain e riproduzione

Rouge originale dal repository vic/rouge, Ruby3.2.3

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
ruby -I /path/to/rouge/lib run.rb hello.rg
```

## Risultato atteso e stato

Hello, World! su stdout.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://github.com/vic/rouge

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.rg` | [hello.rg](hello.rg) verificato |
