# #037 Arc

Stampare esattamente Hello, World! seguito da newline con prn in Arc.

## File

- `hello.arc`

## Toolchain and verification

Anarki stable (Arc 3.2 con patch comunitarie), commit 8421605f4a75a0f7fc9a0bed83a87affa1137fab; Racket 8.18 [cs].

Install Racket 8.18 and get Anarki to the client used:

```sh
git clone https://github.com/arclanguage/anarki.git anarki
git -C anarki checkout 8421605f4a75a0f7fc9a0bed83a87affa1137fab
```

The commit belongs to the `stable` branch, based on Arc 3.2.
of the example, adapt the path of Anarki and start the official loader:

```sh
racket --version
racket -f /percorso/anarki/as.scm hello.arc
```

On Windows the same command accepts a quoted path towards `as.scm`.
The minimum distribution of Racket must also have the packages required by
Anarki (e.g. `mzscheme`, `compatibility-lib` and `net-lib` ).
Runs the file and ends; it does not open the interactive cycle when receiving a file.

## Expected result

Exit 0; stdout esattamente Hello, World! seguito da newline; stderr vuoto.

## State of the test

syntax verified. behavior verified.

Real execution with Anarki stable on Racket; charge and evaluate the Arc source, no emulation of the Python language.

Actual Windows x64 test of 2026-10-08T11:01:56.068379+00:00: [log](verification/result.json).
The log includes hash SHA-256 of the source, observed versions, commands, exit codes, stdout and stderr.

## Primary sources

- [https://arclanguage.github.io/](https://arclanguage.github.io/)
- [https://github.com/arclanguage/anarki/tree/8421605f4a75a0f7fc9a0bed83a87affa1137fab](https://github.com/arclanguage/anarki/tree/8421605f4a75a0f7fc9a0bed83a87affa1137fab)
- [https://github.com/arclanguage/anarki/blob/8421605f4a75a0f7fc9a0bed83a87affa1137fab/arc.arc](https://github.com/arclanguage/anarki/blob/8421605f4a75a0f7fc9a0bed83a87affa1137fab/arc.arc)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.arc` | [hello.arc](hello.arc) verified |
