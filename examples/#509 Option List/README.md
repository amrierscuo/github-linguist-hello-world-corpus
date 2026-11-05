# #509 Option List

The original `.rspec` selects RSpec's documentation formatter and disables color. The accompanying Ruby specification has one passing arithmetic assertion and the greeting as its example-group name.

## Recorded verification

**Syntax and behavior verified on November 5, 2026.** Ruby 3.2.3 and RSpec 3.13 ran the unchanged original files in Ubuntu WSL. The formatter options were loaded automatically from `.rspec`; they were not repeated on the command line.

```sh
rspec hello_spec.rb
```

The output includes:

```text
Hello, World!
  adds two integers

1 example, 0 failures
```

No ANSI color sequences were present. An isolated control using the identical `hello_spec.rb` without `.rspec` passed using the default progress formatter, without the greeting heading or example description. This confirms that the option-list file changes the consumer's behavior.

[Native commands, toolchain versions, both outputs and exact SHA-256 values](verification/native_20261105.json).

Canonical type `data`, language_id `723589315`. This entry is recognized by filenames, so this check adds no language-extension pair and makes no claim about GitHub language statistics.

Sources:

- [RSpec command-line configuration](https://rspec.info/features/3-13/rspec-core/configuration/command-line/)
- [RSpec's native configuration-option loader](https://github.com/rspec/rspec-core/blob/v3.13.0/lib/rspec/core/configuration_options.rb)
