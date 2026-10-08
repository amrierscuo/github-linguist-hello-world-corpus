# 0337 — JavaScript: `.pac`

Ruolo: Proxy Auto-Configuration valido: funzione restituisce DIRECT, greeting è dato separato; non cambia proxy OS.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Node.js 22.20.0. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Parser PAC originale offline: caricare hello.pac e chiamare FindProxyForURL con example.invalid
```

Risultato atteso: Hello, World! nel log/valore/risposta o geometria secondo il ruolo; PAC restituisce DIRECT senza rete.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.pac`: `47984106a219916b503577a800d7a8727bea4fa908094d45f9aaf9174f60cc63`

Fonti primarie:

- https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Proxy_servers_and_tunneling/Proxy_Auto-Configuration_PAC_file
- https://nodejs.org/api/console.html#consolelogdata-args
