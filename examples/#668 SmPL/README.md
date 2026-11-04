# #668 SmPL

La semantic patch originale `hello.cocci` sostituisce `puts("Goodbye")` con
`puts("Hello, World!")` in the original C fixtures `input.c`.

## Toolchain and reproduction

Coccinelle spatch 1.1.1, pacchetto Ubuntu amd64 1.1.1.deb-5build1, compilato
con OCaml 4.14.1; GCC 13.3.0. Ubuntu 24.04 tramite WSL2.
The original Coccinelle package is extracted only in a work directory;
no global installations or additional dependencies are required for this patch.

From the example directory, with available spatch and an external output:

```sh
mkdir -p <output>/build
spatch --version
spatch --sp-file hello.cocci input.c -o <output>/build/hello.c
gcc -std=c11 -Wall -Wextra -pedantic <output>/build/hello.c -o <output>/build/hello
<output>/build/hello
```

For the extracted package, use the `<prefisso>/usr/bin/spatch` track and set
`COCCINELLE_HOME=<prefisso>/usr/lib/coccinelle`, as in the real log.
Result: patch applied, successful compilation and `Hello, World!` followed by LF,
exit code 0. The source generated contains replacement and no longer contains
la chiamata precedente.

## Status and evidence

syntax **verified** from the original SmPL parser; behavior **verified** by means of
real transformation, GCC compilation and execution of the result.
The test only concerns the original fixtures, without patching project sources
The bytes of `hello.cocci` and `input.c` remain unchanged.

[Log nativo](verification/native.json): versioni, comandi, exit code, stdout/stderr,
hash SHA-256 of original artifacts, package tool, C generated and
binario eseguito. La nota `path_normalization` descrive le sostituzioni dei percorsi.
Sources and generated tracks remain in the external work directory.

## Primary sources

- [Coccinelle, progetto originale](https://coccinelle.gitlabpages.inria.fr/website/)
- [Repository e documentazione originale](https://github.com/coccinelle/coccinelle)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.cocci` | [hello.cocci](hello.cocci) verified |
