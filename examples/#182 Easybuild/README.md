# #182 Easybuild

Describe an EasyBuild recipe that installs a hello-world local script and performs its minimal control.

Canonical type `data`, language_id `342840477`.

Suggested toolchain: EasyBuild 5.x in Linux, tools for environmental modules.

From the example directory:

```sh
eb HelloWorld-1.0.eb --prefix ./build/easybuild
```

Expected result: accepted recipe; bin/hello-world script installed in the dedicated prefix; `Hello, World!\n` print execution.

Bundle does not compile libraries: postinstall instructions produce an original script. example.invalid is an illustration URL; it is not used to download sources.

Initial state: created; syntax and behavioral verification pending. native toolchain not yet performed: syntax and behavior verifications remain pending.

Sources of linguaggio/formato and original implementations:

- [EasyBuild — easyconfig](https://docs.easybuild.io/writing-easyconfig-files/)
- [Bundle easyblock originale](https://github.com/easybuilders/easybuild-easyblocks/blob/develop/easybuild/easyblocks/generic/bundle.py)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.eb` | [HelloWorld-1.0.eb](HelloWorld-1.0.eb) created; verification pending |
