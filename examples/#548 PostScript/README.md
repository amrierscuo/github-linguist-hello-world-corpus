# #548 PostScript

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Play PostScript and print Hello, World! without opening a display.

def lega greeting a una stringa; print usa lo stack e l’IO PostScript nativo. Il file è un programma PostScript, senza invocazioni shell.

## Toolchain and reproduction

Ghostscript10.02.1 ufficiale Ubuntu

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
gs -q -dNODISPLAY -dBATCH -dNOPAUSE hello.ps
```

## Expected result and status

Hello, World! seguito da newline; exit0.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://ghostscript.readthedocs.io/en/latest/Use.html
- https://www.adobe.com/jp/print/postscript/pdfs/PLRM.pdf

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ps` | [hello.ps](hello.ps), [verify.ps](variants/pfa-ae218071/verify.ps) created; verification pending |
| `.eps` | [hello.eps](variants/eps-93aca94e/hello.eps) created; verification pending |
| `.epsi` | [hello.epsi](variants/epsi-9a1058bf/hello.epsi) created; verification pending |
| `.pfa` | [hello.pfa](variants/pfa-ae218071/hello.pfa) verified |
