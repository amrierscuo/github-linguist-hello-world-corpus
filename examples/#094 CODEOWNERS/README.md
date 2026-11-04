# #094 CODEOWNERS

Join in an example CODEOWNERS the route / hello.txt to the owner hello@ example.invalid, and check the match with a local parser.

## Toolchain

Python 3.13.9; codeowners 0.9.0 community parser

## Commands and procedure

From this folder:

```sh
python -m pip install -r requirements.txt
python verify.py
```

The local parser reads syntax and applies the path rule.
remains illustrative and does not match a GitHub account. This file is
in the individual sample, not in .github / CODEOWNERS: does not allocate auditors
to the corpus repository.

## Expected result

Local Parser: hello.txt -> EMAIL hello@ example.invalid, other.txt -> no owner. GitHub resolution would require a real eligible account.

## Status

syntax verified; behavioral verification pending.

Email illustrated on the reserved domain example.invalid; it does not indicate a real user and does not produce revision requests. Do not use this file as an actual CODEOWNERS of the public repository.

Actual verification of 2026-10-08T11:33:36.889535+00:00 on Windows x64: [log](verification/result.json).
The log includes hash SHA-256 of the source and the checkers, versions, commands, exit codes, stdout, stderr and test limits.

Remaining requirements:
- GitHub eligibility and review assignment not verifiable with an illustrative address.

## Primary sources

- [https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
- [https://github.com/sbdchd/codeowners](https://github.com/sbdchd/codeowners)
