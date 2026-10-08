# 0676 — SourcePawn — `.inc`

Include SourcePawn con include guard e funzione stock.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.inc`.

Controllo previsto, dalla cartella della variante:

```text
spcomp main.sp -i . -o work/hello.smx; isolated SourceMod load
```

Risultato atteso: server console Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://wiki.alliedmods.net/Introduction_to_SourcePawn_1.7](https://wiki.alliedmods.net/Introduction_to_SourcePawn_1.7)
- [https://www.sourcemod.net/](https://www.sourcemod.net/)
