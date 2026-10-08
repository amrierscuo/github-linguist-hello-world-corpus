# #585 RBS

Analizzare un alias RBS di tipo string literal uguale al saluto.

Tipo canonico `data`, language_id `899227493`.

Toolchain prevista: Ruby e RBS parser.

Dalla cartella dell’esempio:

```sh
ruby verify.rb
```

Risultato atteso: type alias greeting con literal Hello, World!.

Un type alias non esegue Ruby. La verifica riguarda la dichiarazione e il valore nel suo AST.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Ruby 3.2.3 + RBS parser. [Log](verification/result.json). 

Fonti:

- [RBS syntax](https://github.com/ruby/rbs/blob/master/docs/syntax.md)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.rbs` | [hello.rbs](hello.rbs) verificato |
