# #288 Hack

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Eseguire il punto di ingresso Hack e stampare Hello, World!.

Il sorgente Hack dichiara <<__EntryPoint>> e main():void, con concatenazione ed echo. Il tag <?hh non è richiesto nei file .hack moderni. PHP non verifica questo punto di ingresso o il sistema di tipi Hack.

## Toolchain e riproduzione

HHVM/Hack e typechecker hh_client; versioni effettive da registrare

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
Con progetto Hack appropriato: hh_client
```

```text
hhvm hello.hack
```

## Risultato atteso e stato

stdout Hello, World! seguito da newline.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compilatore/runtime nativo eseguito per questa voce.

Impedimenti: HHVM/Hack e il typechecker non disponibili; verifiche pendenti.

## Fonti primarie

- https://docs.hhvm.com/hack/source-code-fundamentals/program-structure/
- https://hacklang.org/

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.hack` | [hello.hack](hello.hack), [driver.hack](variants/hhi-b673df30/driver.hack) creato, verifiche pendenti |
| `.hh` | [hello.hh](variants/hh-bc9ff2ca/hello.hh) creato, verifiche pendenti |
| `.hhi` | [hello.hhi](variants/hhi-b673df30/hello.hhi) creato, verifiche pendenti |
| `.php` | [hello.php](variants/php-7410d4a4/hello.php) creato, verifiche pendenti |
