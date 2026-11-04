# #586 RDoc

Render a RDoc title with the original HTML form.

Canonical type `prose`, language_id `309`.

Suggested toolchain: Ruby and RDoc markup parser/HTML formatter.

From the example directory:

```sh
ruby verify.rb
```

Expected result: HTML with heading h1 containing Hello, World!.

The result is obtained from the parser and the form of the Ruby library.

Recorded status: syntax verified; behavior verified. Toolchain: Ruby 3.2.3 + RDoc markup formatter. [Log](verification/result.json).

Sources:

- [Ruby RDoc markup](https://ruby.github.io/rdoc/RDoc/Markup.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.rdoc` | [hello.rdoc](hello.rdoc) verified |
