# 563 — Public Key — `.asc`

Chiave pubblica OpenPGP Ed25519 originale, generata realmente da GnuPG con UID `Hello, World! <corpus@example.invalid>`. Il file `greeting.txt` e il generatore sono inclusi; chiavi private e keyring di prova restano sotto `work`.

Dalla cartella della variante, con Python e GnuPG disponibili in WSL Ubuntu:

```text
python generate.py /absolute/work/verify_replacement_asc_hello
```

Il generatore scrive `hello.asc` nella directory di build, importa la chiave in un keyring pubblico indipendente e verifica l’UID letterale. Nessun invio a keyserver.

Risultato atteso: `Hello, World! <corpus@example.invalid>` e chiave pubblica Ed25519 riconosciuta.

Stato: sintassi e semantica verificate. Toolchain osservata: gpg (GnuPG) 2.4.4. Log `verification/result.json` con SHA-256 di ogni sorgente/helper, comandi, ambiente, exit code e output reali.

Fonte primaria: [GnuPG OpenPGP Key Management](https://www.gnupg.org/documentation/manuals/gnupg/OpenPGP-Key-Management.html).
