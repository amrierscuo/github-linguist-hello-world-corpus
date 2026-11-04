# #509 Option List

Upload a list of RSpec options and get the greeting as header of the formatter documentation.

Canonical type `data`, language_id `723589315`.

Suggested toolchain: Ruby and RSpec.

From the example directory:

```sh
rspec hello_spec.rb
```

Expected result: formatter documentation shows Hello, World!; an example passes.

The primary artifact is .rspec: the verification must use the options of that file, not a command that repeats it.

Initial state: created; syntax and behavioral verification pending. Toolchain not yet performed: syntax and behavior remain pending.

Sources:

- [RSpec options](https://rspec.info/features/3-13/rspec-core/configuration/command-line/)
