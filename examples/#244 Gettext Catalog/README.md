# #244 Gettext Catalog

## Latest recorded verification

Latest extension checks:
- `.pot`: GNU gettext accepted and compiled the exact POT template; msgattrib returned its untranslated Hello, World! entry. GNUTranslations loaded the compiled catalog and preserved untranslated and unknown keys. This checks template behavior, not a supplied translation. [Evidence](verification/native_20261105_batch_2e706f74.json).

Fill out a Gettext catalog that translates the greeting key in Hello, World!.

## Toolchain

msgfmt (GNU gettext-tools) 0.21; Python 3.13.9 gettext.GNUTranslations

## Commands and procedure

msgfmt --check --check-header -o build/hello.mo hello.po; python verify.py build/hello.mo

## Expected result

Accepted catalog; lookup greeting returns greeting; unknown key keeps your text.

## Status

syntax and behavior verified.

Il .po include header completi e indirizzi illustrativi example.invalid. GNU msgfmt valida e compila un MO reale; GNUTranslations lo carica per il lookup. Il MO binario è mantenuto solo in work.

Actual verification of 2026-10-08T12:17:31.360561+00:00 on WSL msgfmt + Windows Python: [log](verification/result.json).
The log retains SHA-256 of sorgenti/checker, versioni/comandi real, exit codes, stdout/stderr and test limits.

## Primary sources

- [https://www.gnu.org/software/gettext/manual/html_node/PO-Files.html](https://www.gnu.org/software/gettext/manual/html_node/PO-Files.html)
- [https://www.gnu.org/software/gettext/manual/html_node/msgfmt-Invocation.html](https://www.gnu.org/software/gettext/manual/html_node/msgfmt-Invocation.html)
- [https://docs.python.org/3/library/gettext.html](https://docs.python.org/3/library/gettext.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.po` | [hello.po](hello.po) verified |
| `.pot` | [hello.pot](variants/ext-pot-2e706f74/hello.pot) syntax and behavior verified |