# #204 Factor

Voce canonica `Factor`, tipo `programming`, language_id `108`.

Concatenare due stringhe sullo stack Factor e stampare il saluto.

## Toolchain e riproduzione

Required authentic toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64**.

Richiede il VM del linguaggio Factor e la sua immagine/librerie. Usare l’eseguibile della distribuzione factorcode.org, evitando l’omonimo comando GNU di fattorizzazione intera.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
factor hello.factor
```

Risultato atteso: Una riga Hello, World!.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

USING importa io e sequences; append concatena le stringhe prima di print. Il VM è assente.

Requisiti residui:

- Factor language VM/image is unavailable; GNU coreutils factor would not verify Factor language.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sorgenti verificati in staging. I soli probe di disponibilità non attestano parsing
o esecuzione. Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://factorcode.org/](https://factorcode.org/)
- [https://github.com/factor/factor](https://github.com/factor/factor)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.factor` | [hello.factor](hello.factor) creato, verifiche pendenti |
