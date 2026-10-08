# #205 Fancy

Voce canonica `Fancy`, tipo `programming`, language_id `109`.

Inviare println a una stringa Fancy contenente il saluto.

## Toolchain e riproduzione

Required authentic toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64**.

Richiede il compilatore/runtime Fancy originale e il VM Rubinius compatibile. Nessuna traduzione manuale in Ruby è usata come prova.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
fancy hello.fy
```

Risultato atteso: Una riga Hello, World!.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

La sintassi a invio di messaggi segue il progetto bakkdoor/fancy. Il runtime non è disponibile.

Requisiti residui:

- Fancy and its required Rubinius VM are unavailable.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sorgenti verificati in staging. I soli probe di disponibilità non attestano parsing
o esecuzione. Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://github.com/bakkdoor/fancy](https://github.com/bakkdoor/fancy)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.fy` | [hello.fy](hello.fy), [greeting.fy](variants/ext-fancypack-2e66616e63797061636b/greeting.fy) creato, verifiche pendenti |
| `.fancypack` | [hello.fancypack](variants/ext-fancypack-2e66616e63797061636b/hello.fancypack) creato, verifiche pendenti |
