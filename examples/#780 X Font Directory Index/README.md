# #780 X Font Directory Index

Voce canonica `X Font Directory Index`, tipo `data`, language_id `208700028`.

Index X Source Directory original for a BDF minimum font, with alias `Hello, World!` and FAMILY_NAME properties containing greeting.

## Toolchain and reproduction

mkfontdir / Xvfb / xlsfonts, 7.7+6build2; 1:7.7+6build3; 2:21.1.12-1ubuntu1.6. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Linux: xfonts-utils 1:7.7+6build3, x11-utils 7.7+6build2, Xvfb 2:21.1.12-1ubuntu1.6 and Python 3.12. Serves the font path of fallback / usr/share/fonts/X11/misc. The driver copy font and alias in the external output directory; Xvfb is started without TCP and finished at the end.

Comando/procedura from the directory of the example, unless explicit indications:

```text
python3 verify.py <directory-font-output-esterna>
```

Expected result: Index generated equal to fonts.dir, alias Hello, World! solved by Xvfb and PASS.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

mkfontdir generates fonts.dir and is compared with the original index. A true Xvfb loads that font path; xlsfonts solves the alias and reads the data from the server. The font has a single glyph space: the declared behavior covers index, alias and property, not the design of the greeting letters.

Remaining requirements:

No residual requirement for the stated scope.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://www.x.org/docs/man/man.pdf](https://www.x.org/docs/man/man.pdf)
- [https://xorg.freedesktop.org/archive/X11R6.9.0/doc/PDF/fonts.pdf](https://xorg.freedesktop.org/archive/X11R6.9.0/doc/PDF/fonts.pdf)
