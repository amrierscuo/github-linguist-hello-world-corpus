# #440 Modula-3

Fill Modula- 3 with IO and a Main program.

Canonical type `programming`, language_id `564743864`.

Suggested toolchain: Critical Mass Modula- 3 cm3 and libm3.

From the example directory:

```sh
cm3
Eseguire l’eseguibile hello della directory target generata da cm3.
```

Expected result: stdout Hello, World! and newline.

EXPORTS Main makes the module the entry point of the program.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [CM3 — repository originale](https://github.com/modula3/cm3)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.i3` | [Greeting.i3](variants/i3-5aa7c7e3/Greeting.i3) created; verification pending |
| `.ig` | [Greeting.ig](variants/ig-bbf774c6/Greeting.ig) created; verification pending |
| `.m3` | [Hello.m3](Hello.m3), [Greeting.m3](variants/i3-5aa7c7e3/Greeting.m3), [Main.m3](variants/i3-5aa7c7e3/Main.m3), [TextGreeting.m3](variants/ig-bbf774c6/TextGreeting.m3), [Main.m3](variants/ig-bbf774c6/Main.m3), [TextGreeting.m3](variants/mg-63058c94/TextGreeting.m3), [Main.m3](variants/mg-63058c94/Main.m3) created; verification pending |
| `.mg` | [Greeting.mg](variants/mg-63058c94/Greeting.mg) created; verification pending |
