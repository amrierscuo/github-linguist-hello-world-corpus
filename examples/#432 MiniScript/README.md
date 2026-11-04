# #432 MiniScript

Voce canonica `MiniScript`, tipo `programming`, language_id `704299647`.

Stampare Hello, World! in MiniScript.

## Toolchain and reproduction

Original JoeStrout MiniScript C# sources at b4510312059df4288af3ce849b235535a4e1bfa7 + Microsoft Roslyn Toolset 4.8.0 / .NET Framework.

The official MiniScript C# sources are required to the specified commit, Roslyn 4.8.0 and .NET Framework. Fill the unchanged driver in a temporary directory and start it with hello.ms as a local file in the current directory.

```text
Compilare Verify.cs con i sorgenti ufficiali MiniScript-cs; eseguire verify.exe dalla directory contenente hello.ms.
```

Exit 0, stdout exactly Hello, World! followed by newline.

## Status and evidence

Artifact **created**; syntax **verified**; behavior **verified**.

La funzione greet riceve il destinatario e stampa il saluto; viene realmente compilata ed eseguita dal parser/runtime MiniScript originale. end function distingue questo sorgente dagli altri linguaggi che usano .ms. Il driver C# resta invariato.

Current evidence: [recognition.json](verification/recognition.json), with a UTC timestamp, native commands, exit codes, stdout/stderr, toolchain details and SHA-256 values for modified sources and drivers. Earlier evidence is retained as history. Expected Linguist classification is distinct from the statistics actually observed on GitHub. This batch applies no language override.

## Primary sources

- https://miniscript.org/wiki/Print
- https://github.com/JoeStrout/miniscript
- https://miniscript.org/wiki/Function
- https://github.com/github-linguist/linguist/blob/v9.7.0/lib/linguist/heuristics.yml

## Extension coverage

Suffix checks are recorded separately.

| Extension | File and status |
| --- | --- |
| `.ms` | [hello.ms](hello.ms) syntax and behavior verified |
