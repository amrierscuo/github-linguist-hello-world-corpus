# 0532: Perl: `.cgi`

Ruolo: Script Perl CGI con header Content-Type; nessun server avviato.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Authentic Perl interpreter, This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi. The log records the version used for the check. Other application environments remain unverified.

Proposed verification procedure, not performed, by the directory of the variant:

```text
perl -c hello.cgi; perl hello.cgi
```

Expected result: Header CGI and body Hello, World!

Individual status: artifact created `true`, syntax verified `true`, behavior verified `true`. Greeting data or configuration alone does not establish execution.

Blockers:

- No impediment for the scope actually verified.

SHA-256 of variant files:

- `hello.cgi`: `387a87b72d7862dd9aff2aa0986ca12f1de529cd88bcb74cce0e3226ca5be5bd`

Primary sources:

- https://perldoc.perl.org/perlrun
- https://perldoc.perl.org/perlintro

Additive test actually performed:

Perl original: compile check; execution of the driver or TAP with tests. The .al only has syntax verified because AutoLoader is not exercised.

Log: `verification/native.json`. The proposed procedures above that were not run are distinct from the commands recorded in the log.

Tool/versione osservata: This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi
