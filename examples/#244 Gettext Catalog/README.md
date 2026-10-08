# #244 Gettext Catalog

Compilare un catalogo Gettext che traduce la chiave greeting in Hello, World!.

## Toolchain

msgfmt (GNU gettext-tools) 0.21; Python 3.13.9 gettext.GNUTranslations

## Comandi e procedura

msgfmt --check --check-header -o build/hello.mo hello.po; python verify.py build/hello.mo

## Risultato atteso

Catalogo accettato; lookup greeting restituisce il saluto; chiave sconosciuta conserva il proprio testo.

## Stato

Sintassi e semantica verificate.

Il .po include header completi e indirizzi illustrativi example.invalid. GNU msgfmt valida e compila un MO reale; GNUTranslations lo carica per il lookup. Il MO binario è mantenuto solo in work.

Verifica effettiva del 2026-10-08T12:17:31.360561+00:00 su WSL msgfmt + Windows Python: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

## Fonti primarie

- [https://www.gnu.org/software/gettext/manual/html_node/PO-Files.html](https://www.gnu.org/software/gettext/manual/html_node/PO-Files.html)
- [https://www.gnu.org/software/gettext/manual/html_node/msgfmt-Invocation.html](https://www.gnu.org/software/gettext/manual/html_node/msgfmt-Invocation.html)
- [https://docs.python.org/3/library/gettext.html](https://docs.python.org/3/library/gettext.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.po` | [hello.po](hello.po) verificato |
| `.pot` | [hello.pot](variants/ext-pot-2e706f74/hello.pot) creato, verifiche pendenti |
