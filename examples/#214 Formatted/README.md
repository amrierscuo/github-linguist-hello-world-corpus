# #214 Formatted

Voce canonica `Formatted`, tipo `data`, language_id `113`.

Rappresentare il saluto come campo di un record a larghezza fissa e leggerlo con un parser esistente secondo il layout dichiarato.

## Toolchain e riproduzione

Existing NumPy genfromtxt fixed-width record parser — 2.3.5. Ambiente della prova: **Windows x64**.

NumPy 2.3.5 su Python 3.13.9. Layout originale: id intero di 3 colonne, greeting di 13 colonne, lunghezza intera di 4 colonne; ogni record termina con LF.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
python -m pip install numpy==2.3.5; python verify.py hello.for
```

Risultato atteso: Un record: id=1, greeting=Hello, World!, length=13; PASS.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Formatted è una categoria ampia di dati nella baseline Linguist: i campioni includono report e tabelle con formati differenti. I flag positivi riguardano esclusivamente questo layout esplicito letto da numpy.genfromtxt; non si attribuisce una grammatica universale alla categoria, né validità EAM/Finnis–Sinclair a questo file.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sorgenti verificati in staging. I soli probe di disponibilità non attestano parsing
o esecuzione. Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://github.com/github-linguist/linguist/tree/main/samples/Formatted](https://github.com/github-linguist/linguist/tree/main/samples/Formatted)
- [https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.for` | [hello.for](hello.for) verificato |
| `.eam.fs` | [hello.eam.fs](variants/ext-eam-fs-2e65616d2e6673/hello.eam.fs) creato, verifiche pendenti |
