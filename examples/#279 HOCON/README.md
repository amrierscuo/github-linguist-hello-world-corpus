# #279 HOCON

Voce canonica `HOCON`, tipo `data`, language_id `679725279`.

Risolvere una sostituzione HOCON e una concatenazione per ottenere il saluto.

## Toolchain e riproduzione

Official Lightbend/Typesafe Config HOCON implementation — 1.4.3. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Typesafe/Lightbend Config 1.4.3 ufficiale da Maven Central e JDK 21. Il Java helper chiama ConfigFactory.parseFile(...).resolve().

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
java --class-path .tools/config-1.4.3.jar HoconCheck.java hello.hocon
```

Risultato atteso: Hello, World! e PASS: official HOCON parser, concatenation and substitution resolution.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il valore message combina un frammento letterale, ${target} e un punto esclamativo. Il parser e il resolver autentici producono e verificano il valore finale.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://github.com/lightbend/config/blob/main/HOCON.md](https://github.com/lightbend/config/blob/main/HOCON.md)
- [https://github.com/lightbend/config](https://github.com/lightbend/config)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.hocon` | [hello.hocon](hello.hocon) verificato |
