# 0216 Fortran — variante `.fpp`

Ruolo: Fortran fixed form; il ruolo del .fpp include preprocessamento ma il modello non richiede macro.

Tipo variante: **alias**. Copia byte-identica di examples/#216 Fortran/hello.f

Copia byte-identica del modello dichiarato: l’uguaglianza dei byte non equivale a una nuova prova della toolchain sul nuovo suffisso.

## Comando o procedura di verifica

Dalla directory della variante, salvo i riferimenti espliciti al modello. `<output>`
indica una directory temporanea esterna; dipendenze e prodotti compilati non fanno
parte del deliverable.

```text
gfortran -x f77 -ffixed-form -cpp hello.fpp -o <output>/hello; <output>/hello
```

Risultato atteso: Compilazione/run exit 0; saluto esatto seguito da newline.

## Stato

Artefatto: **creato**.
Sintassi: **non verificata**. Semantica: **non verificata**.
Nessun flag positivo viene ereditato dal campione principale o da un altro suffisso.
Il solo controllo dei byte/metadati non viene presentato come parsing o esecuzione.

Requisiti residui:
- La variante non è ancora stata controllata con la toolchain nativa indicata.

## Fonti primarie

- [https://gcc.gnu.org/onlinedocs/gfortran/Fortran-Dialect-Options.html](https://gcc.gnu.org/onlinedocs/gfortran/Fortran-Dialect-Options.html)
- [https://gcc.gnu.org/onlinedocs/gfortran/](https://gcc.gnu.org/onlinedocs/gfortran/)
- [https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml](https://github.com/github-linguist/linguist/blob/main/lib/linguist/languages.yml)
