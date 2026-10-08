# #532 Perl

Voce canonica `Perl`, tipo `programming`, language_id `282`.

Eseguire un programma Perl con interpolazione del parametro World.

## Toolchain e riproduzione

Authentic Perl interpreter — This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Perl autentico disponibile in Ubuntu WSL, versione nel log.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
perl -c hello.pl; perl hello.pl
```

Risultato atteso: Il risultato conforme contiene Hello, World!, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Syntax check e runtime reali, stdout esatto.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://perldoc.perl.org/perlintro](https://perldoc.perl.org/perlintro)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pl` | [hello.pl](hello.pl), [driver.pl](variants/ph-d462b572/driver.pl), [driver.pl](variants/pm-c810ce30/driver.pl) creato, verifiche pendenti |
| `.al` | [greeting.al](variants/al-ceb20bd5/greeting.al) sintassi verificata |
| `.cgi` | [hello.cgi](variants/cgi-89feb572/hello.cgi) verificato |
| `.fcgi` | [hello.fcgi](variants/fcgi-209194e4/hello.fcgi) creato, verifiche pendenti |
| `.perl` | [hello.perl](variants/perl-ffad7d6b/hello.perl) verificato |
| `.ph` | [hello.ph](variants/ph-d462b572/hello.ph) verificato |
| `.plx` | [hello.plx](variants/plx-e52b193c/hello.plx) verificato |
| `.pm` | [Greeting.pm](variants/pm-c810ce30/Corpus/Greeting.pm) verificato |
| `.psgi` | [hello.psgi](variants/psgi-c2b00512/hello.psgi) creato, verifiche pendenti |
| `.t` | [hello.t](variants/t-3c247edb/hello.t) verificato |
