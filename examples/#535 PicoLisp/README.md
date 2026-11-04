# #535 PicoLisp

Voce canonica `PicoLisp`, tipo `programming`, language_id `285`.

Print greetings with prinl and exit the process PicoLisp.

## Toolchain and reproduction

Authentic PicoLisp native interpreter 23.12-1build2.

Command from the sample directory with PicoLisp 23.12-1build2. No external libraries are required: de, prinl and bye are native primitive.

```text
picolisp hello.l
```

Exit 0, stdout exactly Hello, World! followed by newline.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The PicoLisp de greet function receives Audience and uses prinl; the World greet call produces exactly the greeting, then bye ends the process. The definition makes explicit the dialect and distinguishes .l from Lex/Common Lisp.

Current evidence: [recognition.json](verification/recognition.json), with a UTC timestamp, native commands, exit codes, stdout/stderr, toolchain details and SHA-256 values for modified sources and drivers. Earlier evidence is retained as history. Expected Linguist classification is distinct from the statistics actually observed on GitHub. This batch applies no language override.

## Primary sources

- https://software-lab.de/doc/refP.html#prinl
- https://software-lab.de/doc/refD.html#de
- https://github.com/github-linguist/linguist/blob/v9.7.0/lib/linguist/heuristics.yml

## Extension coverage

Suffix checks are recorded separately.

| Extension | File and status |
| --- | --- |
| `.l` | [hello.l](hello.l) syntax and behavior verified |
