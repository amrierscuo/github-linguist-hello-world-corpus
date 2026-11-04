# #505 OpenRC runscript

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
