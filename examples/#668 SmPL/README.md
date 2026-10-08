# #668 SmPL

La semantic patch originale `hello.cocci` sostituisce `puts("Goodbye")` con
`puts("Hello, World!")` nella fixture C originale `input.c`.

## Toolchain e riproduzione

Coccinelle spatch 1.1.1, pacchetto Ubuntu amd64 1.1.1.deb-5build1, compilato
con OCaml 4.14.1; GCC 13.3.0. Ubuntu 24.04 tramite WSL2.
Il pacchetto originale Coccinelle è estratto solo in una directory di lavoro;
non sono necessarie installazioni globali o ulteriori dipendenze per questa patch.

Dalla directory dell’esempio, con spatch disponibile e un output esterno:

```sh
mkdir -p <output>/build
spatch --version
spatch --sp-file hello.cocci input.c -o <output>/build/hello.c
gcc -std=c11 -Wall -Wextra -pedantic <output>/build/hello.c -o <output>/build/hello
<output>/build/hello
```

Per il pacchetto estratto, usare il binario `<prefisso>/usr/bin/spatch` e impostare
`COCCINELLE_HOME=<prefisso>/usr/lib/coccinelle`, come nel log reale.
Risultato: patch applicata, compilazione riuscita e `Hello, World!` seguito da LF,
exit code 0. Il sorgente generato contiene la sostituzione e non contiene più
la chiamata precedente.

## Stato ed evidenza

Sintassi **verificata** dal parser SmPL originale; semantica **verificata** tramite
trasformazione reale, compilazione GCC ed esecuzione del risultato.
La prova riguarda solo la fixture originale, senza patchare sorgenti di progetto
o del kernel. I byte di `hello.cocci` e `input.c` rimangono invariati.

[Log nativo](verification/native.json): versioni, comandi, exit code, stdout/stderr,
hash SHA-256 degli artefatti originali, del pacchetto tool, del C generato e del
binario eseguito. La nota `path_normalization` descrive le sostituzioni dei percorsi.
Sorgenti e binari generati rimangono nella directory di lavoro esterna.

## Fonti primarie

- [Coccinelle, progetto originale](https://coccinelle.gitlabpages.inria.fr/website/)
- [Repository e documentazione originale](https://github.com/coccinelle/coccinelle)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cocci` | [hello.cocci](hello.cocci) verificato |
