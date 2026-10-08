# #191 Elm

Compilare un programma Elm che mostra Hello, World! come nodo di testo nel browser.

Tipo canonico `programming`, language_id `101`.

Toolchain prevista: Elm 0.19.1 e browser.

Dalla cartella dell’esempio:

```sh
elm make src/Main.elm --output=build/index.html
Aprire build/index.html in un browser.
```

Risultato atteso: testo visibile della pagina esattamente Hello, World!.

Le dipendenze Elm sono fissate alle versioni nel manifest. Il compilatore può richiedere l’accesso al registro dei pacchetti; compilazione e osservazione DOM vengono tracciate separatamente.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain nativa non ancora eseguita: le verifiche di sintassi e semantica restano pendenti.

Fonti del linguaggio/formato e implementazioni originali:

- [Elm — testo HTML e architettura](https://guide.elm-lang.org/architecture/text_fields.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.elm` | [Main.elm](src/Main.elm) creato, verifiche pendenti |
