# #464 Nemerle

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Compilare Nemerle e stampare Hello, World!.

module Hello espone Main():void; def definisce audience e Console.WriteLine effettua l’IO.

## Toolchain e riproduzione

Compiler Nemerle/.NET originale; versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
ncc -out:Hello.exe Hello.n
```

```text
Eseguire Hello.exe dopo compilazione.
```

## Risultato atteso e stato

Hello, World! seguito da newline; exit0.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: Compiler Nemerle non preparato.

## Fonti primarie

- https://github.com/rsdn/nemerle
- https://rsdn.org/article/Nemerle/TheNemerleLanguage.xml

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.n` | [Hello.n](Hello.n) creato, verifiche pendenti |
