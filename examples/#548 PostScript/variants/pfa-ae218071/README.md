# 0548 — PostScript: `.pfa`

Ruolo: Font PostScript Type 1 ASCII minimo: FullName del saluto e sola glyph .notdef con hsbw/endchar; lenIV -1 disabilita cifratura delle charstring. Non contiene glifi delle lettere del saluto.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Ghostscript10.02.1 ufficiale Ubuntu. La versione osservata nella prova effettiva è riportata nel log; gli ambienti applicativi non esercitati restano pendenti.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
gs -dSAFER -dBATCH -dNOPAUSE -dNODISPLAY hello.pfa verify.ps
```

Risultato atteso: Font definito e FontInfo.FullName = Hello, World!; .notdef vuota renderizzabile.

Stato individuale: artefatto creato `true`, sintassi verificata `true`, semantica verificata `true`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- Nessun impedimento per l’ambito effettivamente verificato.

SHA-256 dei file della variante:

- `hello.pfa`: `c5df05a925489cb214002efc659f79c61ac44fd67f602cac112352a9b9ede971`
- `verify.ps`: `dacf972adb3044ad100fdcd921461423b8d3c2a7013926bb4ee32036e238724f`

Fonti primarie:

- https://adobe-type-tools.github.io/font-tech-notes/pdfs/T1_SPEC.pdf
- https://ghostscript.readthedocs.io/en/latest/Use.html
- https://www.adobe.com/jp/print/postscript/pdfs/PLRM.pdf

Prova aggiuntiva realmente eseguita:

Ghostscript definisce font Type1, legge FullName esatto Hello, World! e interpreta show della glyph .notdef; non pretende glifi testuali del saluto.

Log: `verification/native.json`. Le procedure proposte sopra non eseguite restano distinte dai comandi nel log.

Tool/versione osservata: 10.02.1
