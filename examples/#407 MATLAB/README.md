# #407 MATLAB

Run a MATLAB script that prints Hello, World!.

Canonical type `programming`, language_id `225`.

Toolchain provided: MATLAB or GNU Octave for this compatible subset.

From the example directory:

```sh
octave --no-gui --quiet hello.m
```

Expected result: stdout Hello, World! and LF.

Any Octave test will be indicated as Octave compatibility; no test is given to MATLAB runtime without having performed it.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [MathWorks — disp](https://www.mathworks.com/help/matlab/ref/disp.html)
- [GNU Octave — manuale](https://docs.octave.org/latest/)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.matlab` | [hello.matlab](variants/matlab-67b3d23b/hello.matlab) created; verification pending |
| `.m` | [hello.m](hello.m) created; verification pending |
