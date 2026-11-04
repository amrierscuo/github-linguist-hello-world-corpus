# 0532: Perl: `.al`

Role: Autosplit/autoload Perl: file package::greeting, not main program.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Authentic Perl interpreter, This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi. The log records the version used for the check. Other application environments remain unverified.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Perl AutoLoader: collocare greeting.al nella directory auto/Corpus/Greeting e invocare greeting via modulo host
```

Expected result: Hello, World! returned by the sub

Individual status: artifact created `true`, syntax verified `true`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The language parser accepted the file; the application-specific schema, loader and semantics remain unverified.

SHA-256 of variant files:

- `greeting.al`: `e8369f9c7386527631e57d8265ac04998c4c42157d95a75d6b21f25f0ac7ecb1`

Primary sources:

- https://perldoc.perl.org/AutoLoader
- https://perldoc.perl.org/perlintro

Additive test actually performed:

Perl original: compile check; execution of the driver or TAP with tests. The .al only has syntax verified because AutoLoader is not exercised.

Log: `verification/native.json`. The proposed procedures above that were not run are distinct from the commands recorded in the log.

Tool/versione osservata: This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi
