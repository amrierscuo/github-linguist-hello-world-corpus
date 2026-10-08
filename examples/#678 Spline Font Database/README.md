# #678 Spline Font Database

Aprire un Spline Font Database e recuperare il FullName del font.

Tipo canonico `data`, language_id `767169629`.

Toolchain prevista: FontForge.

Dalla cartella dell’esempio:

```sh
fontforge -lang=ff -c 'Open($1); Print($fullname);' hello.sfd
```

Risultato atteso: FontForge accetta il font e legge FullName Hello, World!.

Il font contiene metadati e nessun glifo: l’obiettivo è il nome del font, non il rendering del saluto.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain non ancora eseguita: sintassi e semantica restano pendenti.

Fonti:

- [FontForge SFD](https://fontforge.org/docs/techref/sfdformat.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.sfd` | [hello.sfd](hello.sfd) creato, verifiche pendenti |
