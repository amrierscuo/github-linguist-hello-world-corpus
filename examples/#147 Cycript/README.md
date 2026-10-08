# #147 Cycript

Voce canonica e ordine del `reference/languages.yml` del corpus. I sorgenti e fixture sono originali; eventuali dump/bundle provengono dagli strumenti indicati.

## Obiettivo

Usare l’interoperabilità C di Cycript per passare il saluto a puts.

Il sorgente combina concatenazione ECMAScript e il cast Cycript (typedef const char *). La chiamata puts richiede le dichiarazioni libc disponibili nel runtime Cycript. Il file va verificato nel motore originale: Node.js non interpreta questa sintassi FFI.

## Toolchain e riproduzione

Cycript con JavaScriptCore e binding libc, su piattaforma supportata; versione effettiva da registrare

Comandi nella cartella dell’esempio con la toolchain disponibile nel PATH. Usare una copia temporanea: database, oggetti, audio e altri output di prova non appartengono al corpus.

```text
cycript hello.cy
```

## Risultato atteso e stato

puts emette Hello, World! e newline.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Il sorgente è documentato; parser/compilatore/runtime nativo non è stato eseguito per questa voce.

Impedimenti: Cycript/JavaScriptCore con binding C non disponibili nell’ambiente corrente; parsing e FFI restano pendenti.

## Fonti primarie

- https://www.cycript.org/manual/
- https://www.cycript.org/

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cy` | [hello.cy](hello.cy) creato, verifiche pendenti |
