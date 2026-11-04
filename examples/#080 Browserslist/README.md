# #080 Browserslist

Canonical entry from the corpus's `reference/languages.yml`. The reference and its order remain unchanged. The source was written for this example.

## Goal

Solve a Browserslist configuration in two explicit and deterministic targets.

Browserslist is a target configuration format, so the relevant result is browser selection. .browserslistrc is read and solved by the authentic Browserslist library; verify.cjs only controls the product list.Explicit versions avoid queries dependent on the date.

## Toolchain and reproduction

Browserslist 4.29.3; Node.js 22.20.0

Command from the example folder, with the toolchain indicated available in the PATH. Run the build in a temporary copy to keep the generated files out of the corpus.

```text
node verify.cjs <directory-node_modules-con-browserslist>
```

## Expected result and status

chrome 100
firefox 100
PASS: expected explicit browser targets

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The `verification/toolchain.json` log records actual commands, versioni/provenienza of the toolchain, output codes, stdout/stderr and SHA-256 of the proven sources.

## Primary sources

- https://github.com/browserslist/browserslist
