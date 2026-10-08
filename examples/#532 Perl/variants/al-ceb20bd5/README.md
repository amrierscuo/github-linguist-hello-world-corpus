# 0532 — Perl: `.al`

Ruolo: Autosplit/autoload Perl: file package::greeting, non programma main.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Authentic Perl interpreter — This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi. La versione osservata nella prova effettiva è riportata nel log; gli ambienti applicativi non esercitati restano pendenti.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Perl AutoLoader: collocare greeting.al nella directory auto/Corpus/Greeting e invocare greeting via modulo host
```

Risultato atteso: Hello, World! restituito dalla sub

Stato individuale: artefatto creato `true`, sintassi verificata `true`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- Parser del linguaggio accettato; schema/loader/semantica applicativa specifici restano non verificati.

SHA-256 dei file della variante:

- `greeting.al`: `e8369f9c7386527631e57d8265ac04998c4c42157d95a75d6b21f25f0ac7ecb1`

Fonti primarie:

- https://perldoc.perl.org/AutoLoader
- https://perldoc.perl.org/perlintro

Prova aggiuntiva realmente eseguita:

Perl originale: compile check; esecuzione del driver o TAP con prove. Il .al ha solo sintassi verificata perché AutoLoader non esercitato.

Log: `verification/native.json`. Le procedure proposte sopra non eseguite restano distinte dai comandi nel log.

Tool/versione osservata: This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi
