# 0492: Objective-C: `.h`

Role: Header Objective-C with Greeting function statement; implementation and driver aside.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0; GNU libobjc4 14.2.0. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
clang/GNUstep o Xcode: compilare greeting.m che importa hello.h; link Foundation e avviare
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `greeting.m`: `db0f805d693d166be828dc4d5f3a54b6a4e51454cb8c65e3f1c1958339cdbdac`
- `hello.h`: `6691c033ea05a9027640445c1ea37b8440b50c75b640db4fa99aff4b9ea76e13`

Primary sources:

- https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/
- https://gcc.gnu.org/onlinedocs/gcc/Objective-C.html
