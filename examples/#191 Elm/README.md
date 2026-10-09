# #191 Elm

Il programma Elm mostra `Hello, World!` come nodo di testo nella pagina.

Tipo canonico `programming`, language_id `101`.

## Toolchain e riproduzione

Prova eseguita con Elm 0.19.1 su Windows x64. Il manifest fissa `elm/core` 1.0.5, `elm/html` 1.0.0, `elm/json` 1.1.3 e `elm/virtual-dom` 1.0.3.

Dalla cartella dell'esempio, con una directory di output già creata:

```sh
elm make src/Main.elm --output=build/index.html
```

Aprire il file HTML generato in un browser: il testo applicativo deve essere esattamente `Hello, World!`.

Il controllo automatico usa Node 22.20.0 e jsdom 26.1.0, installati fuori dal corpus. Con `NODE_PATH` che indica la cartella `node_modules` di queste dipendenze:

```sh
node verification/check_dom.cjs build/index.html
```

Il controllo esegue il JavaScript originale prodotto da Elm, verifica `Elm.Main.init`, il nodo di testo applicativo e l'assenza di errori. I nodi `<script>` non fanno parte del testo visibile. Un secondo DOM senza esecuzione deve mantenere vuoto il mount, quindi il successo non dipende dalla semplice presenza della stringa nel codice generato.

## Stato ed evidenza

Sintassi e semantica verificate. Il browser reale mostra `Hello, World!`; l'albero di accessibilità conferma lo stesso testo. La console riporta solo l'avviso Elm relativo alla modalità DEV.

[Log nativo](verification/native.json) con comandi reali, versioni, stdout/stderr, timestamp UTC e SHA256 degli input e dell'HTML generato. La compilazione avviene su copie byte-identiche del manifest e del sorgente in una directory di lavoro isolata. Il DOM jsdom verifica l'esecuzione; la prova nel browser documenta anche l'osservazione visiva.

![Pagina prodotta da Elm nel browser](verification/browser.png)

Toolchain, pacchetti ed HTML compilato rimangono nella directory di lavoro.

## Fonti primarie

- [Compilare con elm make](https://guide.elm-lang.org/install/elm.html)
- [Elm e testo HTML](https://guide.elm-lang.org/architecture/text_fields.html)
- [Esecuzione script in jsdom](https://github.com/jsdom/jsdom#executing-scripts)

## Copertura delle estensioni

Ogni suffisso mantiene la propria prova; le varianti pendenti non ereditano le verifiche.

| Estensione | File e stato |
| --- | --- |
| `.elm` | [Main.elm](src/Main.elm) sintassi e semantica verificate |
