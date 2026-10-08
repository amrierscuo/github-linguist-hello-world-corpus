# #134 Common Workflow Language

Descrivere in CWL 1.2 un comando echo con input string di default Hello, World! e catturare stdout in un output File hello.txt.

## Riproduzione

Toolchain: cwltool 3.3.20260925135507; Python 3.12.3. Ambiente della prova: Ubuntu 24.04 WSL2 x86_64.

```text
cwltool --validate hello.cwl
cwltool --no-container --outdir results hello.cwl job.yml
Verificare results/hello.txt esattamente Hello, World! seguito da newline.
```

Risultato atteso: Validazione riuscita; job exit 0; output File hello.txt con contenuto esattamente Hello, World! seguito da newline.

## Verifica

Sintassi e semantica verificate il 2026-10-08T23:34:15.412306+00:00. Le varianti hanno prove separate nel log quando consumate.

[Prova nativa](verification/finish_native.json) contiene versioni, comandi reali, exit code, output e SHA-256. I percorsi locali sono sostituiti da segnaposto. Compilati e dipendenze restano fuori dal corpus.

## Fonti primarie

- [https://www.commonwl.org/v1.2/CommandLineTool.html](https://www.commonwl.org/v1.2/CommandLineTool.html)
- [https://github.com/common-workflow-language/cwltool](https://github.com/common-workflow-language/cwltool)
- [https://www.commonwl.org/user_guide/topics/outputs.html](https://www.commonwl.org/user_guide/topics/outputs.html)

## Copertura delle estensioni

Le verifiche dei suffissi sono registrate separatamente.

| Estensione | File e stato |
| --- | --- |
| `.cwl` | [hello.cwl](hello.cwl) sintassi e semantica verificate |
