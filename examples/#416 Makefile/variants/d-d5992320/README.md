# 0416: Makefile: `.d`

Role: Make dependency fragment: hello.o relationship: hello.c, includes from the Support Makefile.

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: GNU Make on Ubuntu 24.04. The log records the version used for the check. Other application environments remain unverified.

Proposed verification procedure, not performed, by the directory of the variant:

```text
make -f Makefile; ./hello
```

Expected result: Hello, World!

Individual status: artifact created `true`, syntax verified `true`, behavior verified `true`. Greeting data or configuration alone does not establish execution.

Blockers:

- No impediment for the scope actually verified.

SHA-256 of variant files:

- `Makefile`: `c48a2b7ba6f1ee0a439b1d28d4aa194b79635e80ccab6cc9d6411f906d10804e`
- `hello.c`: `ed022c4313ef7444150bc047da163dd09eb5ae942093b1e6c97e1cf32dfbad7a`
- `hello.d`: `6d8c2cb1c59f2480bbaaa17229e7f4d43e458e8b7a44f4bfdc17cd316bc11be6`

Primary sources:

- https://www.gnu.org/software/make/manual/html_node/Automatic-Prerequisites.html
- https://www.gnu.org/software/make/manual/html_node/Recipes.html

Additive test actually performed:

Original make includes fragment dependencies .d; GCC compiles the fixtures; binary executed in the work, exact stdout Hello, World! and LF.

Log: `verification/native.json`. The proposed procedures above that were not run are distinct from the commands recorded in the log.

Tool/versione osservata: [{'command': ['wsl', '--exec', 'make', '--version'], 'exit_code': 0, 'stdout': 'GNU Make 4.3\nBuilt for x86_64-pc-linux-gnu\nCopyright (C) 1988-2020 Free Software Foundation, Inc.\nLicense GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>\nThis is free software: you are free to change and redistribute it.\nThere is NO WARRANTY, to the extent permitted by law.\n', 'stderr': ''}, {'command': ['wsl', '--exec', 'gcc', '--version'], 'exit_code': 0, 'stdout': 'gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0\nCopyright (C) 2023 Free Software Foundation, Inc.\nThis is free software; see the source for copying conditions.  There is NO\nwarranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.\n\n', 'stderr': ''}]
