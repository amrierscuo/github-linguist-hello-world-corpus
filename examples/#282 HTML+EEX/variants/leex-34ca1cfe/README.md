# 0282 — HTML+EEX: `.leex`

Ruolo: Template Live EEx storico per Phoenix.LiveView.Engine 0.11; necessita della versione storica compatibile.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Elixir1.14.0, Erlang/OTP25 e ERTS13.2.2.5, pacchetti Ubuntu. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Phoenix.LiveView.Engine 0.11: compilare con EEx usando engine Phoenix.LiveView.Engine, assigns audience="World"
```

Risultato atteso: <p>Hello, World!</p>

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.leex`: `738e9c2e7a79a1b3f9f8d47f0db8f16ddb919f21c2c04cb87ed69e9f300d2cbe`

Fonti primarie:

- https://phoenix-live-view.hexdocs.pm/0.11.0/Phoenix.LiveView.Engine.html
- https://hexdocs.pm/eex/EEx.html
- https://elixir-lang.org/
