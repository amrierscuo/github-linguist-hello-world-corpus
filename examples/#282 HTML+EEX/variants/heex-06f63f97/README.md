# 0282: HTML+EEX: `.heex`

Ruolo: Template HTML-aware HEEx; usa assigns di Phoenix anziché variabili EEx locali.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Elixir1.14.0, Erlang/OTP25 e ERTS13.2.2.5, pacchetti Ubuntu. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Phoenix.Component: embed_templates; render del template con assigns audience="World" e conversione in HTML
```

Expected result: <p> Hello, World! </p>

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.heex`: `738e9c2e7a79a1b3f9f8d47f0db8f16ddb919f21c2c04cb87ed69e9f300d2cbe`

Primary sources:

- https://hexdocs.pm/phoenix_live_view/Phoenix.Component.html
- https://hexdocs.pm/eex/EEx.html
- https://elixir-lang.org/
