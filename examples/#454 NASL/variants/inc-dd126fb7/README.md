# 0454 — NASL: `.inc`

Ruolo: Include NASL con funzione di saluto e caller separato.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Authentic Greenbone OpenVAS NASL interpreter — openvas-nasl 22.7.9; ; Copyright (C) 2002 - 2004 Tenable Network Security; Copyright (C) 2022 Greenbone Networks GmbH. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
NASL originale: caricare driver.nasl senza target di rete
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `driver.nasl`: `85f71558fcc4f5b8cf802078a9b0fb30a5e098b45fc02923e14718fea9a30b3f`
- `hello.inc`: `5bfffc3e2878a4a9f76d701681774a11956f300a40f657a451fe903e4fa482be`

Fonti primarie:

- https://github.com/greenbone/openvas-scanner
