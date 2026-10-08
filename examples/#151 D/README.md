# #151 D

Voce canonica e ordine del `reference/languages.yml` del corpus. I sorgenti e fixture sono originali; eventuali dump/bundle provengono dagli strumenti indicati.

## Obiettivo

Compilare D in modalità BetterC e stampare il saluto tramite l’ABI C.

Il sorgente D dichiara greeting con const(char)*, @nogc e nothrow. main e puts usano extern(C). La modalità BetterC esclude dipendenze dalla GC e dal runtime D completo; la funzione greeting conserva il mangling D. Questa è una verifica del sottoinsieme BetterC dichiarato esplicitamente.

## Toolchain e riproduzione

LDC 1.43.0, Linux x86_64 ufficiale; linker GNU su Ubuntu WSL

Comandi nella cartella dell’esempio con la toolchain disponibile nel PATH. Usare una copia temporanea: database, oggetti, audio e altri output di prova non appartengono al corpus.

```text
ldc2 -betterC hello.d -of=hello
```

```text
./hello
```

## Risultato atteso e stato

stdout esatto Hello, World! seguito da newline; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra versioni e provenienza, SHA-256 dei sorgenti, comandi effettivi, exit, stdout e stderr normalizzati.

## Fonti primarie

- https://dlang.org/spec/betterc.html
- https://github.com/ldc-developers/ldc/releases/tag/v1.43.0

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.d` | [hello.d](hello.d), [consumer.d](variants/ext-di-2e6469/consumer.d), [greeting.d](variants/ext-di-2e6469/greeting.d) creato, verifiche pendenti |
| `.di` | [greeting.di](variants/ext-di-2e6469/greeting.di) creato, verifiche pendenti |
