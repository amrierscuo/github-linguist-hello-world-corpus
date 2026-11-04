# 0532: Perl: `.ph`

Role: Header Perl in h2ph style with constant definition; require in the driver.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: Authentic Perl interpreter, This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi. The log records the version used for the check. Other application environments remain unverified.

Proposed verification procedure, not performed, by the directory of the variant:

```text
perl driver.pl
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `true`, behavior verified `true`. Greeting data or configuration alone does not establish execution.

Blockers:

- No impediment for the scope actually verified.

SHA-256 of variant files:

- `_h2ph_pre.ph`: `97a18ae8e28c3a8e24dc4a46fbb47a8106f7ca3e9e7a2015212caa44bf64db43`
- `driver.pl`: `bf52d94afda3bdda238b8a3eea136accc7628b4936a6b026d345782532b94c98`
- `hello.ph`: `28846bd1ef77bab45294429d8381cb9c792ea69c9df6aefa6dbb52b8df66fbad`

Primary sources:

- https://perldoc.perl.org/h2ph
- https://perldoc.perl.org/perlintro

Additive test actually performed:

Perl original: compile check; execution of the driver or TAP with tests. The .al only has syntax verified because AutoLoader is not exercised.

Log: `verification/native.json`. The proposed procedures above that were not run are distinct from the commands recorded in the log.

Tool/versione osservata: This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi
