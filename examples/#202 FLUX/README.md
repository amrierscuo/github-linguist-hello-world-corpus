# #202 FLUX

Voce canonica `FLUX`, tipo `programming`, language_id `106`.

Definire in UMass FLUX una sorgente GetGreeting e un nodo PrintGreeting collegati da un flusso; le implementazioni C++ stampano il primo evento e terminano.

## Toolchain e riproduzione

Required authentic toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64**.

Richiede il compilatore Java storico di emeryberger/flux, le dipendenze della distribuzione e il driver C++ generato. Seguire la procedura upstream per il backend thread. mImpl.h è prodotto dal generatore e non viene inventato nel corpus.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
Nel checkout ufficiale Flux: ant; java -cp bin:lib/jdsl.jar:lib/javacuplex.jar:lib/getopt.jar edu.umass.cs.flux.Main -r build/server -t hello.fx; copiare mImpl.cpp nel server generato; compilare il server C++ generato con pthread; eseguirlo
```

Risultato atteso: Generazione/compilazione riuscite; server emette una riga Hello, World! e termina 0.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Questa voce è FLUX per server ad alte prestazioni e flussi di task. Le firme GetGreeting_out e PrintGreeting_in seguono il backend originale. La terminazione dopo il primo evento evita un loop illimitato della sorgente; senza toolchain non sono attribuiti flag positivi.

Requisiti residui:

- Historical UMass Flux Java compiler and generated C++ runtime are not built; mImpl.cpp depends on generated mImpl.h.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sorgenti verificati in staging. I soli probe di disponibilità non attestano parsing
o esecuzione. Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://github.com/emeryberger/flux](https://github.com/emeryberger/flux)
- [https://www.usenix.org/legacy/event/usenix06/tech/full_papers/burns/burns_html/__flux-usenix-06.html](https://www.usenix.org/legacy/event/usenix06/tech/full_papers/burns/burns_html/__flux-usenix-06.html)
- [https://github.com/github-linguist/linguist/tree/main/samples/FLUX](https://github.com/github-linguist/linguist/tree/main/samples/FLUX)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.fx` | [hello.fx](hello.fx) creato, verifiche pendenti |
| `.flux` | [hello.flux](variants/ext-flux-2e666c7578/hello.flux) creato, verifiche pendenti |
