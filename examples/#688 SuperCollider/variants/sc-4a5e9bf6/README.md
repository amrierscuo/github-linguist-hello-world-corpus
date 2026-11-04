# SuperCollider .sc

`hello.sc` contains the `CorpusGreeting` class with the `message` class method.

The class was compiled in the SCClassLibrary isolated from sclang 3.13.0 and the method was executed by [run_class.scd](../../verification/run_class.scd). The post output contains a row exactly `Hello, World!`; the process ends with exit code 0.

The `.sc` variant does not run as a simple script. The configuration of the class library and the reproducible commands are described in the [README principale](../../README.md). The [log](../../verification/resume_native.json) records the compilation of 330 file included this class, the actual invocation, versions and SHA256 verified.

Fonte primaria: [Writing Classes](https://doc.sccode.org/Guides/WritingClasses.html).
