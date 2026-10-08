# 0532 — Perl: `.t`

Ruolo: Test Perl TAP con asserzione del valore e diagnostico, non output main.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Authentic Perl interpreter — This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi. La versione osservata nella prova effettiva è riportata nel log; gli ambienti applicativi non esercitati restano pendenti.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
prove hello.t
```

Risultato atteso: Un test TAP PASS; valore verificato Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `true`, semantica verificata `true`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- Nessun impedimento per l’ambito effettivamente verificato.

SHA-256 dei file della variante:

- `hello.t`: `0c2d700513ea3f0d8014dbd466a432b932812ea5a1b8b6fe9ec8b821a74fb2bc`

Fonti primarie:

- https://perldoc.perl.org/Test::More
- https://perldoc.perl.org/perlintro

Prova aggiuntiva realmente eseguita:

Perl originale: compile check; esecuzione del driver o TAP con prove. Il .al ha solo sintassi verificata perché AutoLoader non esercitato.

Log: `verification/native.json`. Le procedure proposte sopra non eseguite restano distinte dai comandi nel log.

Tool/versione osservata: This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi
