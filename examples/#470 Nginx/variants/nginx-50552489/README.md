# 0470 — Nginx: `.nginx`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#470 Nginx/hello.nginxconf.

Toolchain richiesta: Nginx1.24.0 Ubuntu, Python3 della fixture locale. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.nginx; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: Configurazione accettata; HTTP200/body esatto Hello, World!; CLEANUP confermato.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.nginx`: `41ef8b7f6b42418b067520314e2e5d2a710e0ec8f45adbac64988d5253ec981d`
- `verify.py`: `4726c2a66dd3ec19f94ddb8948571b052d1334f34814986d4c22170e8afba957`

Fonti primarie:

- https://nginx.org/en/docs/http/ngx_http_rewrite_module.html#return
- https://nginx.org/en/docs/switches.html
