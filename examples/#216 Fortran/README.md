# #216 Fortran

Voce canonica `Fortran`, tipo `programming`, language_id `107`.

Compilare un programma Fortran in forma fissa e scrivere una stringa concatenata di tredici caratteri.

## Toolchain e riproduzione

GNU Fortran compiler extracted locally from Ubuntu — GNU Fortran (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0. Ambiente della prova: **Ubuntu 24.04 WSL2/Linux x86_64**.

GNU Fortran 13.3.0 su Ubuntu 24.04. La prova usa il compilatore estratto localmente, librerie Fortran locali e assembler/linker GCC 13 già presenti. Le righe rispettano le colonne della forma fissa.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
gfortran -std=legacy -ffixed-form hello.f -o build/hello; ./build/hello
```

Risultato atteso: Compilazione/run exit 0; saluto esatto seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

La voce Fortran canonica usa qui il formato fixed form; CHARACTER*13 e WRITE con formato A producono il saluto senza padding aggiuntivo.

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
| `.f` | [hello.f](hello.f) verificato |
| `.f77` | [hello.f77](variants/ext-f77-2e663737/hello.f77) creato, verifiche pendenti |
| `.for` | [hello.for](variants/ext-for-2e666f72/hello.for) creato, verifiche pendenti |
| `.fpp` | [hello.fpp](variants/ext-fpp-2e667070/hello.fpp) creato, verifiche pendenti |
