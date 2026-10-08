# 0696 — `.8xp`

Programma TI-84 Plus tokenizzato e contenitore/checksum prodotti realmente dalla libreria originale tivars; sorgente Disp originale e generatore inclusi. Nessuna esecuzione su calcolatrice/emulatore dichiarata.

Provenienza: produttore/serializzatore originale eseguito, come registrato nel log.

Artefatto principale: `hello.8xp`.

Controllo previsto:

```text
python --version
python generate.py
```

Risultato atteso: tivars rilegge Disp "Hello, World!" identico; esecuzione su TI-84 Plus ancora pendente.

Stato: creato; sintassi verificata; semantica non verificata.

Toolchain osservata: tivars 1.1.1; Python 3.13.9.

Ambito reale: Serializzazione/tokenizzazione nativa e roundtrip con tivars. Il parser riconosce il programma e preserva i token di Disp; un runtime TI non è stato eseguito.

Log: `verification/result.json`; SHA-256 di ogni sorgente/supporto della variante, comandi, exit code e output effettivi. Build/cache restano sotto `work/verify_extensions_561_836`.

Blocchi: Esecuzione del programma su calcolatrice/emulatore TI-84 Plus ancora pendente.

Fonti primarie:

- [https://github.com/TI-Toolkit/tivars_lib_py](https://github.com/TI-Toolkit/tivars_lib_py)
