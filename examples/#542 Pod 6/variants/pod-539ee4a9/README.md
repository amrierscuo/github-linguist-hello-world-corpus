# 0542 — Pod 6: `.pod`

Ruolo: Alias di estensione per lo stesso formato testuale del sorgente principale.

Provenienza: Copia byte-identica del sorgente originale del corpus: examples/#542 Pod 6/hello.pod6.

Toolchain richiesta: Rakudo/MoarVM2022.12 originale, parser Pod6 e renderer Pod::To::Text. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Usare la toolchain del README principale sul file hello.pod; eventuali file generati e rinomine richieste dal compilatore vanno in una directory di lavoro.
```

Risultato atteso: Documento renderizzato contiene Hello, World!.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.pod`: `a0a2603939cf43362da0a40d2fbed3e79ffff948694dca57c6b341444f8ed01b`

Fonti primarie:

- https://docs.raku.org/language/pod
