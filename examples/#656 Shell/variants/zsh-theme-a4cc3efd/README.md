# 0656 — Shell — `.zsh-theme`

Tema prompt Zsh: modifica PROMPT nel solo processo di prova.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.zsh-theme`.

Controllo previsto, dalla cartella della variante:

```text
zsh -f -c 'source ./hello.zsh-theme; print -r -- "$PROMPT"'
```

Risultato atteso: prompt include Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://zsh.sourceforge.io/Doc/Release/Prompt-Expansion.html](https://zsh.sourceforge.io/Doc/Release/Prompt-Expansion.html)
