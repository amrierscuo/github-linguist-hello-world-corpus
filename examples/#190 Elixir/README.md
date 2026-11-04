# #190 Elixir

Run an Elixir script that prints Hello, World! followed by newline.

Canonical type `programming`, language_id `100`.

Suggested toolchain: Elixir 1.x with Erlang/OTP compatible.

From the example directory:

```sh
elixir hello.exs
```

Expected result: exact stdout `Hello, World!\n`, 0. output

The script does not start network applications. The command also requires the Erlang runtime of the distribution.

Recorded status: syntax verified; behavior verified. Toolchain: Elixir 1.14.0 + Erlang OTP 25 / ERTS 13.2.2.5 Linux original packages. See [log](verification/verification.log).

Sources of linguaggio/formato and original implementations:

- [Elixir — introduzione](https://elixir.hexdocs.pm/introduction.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.ex` | [hello.ex](variants/ext-ex-2e6578/hello.ex) created; verification pending |
| `.exs` | [hello.exs](hello.exs) verified |
