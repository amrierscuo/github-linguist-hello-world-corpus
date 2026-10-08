# 0214 Formatted — variante `.eam.fs`

Ruolo: Dataset nativo EAM/Finnis–Sinclair a una specie: embedding array di 13 valori che codifica il saluto; fixture numerica didattica non calibrata, distinta dal record fixed-width .for.

Tipo variante: **adapted**. Modello di partenza: examples/#214 Formatted/hello.for; contenuto adattato/originale per questo suffisso.

Variante originale adattata al ruolo del suffisso; i file principali esistenti non sono modificati. Nessuna verifica viene ereditata dal modello.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
Reader EAM/FS originale (LAMMPS pair_style eam/fs o ASE EAM): caricare hello.eam.fs e controllare le 13 tabulazioni embedding contro i code point del saluto.
```

Risultato atteso: Reader accetta header, array F(rho), rho(r) e r*phi(r); i 13 campioni F codificano Hello, World!.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://github.com/github-linguist/linguist/tree/main/samples/Formatted](https://github.com/github-linguist/linguist/tree/main/samples/Formatted)
- [https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
- [https://docs.lammps.org/pair_eam.html](https://docs.lammps.org/pair_eam.html)
