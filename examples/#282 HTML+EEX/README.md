# #282 HTML+EEX

Voce e ordine canonici del `reference/languages.yml` del corpus. Sorgenti e fixture sono originali.

## Obiettivo

Renderizzare HTML+EEx e sostituire audience con World.

EEx.eval_file analizza il template ed esegue l’espressione con binding audience. Il renderer è EEx originale. Il launcher della prova imposta ROOTDIR/BINDIR per l’ERTS isolato e poi esegue erlexec originale; non sostituisce parser o renderer.

## Toolchain e riproduzione

Elixir1.14.0, Erlang/OTP25 e ERTS13.2.2.5, pacchetti Ubuntu

Comandi nella cartella dell’esempio con gli strumenti disponibili nel PATH. Usare una copia temporanea per build e output; le dipendenze della prova sono isolate in work.

```text
elixir render.exs
```

## Risultato atteso e stato

stdout <p>Hello, World!</p> seguito da newline; exit 0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra provenienza/versioni, SHA-256 dei sorgenti, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://hexdocs.pm/eex/EEx.html
- https://elixir-lang.org/

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.html.eex` | [hello.html.eex](hello.html.eex) verificato |
| `.heex` | [hello.heex](variants/heex-06f63f97/hello.heex) creato, verifiche pendenti |
| `.leex` | [hello.leex](variants/leex-34ca1cfe/hello.leex) creato, verifiche pendenti |
