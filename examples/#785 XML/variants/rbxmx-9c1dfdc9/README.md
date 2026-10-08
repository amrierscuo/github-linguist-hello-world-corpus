# 0785 — XML — `.rbxmx`

Fixture del linguaggio XML per suffisso .rbxmx associato a application-specific XML descriptor. Il payload è XML originale ben formato; NON rappresenta lo schema proprietario né un export importabile da quell’applicazione.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.rbxmx`.

Controllo previsto, dalla cartella della variante:

```text
XML parser: parse hello.rbxmx and assert fixture/greeting text; native application schema NOT checked
```

Risultato atteso: payload XML leggibile e greeting Hello, World!; compatibilità applicativa non dichiarata.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://www.w3.org/TR/xml/](https://www.w3.org/TR/xml/)
