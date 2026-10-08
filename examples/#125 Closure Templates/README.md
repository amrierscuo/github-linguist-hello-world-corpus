# #125 Closure Templates

Voce canonica: `Closure Templates`, tipo `markup`, `language_id: 357046146`.

Compilare il template Soy parametrico e renderizzare Hello, World! in modalità text; verificare anche Hello, Reader! cambiando il parametro.

## Toolchain e riproduzione

Official Google Closure Templates SoyFileSet compiler and SoyTofu renderer — 2024-02-26. Ambiente della prova: **Windows x64**.

Scaricare il JAR ufficiale Maven com.google.template:soy:2024-02-26 con classifier SoyToJsSrcCompiler in .tools. Contiene anche SoyFileSet/SoyTofu e le dipendenze Java. Richiede un JDK; qui è stato usato OpenJDK 21.0.12.1.

Comando/procedura dalla directory dell’esempio, salvo la directory build esplicitamente indicata:

```text
java --class-path .tools/soy-2024-02-26-SoyToJsSrcCompiler.jar SoyCheck.java hello.soy
```

Risultato atteso: Exit 0; Hello, World! e PASS: official Soy compile/render and parameter control.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

SoyCheck.java delega parsing, typecheck e rendering alle API ufficiali Soy. Due avvisi di deprecazione delle API legacy SoyFileSet.builder/compileToTofu non impediscono la verifica positiva. Il testo renderizzato viene confrontato esattamente per due valori del parametro.

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

- [https://github.com/google/closure-templates](https://github.com/google/closure-templates)
- [https://github.com/google/closure-templates/blob/master/documentation/reference/templates.md](https://github.com/google/closure-templates/blob/master/documentation/reference/templates.md)
- [https://repo.maven.apache.org/maven2/com/google/template/soy/2024-02-26/](https://repo.maven.apache.org/maven2/com/google/template/soy/2024-02-26/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.soy` | [hello.soy](hello.soy) verificato |
