# #072 Blueprint

Voce canonica del `reference/languages.yml` del corpus. Il riferimento e il suo ordine restano invariati. Il sorgente è originale di questo esempio.

## Obiettivo

Compilare un Blueprint GTK 4 che descrive una GtkLabel con testo Hello, World!.

La verifica prevista usa il compilatore GNOME e i tipi GTK importati. Questo esempio dichiara un widget; non avvia un’applicazione grafica o una finestra.

## Toolchain e riproduzione

GNOME Blueprint compiler upstream; Python 3 e PyGObject 3.48.2; GTK 4 introspection richiesta

Comandi dalla cartella dell’esempio, con la toolchain indicata disponibile nel PATH. Eseguire la build in una copia temporanea per mantenere fuori dal corpus i file generati.

```text
blueprint-compiler compile --output hello.ui hello.blp
```

```text
Controllare hello.ui: classe GtkLabel e proprietà label con valore Hello, World!.
```

## Risultato atteso e stato

Compilazione riuscita; GtkBuilder XML conserva la label e il suo testo.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Il log `verification/toolchain.json` registra comandi effettivi, versioni/provenienza della toolchain, codici di uscita, stdout/stderr e SHA-256 dei sorgenti provati. I percorsi della macchina sono normalizzati.

Impedimenti: Namespace GTK 4 delle librerie GObject introspection non disponibile nel WSL. Il compilatore originale non arriva alla validazione del file.

## Fonti primarie

- https://gnome.pages.gitlab.gnome.org/blueprint-compiler/
- https://gitlab.gnome.org/GNOME/blueprint-compiler

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.blp` | [hello.blp](hello.blp) creato, verifiche pendenti |
