# #027 Alpine Abuild

A fresh native APK build, its check step, an offline installation into a disposable Alpine root, and execution of the byte-identical installed script all passed.

Canonical type: `programming`. Linguist language ID: `14`.

## Recorded verification

**Syntax and behavior verified** on November 4, 2026 with Alpine Linux 3.23.6, abuild 3.16.0-r0 and apk-tools 3.0.8-r0.

[Recorded commands, outputs and hashes](verification/native_20261104_alpine_receipt.json).
[Earlier verification record](verification/toolchain.json).

## Reproduce the check

In a disposable Alpine environment with abuild, apk-tools, BusyBox, OpenSSL and a configured local signing key, copy only APKBUILD and hello.sh into a build directory. Run `abuild -r`. The recorded isolated root used `abuild -F -d validate` before its fresh build. Install the resulting test package offline in that same disposable root, compare `/usr/bin/corpus-hello` with `hello.sh`, and run the installed script. The evidence lists the exact commands and output. The package recipe does not need its example URL.

## Primary sources

- https://wiki.alpinelinux.org/wiki/APKBUILD_Reference
- https://github.com/alpinelinux/abuild/blob/master/APKBUILD.5.scd
- https://dl-cdn.alpinelinux.org/alpine/v3.23/releases/x86_64/
