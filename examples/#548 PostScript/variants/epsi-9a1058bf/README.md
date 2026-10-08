# 0548 — PostScript: `.epsi`

Ruolo: EPS con sezione preview ASCII 1-bit conforme EPSI; preview minima illustrativa bianca, saluto nel contenuto vettoriale.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Ghostscript10.02.1 ufficiale Ubuntu. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Ghostscript: renderizzare hello.epsi; tool EPSI originale per leggere BeginPreview
```

Risultato atteso: Testo Hello, World! nel rendering vettoriale; preview bianca di 8x1 pixel

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.epsi`: `ebd943bd51b0df143b46be7735743e0364899ca4513c16f89567df05f8adbe80`

Fonti primarie:

- https://www.adobe.com/content/dam/acom/en/devnet/actionscript/articles/5002.EPSF_Spec.pdf
- https://ghostscript.readthedocs.io/en/latest/Use.html
- https://www.adobe.com/jp/print/postscript/pdfs/PLRM.pdf
