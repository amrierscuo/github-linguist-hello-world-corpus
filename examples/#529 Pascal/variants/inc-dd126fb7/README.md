# 0529 — Pascal: `.inc`

Ruolo: Include Pascal con procedura Greet; driver usa direttiva I.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Genuine Free Pascal compiler — 3.2.2. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
fpc driver.pas; ./driver
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `driver.pas`: `7636fe3a7b10fc7201b919ac2ff4d125cd68a089f2164e94a4e09c4331f3a3f7`
- `hello.inc`: `f02281eb8fb13b30830dcdf061635663c34745dfccd82acc4389e4109a5e93c7`

Fonti primarie:

- https://www.freepascal.org/docs-html/prog/progsu40.html
- https://www.freepascal.org/docs.html
