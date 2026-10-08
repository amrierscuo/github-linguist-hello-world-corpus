# #338 JavaScript+ERB

Renderizzare JavaScript+ERB con Ruby e poi eseguire il JavaScript generato in Node.

Tipo canonico `programming`, language_id `914318960`.

Toolchain prevista: Ruby ERB standard library e Node.js 22.

Dalla cartella dell’esempio:

```sh
ruby verify.rb
```

Risultato atteso: stdout Hello, World! e LF, entrambi i runtime terminano con successo.

Il saluto è inserito come literal quotato da Ruby String.dump; il template non è trattato come JavaScript puro.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Ruby 3.2.3 ERB + Node.js 22.20.0. [Log](verification/result.json). 

Fonti:

- [Ruby — ERB](https://docs.ruby-lang.org/en/master/ERB.html)
- [Node.js — console](https://nodejs.org/api/console.html)

Ruby ERB viene dalla libreria standard Ruby 3.2.3. NODE_BINARY può indicare un percorso Node completo; il checker lo passa a Open3 come argv, preservando gli spazi nel percorso.

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.js.erb` | [hello.js.erb](hello.js.erb) verificato |
