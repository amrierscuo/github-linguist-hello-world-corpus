# #338 JavaScript+ERB

Render JavaScript+ ERB with Ruby and then execute the JavaScript generated in Node.

Canonical type `programming`, language_id `914318960`.

Suggested toolchain: Ruby ERB standard library and Node.js 22.

From the example directory:

```sh
ruby verify.rb
```

Expected result: stdout Hello, World! and LF, both runtimes successfully finish.

Greeting is included as a literal quoted by Ruby String.dump; the template is not treated as pure JavaScript.

Recorded status: syntax verified; behavior verified. Toolchain: Ruby 3.2.3 ERB + Node.js 22.20.0. [Log](verification/result.json).

Sources:

- [Ruby — ERB](https://docs.ruby-lang.org/en/master/ERB.html)
- [Node.js — console](https://nodejs.org/api/console.html)

Ruby ERB comes from the standard Ruby 3.2.3 library. NODE_BINARY can indicate a complete Node path; the checker passes it to Open3 as argv, preserving the spaces in the path.

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.js.erb` | [hello.js.erb](hello.js.erb) verified |
