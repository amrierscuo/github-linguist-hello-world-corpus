# #072 Blueprint

Voce canonica: `Blueprint`, tipo `markup`, language_id `765545512`.

Fill out a Blueprint GTK 4 that describes a GtkLabel with Hello, World! text.

## Toolchain and reproduction

GNOME Blueprint compiler source snapshot; GTK 4.14.5; PyGObject 3.48.2; Python 3.12.3.

Blueprint compiler, Python/PyGObject and GTK4 with typelib transitive; graphical session or virtual display for Gtk.init. In the GI_TYPELIB_PATH and LD_LIBRARY_PATH test they point to a locally extracted Ubuntu prefix.

Commands from the directory of the example; `<output>` indicates a temporary directory external to the corpus.

```text
blueprint-compiler compile --output <output>/hello.ui hello.blp
Python/PyGObject: Gtk.init(); b = Gtk.Builder.new_from_file("<output>/hello.ui"); widget = b.get_object("greeting"); assert isinstance(widget, Gtk.Label); assert widget.get_label() == "Hello, World!"
```

Expected result: Compiler exit 0; GTK4 GtkBuilder creates a GtkLabel with get_label() exactly Hello, World!.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

The GNOME compiler resolves GTK4 types and produces GtkBuilder XML. The semantic check instantiates the result with Gtk.Builder, checks that greeting is a Gtk.Label and reads its label property: Hello, World!. No window is displayed. The GTK4 runtime, typelib and dependencies were extracted into work, with a WSLg display available.

Real test: [finish.json](verification/finish.json), with UTC, commands, versions, exit code, stdout/stderr and SHA-256 of sources.

## Primary sources

- https://gnome.pages.gitlab.gnome.org/blueprint-compiler/
- https://gitlab.gnome.org/GNOME/blueprint-compiler

## Extension coverage

Suffix checks are recorded separately.

| Extension | File and status |
| --- | --- |
| `.blp` | [hello.blp](hello.blp) syntax and behavior verified |
