# #128 CoNLL-U

Voce canonica: `CoNLL-U`, tipo `data`, `language_id: 421026389`.

Rappresentare Hello, World! come quattro token CoNLL-U con un albero UD e ricostruire esattamente il testo usando SpaceAfter.

## Toolchain e riproduzione

Original Universal Dependencies udtools validator and existing conllu reader — 0.2.8; 6.0.0. Ambiente della prova: **Windows x64**.

In un venv: python -m pip install udtools==0.2.8 conllu==6.0.0. udvalidate è l’entry point del pacchetto originale UniversalDependencies/tools. La prova locale invoca la medesima funzione udtools.cli.main dal Python isolato sotto work.

Comando/procedura dalla directory dell’esempio, salvo la directory build esplicitamente indicata:

```text
udvalidate --lang en --level 3 hello.conllu; python verify.py hello.conllu
```

Risultato atteso: Validatore originale: *** PASSED ***; ricostruzione Hello, World!; PASS delle asserzioni sul token World e sulla radice.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il validatore originale verifica livello 3: formato, albero e annotazioni universali. Non si dichiara validazione linguistica completa dei livelli successivi. verify.py usa il parser conllu esistente e controlla detokenizzazione, radice e vocative; le annotazioni sono un piccolo esempio didattico originale, non una treebank esterna.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
versioni/toolchain e SHA-256 degli artefatti. La proprietà `path_normalization` documenta
le sostituzioni dei percorsi locali. `<corpus>` identifica i file relativi inclusi nel
corpus finale, che sono stati verificati prima nella directory di staging. I byte dei
sorgenti restano quelli identificati dai checksum. I soli probe di disponibilità degli
strumenti non attestano parsing o esecuzione. Dipendenze e prodotti compilati restano
nella directory di lavoro e non sono inclusi nel corpus.

## Fonti primarie

- [https://universaldependencies.org/format.html](https://universaldependencies.org/format.html)
- [https://github.com/UniversalDependencies/tools/tree/master/udtools](https://github.com/UniversalDependencies/tools/tree/master/udtools)
- [https://universaldependencies.org/u/dep/vocative.html](https://universaldependencies.org/u/dep/vocative.html)
- [https://github.com/EmilStenstrom/conllu](https://github.com/EmilStenstrom/conllu)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.conllu` | [hello.conllu](hello.conllu) verificato |
| `.conll` | [hello.conll](variants/ext-conll-2e636f6e6c6c/hello.conll) creato, verifiche pendenti |
