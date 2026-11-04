# 0412: MQL5: `.mqh`

Ruolo: Header MQL con funzione di saluto e include guard; script driver separato.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: MetaTrader 5 MetaEditor/compiler. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
MetaEditor: compilare driver.mq5; eseguire solo il driver nel terminale di test
```

Expected result: Hello, World! in the log

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `driver.mq5`: `15427813b05b8d56597fb04f22d728c2df82fa338dd90ea4e2247ea300beecc7`
- `hello.mqh`: `4bfd7b1c085b5be99e2ef9cd96d39efdf509667aaa07ac6486e86dcef421b0c6`

Primary sources:

- https://www.mql5.com/en/docs/basis/preprosessor/include
- https://www.mql5.com/en/docs/event_handlers/onstart
- https://www.mql5.com/en/docs/common/print
