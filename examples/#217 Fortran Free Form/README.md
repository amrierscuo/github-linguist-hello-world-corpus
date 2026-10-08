# #217 Fortran Free Form

Voce canonica `Fortran Free Form`, tipo `programming`, language_id `761352333`.

Compilare un programma Fortran 2008 in forma libera e stampare una concatenazione parametrica.

## Toolchain e riproduzione

GNU Fortran compiler extracted locally from Ubuntu — GNU Fortran (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0. Ambiente della prova: **Ubuntu 24.04 WSL2/Linux x86_64**.

GNU Fortran 13.3.0 su Ubuntu 24.04. implicit none, parametro character e righe free form distinguono questo sorgente dalla voce a forma fissa.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
gfortran -std=f2008 -ffree-form hello.f90 -o build/hello; ./build/hello
```

Risultato atteso: Compilazione/run exit 0; saluto esatto seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il compilatore autentico viene invocato con -ffree-form e -std=f2008. La prova esegue il prodotto compilato e confronta stdout.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sorgenti verificati in staging. I soli probe di disponibilità non attestano parsing
o esecuzione. Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://gcc.gnu.org/onlinedocs/gfortran/Fortran-Dialect-Options.html](https://gcc.gnu.org/onlinedocs/gfortran/Fortran-Dialect-Options.html)
- [https://gcc.gnu.org/onlinedocs/gfortran/](https://gcc.gnu.org/onlinedocs/gfortran/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.f90` | [hello.f90](hello.f90) verificato |
| `.f03` | [hello.f03](variants/ext-f03-2e663033/hello.f03) creato, verifiche pendenti |
| `.f08` | [hello.f08](variants/ext-f08-2e663038/hello.f08) creato, verifiche pendenti |
| `.f95` | [hello.f95](variants/ext-f95-2e663935/hello.f95) creato, verifiche pendenti |
