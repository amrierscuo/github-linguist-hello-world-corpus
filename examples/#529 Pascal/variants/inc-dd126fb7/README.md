# 0529: Pascal: `.inc`

Ruolo: Include Pascal con procedura Greet; driver usa direttiva I.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Genuine Free Pascal compiler, 3.2.2. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
fpc driver.pas; ./driver
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `driver.pas`: `7636fe3a7b10fc7201b919ac2ff4d125cd68a089f2164e94a4e09c4331f3a3f7`
- `hello.inc`: `f02281eb8fb13b30830dcdf061635663c34745dfccd82acc4389e4109a5e93c7`

Primary sources:

- https://www.freepascal.org/docs-html/prog/progsu40.html
- https://www.freepascal.org/docs.html
