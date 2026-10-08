# #451 Muse

Voce canonica `Muse`, tipo `prose`, language_id `474864066`.

Pubblicare un documento Emacs Muse originale in HTML con il saluto nel corpo.

## Toolchain e riproduzione

Required genuine toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Richiede Emacs Muse e le librerie muse-html/muse-publish. La procedura documentata pubblica nella directory corrente.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
Aprire hello.muse in Emacs con Muse attivo; M-x muse-project-publish-this-file; selezionare lo stile html.
```

Risultato atteso: Hello, World!

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Motore Emacs Muse assente; titolo e paragrafo sono sorgente Muse originale.

Requisiti residui:

- Emacs Muse publishing engine is not configured.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.gnu.org/software/emacs-muse/manual/muse.html](https://www.gnu.org/software/emacs-muse/manual/muse.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.muse` | [hello.muse](hello.muse) creato, verifiche pendenti |
