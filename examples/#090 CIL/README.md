# #090 CIL

Compilare una policy SELinux CIL minima che dichiara hello_world_t e autorizza read su greeting_file_t; tutti i simboli e il contesto devono risolversi.

## Toolchain

SELinux secilc 3.5-1; Ubuntu libsepol 3.5

## Comandi e procedura

Con secilc 3.5 su Linux, usando una cartella temporanea di build:

```sh
mkdir -p build
secilc hello.cil -o build/hello.policy -f build/file_contexts
```

Il sorgente è una policy CIL autonoma minima, con classe file, SID kernel,
utente, ruolo, tipi e una sola regola allow. Il risultato binario dimostra la
compilazione e risoluzione del modello; non è un artefatto da installare come
policy effettiva della macchina. Il test non esegue semodule né setenforce.

## Risultato atteso

Compilazione nativa exit 0 e policy binaria prodotta; nessun simbolo o contesto non risolto.

## Stato

Sintassi e semantica verificate.

Questa voce canonica usa SELinux Common Intermediate Language (.cil), non l'IL del CLR. Il saluto è rappresentato dal tipo hello_world_t: CIL non stampa testo. La prova produce una policy temporanea e non la carica sul sistema.

Verifica effettiva del 2026-10-08T11:33:17.269986+00:00 su WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
Il log include hash SHA-256 della sorgente e dei checker, versioni, comandi, codici di uscita, stdout, stderr e limiti della prova.

## Fonti primarie

- [https://github.com/SELinuxProject/selinux/tree/master/secilc/docs](https://github.com/SELinuxProject/selinux/tree/master/secilc/docs)
- [https://github.com/SELinuxProject/selinux-notebook/blob/main/src/cil_overview.md](https://github.com/SELinuxProject/selinux-notebook/blob/main/src/cil_overview.md)
- [https://github.com/github-linguist/linguist/tree/main/samples/CIL](https://github.com/github-linguist/linguist/tree/main/samples/CIL)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cil` | [hello.cil](hello.cil) verificato |
