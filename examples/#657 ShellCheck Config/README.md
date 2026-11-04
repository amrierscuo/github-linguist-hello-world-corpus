# #657 ShellCheck Config

Read the .shellcheckrc configuration with ShellCheck and check the script.

## Toolchain

ShellCheck - shell script analysis tool
version: 0.9.0
license: GNU General Public License, version 3
website: https://www.shellcheck.net

## Procedure

shellcheck hello.sh; sh hello.sh

## Expected result

Hello, World!

## Status

syntax and behavior verified.

The test checks that ShellCheck finds the local configuration without altering global configurations; the script is actually executed.

Real check 2026-10-08T13:23:05.420327+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://github.com/koalaman/shellcheck/wiki/Directive](https://github.com/koalaman/shellcheck/wiki/Directive)
