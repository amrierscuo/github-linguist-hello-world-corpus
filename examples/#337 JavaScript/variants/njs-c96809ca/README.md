# 0337 — JavaScript: `.njs`

Ruolo: Modulo Nginx njs che esporta handler HTTP; usare solo loopback se eseguito.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Node.js 22.20.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
njs -c o nginx -t con js_import hello.njs; chiamare handler solo su 127.0.0.1 e arrestare server
```

Risultato atteso: Hello, World! nel log/valore/risposta o geometria secondo il ruolo; PAC restituisce DIRECT senza rete.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.njs`: `4559a47913cb7303394866afd2679e82699081d7fc29b704a7535e944fe574da`

Fonti primarie:

- https://nginx.org/en/docs/njs/
- https://nodejs.org/api/console.html#consolelogdata-args
