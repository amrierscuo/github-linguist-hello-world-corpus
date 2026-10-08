# #174 E-mail

Decodificare un messaggio e-mail RFC 5322/MIME con subject e body Hello, World!.

## Toolchain

Python 3.13.9; stdlib email BytesParser RFC 5322/MIME

## Comandi e procedura

python --version; python verify.py

## Risultato atteso

Parser senza difetti; subject e corpo corretti; serializzazione SMTP e rilettura conservano il corpo.

## Stato

Sintassi e semantica verificate.

Tutti gli indirizzi usano il dominio illustrativo example.invalid. Il file ha newline CRLF e charset UTF-8. Questa è una prova del messaggio locale: nessuna e-mail viene inviata.

Verifica effettiva del 2026-10-08T11:56:14.159762+00:00 su Windows x64: [log](verification/result.json).
Hash delle sorgenti/checker, versioni e comandi reali, codici di uscita, stdout/stderr e limiti della prova sono nel log.

## Fonti primarie e riferimento di formato

- [https://www.rfc-editor.org/rfc/rfc5322](https://www.rfc-editor.org/rfc/rfc5322)
- [https://docs.python.org/3/library/email.parser.html](https://docs.python.org/3/library/email.parser.html)
- [https://docs.python.org/3/library/email.policy.html](https://docs.python.org/3/library/email.policy.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.eml` | [hello.eml](hello.eml) verificato |
| `.mbox` | [hello.mbox](variants/ext-mbox-2e6d626f78/hello.mbox) creato, verifiche pendenti |
