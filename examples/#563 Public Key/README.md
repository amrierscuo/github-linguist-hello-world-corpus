# #563 Public Key

Read a public demonstration key Ed25519 with commentary on the greeting.

## Toolchain

OpenSSH_9.6p1 Ubuntu-3ubuntu13.19, OpenSSL 3.0.13 30 Jan 2024

## Procedure

ssh-keygen -t ed25519 -N "" -C "Hello, World!" -f <work-private-key>; ssh-keygen -lf hello.pub

## Expected result

ssh-keygen recognizes ED25519 and shows the comment Hello, World!.

## Status

syntax and behavior verified.

hello.pub is really generated for this example. The corpus contains only the public key; the temporary private key remains in work. The goal is the valid key and comment, do not encrypt greeting.

Real check 2026-10-08T13:16:51.649710+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://man.openbsd.org/ssh-keygen](https://man.openbsd.org/ssh-keygen)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.asc` | [hello.asc](variants/asc-431e050a/hello.asc) verified |
| `.pub` | [hello.pub](hello.pub) verified |
