# #273 Groovy Server Pages

Voce canonica `Groovy Server Pages`, tipo `programming`, language_id `143`.

Renderizzare una pagina GSP text/plain interpolando la variabile di modello name.

## Toolchain e riproduzione

Required genuine toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede il motore nativo Grails Groovy Server Pages e un contesto applicazione web. Posizionare hello.gsp in grails-app/views e fornire il modello dal controller.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
Applicazione Grails locale: render(view: "/hello", model: [name: "World"]); richiedere la route locale e confrontare il body
```

Risultato atteso: Risposta text/plain Hello, World!.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

La direttiva page e l’espressione ${name} sono GSP reali. Un renderer Groovy generico non dimostrerebbe la gestione della direttiva o il motore Grails; nessuno viene usato come prova.

Requisiti residui:

- Native Grails GSP engine and web application context are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://grails.apache.org/docs-legacy-gsp/6.0.0-M1/guide/](https://grails.apache.org/docs-legacy-gsp/6.0.0-M1/guide/)
- [https://grails.apache.org/guides/creating-your-first-grails-app/4/guide/index.html](https://grails.apache.org/guides/creating-your-first-grails-app/4/guide/index.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.gsp` | [hello.gsp](hello.gsp) creato, verifiche pendenti |
