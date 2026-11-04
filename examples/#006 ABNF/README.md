# #006 ABNF

`hello.abnf` defines the `greeting` rule, which recognizes exactly the 13
ASCII `Hello, World!` characters. Use ABNF RFC 5234 with `%s` extension
RFC 7405 to make matching case-sensitive. The file is ASCII
con terminatori CRLF.

## Toolchain and commands

**Python 3.10 o successivo** e pacchetto esterno **abnf 2.9.0**. Installazione
isolated, from the example folder (Windows PowerShell):

```powershell
python -m venv .venv
.venv/Scripts/python.exe -m pip install abnf==2.9.0
.venv/Scripts/python.exe verify.py
```

`verify.py` uploads the file to the library parser; does not implement a parser
of its own for ABNF. It accepts the exact greeting and checks that three
counterexamples: a capital changed, the absent comma and a final space.
The construction phase of the parser takes place in the verification.

Expected result: 0 code, confirmation of grammar loading,
`ACCEPT: Hello, World!`, tre righe `REJECT` e
`PASS: syntax and exact greeting semantics`.

## Status

syntax **verified** e behavior **verified** tramite abnf 2.9.0 con
Python 3.13.9 su Windows x64. Comando effettivo, output, codice di uscita e hash
are in `verification/abnf.json`. The dependence used in the session is isolated
in the external workbook to the corpus.

## Primary sources

- [RFC Editor, RFC 5234: ABNF](https://www.rfc-editor.org/rfc/rfc5234).
- [RFC Editor, RFC 7405: stringhe sensibili alle maiuscole](https://www.rfc-editor.org/rfc/rfc7405.html).
- [abnf, progetto e API del parser](https://github.com/declaresub/abnf).

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.abnf` | [hello.abnf](hello.abnf) verified |
