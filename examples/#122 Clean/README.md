# #122 Clean

Voce canonica: `Clean`, tipo `programming`, `language_id: 60`.

Aprire lo stream console attraverso il world unico Clean, concatenare il saluto, scriverlo e chiudere lo stream.

## Toolchain e riproduzione

Clean 3.1 stable distribution, local clm — 3.1. Ambiente della prova: **Ubuntu 24.04 WSL2/Linux x86_64**.

Distribuzione ufficiale Clean 3.1 Linux x86_64, installata con make in una directory di lavoro. Se clm non risolve i percorsi interni, impostare CLEANLIB=<clean>/lib/exe, CLEANPATH=<clean>/lib/StdEnv e CLEANILIB=<clean>/lib. Compilare una copia di Hello.icl: clm crea i suoi prodotti accanto al modulo.

Comando/procedura dalla directory dell’esempio, salvo la directory build esplicitamente indicata:

```text
clm -nr -nt -nw Hello -o hello; ./hello
```

Risultato atteso: Compilazione riuscita; stdout esattamente Hello, World! seguito da LF.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Start passa il valore *World a stdio e fclose, rispettando la disciplina di unicità. -nr disabilita la stampa automatica del valore finale world da parte del runtime; -nt disabilita il timing. La prova cattura il vero compilatore Clean e la toolchain locale.

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

- [https://clean.cs.ru.nl/Download_Clean](https://clean.cs.ru.nl/Download_Clean)
- [https://clean.cs.ru.nl/*NIX_Instructions](https://clean.cs.ru.nl/*NIX_Instructions)
- [https://clean.cs.ru.nl/Clean_language_report](https://clean.cs.ru.nl/Clean_language_report)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.icl` | [Hello.icl](Hello.icl), [Consumer.icl](variants/ext-dcl-2e64636c/Consumer.icl), [Greeting.icl](variants/ext-dcl-2e64636c/Greeting.icl) creato, verifiche pendenti |
| `.dcl` | [Greeting.dcl](variants/ext-dcl-2e64636c/Greeting.dcl) creato, verifiche pendenti |
