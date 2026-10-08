# #623 Roff

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Renderizzare il paragrafo Hello, World! in Roff.

Documento roff originale senza pacchetto macro; la prova usa formatter e postprocessor GNU groff.

## Toolchain e riproduzione

GNU groff1.23.0

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
groff -Tascii hello.roff
```

## Risultato atteso e stato

Output testuale contiene Hello, World!.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://www.gnu.org/software/groff/manual/groff.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.roff` | [hello.roff](hello.roff), [main.roff](variants/tmac-730eca82/main.roff) creato, verifiche pendenti |
| `.1` | [hello.1](variants/1-f7f4791a/hello.1) creato, verifiche pendenti |
| `.1in` | [hello.1in](variants/1in-6e7b1a94/hello.1in) creato, verifiche pendenti |
| `.1m` | [hello.1m](variants/1m-7f066f37/hello.1m) creato, verifiche pendenti |
| `.1x` | [hello.1x](variants/1x-7bfba87c/hello.1x) creato, verifiche pendenti |
| `.2` | [hello.2](variants/2-4d02623e/hello.2) creato, verifiche pendenti |
| `.3` | [hello.3](variants/3-935a3a42/hello.3) creato, verifiche pendenti |
| `.3in` | [hello.3in](variants/3in-5e94d8c2/hello.3in) creato, verifiche pendenti |
| `.3m` | [hello.3m](variants/3m-9b77779e/hello.3m) creato, verifiche pendenti |
| `.3p` | [hello.3p](variants/3p-3cf4f404/hello.3p) creato, verifiche pendenti |
| `.3pm` | [hello.3pm](variants/3pm-8f3210f6/hello.3pm) creato, verifiche pendenti |
| `.3qt` | [hello.3qt](variants/3qt-f5ff2f97/hello.3qt) creato, verifiche pendenti |
| `.3x` | [hello.3x](variants/3x-a9b9c037/hello.3x) creato, verifiche pendenti |
| `.4` | [hello.4](variants/4-33df2dbc/hello.4) creato, verifiche pendenti |
| `.5` | [hello.5](variants/5-4b1e53e6/hello.5) creato, verifiche pendenti |
| `.6` | [hello.6](variants/6-ae3ae580/hello.6) creato, verifiche pendenti |
| `.7` | [hello.7](variants/7-11de1834/hello.7) creato, verifiche pendenti |
| `.8` | [hello.8](variants/8-5429ab03/hello.8) creato, verifiche pendenti |
| `.9` | [hello.9](variants/9-523c2e7c/hello.9) creato, verifiche pendenti |
| `.l` | [hello.l](variants/l-ac16c41b/hello.l) creato, verifiche pendenti |
| `.man` | [hello.man](variants/man-ced7911e/hello.man) creato, verifiche pendenti |
| `.mdoc` | [hello.mdoc](variants/mdoc-e2a9af6c/hello.mdoc) creato, verifiche pendenti |
| `.me` | [hello.me](variants/me-a72dc235/hello.me) creato, verifiche pendenti |
| `.ms` | [hello.ms](variants/ms-5138d9ae/hello.ms) creato, verifiche pendenti |
| `.n` | [hello.n](variants/n-3852639b/hello.n) creato, verifiche pendenti |
| `.nr` | [hello.nr](variants/nr-ec75feb3/hello.nr) creato, verifiche pendenti |
| `.rno` | [hello.rno](variants/rno-4ebd8568/hello.rno) creato, verifiche pendenti |
| `.tmac` | [hello.tmac](variants/tmac-730eca82/hello.tmac) creato, verifiche pendenti |
