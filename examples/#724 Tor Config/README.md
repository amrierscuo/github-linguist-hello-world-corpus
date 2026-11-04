# #724 Tor Config

Validate a minimal torrc with disabled network.

## Toolchain

Tor version 0.4.9.11.
This build of Tor is covered by the GNU General Public License (https://www.gnu.org/licenses/gpl-3.0.en.html)
Tor is running on Linux with Libevent 2.1.12-stable, OpenSSL 3.0.13, Zlib 1.3, Liblzma 5.4.5, Libzstd 1.5.5 and Glibc 2.39 as libc.
Tor compiled with GCC version 13.3.0

## Procedure

tor --verify-config -f torrc --DataDirectory <work-directory>

## Expected result

Configuration was valid; nessun listener/rete avviati.

## Status

syntax and behavior verified.

The goal of configuration is a valid parsing of the SocksPort/DisableNetwork directives; the greeting is a documentary comment, without starting Tor.

Real check 2026-10-08T13:30:09.923658+00:00: [log](verification/result.json).
The log includes SHA-256 of sorgenti/checker, versions, commands, exit codes, stdout/stderr and verification field.

## Primary sources

- [https://spec.torproject.org/tor-manual.html](https://spec.torproject.org/tor-manual.html)
