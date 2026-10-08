# 0532 — Perl: `.fcgi`

Ruolo: Script Perl FastCGI con loop FCGI del saluto.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Authentic Perl interpreter — This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
perl -c hello.fcgi con FCGI installato; host FastCGI locale, richiesta loopback e cleanup
```

Risultato atteso: Corpo risposta Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.fcgi`: `53b76453f70f7086dc342772690a7c22f4f86ba6f8d0dc81c9a53e48d5fb8535`

Fonti primarie:

- https://metacpan.org/pod/FCGI
- https://perldoc.perl.org/perlintro
