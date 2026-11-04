# #810 cURL Config

Read .curlrc and consume header greeting via HTTP loopback.

## Toolchain

curl 8.21.0 (Windows) libcurl/8.21.0 Schannel zlib/1.3.2 WinIDN WinLDAP; CPython3.13.9

## Procedure

python verify.py <curl-executable>

## Expected result

Hello, World!

## Status

syntax and behavior verified.

The server response comes from the received header: actual proof of configuration options. Ephemeral loopback port, no external request.

Real check 2026-10-08T13:38:35.028326+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://curl.se/docs/manpage.html#-K](https://curl.se/docs/manpage.html#-K)
