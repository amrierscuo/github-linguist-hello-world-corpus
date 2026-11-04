# #274 GtkRC

Voce canonica `GtkRC`, tipo `data`, language_id `876401352`.

Define a GtkRC style called Hello, World! and apply the color to the widget greeting of a GTK 2. test

## Toolchain and reproduction

Required genuine toolchain not available/configured, unavailable / not verified. Test environment: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Requires GTK 2.24, development header and local display or Xvfb. The runtime library has been extracted under work, but the widget test requirements are not configured.

Comando/procedura from the directory of the example, unless explicit indications:

```text
cc check.c -o build/check $(pkg-config --cflags --libs gtk+-2.0); xvfb-run build/check hello.gtkrc
```

Expected result: Parsing and style lookup successful; correct color and greeting issued by the widget.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

Greeting is an effective GtkRC style identifier, not a comment. check.c creates a GtkLabel with that text and must check RGB 0x2020/0x3030/0x4040 values of the solved color.

Remaining requirements:

- GTK 2 runtime package is available locally, but headers/toolchain and a headless display for widget style assertion are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr and SHA-256 of artifacts. `path_normalization` describes the sun
local path substitutions; `<corpus>` identifies the final sources verified
first in staging. Tool availability checks alone do not establish parsing or execution.
Dependencies and build outputs stay in the working directory.

## Primary sources

- [https://gitlab.gnome.org/GNOME/gtk/-/blob/gtk-2-24/gtk/gtkrc.c](https://gitlab.gnome.org/GNOME/gtk/-/blob/gtk-2-24/gtk/gtkrc.c)
- [https://gitlab.gnome.org/GNOME/gtk/-/blob/gtk-2-24/docs/reference/gtk/tmpl/gtkrc.sgml](https://gitlab.gnome.org/GNOME/gtk/-/blob/gtk-2-24/docs/reference/gtk/tmpl/gtkrc.sgml)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.gtkrc` | [hello.gtkrc](hello.gtkrc) created; verification pending |
