# #190 Elixir

Eseguire uno script Elixir che stampa Hello, World! seguito da newline.

Tipo canonico `programming`, language_id `100`.

Toolchain prevista: Elixir 1.x con Erlang/OTP compatibile.

Dalla cartella dell’esempio:

```sh
elixir hello.exs
```

Risultato atteso: stdout esatto `Hello, World!\n`, uscita 0.

Lo script non avvia applicazioni di rete. Il comando richiede anche il runtime Erlang della distribuzione.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Elixir 1.14.0 + Erlang OTP 25 / ERTS 13.2.2.5 Linux original packages. Vedere [log](verification/verification.log). 

Fonti del linguaggio/formato e implementazioni originali:

- [Elixir — introduzione](https://elixir.hexdocs.pm/introduction.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ex` | [hello.ex](variants/ext-ex-2e6578/hello.ex) creato, verifiche pendenti |
| `.exs` | [hello.exs](hello.exs) verificato |
