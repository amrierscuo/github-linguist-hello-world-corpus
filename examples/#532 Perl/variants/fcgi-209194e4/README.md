# 0532: Perl: `.fcgi`

Role: Script Perl FastCGI with FCGI loop of greeting.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Authentic Perl interpreter, This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
perl -c hello.fcgi con FCGI installato; host FastCGI locale, richiesta loopback e cleanup
```

Expected result: Response body Hello, World!

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.fcgi`: `53b76453f70f7086dc342772690a7c22f4f86ba6f8d0dc81c9a53e48d5fb8535`

Primary sources:

- https://metacpan.org/pod/FCGI
- https://perldoc.perl.org/perlintro
