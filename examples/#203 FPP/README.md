# #203 FPP

Voce canonica `FPP`, tipo `programming`, language_id `252360067`.

Dichiarare una costante stringa Greeting nel modulo Corpus del linguaggio NASA FPP.

## Toolchain e riproduzione

Required authentic toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64**.

Richiede gli strumenti autentici NASA FPP. La build corrente upstream usa Scala/sbt e JDK 25; non sono configurati qui. Il modello è una dichiarazione FPP, quindi l’obiettivo è il valore della costante, non un processo console autonomo.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
fpp-check hello.fpp; fpp-to-xml -d build hello.fpp
```

Risultato atteso: FPP accettato; costante Corpus.Greeting uguale a Hello, World!.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Il saluto è il valore effettivo della costante. Nessun parser XML o YAML generico sostituisce fpp-check.

Requisiti residui:

- FPP analysis/translation tools are unavailable; current upstream build requires Scala sbt and JDK 25.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sorgenti verificati in staging. I soli probe di disponibilità non attestano parsing
o esecuzione. Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://nasa.github.io/fpp/fpp-spec.html](https://nasa.github.io/fpp/fpp-spec.html)
- [https://nasa.github.io/fpp/fpp-users-guide.html](https://nasa.github.io/fpp/fpp-users-guide.html)
- [https://github.com/nasa/fpp](https://github.com/nasa/fpp)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.fpp` | [hello.fpp](hello.fpp), [consumer.fpp](variants/ext-fppi-2e66707069/consumer.fpp) creato, verifiche pendenti |
| `.fppi` | [hello.fppi](variants/ext-fppi-2e66707069/hello.fppi) creato, verifiche pendenti |
