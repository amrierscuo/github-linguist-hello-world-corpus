# #054 BBCode

Voce canonica: `BBCode`, tipo `markup`, `language_id: 206921123`.

Renderizzare il saluto BBCode come testo in grassetto, ottenendo HTML strong con Hello, World!.

## Toolchain e riproduzione

Original dcwatson/bbcode Python parser/renderer — 1.1.0. Ambiente della prova: **Windows x64**.

Toolchain: Python 3.13.9 e parser/renderer dcwatson/bbcode 1.1.0. Qui la dipendenza è isolata in work; per la riproduzione si può installarla in un venv.

Comando/procedura dalla directory dell’esempio:

```text
python -m pip install bbcode==1.1.0; python verify.py hello.bbcode
```

Risultato atteso: Exit 0; <strong>Hello, World!</strong>; PASS del saluto bold e controllo italic.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

BBCode non ha una grammatica universale unica. Lo stato positivo riguarda l’accettazione e la resa dei tag b/i da parte di questa libreria esistente, che è permissiva; non è un validatore strict per tutti i forum.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain e SHA-256 degli artefatti. `path_normalization` descrive le sostituzioni dei
percorsi della macchina; i byte dei sorgenti restano quelli identificati dai checksum.
Se il log registra solo disponibilità degli strumenti, nessun parsing o runtime è attestato.
Gli strumenti, le dipendenze e i prodotti di verifica restano nella directory di lavoro.

## Fonti primarie

- [https://bbcode.readthedocs.io/en/latest/](https://bbcode.readthedocs.io/en/latest/)
- [https://github.com/dcwatson/bbcode](https://github.com/dcwatson/bbcode)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bbcode` | [hello.bbcode](hello.bbcode) verificato |
