# 0466 — NetLinx+ERB: `.axi.erb`

Ruolo: Template ERB di include NetLinx con funzione del saluto e assegnazione audience, non programma .axs.

Provenienza: Sorgente originale scritto per il ruolo specifico della variante, usando la documentazione citata.

Toolchain richiesta: ERB originale Ruby3.2.3; compiler/runtime NetLinx non preparati. La versione specifica della nuova variante non è attestata da un eseguibile in questo lotto.

Procedura di verifica proposta, non eseguita, dalla directory della variante:

```text
ruby render.rb; poi NetLinx Studio include di hello.axi nel progetto di test
```

Risultato atteso: Include generato con Hello, World!; runtime controller pendente

Stato individuale: artefatto creato `true`, sintassi verificata `false`, semantica verificata `false`. La presenza di dati/configurazioni del saluto non implica esecuzione.

Impedimenti:

- La variante non è stata sottoposta a una nuova prova del parser/compiler/runtime originale; le verifiche del sorgente principale non vengono ereditate.

SHA-256 dei file della variante:

- `hello.axi.erb`: `8c2441b28ea9f2841dbd7201f8b3b2d25a62270aaa3d78f438f0ab89d80c24f5`
- `render.rb`: `710ac885e567c3889f2fb6584fc759c193dd42d50c243cd2feaae3f6ff7df69e`

Fonti primarie:

- https://docs.ruby-lang.org/en/3.2/ERB.html
- https://www.amx.com/ko/site_elements/amx-language-reference-guide-netlinx-programming-language
