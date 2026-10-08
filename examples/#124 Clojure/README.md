# #124 Clojure

Voce canonica: `Clojure`, tipo `programming`, `language_id: 62`.

Concatenare le due parti del saluto in una binding let Clojure e stamparle con println.

## Toolchain e riproduzione

Official Clojure JVM runtime — 1.12.0. Ambiente della prova: **Windows x64**.

Mettere in .tools i JAR ufficiali clojure 1.12.0, spec.alpha 0.5.238 e core.specs.alpha 0.4.74 dal Maven Central. Il wildcard classpath funziona con java su Windows e Linux. Prova con Microsoft OpenJDK 21.0.12.1.

Comando/procedura dalla directory dell’esempio, salvo la directory build esplicitamente indicata:

```text
java -cp ".tools/*" clojure.main hello.clj
```

Risultato atteso: Exit 0; stdout esattamente Hello, World! seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il runtime Clojure autentico legge e compila le forme del file originale prima di eseguirle; il log lega i tre JAR con SHA-256. Non serve un progetto Leiningen o una installazione globale della CLI.

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

- [https://clojure.org/reference/repl_and_main](https://clojure.org/reference/repl_and_main)
- [https://clojure.org/reference/special_forms#let](https://clojure.org/reference/special_forms#let)
- [https://repo.maven.apache.org/maven2/org/clojure/clojure/1.12.0/](https://repo.maven.apache.org/maven2/org/clojure/clojure/1.12.0/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.clj` | [hello.clj](hello.clj) verificato |
| `.bb` | [hello.bb](variants/ext-bb-2e6262/hello.bb) creato, verifiche pendenti |
| `.boot` | [hello.boot](variants/ext-boot-2e626f6f74/hello.boot) creato, verifiche pendenti |
| `.cl2` | [hello.cl2](variants/ext-cl2-2e636c32/hello.cl2) creato, verifiche pendenti |
| `.cljc` | [hello.cljc](variants/ext-cljc-2e636c6a63/hello.cljc) creato, verifiche pendenti |
| `.cljs` | [hello.cljs](variants/ext-cljs-2e636c6a73/hello.cljs) creato, verifiche pendenti |
| `.cljs.hl` | [hello.cljs.hl](variants/ext-cljs-hl-2e636c6a732e686c/hello.cljs.hl) creato, verifiche pendenti |
| `.cljscm` | [hello.cljscm](variants/ext-cljscm-2e636c6a73636d/hello.cljscm) creato, verifiche pendenti |
| `.cljx` | [hello.cljx](variants/ext-cljx-2e636c6a78/hello.cljx) creato, verifiche pendenti |
| `.hic` | [hello.hic](variants/ext-hic-2e686963/hello.hic) creato, verifiche pendenti |
