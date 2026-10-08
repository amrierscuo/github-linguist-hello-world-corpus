# #209 Filebench WML

Voce canonica `Filebench WML`, tipo `programming`, language_id `111`.

Usare il comando echo del Workload Model Language Filebench per emettere il saluto, senza workload di I/O.

## Toolchain e riproduzione

Required authentic toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64**.

Richiede Filebench. L’esempio non crea file dati o processi worker e non cambia parametri di sistema. Il tool non è disponibile.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
filebench -f hello.f
```

Risultato atteso: File WML accettato; output Filebench contenente Hello, World!.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Il saluto è un argomento del comando WML echo; manca la prova del vero parser/runtime.

Requisiti residui:

- Filebench WML parser/runtime is unavailable.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sorgenti verificati in staging. I soli probe di disponibilità non attestano parsing
o esecuzione. Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://github.com/filebench/filebench/wiki/Workload-model-language](https://github.com/filebench/filebench/wiki/Workload-model-language)
- [https://github.com/filebench/filebench](https://github.com/filebench/filebench)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.f` | [hello.f](hello.f) creato, verifiche pendenti |
