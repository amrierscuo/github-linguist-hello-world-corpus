# 0404 — M3U: `.m3u`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#404 M3U/hello.m3u8.

Toolchain richiesta: Python 3.13.9 + m3u8 6.0.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.m3u; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: un segmento di 1s con titolo e URI attesi; stdout saluto e LF.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.m3u`: `dfcf5cbb67ed6a5acdc32e72686535b11b3d47423cc36b046cff707bd2122462`
- `verify.py`: `ee8954b2a5c23e0030ab6dcfdf09d5c57468e7777f2637e483dbd97df8f0dd9c`

Fonti primarie:

- https://www.rfc-editor.org/rfc/rfc8216
- https://github.com/globocom/m3u8
