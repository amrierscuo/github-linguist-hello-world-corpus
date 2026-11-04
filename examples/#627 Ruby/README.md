# #627 Ruby

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Eseguire Ruby e stampare Hello, World!.

La variabile audience viene concatenata da Ruby e inviata a puts.

## Toolchain and reproduction

Ruby3.2.3 originale

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
ruby hello.rb
```

## Expected result and status

Hello, World! su stdout.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://docs.ruby-lang.org/en/3.2/syntax/assignment_rdoc.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.rb` | [hello.rb](hello.rb), [greeting.rb](variants/eye-a4e8f371/greeting.rb), [hello.rb](variants/gemspec-aea1a1bf/hello.rb), [greeting.rb](variants/god-b5030de8/greeting.rb), [greeting_spec.rb](variants/mspec-5a0076c7/greeting_spec.rb), [greeting.rb](variants/pluginspec-34c2c898/greeting.rb), [hello.rb](variants/rbi-72901eb3/hello.rb), [greeting.rb](variants/rbuild-2105022d/greeting.rb), [greeting.rb](variants/spec-98ef28e4/greeting.rb) created; verification pending |
| `.builder` | [hello.builder](variants/builder-7b1ea7a5/hello.builder) created; verification pending |
| `.eye` | [hello.eye](variants/eye-a4e8f371/hello.eye) created; verification pending |
| `.fcgi` | [hello.fcgi](variants/fcgi-209194e4/hello.fcgi) created; verification pending |
| `.gemspec` | [hello.gemspec](variants/gemspec-aea1a1bf/hello.gemspec) created; verification pending |
| `.god` | [hello.god](variants/god-b5030de8/hello.god) created; verification pending |
| `.jbuilder` | [hello.jbuilder](variants/jbuilder-3dcc02a0/hello.jbuilder) created; verification pending |
| `.mspec` | [hello.mspec](variants/mspec-5a0076c7/hello.mspec) created; verification pending |
| `.pluginspec` | [hello.pluginspec](variants/pluginspec-34c2c898/hello.pluginspec) created; verification pending |
| `.podspec` | [hello.podspec](variants/podspec-4bc278ff/hello.podspec) created; verification pending |
| `.prawn` | [hello.prawn](variants/prawn-3c3ab28a/hello.prawn) created; verification pending |
| `.rabl` | [hello.rabl](variants/rabl-d915eb5e/hello.rabl) created; verification pending |
| `.rake` | [hello.rake](variants/rake-2eae2343/hello.rake) created; verification pending |
| `.rbi` | [hello.rbi](variants/rbi-72901eb3/hello.rbi) created; verification pending |
| `.rbuild` | [hello.rbuild](variants/rbuild-2105022d/hello.rbuild) created; verification pending |
| `.rbw` | [hello.rbw](variants/rbw-99e25565/hello.rbw) created; verification pending |
| `.rbx` | [hello.rbx](variants/rbx-a931b946/hello.rbx) created; verification pending |
| `.ru` | [hello.ru](variants/ru-98027f7e/hello.ru) created; verification pending |
| `.ruby` | [hello.ruby](variants/ruby-c7d080c9/hello.ruby) created; verification pending |
| `.spec` | [hello.spec](variants/spec-98ef28e4/hello.spec) created; verification pending |
| `.thor` | [hello.thor](variants/thor-62b809ed/hello.thor) created; verification pending |
| `.watchr` | [hello.watchr](variants/watchr-53df3419/hello.watchr) created; verification pending |
