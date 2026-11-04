# #148 Cylc

The canonical entry and order come from the corpus's `reference/languages.yml`. Sources and fixtures are original; any dumps or bundles come from the stated tools.

## Goal

Define a Cylc workflow to a cycle with a task that prints Hello, World!.

flow.cylc uses cycling mode integer and graph R1, with explicit task runtime. The test is for the original configuration and graph validator. In order to verify the behavior of scheduling, you need to run install/play and check the job log; you do not count a simple manual execution of the shell script.

## Toolchain and reproduction

Cylc Flow 8.6.6; Python 3.12.3 su Ubuntu WSL

Commands in the example folder with the toolchain available in PATH. Use a temporary copy: databases, objects, audio and other test outputs do not belong to the corpus.

```text
cylc validate .
cylc install . --workflow-name corpus-greeting
```

```text
cylc play corpus-greeting
```

## Expected result and status

Workflow valid; the greeting/1 job produces Hello, World! and the workflow concludes the only cycle.

Artifact created: yes. syntax verified: no. behavior verified: no.

The `verification/toolchain.json` log records versions and provenance, SHA-256 of the source, actual commands, exit, stdout and stderr normalized.

Commitments: Cylc 8.6.6 properly starts CLI, but validated does not end within 90 seconds in WSL. The attempt is recorded and the related process has been arrested; scheduler and task have not been initiated.

## Primary sources

- https://cylc.github.io/cylc-doc/latest/html/tutorial/runtime/introduction.html
- https://github.com/cylc/cylc-flow

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cylc` | [flow.cylc](flow.cylc) created; verification pending |
