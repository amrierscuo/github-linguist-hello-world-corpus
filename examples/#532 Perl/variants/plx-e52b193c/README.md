# 0532: Perl: `.plx`

Role: Alias extension for the same text format as the main source.

Origin: Byte-identical copy of the original corpus source: examples/#532 Perl/hello.pl.

Required toolchain: Authentic Perl interpreter, This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi. The log records the version used for the check. Other application environments remain unverified.

Proposed verification procedure, not performed, by the directory of the variant:

```text
Usare la toolchain del README principale sul file hello.plx; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Expected result: The conformed result contains Hello, World!, according to the framework described.

Individual status: artifact created `true`, syntax verified `true`, behavior verified `true`. Greeting data or configuration alone does not establish execution.

Blockers:

- No impediment for the scope actually verified.

SHA-256 of variant files:

- `hello.plx`: `8282ea45dea2901f533f4afb329f4fb75983a128618abd230e065601b281fb4d`

Primary sources:

- https://perldoc.perl.org/perlintro

Additive test actually performed:

Perl original: compile check; execution of the driver or TAP with tests. The .al only has syntax verified because AutoLoader is not exercised.

Log: `verification/native.json`. The proposed procedures above that were not run are distinct from the commands recorded in the log.

Tool/versione osservata: This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi
