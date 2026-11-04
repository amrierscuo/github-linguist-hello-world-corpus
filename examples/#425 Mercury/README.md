# #425 Mercury

Fill out a deterministic Mercury program with me you are threading.

Canonical type `programming`, language_id `229`.

Suggested toolchain: Mercury mmc and grade runtime installed.

From the example directory:

```sh
mmc --make hello
./hello
```

Expected result: stdout Hello, World! and LF, exit 0.

main declares determinism det and uses! IO to pass the state of I/O.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [Mercury — programma hello](https://www.mercurylang.org/information/doc-latest/mercury_user_guide/Hello-world.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.m` | [hello.m](hello.m) created; verification pending |
| `.moo` | [hello.moo](variants/moo-3e77aff6/hello.moo) created; verification pending |
