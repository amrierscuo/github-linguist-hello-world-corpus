# #432 MiniScript

Voce canonica `MiniScript`, tipo `programming`, language_id `704299647`.

Stampare Hello, World! in MiniScript.

## Toolchain e riproduzione

Original JoeStrout MiniScript C# sources at b4510312059df4288af3ce849b235535a4e1bfa7 + Microsoft Roslyn Toolset 4.8.0 / .NET Framework.

Occorrono i sorgenti MiniScript C# ufficiali al commit indicato, Roslyn 4.8.0 e .NET Framework. Compilare il driver invariato in una directory temporanea e avviarlo con hello.ms come file locale nella directory corrente.

```text
Compilare Verify.cs con i sorgenti ufficiali MiniScript-cs; eseguire verify.exe dalla directory contenente hello.ms.
```

Risultato atteso: Exit 0, stdout esattamente Hello, World! seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

La funzione greet riceve il destinatario e stampa il saluto; viene realmente compilata ed eseguita dal parser/runtime MiniScript originale. end function distingue questo sorgente dagli altri linguaggi che usano .ms. Il driver C# resta invariato.

Prova corrente: [recognition.json](verification/recognition.json), con UTC, comandi nativi, exit code, stdout/stderr, toolchain e SHA-256 dei sorgenti modificati e dei driver. Le prove precedenti restano come storico. L’identificazione prevista da Linguist è distinta dall’esito effettivo delle statistiche GitHub; questo lotto non applica override di linguaggio.

## Fonti primarie

- https://miniscript.org/wiki/Print
- https://github.com/JoeStrout/miniscript
- https://miniscript.org/wiki/Function
- https://github.com/github-linguist/linguist/blob/v9.7.0/lib/linguist/heuristics.yml

## Copertura delle estensioni

Le verifiche dei suffissi sono registrate separatamente.

| Estensione | File e stato |
| --- | --- |
| `.ms` | [hello.ms](hello.ms) sintassi e semantica verificate |
