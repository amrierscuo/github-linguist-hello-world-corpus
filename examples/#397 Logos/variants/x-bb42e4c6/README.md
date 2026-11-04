# 0397: Logos: `.x`

Role: Logos without preprocessing C automatic: %ctor Objective-C greeting.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Theos Logos master snapshot; This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Theos Logos: logos.pl hello.x > generated.m; compilare ObjC con import Foundation nel progetto iOS di test
```

Expected result: iOS Log with Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.x`: `3dcc29dcd2e4cb81135612064a23ea5a8d7fa50e774cf8b4daae8b3f2c43ff09`

Primary sources:

- https://theos.dev/docs/logos
- https://theos.dev/docs/logos-syntax
- https://github.com/theos/logos
