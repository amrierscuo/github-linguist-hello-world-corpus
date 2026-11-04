# 0532: Perl: `.psgi`

Role: Application PSGI: coderef that returns status, headers and body array.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Authentic Perl interpreter, This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Plack::Test locale: do hello.psgi; richiedere GET / nel test in-process (nessuna porta esterna)
```

Expected result: HTTP 200 and Hello, World! body

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.psgi`: `a2703aaa4f0a0efb7e25005a155c5bbae3161d265c6ea8167a79ceec499530b6`

Primary sources:

- https://psgi.github.io/
- https://metacpan.org/pod/Plack::Test
- https://perldoc.perl.org/perlintro
