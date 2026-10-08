# #048 Awk

Voce canonica: `Awk`, tipo `programming`, `language_id: 28`.

Eseguire il blocco BEGIN Awk senza input e stampare il saluto concatenato.

## Toolchain e riproduzione

GNU Awk — GNU Awk 5.2.1, API 3.2, PMA Avon 8-g1, (GNU MPFR 4.2.1, GNU MP 6.3.0). Ambiente della prova: **Ubuntu 24.04 WSL2/Linux x86_64**.

Richiede GNU Awk 5.2.1; prova eseguita in Ubuntu 24.04 WSL2.

Comando/procedura dalla directory dell’esempio:

```text
gawk -f hello.awk
```

Risultato atteso: Exit 0; stdout Hello, World! seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il concatenamento Awk si esprime affiancando stringhe; BEGIN esegue il programma prima della lettura dei record.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain e SHA-256 degli artefatti. `path_normalization` descrive le sostituzioni dei
percorsi della macchina; i byte dei sorgenti restano quelli identificati dai checksum.
Se il log registra solo disponibilità degli strumenti, nessun parsing o runtime è attestato.
Gli strumenti, le dipendenze e i prodotti di verifica restano nella directory di lavoro.

## Fonti primarie

- [https://www.gnu.org/software/gawk/manual/gawk.html](https://www.gnu.org/software/gawk/manual/gawk.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.awk` | [hello.awk](hello.awk) verificato |
| `.auk` | [hello.auk](variants/ext-auk-2e61756b/hello.auk) creato, verifiche pendenti |
| `.gawk` | [hello.gawk](variants/ext-gawk-2e6761776b/hello.gawk) creato, verifiche pendenti |
| `.mawk` | [hello.mawk](variants/ext-mawk-2e6d61776b/hello.mawk) creato, verifiche pendenti |
| `.nawk` | [hello.nawk](variants/ext-nawk-2e6e61776b/hello.nawk) creato, verifiche pendenti |
