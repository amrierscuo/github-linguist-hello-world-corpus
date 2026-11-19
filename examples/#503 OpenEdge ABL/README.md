# #503 OpenEdge ABL

## Verified on November 19, 2026

FWD converted the unchanged ABL program. The generated source and compiled JVM instructions bind the exact greeting to the informational message operation with its OK button. The check inspects compiled behavior and opens no dialog.

Run `ant ant-compile && ant convert.list, then compile Hello.java and inspect corpus.greeting.Hello with javap -c -p`.

[Commands, toolchain, output and SHA-256](verification/native_20261119_wave800_main.json).

<details>
<summary>Earlier instructions and evidence</summary>

Show greeting in an informative window ABL.

Canonical type `programming`, language_id `264`.

Suggested toolchain: Progress OpenEdge ABL.

From the example directory:

```sh
pro -p hello.p
```

Expected result: alert box with Hello, World!.

It requires the OpenEdge runtime; it is not interpreted as another Pascal.

Initial state: created; syntax and behavioral verification pending. Runtime Progress OpenEdge unavailable.

Sources:

- [Progress MESSAGE](https://docs.progress.com/bundle/abl-reference/page/MESSAGE-statement.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.p` | [hello.p](hello.p), [driver.p](variants/cls-699ea095/driver.p) created; verification pending |
| `.cls` | [CorpusGreeting.cls](variants/cls-699ea095/CorpusGreeting.cls) created; verification pending |
| `.w` | [hello.w](variants/w-931a997c/hello.w) created; verification pending |

</details>
