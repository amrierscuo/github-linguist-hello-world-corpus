# 0746 — Valve Data Format — `.vmf`

Valve Map Format con worldspawn originale e metadato message; non file KeyValues generico rinominato.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.vmf`.

Controllo previsto, dalla cartella della variante:

```text
Hammer: open hello.vmf in an isolated project; inspect worldspawn message
```

Risultato atteso: message == Hello, World!; nessuna geometria/gioco avviato.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://developer.valvesoftware.com/wiki/Valve_Map_Format](https://developer.valvesoftware.com/wiki/Valve_Map_Format)
