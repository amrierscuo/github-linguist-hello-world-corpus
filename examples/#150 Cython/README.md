# #150 Cython

Voce canonica e ordine del `reference/languages.yml` del corpus. I sorgenti e fixture sono originali; eventuali dump/bundle provengono dagli strumenti indicati.

## Obiettivo

Compilare un modulo Cython con variabile cdef str e stamparne il valore durante l’import.

Il parser/compiler Cython genera C da hello.pyx; un compilatore C costruisce un’estensione CPython reale e Python la importa. Nel log la compilazione GCC usa header Python isolati ed esegue il .so in WSL. setup.py offre il normale percorso setuptools per riprodurre la build con Cython e un toolchain C disponibili.

## Toolchain e riproduzione

Cython 3.3.0; GNU C 13.3.0; CPython 3.12.3 Ubuntu WSL (generazione C su Windows Python 3.13.9)

Comandi nella cartella dell’esempio con la toolchain disponibile nel PATH. Usare una copia temporanea: database, oggetti, audio e altri output di prova non appartengono al corpus.

```text
python setup.py build_ext --inplace
```

```text
python -c "import hello"
```

## Risultato atteso e stato

stdout esatto Hello, World! seguito da newline; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra versioni e provenienza, SHA-256 dei sorgenti, comandi effettivi, exit, stdout e stderr normalizzati.

## Fonti primarie

- https://docs.cython.org/en/latest/src/userguide/source_files_and_compilation.html
- https://github.com/cython/cython

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pyx` | [hello.pyx](hello.pyx), [hello.pyx](variants/ext-pxd-2e707864/hello.pyx), [consumer.pyx](variants/ext-pxi-2e707869/consumer.pyx) creato, verifiche pendenti |
| `.pxd` | [hello.pxd](variants/ext-pxd-2e707864/hello.pxd) creato, verifiche pendenti |
| `.pxi` | [hello.pxi](variants/ext-pxi-2e707869/hello.pxi) creato, verifiche pendenti |
