# 0548 — PostScript: `.eps`

Ruolo: Encapsulated PostScript con BoundingBox e disegno del saluto, distinto dal print su stdout.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Ghostscript10.02.1 ufficiale Ubuntu. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
gs -dSAFER -dBATCH -dNOPAUSE -sDEVICE=pngalpha -sOutputFile=hello.png hello.eps
```

Risultato atteso: Testo Hello, World! nell’immagine

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.eps`: `954792c93b8c980d3b8afa4f3f50170043e103dff7adc01ffef9363be4b80af7`

Fonti primarie:

- https://www.adobe.com/content/dam/acom/en/devnet/actionscript/articles/5002.EPSF_Spec.pdf
- https://ghostscript.readthedocs.io/en/latest/Use.html
- https://www.adobe.com/jp/print/postscript/pdfs/PLRM.pdf
