# #545 Pony

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Compilare Pony e stampare Hello, World!.

L’actor Main riceve Env, crea audience e scrive con env.out.print. La concatenazione usa String.

## Toolchain e riproduzione

ponyc originale; versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
ponyc .
```

```text
./main
```

## Risultato atteso e stato

Hello, World! seguito da newline; exit0.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Compiler/runtime Pony non preparati.

## Fonti primarie

- https://tutorial.ponylang.io/getting-started/hello-world.html
- https://tutorial.ponylang.io/expressions/variables.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pony` | [main.pony](main.pony) creato, verifiche pendenti |
