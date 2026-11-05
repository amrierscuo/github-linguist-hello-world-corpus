# Native verification: November 5, 2026

## #509 Option List

The unchanged original `.rspec` and `hello_spec.rb` passed with Ruby 3.2.3 and RSpec 3.13 in Ubuntu WSL. RSpec automatically loaded `--format documentation` and `--no-color` from the option-list file. The output included the exact `Hello, World!` heading, `adds two integers`, and `1 example, 0 failures`, without ANSI color.

A control copied only the byte-identical Ruby source into an empty directory. The same command passed using the default progress formatter and did not emit the greeting heading or example description. The formatter options were never supplied on the command line.

[Commands, versions, outputs, assertions, archive identities and source SHA-256 values](../examples/%23509%20Option%20List/verification/native_20261105.json).

The toolchain was extracted under the local work directory and used an isolated home/configuration. No system packages were installed, and no .NET toolchain, graphical application or popup was invoked. Sources were unchanged.

Main samples now have **549/836 syntax checks** and **522/836 behavior checks** recorded, leaving **314 behavior checks pending**. Option List has canonical filenames but no extensions, so extension verification counts remain **671/1749 syntax** and **597/1749 behavior**. This data-format test does not add a name to GitHub's Languages statistics.
