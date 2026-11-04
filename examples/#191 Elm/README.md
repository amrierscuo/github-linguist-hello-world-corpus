# #191 Elm

The Elm program shows `Hello, World!` as a text node on the page.

Canonical type `programming`, language_id `101`.

## Toolchain and reproduction

Test performed with Elm 0.19.1 on Windows x64. The fixed poster `elm/core` 1.0.5, `elm/html` 1.0.0, `elm/json` 1.1.3 and `elm/virtual-dom` 1.0.3.

From the example folder, with an output directory already created:

```sh
elm make src/Main.elm --output=build/index.html
```

Open the HTML file generated in a browser: the application text must be exactly `Hello, World!`.

Automatic control uses Node 22.20.0 and jsdom 26.1.0, installed outside the corpus. With `NODE_PATH` indicating the `node_modules` folder of these dependencies:

```sh
node verification/check_dom.cjs build/index.html
```

The control performs the original JavaScript produced by Elm, `Elm.Main.init` verification, the application text node and the absence of errors. The `<script>` nodes are not part of the visible text. A second DOM without execution must keep the mount empty, so the success does not depend on the simple presence of the string in the generated code.

## Status and evidence

syntax and behavior verified. The real browser shows `Hello, World!`; the accessibility tree confirms the same text. The console only reports Elm's notice on the DEV mode.

[Log nativo](verification/native.json) con comandi reali, versioni, stdout/stderr, timestamp UTC e SHA256 degli input e dell'HTML generato. La compilazione avviene su copie byte-identiche del manifest e del sorgente in una directory di lavoro isolata. Il DOM jsdom verifica l'esecuzione; la prova nel browser documenta anche l'osservazione visiva.

![Pagina prodotta da Elm nel browser](verification/browser.png)

Toolchain, packages and HTML compiled remain in the work directory.

## Primary sources

- [Compilare con elm make](https://guide.elm-lang.org/install/elm.html)
- [Elm e testo HTML](https://guide.elm-lang.org/architecture/text_fields.html)
- [Esecuzione script in jsdom](https://github.com/jsdom/jsdom#executing-scripts)

## Extension coverage

Each suffix maintains its own test; the pending variants do not inherit verifications.

| Extension | File and status |
| --- | --- |
| `.elm` | [Main.elm](src/Main.elm) syntax and behavior verified |
