# #139 Creole

Voce canonica: `Creole`, tipo `prose`, `language_id: 71`.

Renderizzare un documento Creole 1.0 con heading, saluto in grassetto e una frase in corsivo.

## Toolchain e riproduzione

Existing creoleparser Creole 1.0 renderer with Genshi — 0.7.5; 0.7.11. Ambiente della prova: **Windows x64**.

Python 3.13.9, creoleparser 0.7.5 e Genshi 0.7.11. Dipendenze isolate in work; per riprodurre usare un venv. Il renderer restituisce byte UTF-8, che verify.py decodifica prima delle asserzioni.

Comando/procedura dalla directory dell’esempio, salvo la directory build esplicitamente indicata:

```text
python -m pip install creoleparser==0.7.5; python verify.py hello.creole
```

Risultato atteso: HTML con <h1>Greeting</h1>, <strong>Hello, World!</strong> e il controllo <em>A small Creole document.</em>; PASS.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

È il parser/renderer Creole 1.0 esistente, che è permissivo per testo generico. La prova riguarda l’accettazione e il rendering delle tre strutture dichiarate, non un validatore universale strict per tutte le estensioni wiki.

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

- [https://github.com/wikiotics/creoleparser](https://github.com/wikiotics/creoleparser)
- [https://creoleparser.readthedocs.io/en/latest/](https://creoleparser.readthedocs.io/en/latest/)
- [https://www.wikicreole.org/wiki/Creole1.0](https://www.wikicreole.org/wiki/Creole1.0)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.creole` | [hello.creole](hello.creole) verificato |
