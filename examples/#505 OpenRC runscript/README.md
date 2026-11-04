# #505 OpenRC runscript

## Latest recorded verification

**Syntax and behavior verified** on November 4, 2026.

Native OpenRC start invoked the original script and ebegin emitted its greeting. Only a disposable Alpine fixture was modified; no host service was started.

[Native commands, versions, outputs and SHA-256](verification/native_20261104_followup_main.json). [Earlier evidence](verification/result.json).

<details>
<summary>Original instructions and earlier status</summary>

Play an OpenRC script that initiates a demonstration service and shows greeting.

Canonical type `programming`, language_id `265`.

Suggested toolchain: OpenRC openrc-run; sh for initial grammar control.

From the example directory:

```sh
sh -n hello
openrc-run hello start
```

Expected result: valid syntax shell; demonstrative start with Hello, World! message.

The script remains in the corpus and is not installed in / etc/init.d. sh -n does not test the OpenRC functions.

Registered state: syntax verified; behavioral verification pending. Toolchain: Ubuntu POSIX sh syntax only. [Log](verification/result.json). Sintassi POSIX shell verificata; openrc-run non eseguito. Semantica e funzioni OpenRC pendenti.

Sources:

- [OpenRC service scripts](https://github.com/OpenRC/openrc/blob/master/service-script-guide.md)

</details>
