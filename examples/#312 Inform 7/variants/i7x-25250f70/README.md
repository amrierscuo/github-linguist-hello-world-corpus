# 0312 — Inform 7: `.i7x`

Ruolo: Estensione Inform 7 con intestazione Begins/Ends Here e frase riutilizzabile.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: inform7 version 10.1.2 'Krypton' (29 August 2022); Inform 6 Inform 6.41 for Linux (22nd July 2022); Frotz 2.54. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
Inform 7: installare Corpus Greeting.i7x e compilare il fixture hello.ni; eseguire lo story file
```

Risultato atteso: Hello, World!

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `Corpus Greeting.i7x`: `89648915fab2d3344e5b8ee081536d9eeb8ace4ebb4cf0a67d383413453373f5`
- `hello.ni`: `54009cbe19bf2aea007a5adc7ef87777d0b00e675e75cebfefb0b3e370b81028`

Fonti primarie:

- https://ganelson.github.io/inform-website/book/WI_27_1.html
- https://github.com/ganelson/inform/releases/tag/v10.1.2
- https://ganelson.github.io/inform-website/
- https://davidgriffith.gitlab.io/frotz/
