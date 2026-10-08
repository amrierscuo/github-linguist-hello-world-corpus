# #140 Crystal

Voce canonica: `Crystal`, tipo `programming`, `language_id: 72`.

Interpolare il destinatario in una stringa Crystal, compilarla in un eseguibile nativo e stamparla.

## Toolchain e riproduzione

Native Crystal Ubuntu compiler extracted locally — Crystal 1.11.2 (2024-04-01); ; LLVM: 17.0.6; Default target: x86_64-pc-linux-gnu. Ambiente della prova: **Ubuntu 24.04 WSL2/Linux x86_64**.

Crystal 1.11.2 dal pacchetto Ubuntu, estratto localmente con GC/libevent e librerie richieste. Per questo pacchetto estratto impostare CRYSTAL_PATH verso usr/lib/crystal/lib e LD_LIBRARY_PATH/LIBRARY_PATH alle librerie locali. Non sono installate dipendenze globali.

Comando/procedura dalla directory dell’esempio, salvo la directory build esplicitamente indicata:

```text
crystal build hello.cr -o build/hello; ./build/hello
```

Risultato atteso: Compilazione exit 0; stdout esattamente Hello, World! seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Il sorgente usa interpolazione #{target} e puts. Il log cattura la vera toolchain Crystal; eventuali problemi di dipendenze native non vengono confusi con un esito positivo sul sorgente.

Requisiti residui:

- Native verification did not complete successfully; see genuine command output.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
versioni/toolchain e SHA-256 degli artefatti. La proprietà `path_normalization` documenta
le sostituzioni dei percorsi locali. `<corpus>` identifica i file relativi inclusi nel
corpus finale, che sono stati verificati prima nella directory di staging. I byte dei
sorgenti restano quelli identificati dai checksum. I soli probe di disponibilità degli
strumenti non attestano parsing o esecuzione. Dipendenze e prodotti compilati restano
nella directory di lavoro e non sono inclusi nel corpus.

## Fonti primarie

- [https://crystal-lang.org/reference/1.11/](https://crystal-lang.org/reference/1.11/)
- [https://crystal-lang.org/reference/1.11/syntax_and_semantics/literals/string.html](https://crystal-lang.org/reference/1.11/syntax_and_semantics/literals/string.html)
- [https://crystal-lang.org/reference/1.11/man/crystal/index.html](https://crystal-lang.org/reference/1.11/man/crystal/index.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cr` | [hello.cr](hello.cr) creato, verifiche pendenti |
