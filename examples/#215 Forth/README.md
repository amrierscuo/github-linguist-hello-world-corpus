# #215 Forth

Voce canonica `Forth`, tipo `programming`, language_id `114`.

Definire la parola Forth greet, scrivere il saluto con ." e terminare l’interprete.

## Toolchain e riproduzione

Gforth native interpreter and original gforth.fi image — gforth 0.7.3. Ambiente della prova: **Ubuntu 24.04 WSL2/Linux x86_64**.

Gforth 0.7.3, con il motore e l’immagine gforth.fi originali della distribuzione Ubuntu. La prova li usa da un’estrazione locale, configurando il percorso delle librerie.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
gforth hello.fth
```

Risultato atteso: Exit 0; saluto esatto seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

La parola viene realmente compilata nell’interprete Forth e poi eseguita; cr aggiunge newline e bye termina con successo.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sorgenti verificati in staging. I soli probe di disponibilità non attestano parsing
o esecuzione. Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.complang.tuwien.ac.at/forth/gforth/Docs-html/](https://www.complang.tuwien.ac.at/forth/gforth/Docs-html/)
- [https://forth-standard.org/standard/core/Dotp](https://forth-standard.org/standard/core/Dotp)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.fth` | [hello.fth](hello.fth) verificato |
| `.4th` | [hello.4th](variants/ext-4th-2e347468/hello.4th) creato, verifiche pendenti |
| `.f` | [hello.f](variants/ext-f-2e66/hello.f) creato, verifiche pendenti |
| `.for` | [hello.for](variants/ext-for-2e666f72/hello.for) creato, verifiche pendenti |
| `.forth` | [hello.forth](variants/ext-forth-2e666f727468/hello.forth) creato, verifiche pendenti |
| `.fr` | [hello.fr](variants/ext-fr-2e6672/hello.fr) creato, verifiche pendenti |
| `.frt` | [hello.frt](variants/ext-frt-2e667274/hello.frt) creato, verifiche pendenti |
| `.fs` | [hello.fs](variants/ext-fs-2e6673/hello.fs) creato, verifiche pendenti |
