# #745 Vala

Fill out Vala in C and print your greeting.

Canonical type `programming`, language_id `386`.

Toolchain provided: Vala 0.56.16; GLib2.80.0; GCC13.3.0; WSL Ubuntu24.04.

From the example directory:

```sh
mkdir -p build
valac --directory=build -o hello hello.vala
./build/hello
```

Expected result: stdout Hello, World! and newline.

The check must include valac; fill out a handwritten C does not verify Vala.

Recorded status: syntax verified; behavior verified. Toolchain: Vala 0.56.16; GLib2.80.0; GCC13.3.0; WSL Ubuntu24.04. [Log](verification/result.json).

Sources:

- [Vala tutorial](https://docs.vala.dev/tutorials/programming-language/main.html)

The real verification uses original Ubuntu packages extracted under `work/tools_741_760/ubuntu` and build directories separated under `work/tools_741_760`; compiled artifacts are not part of the corpus.

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.vala` | [hello.vala](hello.vala), [main.vala](variants/vapi-45f688d8/main.vala) created; verification pending |
| `.vapi` | [hello.vapi](variants/vapi-45f688d8/hello.vapi) created; verification pending |
