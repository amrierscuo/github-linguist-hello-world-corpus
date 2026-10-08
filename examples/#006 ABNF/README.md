# #006 ABNF

`hello.abnf` definisce la regola `greeting`, che riconosce esattamente i 13
caratteri ASCII `Hello, World!`. Usa ABNF RFC 5234 con l'estensione `%s` di
RFC 7405 per rendere il confronto sensibile alle maiuscole. Il file è ASCII
con terminatori CRLF.

## Toolchain e comandi

**Python 3.10 o successivo** e pacchetto esterno **abnf 2.9.0**. Installazione
isolata, dalla cartella dell'esempio (Windows PowerShell):

```powershell
python -m venv .venv
.venv/Scripts/python.exe -m pip install abnf==2.9.0
.venv/Scripts/python.exe verify.py
```

`verify.py` carica il file nel parser della libreria; non implementa un parser
ABNF proprio. Accetta il saluto esatto e controlla che siano respinti tre
controesempi: una maiuscola cambiata, la virgola assente e uno spazio finale.
La fase di costruzione del parser avviene nel verificatore.

Risultato atteso: codice 0, conferma del caricamento della grammatica,
`ACCEPT: Hello, World!`, tre righe `REJECT` e
`PASS: syntax and exact greeting semantics`.

## Stato

Sintassi **verificata** e semantica **verificata** tramite abnf 2.9.0 con
Python 3.13.9 su Windows x64. Comando effettivo, output, codice di uscita e hash
sono in `verification/abnf.json`. La dipendenza usata nella sessione è isolata
nella cartella di lavoro esterna al corpus.

## Fonti primarie

- [RFC Editor, RFC 5234: ABNF](https://www.rfc-editor.org/rfc/rfc5234).
- [RFC Editor, RFC 7405: stringhe sensibili alle maiuscole](https://www.rfc-editor.org/rfc/rfc7405.html).
- [abnf, progetto e API del parser](https://github.com/declaresub/abnf).

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.abnf` | [hello.abnf](hello.abnf) verificato |
