# #220 Frege

Voce canonica `Frege`, tipo `programming`, language_id `116`.

Compilare il modulo funzionale Frege Hello in bytecode JVM e invocarne il main.

## Toolchain e riproduzione

Official Frege compiler and runtime JVM jar — 3.25.153; commit 2abfb8f17a795185503b537625afc0cd57e1fac9; Merge: 067cad05 ea4fe246; Author: Ingo Wechsung ; Date:   Sat Jul 11 10:33:45 2026 +0200; ;     Merge pull request #401 from poeik/native-gen-fixes;     ;     Native gen fixes. Ambiente della prova: **Windows x64**.

Frege ufficiale 3.25.153 e JDK 21 su Windows. Su Linux il separatore classpath è : invece di ;. Java generato e classi rimangono in build.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
java -jar .tools/frege-3.25.153.jar -d build Hello.fr; java -cp ".tools/frege-3.25.153.jar;build" Hello
```

Risultato atteso: Compiler exit 0; esecuzione Hello exit 0 e saluto esatto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il compiler Frege ha prodotto e compilato il vero Java; il secondo comando esegue quelle classi con il runtime Frege. Non viene eseguito un equivalente Java scritto a mano.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sorgenti verificati in staging. I soli probe di disponibilità non attestano parsing
o esecuzione. Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://github.com/Frege/frege](https://github.com/Frege/frege)
- [https://github.com/Frege/frege/wiki/Getting-Started](https://github.com/Frege/frege/wiki/Getting-Started)
- [https://repo.maven.apache.org/maven2/org/frege-lang/frege/3.25.153/](https://repo.maven.apache.org/maven2/org/frege-lang/frege/3.25.153/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.fr` | [Hello.fr](Hello.fr) verificato |
