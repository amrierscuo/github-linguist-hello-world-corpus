# #018 ATS

`hello.dats` è un programma **ATS2/Postiats** con `main0`, che chiama `println!`
per scrivere `Hello World` seguito da un a capo. Il preludio è caricato da
`share/atspre_staload.hats`.

Toolchain richiesta: ATS2/Postiats (`patscc`) e un compilatore C supportato,
con `PATSHOME` configurato. Dalla cartella dell'esempio, su un ambiente
Unix o equivalente già configurato:

```sh
patscc -o hello hello.dats
./hello
```

Risultato atteso: una riga `Hello World`, terminazione senza errori.
Sintassi e semantica verificate: **no**. Blocco attuale: `patscc` non è disponibile
nell'ambiente Windows usato per il corpus. Il sorgente è stato confrontato con
la documentazione, ma non è stato compilato né eseguito.

Riferimenti primari: [primo programma e compilazione](https://ats-lang.github.io/FROZEN000/DOCUMENT/INT2PROGINATS/HTML/HTMLTOC/c44.html)
e [ATS-Postiats](https://github.com/githwxi/ATS-Postiats).

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.dats` | [hello.dats](hello.dats), [consumer.dats](variants/ext-hats-2e68617473/consumer.dats), [consumer.dats](variants/ext-sats-2e73617473/consumer.dats) creato, verifiche pendenti |
| `.hats` | [hello.hats](variants/ext-hats-2e68617473/hello.hats) creato, verifiche pendenti |
| `.sats` | [hello.sats](variants/ext-sats-2e73617473/hello.sats) creato, verifiche pendenti |
