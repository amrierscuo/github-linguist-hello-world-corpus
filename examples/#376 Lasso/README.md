# #376 Lasso

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Interpretare Lasso9 e scrivere Hello, World! su stdout.

Il blocco <?lasso dichiara local audience; stdoutnl scrive il risultato della concatenazione. Il riferimento #audience usa lo scope locale Lasso9.

## Toolchain e riproduzione

Lasso9 originale; versione da registrare

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
lasso9 hello.lasso9
```

## Risultato atteso e stato

stdout Hello, World! seguito da newline.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compilatore/runtime nativo eseguito per questa voce.

Impedimenti: Runtime Lasso9 non disponibile; verifiche pendenti.

## Fonti primarie

- https://lassoguide.com/operations/command-line-tools.html
- https://lassoguide.com/language/variables.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.lasso` | [hello.lasso](variants/lasso-86f92243/hello.lasso) creato, verifiche pendenti |
| `.las` | [hello.las](variants/las-2efc32e6/hello.las) creato, verifiche pendenti |
| `.lasso8` | [hello.lasso8](variants/lasso8-e15216c5/hello.lasso8) creato, verifiche pendenti |
| `.lasso9` | [hello.lasso9](hello.lasso9) creato, verifiche pendenti |
