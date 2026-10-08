# #268 Grammatical Framework

Voce canonica `Grammatical Framework`, tipo `programming`, language_id `137`.

Definire una grammatica GF con un albero astratto Hello e linearizzarlo nella concrete syntax inglese.

## Toolchain e riproduzione

Required genuine toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede Grammatical Framework. Greeting.gf dichiara la categoria Message e il costruttore Hello; GreetingEng.gf usa la lincat Str senza dipendere da RGL.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
gf -make GreetingEng.gf; gf GreetingEng.gf; nella shell GF: l Hello
```

Risultato atteso: Grammatica compilata; l Hello restituisce Hello, World!.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

L’obiettivo semantico è la linearizzazione dell’albero, non un programma console generale. La toolchain GF è assente.

Requisiti residui:

- GF compiler and interactive grammar runtime are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.grammaticalframework.org/doc/gf-refman.html](https://www.grammaticalframework.org/doc/gf-refman.html)
- [https://www.grammaticalframework.org/doc/gf-shell-reference.html](https://www.grammaticalframework.org/doc/gf-shell-reference.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.gf` | [Greeting.gf](Greeting.gf), [GreetingEng.gf](GreetingEng.gf) creato, verifiche pendenti |
