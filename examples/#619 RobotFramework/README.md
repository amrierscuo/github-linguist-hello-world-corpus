# #619 RobotFramework

Voce canonica `RobotFramework`, tipo `programming`, language_id `324`.

Run an original Robot Framework test that builds and compares greetings.

## Toolchain and reproduction

Official Robot Framework test parser and execution engine — Robot Framework 7.5 (Python 3.13.9 on win32). Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Robot Framework ufficiale 7.5 e Python 3.13.9.

Comando/procedura from the directory of the example, unless explicit indications:

```text
python -m robot --outputdir build --log NONE --report NONE hello.robot
```

Expected result: Hello, World! in output or compliant data, according to the scope described.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

Parser and real runner, test Should Be Equal past and Log To Console observed; XML output with SHA in the log.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.robot` | [hello.robot](hello.robot), [main.robot](variants/resource-78a02e24/main.robot) created; verification pending |
| `.resource` | [hello.resource](variants/resource-78a02e24/hello.resource) created; verification pending |
