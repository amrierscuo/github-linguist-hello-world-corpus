# #717 Text

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Leggere il saluto come testo UTF8.

La voce canonica Text è prose: la verifica consiste nella decodifica UTF8 e confronto del contenuto, senza dichiarare un compilatore.

## Toolchain e riproduzione

Codec UTF8 e lettore file originali della libreria standard Python

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
python verify.py
```

## Risultato atteso e stato

Hello, World! con LF finale.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://docs.python.org/3/library/pathlib.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.txt` | [hello.txt](hello.txt) verificato |
| `.fr` | [hello.fr](variants/fr-859c52c1/hello.fr) creato, verifiche pendenti |
| `.nb` | [hello.nb](variants/nb-af372417/hello.nb) creato, verifiche pendenti |
| `.ncl` | [hello.ncl](variants/ncl-381c21d0/hello.ncl) creato, verifiche pendenti |
| `.no` | [hello.no](variants/no-0f00f447/hello.no) creato, verifiche pendenti |
