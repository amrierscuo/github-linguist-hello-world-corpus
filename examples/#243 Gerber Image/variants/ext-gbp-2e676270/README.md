# 0243 Gerber Image — variante `.gbp`

Ruolo: Alias convenzionale Gerber RS-274X: stessa immagine vettoriale, non Excellon/NC. Il suffisso non è usato per dichiarare funzioni o completezza di una scheda PCB; il campione Linguist .ncl contiene la stessa grammatica RS-274X.

Tipo variante: **alias**. Copia byte-identica di examples/#243 Gerber Image/hello.gbr

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
PyGerber originale: caricare hello.gbp come Gerber RS-274X, renderizzare e verificare visivamente Hello, World!.
```

Risultato atteso: Parser senza errori; PNG legge Hello, World! con virgola e punto esclamativo.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://www.ucamco.com/en/gerber/downloads](https://www.ucamco.com/en/gerber/downloads)
- [https://github.com/Argmaster/pygerber](https://github.com/Argmaster/pygerber)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
