# #274 GtkRC

Voce canonica `GtkRC`, tipo `data`, language_id `876401352`.

Definire uno stile GtkRC chiamato Hello, World! e applicarne il colore al widget greeting di una prova GTK 2.

## Toolchain e riproduzione

Required genuine toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede GTK 2.24, header di sviluppo e un display locale o Xvfb. La libreria runtime è stata estratta sotto work, ma non sono configurati i requisiti della prova widget.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
cc check.c -o build/check $(pkg-config --cflags --libs gtk+-2.0); xvfb-run build/check hello.gtkrc
```

Risultato atteso: Parsing e style lookup riusciti; colore corretto e saluto emesso dal widget.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Il saluto è un identificatore effettivo di stile GtkRC, non un commento. check.c crea un GtkLabel con quel testo e deve verificare i valori RGB 0x2020/0x3030/0x4040 del colore risolto. La semplice presenza della libreria non attesta il parsing.

Requisiti residui:

- GTK 2 runtime package is available locally, but headers/toolchain and a headless display for widget style assertion are not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://gitlab.gnome.org/GNOME/gtk/-/blob/gtk-2-24/gtk/gtkrc.c](https://gitlab.gnome.org/GNOME/gtk/-/blob/gtk-2-24/gtk/gtkrc.c)
- [https://gitlab.gnome.org/GNOME/gtk/-/blob/gtk-2-24/docs/reference/gtk/tmpl/gtkrc.sgml](https://gitlab.gnome.org/GNOME/gtk/-/blob/gtk-2-24/docs/reference/gtk/tmpl/gtkrc.sgml)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.gtkrc` | [hello.gtkrc](hello.gtkrc) creato, verifiche pendenti |
