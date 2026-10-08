# #135 Component Pascal

Voce canonica: `Component Pascal`, tipo `programming`, `language_id: 67`.

Esportare il comando Hello.Say in Component Pascal e scrivere Hello, World! nel log BlackBox.

## Toolchain e riproduzione

Required native toolchain unavailable or not configured — versione non disponibile / non verificata. Ambiente della prova: **Windows x64**.

Richiede BlackBox Component Builder con la libreria StdLog della stessa distribuzione. Questo modulo sceglie esplicitamente quel runtime Component Pascal; Console di GPCP è una diversa libreria e non viene presupposta.

Comando/procedura dalla directory dell’esempio, salvo la directory build esplicitamente indicata:

```text
BlackBox Component Builder: aprire Hello.cp come modulo di una copia di lavoro; compilare il modulo; invocare il comando Hello.Say e controllare il log.
```

Risultato atteso: Modulo compilato; comando Hello.Say disponibile; log con Hello, World! e newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Say* è una procedura esportata senza argomenti, utilizzabile come comando BlackBox. StdLog.String e StdLog.Ln sono le operazioni di output. La toolchain non è disponibile, quindi non sono dichiarati check positivi.

Requisiti residui:

- BlackBox Component Builder with StdLog library is unavailable; module compilation/invocation is pending.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
versioni/toolchain e SHA-256 degli artefatti. La proprietà `path_normalization` documenta
le sostituzioni dei percorsi locali. `<corpus>` identifica i file relativi inclusi nel
corpus finale, che sono stati verificati prima nella directory di staging. I byte dei
sorgenti restano quelli identificati dai checksum. I soli probe di disponibilità degli
strumenti non attestano parsing o esecuzione. Dipendenze e prodotti compilati restano
nella directory di lavoro e non sono inclusi nel corpus.

## Fonti primarie

- [https://blackboxframework.org/](https://blackboxframework.org/)
- [https://github.com/BlackBoxCenter/blackbox](https://github.com/BlackBoxCenter/blackbox)
- [https://www.oberon.ch/pdf/CP-Lang.pdf](https://www.oberon.ch/pdf/CP-Lang.pdf)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cp` | [Hello.cp](Hello.cp) creato, verifiche pendenti |
| `.cps` | [hello.cps](variants/ext-cps-2e637073/hello.cps) creato, verifiche pendenti |
