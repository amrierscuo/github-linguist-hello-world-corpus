# 0135 Component Pascal — variante `.cps`

Ruolo: Alias testuale dello stesso formato e dello stesso programma/dataset del modello originale.

Tipo variante: **alias**. Copia byte-identica di examples/#135 Component Pascal/Hello.cp

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
BlackBox Component Builder: importare il sorgente hello.cps e invocare il comando esportato del modulo originale.
```

Risultato atteso: Modulo compilato; comando Hello.Say disponibile; log con Hello, World! e newline.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://blackboxframework.org/](https://blackboxframework.org/)
- [https://github.com/BlackBoxCenter/blackbox](https://github.com/BlackBoxCenter/blackbox)
- [https://www.oberon.ch/pdf/CP-Lang.pdf](https://www.oberon.ch/pdf/CP-Lang.pdf)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
