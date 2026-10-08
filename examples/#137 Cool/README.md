# #137 Cool

Voce canonica: `Cool`, tipo `programming`, `language_id: 68`.

Definire la classe Main del linguaggio Cool, ereditare IO e stampare il saluto attraverso out_string e String.concat.

## Toolchain e riproduzione

Required native toolchain unavailable or not configured — versione non disponibile / non verificata. Ambiente della prova: **Windows x64**.

Richiede il compilatore di riferimento Cool di Stanford e il suo runtime SPIM/trap handler compatibile. Il comando esatto del runtime dipende dal wrapper fornito dalla distribuzione e va registrato nella verifica futura.

Comando/procedura dalla directory dell’esempio, salvo la directory build esplicitamente indicata:

```text
coolc -o hello hello.cl; eseguire hello con il wrapper/SPIM della stessa distribuzione Cool
```

Risultato atteso: Cool typecheck/codegen riusciti; runtime MIPS/SPIM emette Hello, World! seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Cool qui è Classroom Object-Oriented Language. Main.main restituisce Object; out_string restituisce SELF_TYPE compatibile. Le stringhe sono concatenate dal metodo String.concat. Non sono stati usati lexer/compiler inventati o equivalenti in un altro linguaggio.

Requisiti residui:

- Stanford Cool coolc and compatible SPIM runtime are unavailable.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
versioni/toolchain e SHA-256 degli artefatti. La proprietà `path_normalization` documenta
le sostituzioni dei percorsi locali. `<corpus>` identifica i file relativi inclusi nel
corpus finale, che sono stati verificati prima nella directory di staging. I byte dei
sorgenti restano quelli identificati dai checksum. I soli probe di disponibilità degli
strumenti non attestano parsing o esecuzione. Dipendenze e prodotti compilati restano
nella directory di lavoro e non sono inclusi nel corpus.

## Fonti primarie

- [https://web.stanford.edu/class/cs143/materials/cool-manual.pdf](https://web.stanford.edu/class/cs143/materials/cool-manual.pdf)
- [https://web.stanford.edu/class/cs143/](https://web.stanford.edu/class/cs143/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cl` | [hello.cl](hello.cl) creato, verifiche pendenti |
