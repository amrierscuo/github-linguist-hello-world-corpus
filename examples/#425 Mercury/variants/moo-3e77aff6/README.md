# 0425 — Mercury: `.moo`

Ruolo: Grammatica Moose originale, non programma Mercury ordinario: riconosce il token hello e restituisce un attributo stringa col saluto.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Mercury mmc e grade runtime installata. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Moose originale: moose hello.moo > hello.m; poi compilare il modulo generato con mmc. Per una prova semantica, implementare parser_state con stream [hello,eof] e invocare il parse generato.
```

Risultato atteso: Il generatore produce Mercury con parse_result greeting("Hello, World!") per i token hello,eof; esecuzione pendente.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.
- Moose e Mercury compatibili non predisposti. La grammatica è documentata; manca l’esecuzione del generatore e del driver parser_state, quindi entrambi i flag restano false.

SHA-256 dei file della variante:

- `hello.moo`: `a8ff8e11682f83328cb82f3241093992df3f7571ab1abef29373ab8194732d5d`

Fonti primarie:

- https://raw.githubusercontent.com/Mercury-Language/mercury/master/extras/moose/README
- https://raw.githubusercontent.com/Mercury-Language/mercury/master/extras/moose/samples/expr.moo
- https://www.mercurylang.org/information/doc-latest/mercury_user_guide/Hello-world.html
