# #053 BASIC

Voce canonica `BASIC`, tipo `programming`, language_id `28923963`.

Print Hello, World! in a BASIC program by choosing the Yabasic dialect.

## Toolchain and reproduction

Yabasic Ubuntu binary package extracted locally yabasic 2.90.3, built on x86_64-pc-linux-gnu.

Command from the sample directory with Yabasic 2.90.3. Line numbers are accepted by this toolchain; the test records its exact stdout.

```text
yabasic hello.bas
```

Exit 0, stdout exactly Hello, World! followed by newline.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Yabasic program with 10 line numbers and 20; the original runtime accepts and prints exactly greeting. The explicit numbering makes BASIC sample recognizable according to the upstream .bas. rule The test is about the Yabasic dialect, not all historical BASIC.

Current evidence: [recognition.json](verification/recognition.json), with a UTC timestamp, native commands, exit codes, stdout/stderr, toolchain details and SHA-256 values for modified sources and drivers. Earlier evidence is retained as history. Expected Linguist classification is distinct from the statistics actually observed on GitHub. This batch applies no language override.

## Primary sources

- https://www.yabasic.de/yabasic.htm
- https://github.com/github-linguist/linguist/blob/v9.7.0/lib/linguist/heuristics.yml

## Extension coverage

Suffix checks are recorded separately.

| Extension | File and status |
| --- | --- |
| `.bas` | [hello.bas](hello.bas) syntax and behavior verified |
