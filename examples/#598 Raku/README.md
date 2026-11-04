# #598 Raku

Run Raku and print your greeting.

Canonical type `programming`, language_id `283`.

Suggested toolchain: Rakudo Raku.

From the example directory:

```sh
raku hello.raku
```

Expected result: stdout Hello, World! and newline.

The source requires Raku; Perl5 does not verify its language.

Recorded status: syntax verified; behavior verified. Toolchain: Rakudo2022.12 + MoarVM2022.12 original runtime. [Log](verification/result.json).

Sources:

- [Raku say](https://docs.raku.org/routine/say)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.6pl` | [hello.6pl](variants/6pl-9b762448/hello.6pl) created; verification pending |
| `.6pm` | [Greeting.6pm](variants/6pm-9ec874b4/Greeting.6pm) created; verification pending |
| `.nqp` | [hello.nqp](variants/nqp-2067113e/hello.nqp) created; verification pending |
| `.p6` | [hello.p6](variants/p6-841002fe/hello.p6) created; verification pending |
| `.p6l` | [Greeting.p6l](variants/p6l-965ff65c/Greeting.p6l) created; verification pending |
| `.p6m` | [Greeting.p6m](variants/p6m-aa906888/Greeting.p6m) created; verification pending |
| `.pl` | [hello.pl](variants/pl-b0d52ba4/hello.pl) created; verification pending |
| `.pl6` | [hello.pl6](variants/pl6-2abc115e/hello.pl6) created; verification pending |
| `.pm` | [Greeting.pm](variants/pm-c810ce30/Greeting.pm) created; verification pending |
| `.pm6` | [Greeting.pm6](variants/pm6-537f0d88/Greeting.pm6) created; verification pending |
| `.raku` | [hello.raku](hello.raku), [main.raku](variants/6pm-9ec874b4/main.raku), [main.raku](variants/p6l-965ff65c/main.raku), [main.raku](variants/p6m-aa906888/main.raku), [main.raku](variants/pm-c810ce30/main.raku), [main.raku](variants/pm6-537f0d88/main.raku), [main.raku](variants/rakumod-ba1cf06e/main.raku) created; verification pending |
| `.rakumod` | [Greeting.rakumod](variants/rakumod-ba1cf06e/Greeting.rakumod) created; verification pending |
| `.t` | [hello.t](variants/t-3c247edb/hello.t) created; verification pending |
