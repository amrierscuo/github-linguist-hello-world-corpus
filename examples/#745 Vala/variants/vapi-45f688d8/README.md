# 0745 — Vala — `.vapi`

Binding Vala per una funzione C originale; distinto da un entrypoint Vala.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.vapi`.

Controllo previsto, dalla cartella della variante:

```text
valac --vapidir=. --pkg hello -X -I. --directory=work -o hello main.vala greeting.c; work/hello
```

Risultato atteso: binding accettato e stdout Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://docs.vala.dev/developer-guides/bindings/writing-vapi-files.html](https://docs.vala.dev/developer-guides/bindings/writing-vapi-files.html)
