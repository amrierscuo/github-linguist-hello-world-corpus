# #724 Tor Config

Validare un torrc minimale con rete disabilitata.

## Toolchain

Tor version 0.4.9.11.
This build of Tor is covered by the GNU General Public License (https://www.gnu.org/licenses/gpl-3.0.en.html)
Tor is running on Linux with Libevent 2.1.12-stable, OpenSSL 3.0.13, Zlib 1.3, Liblzma 5.4.5, Libzstd 1.5.5 and Glibc 2.39 as libc.
Tor compiled with GCC version 13.3.0

## Procedura

tor --verify-config -f torrc --DataDirectory <work-directory>

## Risultato atteso

Configuration was valid; nessun listener/rete avviati.

## Stato

Sintassi e semantica verificate.

Il goal di configurazione è parsing valido delle direttive SocksPort/DisableNetwork; il saluto è un commento documentale, senza avviare Tor.

Verifica reale 2026-10-08T13:30:09.923658+00:00: [log](verification/result.json).
Il log include SHA-256 delle sorgenti/checker, versioni, comandi, codici di uscita, stdout/stderr e ambito della verifica.

## Fonti primarie

- [https://spec.torproject.org/tor-manual.html](https://spec.torproject.org/tor-manual.html)
