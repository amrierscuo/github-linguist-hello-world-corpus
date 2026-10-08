# 0532 — Perl: `.psgi`

Ruolo: Applicazione PSGI: coderef che restituisce status, headers e array body.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Authentic Perl interpreter — This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Plack::Test locale: do hello.psgi; richiedere GET / nel test in-process (nessuna porta esterna)
```

Risultato atteso: HTTP 200 e corpo Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.psgi`: `a2703aaa4f0a0efb7e25005a155c5bbae3161d265c6ea8167a79ceec499530b6`

Fonti primarie:

- https://psgi.github.io/
- https://metacpan.org/pod/Plack::Test
- https://perldoc.perl.org/perlintro
