# 0754 — `.vba`

Vimball autentico prodotto dal plugin originale Vimball; .vmb e .vba sono suffissi supportati della stessa serializzazione testuale. Payload originale, estrazione esclusivamente in work.

Provenienza: produttore/serializzatore originale eseguito, come registrato nel log.

Artefatto principale: `hello.vba`.

Controllo previsto:

```text
vim --version
vim -Nu NONE -i NONE -n -es -S make.vim
```

Risultato atteso: Vimball generato con payload originale; successiva estrazione isolata e CorpusGreeting devono restituire Hello, World!.

Stato: creato; sintassi non verificata; semantica non verificata.

Toolchain osservata: VIM - Vi IMproved 9.1 (2024 Jan 02, compiled Aug 24 2026 22:13:04).

Ambito reale: Generatore originale MkVimball produce il vero archivio testuale con payload originale. Il tentativo batch di estrazione termina prima del controllo finale: nessun esito di parser/estrazione/esecuzione viene dichiarato.

Log: `verification/result.json`; SHA-256 di ogni sorgente/supporto della variante, comandi, exit code e output effettivi. Build/cache restano sotto `work/verify_extensions_561_836`.

Blocchi: Estrazione/importazione del Vimball non verificati: il comando Vim batch termina prima di scrivere il risultato di controllo.

Fonti primarie:

- [https://vimhelp.org/pi_vimball.txt.html](https://vimhelp.org/pi_vimball.txt.html)
