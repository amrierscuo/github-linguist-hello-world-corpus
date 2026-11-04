# 0656: Shell: `.zsh-theme`

Zsh Prompt Theme: PROMPT modification in the trial process alone.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.zsh-theme`.

Control provided, from the folder of the variant:

```text
zsh -f -c 'source ./hello.zsh-theme; print -r -- "$PROMPT"'
```

Expected result: prompt includes Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://zsh.sourceforge.io/Doc/Release/Prompt-Expansion.html](https://zsh.sourceforge.io/Doc/Release/Prompt-Expansion.html)
