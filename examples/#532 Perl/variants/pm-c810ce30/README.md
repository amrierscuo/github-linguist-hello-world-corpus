# 0532 — Perl: `.pm`

Ruolo: Modulo Perl con funzione greeting e valore true finale.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Authentic Perl interpreter — This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi. La versione osservata nella prova effettiva è riportata nel log; gli ambienti applicativi non esercitati restano pendenti.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
perl -I. driver.pl
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `true`, semantica verificata `true`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- Nessun impedimento per l’ambito effettivamente verificato.

SHA-256 dei file della variante:

- `Corpus/Greeting.pm`: `c54727a5ded013ccff1648616c14b86bd3852dde0a29fdcbb188235fc7675161`
- `driver.pl`: `057a7e9100f23bf5ef115eb1d1cfa69e9d391761d08730c65f0e85573f5e10bf`

Fonti primarie:

- https://perldoc.perl.org/perlmod
- https://perldoc.perl.org/perlintro

Prova aggiuntiva realmente eseguita:

Perl originale: compile check; esecuzione del driver o TAP con prove. Il .al ha solo sintassi verificata perché AutoLoader non esercitato.

Log: `verification/native.json`. Le procedure proposte sopra non eseguite restano distinte dai comandi nel log.

Tool/versione osservata: This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi
