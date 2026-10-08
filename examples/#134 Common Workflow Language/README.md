# #134 Common Workflow Language

Voce canonica: `Common Workflow Language`, tipo `programming`, `language_id: 988547172`.

Descrivere in CWL 1.2 un comando echo con input string di default Hello, World! e catturare stdout in un output File hello.txt.

## Toolchain e riproduzione

Common Workflow Language reference cwltool — 3.3.20260925135507. Ambiente della prova: **Ubuntu 24.04 WSL2/Linux x86_64**.

In Linux/WSL2: python -m pip install cwltool==3.3.20260925135507 in un venv o target locale. Usare il vero riferimento cwltool e il comando echo disponibile su PATH; nessun container è necessario. job.yml vuoto seleziona il default dell’input.

Comando/procedura dalla directory dell’esempio, salvo la directory build esplicitamente indicata:

```text
cwltool --validate hello.cwl; cwltool --no-container --outdir results hello.cwl job.yml
```

Risultato atteso: Validazione riuscita; job exit 0; output File hello.txt con contenuto esattamente Hello, World! seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

cwltool nativo Windows non parte perché importa il modulo POSIX pwd. Il tentativo di installazione Linux isolata ha superato il limite; i probe del riferimento Linux non trovano il modulo cwltool. Nessun parsing CWL è attestato. Un parsing YAML generico non sostituisce il validator del linguaggio.

Requisiti residui:

- Native Windows cwltool imports POSIX pwd and cannot start; isolated Linux installation timed out and Linux cwltool module is unavailable.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
versioni/toolchain e SHA-256 degli artefatti. La proprietà `path_normalization` documenta
le sostituzioni dei percorsi locali. `<corpus>` identifica i file relativi inclusi nel
corpus finale, che sono stati verificati prima nella directory di staging. I byte dei
sorgenti restano quelli identificati dai checksum. I soli probe di disponibilità degli
strumenti non attestano parsing o esecuzione. Dipendenze e prodotti compilati restano
nella directory di lavoro e non sono inclusi nel corpus.

## Fonti primarie

- [https://www.commonwl.org/v1.2/CommandLineTool.html](https://www.commonwl.org/v1.2/CommandLineTool.html)
- [https://github.com/common-workflow-language/cwltool](https://github.com/common-workflow-language/cwltool)
- [https://www.commonwl.org/user_guide/topics/outputs.html](https://www.commonwl.org/user_guide/topics/outputs.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cwl` | [hello.cwl](hello.cwl) creato, verifiche pendenti |
