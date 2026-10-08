# #212 Flix

Voce canonica `Flix`, tipo `programming`, language_id `800935960`.

Controllare tipi/effetti del programma Flix e stampare una concatenazione nel main con effetto IO.

## Toolchain e riproduzione

Official Flix compiler and JVM code generator — The Flix Programming Language 0.77.0. Ambiente della prova: **Windows x64**.

Flix ufficiale 0.77.0 e JDK 21. L’inizializzazione crea il progetto di lavoro; mantenere una sola definizione main. I comandi check/run operano sul progetto e non accettano gli stessi argomenti file.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
In una copia di lavoro: java -jar flix.jar init; sostituire src/Main.flix con Main.flix; java -jar flix.jar check --no-install --threads 2; java -jar flix.jar run --no-install --threads 2
```

Risultato atteso: Check exit 0; run exit 0; stdout Hello, World! seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il log attesta check e run riusciti sul progetto contenente una copia identica del sorgente. La risoluzione delle dipendenze del progetto inizializzato produce diagnostica su stderr, senza impedire l’esecuzione.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sorgenti verificati in staging. I soli probe di disponibilità non attestano parsing
o esecuzione. Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://doc.flix.dev/getting-started.html](https://doc.flix.dev/getting-started.html)
- [https://doc.flix.dev/build-and-packages.html](https://doc.flix.dev/build-and-packages.html)
- [https://flix.dev/](https://flix.dev/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.flix` | [Main.flix](Main.flix) verificato |
