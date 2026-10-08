# #770 Whiley

Voce canonica `Whiley`, tipo `programming`, language_id `888779559`.

Funzione pura Whiley originale greeting() che restituisce il saluto come array di code point interi, conforme al modello di stringhe della specifica Whiley.

## Toolchain e riproduzione

Whiley Compiler / verification backend — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Occorre la distribuzione ufficiale Whiley con compilatore e backend compatibili. La guida ufficiale documenta wy init e wy build. Nessun compilatore è stato installato per questa voce.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
In un progetto Whiley temporaneo: wy init; copiare hello.whiley in src/hello.whiley; wy build; valutare hello.greeting() con il runtime Whiley.
```

Risultato atteso: Array di 13 code point corrispondente a Hello, World!.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Sorgente creato da specifica: la lettura del file non è conteggiata come verifica sintattica. La compilazione e il confronto del risultato restituito restano in attesa.

Requisiti residui:

- Compilatore Whiley e backend di verifica assenti; funzione pura definita ma non compilata.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://whiley.org/pdfs/WhileyLanguageSpec.pdf](https://whiley.org/pdfs/WhileyLanguageSpec.pdf)
- [https://whiley.org/learn/](https://whiley.org/learn/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.whiley` | [hello.whiley](hello.whiley) creato, verifiche pendenti |
