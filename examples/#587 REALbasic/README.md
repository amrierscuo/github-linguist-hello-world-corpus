# #587 REALbasic

Import an exported REALbasic module that returns greeting from Message.

Canonical type `programming`, language_id `310`.

Suggested toolchain: REALbasic/Xojo with import text project.

From the example directory:

```sh
Importare Greeting.rbbas e chiamare Greeting.Message in un progetto console di prova.
```

Expected result: filling out the form; Message returns Hello, World!.

The file is an exported form; the host application and the compiler are still open requirements.

Initial state: created; syntax and behavioral verification pending. Compiler REALbasic/Xojo and host project not available.

Sources:

- [Xojo text project format](https://documentation.xojo.com/topics/projects/version_control.html)
- [Xojo modules](https://documentation.xojo.com/topics/code_management/modules.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.rbbas` | [Greeting.rbbas](Greeting.rbbas) created; verification pending |
| `.rbfrm` | [hello.rbfrm](variants/rbfrm-d996a914/hello.rbfrm) created; verification pending |
| `.rbmnu` | [hello.rbmnu](variants/rbmnu-7e96a970/hello.rbmnu) created; verification pending |
| `.rbres` | artifact to generate componente/progetto format specific REALbasic: a real export of the historical IDE is necessary and, for risorse/stato UI, any associated binary data; a .rbbas module is not a substitute. |
| `.rbtbar` | [hello.rbtbar](variants/rbtbar-bfa28cac/hello.rbtbar) created; verification pending |
| `.rbuistate` | artifact to generate componente/progetto format specific REALbasic: a real export of the historical IDE is necessary and, for risorse/stato UI, any associated binary data; a .rbbas module is not a substitute. |
