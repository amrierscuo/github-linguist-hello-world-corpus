# #548 PostScript

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Interpretare PostScript e stampare Hello, World! senza aprire un display.

def lega greeting a una stringa; print usa lo stack e l’IO PostScript nativo. Il file è un programma PostScript, senza invocazioni shell.

## Toolchain e riproduzione

Ghostscript10.02.1 ufficiale Ubuntu

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
gs -q -dNODISPLAY -dBATCH -dNOPAUSE hello.ps
```

## Risultato atteso e stato

Hello, World! seguito da newline; exit0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://ghostscript.readthedocs.io/en/latest/Use.html
- https://www.adobe.com/jp/print/postscript/pdfs/PLRM.pdf

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ps` | [hello.ps](hello.ps), [verify.ps](variants/pfa-ae218071/verify.ps) creato, verifiche pendenti |
| `.eps` | [hello.eps](variants/eps-93aca94e/hello.eps) creato, verifiche pendenti |
| `.epsi` | [hello.epsi](variants/epsi-9a1058bf/hello.epsi) creato, verifiche pendenti |
| `.pfa` | [hello.pfa](variants/pfa-ae218071/hello.pfa) verificato |
