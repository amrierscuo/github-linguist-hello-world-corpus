# #072 Blueprint

Voce canonica: `Blueprint`, tipo `markup`, language_id `765545512`.

Compilare un Blueprint GTK 4 che descrive una GtkLabel con testo Hello, World!.

## Toolchain e riproduzione

GNOME Blueprint compiler source snapshot; GTK 4.14.5; PyGObject 3.48.2; Python 3.12.3.

Blueprint compiler, Python/PyGObject e GTK4 con typelib transitivi; sessione grafica o display virtuale per Gtk.init. Nella prova GI_TYPELIB_PATH e LD_LIBRARY_PATH puntano a un prefisso Ubuntu estratto localmente.

Comandi dalla directory dell’esempio; `<output>` indica una directory temporanea esterna al corpus.

```text
blueprint-compiler compile --output <output>/hello.ui hello.blp
Python/PyGObject: Gtk.init(); b = Gtk.Builder.new_from_file("<output>/hello.ui"); widget = b.get_object("greeting"); assert isinstance(widget, Gtk.Label); assert widget.get_label() == "Hello, World!"
```

Risultato atteso: Compiler exit 0; GTK4 GtkBuilder crea una GtkLabel con get_label() esattamente Hello, World!.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il compiler GNOME risolve i tipi GTK4 e produce GtkBuilder XML. La verifica semantica istanzia realmente il risultato con Gtk.Builder, controlla che greeting sia Gtk.Label e legge la sua proprietà label: Hello, World!. Nessuna finestra viene presentata. Runtime GTK4, typelib e dipendenze estratti in work; display WSLg disponibile.

Prova reale: [finish.json](verification/finish.json), con UTC, comandi, versioni, exit code, stdout/stderr e SHA-256 dei sorgenti. Le sostituzioni dei percorsi sono documentate nel log. I prodotti di compilazione e le dipendenze rimangono nelle directory di lavoro.

## Fonti primarie

- https://gnome.pages.gitlab.gnome.org/blueprint-compiler/
- https://gitlab.gnome.org/GNOME/blueprint-compiler

## Copertura delle estensioni

Le verifiche dei suffissi sono registrate separatamente.

| Estensione | File e stato |
| --- | --- |
| `.blp` | [hello.blp](hello.blp) sintassi e semantica verificate |
