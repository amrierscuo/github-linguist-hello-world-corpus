# 0202 FLUX — variante `.flux`

Ruolo: Sorgente FLUX UMass nello stesso formato .fx; non il linguaggio InfluxDB Flux.

Tipo variante: **alias**. Copia byte-identica di examples/#202 FLUX/hello.fx

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
FLUX UMass compiler: generare il C++ da hello.flux e collegare l’implementazione mImpl.cpp del modello in un progetto temporaneo.
```

Risultato atteso: Generazione/compilazione riuscite; server emette una riga Hello, World! e termina 0.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://github.com/emeryberger/flux](https://github.com/emeryberger/flux)
- [https://www.usenix.org/legacy/event/usenix06/tech/full_papers/burns/burns_html/__flux-usenix-06.html](https://www.usenix.org/legacy/event/usenix06/tech/full_papers/burns/burns_html/__flux-usenix-06.html)
- [https://github.com/github-linguist/linguist/tree/main/samples/FLUX](https://github.com/github-linguist/linguist/tree/main/samples/FLUX)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
