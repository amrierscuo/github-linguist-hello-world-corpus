# #627 Ruby

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Eseguire Ruby e stampare Hello, World!.

La variabile audience viene concatenata da Ruby e inviata a puts.

## Toolchain e riproduzione

Ruby3.2.3 originale

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
ruby hello.rb
```

## Risultato atteso e stato

Hello, World! su stdout.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://docs.ruby-lang.org/en/3.2/syntax/assignment_rdoc.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.rb` | [hello.rb](hello.rb), [greeting.rb](variants/eye-a4e8f371/greeting.rb), [hello.rb](variants/gemspec-aea1a1bf/hello.rb), [greeting.rb](variants/god-b5030de8/greeting.rb), [greeting_spec.rb](variants/mspec-5a0076c7/greeting_spec.rb), [greeting.rb](variants/pluginspec-34c2c898/greeting.rb), [hello.rb](variants/rbi-72901eb3/hello.rb), [greeting.rb](variants/rbuild-2105022d/greeting.rb), [greeting.rb](variants/spec-98ef28e4/greeting.rb) creato, verifiche pendenti |
| `.builder` | [hello.builder](variants/builder-7b1ea7a5/hello.builder) creato, verifiche pendenti |
| `.eye` | [hello.eye](variants/eye-a4e8f371/hello.eye) creato, verifiche pendenti |
| `.fcgi` | [hello.fcgi](variants/fcgi-209194e4/hello.fcgi) creato, verifiche pendenti |
| `.gemspec` | [hello.gemspec](variants/gemspec-aea1a1bf/hello.gemspec) creato, verifiche pendenti |
| `.god` | [hello.god](variants/god-b5030de8/hello.god) creato, verifiche pendenti |
| `.jbuilder` | [hello.jbuilder](variants/jbuilder-3dcc02a0/hello.jbuilder) creato, verifiche pendenti |
| `.mspec` | [hello.mspec](variants/mspec-5a0076c7/hello.mspec) creato, verifiche pendenti |
| `.pluginspec` | [hello.pluginspec](variants/pluginspec-34c2c898/hello.pluginspec) creato, verifiche pendenti |
| `.podspec` | [hello.podspec](variants/podspec-4bc278ff/hello.podspec) creato, verifiche pendenti |
| `.prawn` | [hello.prawn](variants/prawn-3c3ab28a/hello.prawn) creato, verifiche pendenti |
| `.rabl` | [hello.rabl](variants/rabl-d915eb5e/hello.rabl) creato, verifiche pendenti |
| `.rake` | [hello.rake](variants/rake-2eae2343/hello.rake) creato, verifiche pendenti |
| `.rbi` | [hello.rbi](variants/rbi-72901eb3/hello.rbi) creato, verifiche pendenti |
| `.rbuild` | [hello.rbuild](variants/rbuild-2105022d/hello.rbuild) creato, verifiche pendenti |
| `.rbw` | [hello.rbw](variants/rbw-99e25565/hello.rbw) creato, verifiche pendenti |
| `.rbx` | [hello.rbx](variants/rbx-a931b946/hello.rbx) creato, verifiche pendenti |
| `.ru` | [hello.ru](variants/ru-98027f7e/hello.ru) creato, verifiche pendenti |
| `.ruby` | [hello.ruby](variants/ruby-c7d080c9/hello.ruby) creato, verifiche pendenti |
| `.spec` | [hello.spec](variants/spec-98ef28e4/hello.spec) creato, verifiche pendenti |
| `.thor` | [hello.thor](variants/thor-62b809ed/hello.thor) creato, verifiche pendenti |
| `.watchr` | [hello.watchr](variants/watchr-53df3419/hello.watchr) creato, verifiche pendenti |
