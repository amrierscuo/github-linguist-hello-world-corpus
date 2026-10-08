# #790 XS

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Compilare un’estensione Perl XS e leggere Hello, World! dalla funzione C.

xsubpp interpreta davvero Greeting.xs; GCC genera una libreria condivisa poi importata con XSLoader. La funzione XS viene chiamata da Perl e il suo valore confrontato. Output binari restano nella build temporanea.

## Toolchain e riproduzione

Perl5.38.2/xsubpp/ExtUtils::MakeMaker originali, GCC e header libperl-dev isolati

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
perl Makefile.PL; make; perl verify.pl
```

## Risultato atteso e stato

Corpus::Greeting::greeting() restituisce Hello, World!.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://perldoc.perl.org/perlxs

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.xs` | [Greeting.xs](Greeting.xs) verificato |
