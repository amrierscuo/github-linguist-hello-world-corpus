# #791 XSLT

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Applicare XSLT1.0 a XML e produrre Hello, World!.

Il processore XSLT compila il foglio e valuta concat sul contenuto /audience della fixture originale.

## Toolchain e riproduzione

lxml6.1.3 con libxslt originale

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
python verify.py
```

## Risultato atteso e stato

Hello, World! come risultato testuale della trasformazione.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://www.w3.org/TR/1999/REC-xslt-19991116

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.xslt` | [hello.xslt](variants/xslt-6c8e89da/hello.xslt) creato, verifiche pendenti |
| `.xsl` | [hello.xsl](hello.xsl) verificato |
