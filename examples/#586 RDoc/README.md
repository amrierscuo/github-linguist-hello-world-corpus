# #586 RDoc

Renderizzare un titolo RDoc con il formatter HTML originale.

Tipo canonico `prose`, language_id `309`.

Toolchain prevista: Ruby e RDoc markup parser/HTML formatter.

Dalla cartella dell’esempio:

```sh
ruby verify.rb
```

Risultato atteso: HTML con heading h1 contenente Hello, World!.

Il risultato viene ottenuto dal parser e dal formatter della libreria Ruby.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Ruby 3.2.3 + RDoc markup formatter. [Log](verification/result.json). 

Fonti:

- [Ruby RDoc markup](https://ruby.github.io/rdoc/RDoc/Markup.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.rdoc` | [hello.rdoc](hello.rdoc) verificato |
