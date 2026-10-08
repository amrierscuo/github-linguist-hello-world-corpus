# 0294 — Haxe: `.hxsl`

Ruolo: Classe Haxe con shader HXSL Heaps reale in SRC e costante greeting lato host. La costante contiene il saluto; lo shader produce colore uniforme e non disegna lettere.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: Haxe4.3.3, pacchetto Ubuntu4.3.3-1build2. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
In una directory di lavoro copiare GreetingShader.hxsl come GreetingShader.hx; con Haxe + Heaps: haxe -lib heaps -main Main --interp. L’importer nativo del suffisso e il rendering GPU restano da verificare.
```

Risultato atteso: Il driver host stampa Hello, World!; il macro compiler HXSL analizza SRC. Non si promette testo renderizzato dallo shader.

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.
- Heaps/HXSL non predisposto con versione compatibile; macro compilazione non eseguita. Il frontend storico per il suffisso .hxsl e il rendering GPU non sono stati provati.

SHA-256 dei file della variante:

- `GreetingShader.hxsl`: `cd3ab7bf25278971b1e61638f3e594c2e953d5825cffc5ddd2315b9c84528e65`
- `Main.hx`: `6bfefc0879bc46a90004ae87b4398585e238e8ee49857ad5b461fe54f5c7db73`

Fonti primarie:

- https://heaps.io/documentation/hxsl.html
- https://raw.githubusercontent.com/pygments/pygments/master/pygments/lexers/haxe.py
- https://haxe.org/manual/introduction-hello-world.html
- https://api.haxe.org/Sys.html
