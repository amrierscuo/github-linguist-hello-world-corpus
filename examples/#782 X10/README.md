# #782 X10

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Compilare X10 e stampare Hello, World!.

Programma X10 con main(Rail[String]) e x10.io.Console; la toolchain Java ordinaria non sostituisce X10.

## Toolchain e riproduzione

Compilatore/runtime X10, versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
x10c Hello.x10; x10 Hello
```

## Risultato atteso e stato

Hello, World! su stdout.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Compilatore X10 non disponibile; parser ed esecuzione pendenti.

## Fonti primarie

- https://x10-lang.org/articles/11.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.x10` | [Hello.x10](Hello.x10) creato, verifiche pendenti |
