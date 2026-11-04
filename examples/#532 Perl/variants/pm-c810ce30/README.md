# 0532: Perl: `.pm`

Ruolo: Modulo Perl con funzione greeting e valore true finale.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Authentic Perl interpreter, This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi. The log records the version used for the check. Other application environments remain unverified.

Proposed verification procedure, not performed, by the directory of the variant:

```text
perl -I. driver.pl
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `true`, behavior verified `true`. Greeting data or configuration alone does not establish execution.

Blockers:

- No impediment for the scope actually verified.

SHA-256 of variant files:

- `Corpus/Greeting.pm`: `c54727a5ded013ccff1648616c14b86bd3852dde0a29fdcbb188235fc7675161`
- `driver.pl`: `057a7e9100f23bf5ef115eb1d1cfa69e9d391761d08730c65f0e85573f5e10bf`

Primary sources:

- https://perldoc.perl.org/perlmod
- https://perldoc.perl.org/perlintro

Additive test actually performed:

Perl original: compile check; execution of the driver or TAP with tests. The .al only has syntax verified because AutoLoader is not exercised.

Log: `verification/native.json`. The proposed procedures above that were not run are distinct from the commands recorded in the log.

Tool/versione osservata: This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi
