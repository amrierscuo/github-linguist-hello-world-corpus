# 0656 — Shell — `.pacscript`

Ricetta Pacstall originale senza download, dipendenze o checksum inventati; package scrive il proprio script in pkgdir isolato, non installa nel sistema.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.pacscript`.

Controllo previsto, dalla cartella della variante:

```text
bash -n hello.pacscript; Pacstall packaging-only sandbox with pkgdir under /absolute/work (no installation)
```

Risultato atteso: pacchetto di prova contiene script originale che stampa Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://github.com/pacstall/pacstall/wiki/Pacscript-101](https://github.com/pacstall/pacstall/wiki/Pacscript-101)
