# #676 SourcePawn

Fill out a SourcePawn plugin that prints greeting to its upload.

Canonical type `programming`, language_id `354`.

Provided Toolchain: SourceMod spcomp and a Source engine test server.

From the example directory:

```sh
spcomp hello.sp -o build/hello.smx
```

Expected result: compiled plugin and server console contains Hello, World!.

The compiler tries the plugin; the callback requires the game server for the behavior.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [SourcePawn](https://wiki.alliedmods.net/Introduction_to_SourcePawn_1.7)
- [SourceMod](https://www.sourcemod.net/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.sp` | [hello.sp](hello.sp), [main.sp](variants/inc-dd126fb7/main.sp) created; verification pending |
| `.inc` | [hello.inc](variants/inc-dd126fb7/hello.inc) created; verification pending |
