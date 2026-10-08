# 0785 — XML — `.vssettings`

Fixture del linguaggio XML per suffisso .vssettings associato a Visual Studio settings. Il payload è XML originale ben formato; NON rappresenta lo schema proprietario né un export importabile da quell’applicazione.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.vssettings`.

Controllo previsto, dalla cartella della variante:

```text
XML parser: parse hello.vssettings and assert fixture/greeting text; native application schema NOT checked
```

Risultato atteso: payload XML leggibile e greeting Hello, World!; compatibilità applicativa non dichiarata.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://www.w3.org/TR/xml/](https://www.w3.org/TR/xml/)
