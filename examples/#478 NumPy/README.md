# #478 NumPy

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Eseguire un sorgente NumPy e convertire un array uint8 nel saluto Hello, World!.

L’estensione .numpy è canonica in Linguist. Il programma crea un ndarray reale di13byte uint8, controlla la forma e usa tobytes/decode; la prova esegue operazioni della libreria NumPy originale.

## Toolchain e riproduzione

NumPy2.5.3, CPython3.13.9

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
python hello.numpy
```

## Risultato atteso e stato

Hello, World! seguito da newline; exit0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://numpy.org/doc/stable/reference/generated/numpy.array.html
- https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tobytes.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.numpy` | [hello.numpy](hello.numpy) verificato |
| `.numpyw` | [hello.numpyw](variants/numpyw-c25621b9/hello.numpyw) creato, verifiche pendenti |
| `.numsc` | [hello.numsc](variants/numsc-81e0ad98/hello.numsc) creato, verifiche pendenti |
