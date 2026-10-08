# 0532 — Perl: `.plx`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#532 Perl/hello.pl.

Toolchain richiesta: Authentic Perl interpreter — This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi. La versione osservata nella prova effettiva è riportata nel log; gli ambienti applicativi non esercitati restano pendenti.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.plx; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: Il risultato conforme contiene Hello, World!, secondo l’ambito descritto.

Stato individuale: artefatto creato `true`, sintassi verificata `true`, semantica verificata `true`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- Nessun impedimento per l’ambito effettivamente verificato.

SHA-256 dei file della variante:

- `hello.plx`: `8282ea45dea2901f533f4afb329f4fb75983a128618abd230e065601b281fb4d`

Fonti primarie:

- https://perldoc.perl.org/perlintro

Prova aggiuntiva realmente eseguita:

Perl originale: compile check; esecuzione del driver o TAP con prove. Il .al ha solo sintassi verificata perché AutoLoader non esercitato.

Log: `verification/native.json`. Le procedure proposte sopra non eseguite restano distinte dai comandi nel log.

Tool/versione osservata: This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi
