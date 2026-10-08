# 0532 — Perl: `.ph`

Ruolo: Header Perl in stile h2ph con definizione di costante; require nel driver.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Authentic Perl interpreter — This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi. La versione osservata nella prova effettiva è riportata nel log; gli ambienti applicativi non esercitati restano pendenti.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
perl driver.pl
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `true`, semantica verificata `true`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- Nessun impedimento per l’ambito effettivamente verificato.

SHA-256 dei file della variante:

- `_h2ph_pre.ph`: `97a18ae8e28c3a8e24dc4a46fbb47a8106f7ca3e9e7a2015212caa44bf64db43`
- `driver.pl`: `bf52d94afda3bdda238b8a3eea136accc7628b4936a6b026d345782532b94c98`
- `hello.ph`: `28846bd1ef77bab45294429d8381cb9c792ea69c9df6aefa6dbb52b8df66fbad`

Fonti primarie:

- https://perldoc.perl.org/h2ph
- https://perldoc.perl.org/perlintro

Prova aggiuntiva realmente eseguita:

Perl originale: compile check; esecuzione del driver o TAP con prove. Il .al ha solo sintassi verificata perché AutoLoader non esercitato.

Log: `verification/native.json`. Le procedure proposte sopra non eseguite restano distinte dai comandi nel log.

Tool/versione osservata: This is perl 5, version 38, subversion 2 (v5.38.2) built for x86_64-linux-gnu-thread-multi
