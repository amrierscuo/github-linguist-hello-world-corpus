# #264 Gosu

Voce canonica `Gosu`, tipo `programming`, language_id `134`.

Definire la classe Gosu Hello con un main statico che concatena e stampa il saluto.

## Toolchain e riproduzione

Required genuine toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede il compiler e runtime Gosu compatibili. Hello.gs è una classe Gosu; usare il launcher della distribuzione per caricarla e chiamare il main, registrando il comando effettivo.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
Toolchain Gosu: aggiungere la directory della classe al classpath e invocare Hello.main(new String[0]) dal launcher/host della distribuzione
```

Risultato atteso: Classe accettata; invocazione main emette Hello, World!.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

La quickstart ufficiale indica Gosu Lab e un JDK compatibile. La toolchain non è configurata; non viene interpretato il file come Groovy/Java.

Requisiti residui:

- Gosu compiler/runtime is not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://gosu-lang.github.io/quickstart.html](https://gosu-lang.github.io/quickstart.html)
- [https://github.com/gosu-lang/gosu-lang](https://github.com/gosu-lang/gosu-lang)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.gs` | [Hello.gs](Hello.gs) creato, verifiche pendenti |
| `.gst` | [hello.gst](variants/ext-gst-2e677374/hello.gst) creato, verifiche pendenti |
| `.gsx` | [CorpusGreeting.gsx](variants/ext-gsx-2e677378/CorpusGreeting.gsx) creato, verifiche pendenti |
| `.vark` | [hello.vark](variants/ext-vark-2e7661726b/hello.vark) creato, verifiche pendenti |
