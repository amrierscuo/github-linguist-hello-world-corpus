# #134 Common Workflow Language

Describe in CWL 1.2 an echo command with default string input Hello, World! and capture stdout in an output File hello.txt.

## Reproduction

Toolchain: cwltool 3.3.20260925135507; Python 3.12.3. Test environment: Ubuntu 24.04 WSL2 x86_64.

```text
cwltool --validate hello.cwl
cwltool --no-container --outdir results hello.cwl job.yml
Verificare results/hello.txt esattamente Hello, World! seguito da newline.
```

Expected result: Successful validation; job exit 0; output File hello.txt with exact Hello, World! content followed by newline.

## Verification

syntax and behavior verified 2026-10-08T23:34:15.412306+00:00. The variants have separate evidence in the log when consumed.

[Prova nativa](verification/finish_native.json) contains versions, real commands, exit code, output and SHA-256. The local routes are replaced by placeholders.

## Primary sources

- [https://www.commonwl.org/v1.2/CommandLineTool.html](https://www.commonwl.org/v1.2/CommandLineTool.html)
- [https://github.com/common-workflow-language/cwltool](https://github.com/common-workflow-language/cwltool)
- [https://www.commonwl.org/user_guide/topics/outputs.html](https://www.commonwl.org/user_guide/topics/outputs.html)

## Extension coverage

Suffix checks are recorded separately.

| Extension | File and status |
| --- | --- |
| `.cwl` | [hello.cwl](hello.cwl) syntax and behavior verified |
