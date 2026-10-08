# #781 X PixMap

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Leggere un raster XPM che mostra visivamente Hello, World!.

La stringa di saluto è disegnata nei pixel, non in un commento. Pillow ha decodificato il file82×9; l’assistente ha poi ispezionato la preview originale ingrandita con nearest-neighbor e letto Hello, World!. Il log distingue la lettura nativa dalla revisione visiva.

## Toolchain e riproduzione

Pillow12.3.0 decoder XPM originale

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
python verify.py
```

## Risultato atteso e stato

Immagine con glifi neri Hello, World! su sfondo bianco; preview solo nella build temporanea.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://www.x.org/docs/XPM/xpm.pdf

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.xpm` | [hello.xpm](hello.xpm) verificato |
| `.pm` | [hello.pm](variants/pm-c810ce30/hello.pm) creato, verifiche pendenti |
