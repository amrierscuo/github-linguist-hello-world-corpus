# #016 ASN.1

`hello.asn` declares the `Greeting` type ( `UTF8String`) and the `hello` value,
equal to `Hello World`. ASN.1 describes data: the equivalent of Hello World is
fill out the specification, codify the declared value and recover it identical.

Toolchain verified: Python **3.13.9**, asn1tools **0.167.0**, bitstruct **8.23.0**,
pyparsing **3.3.3**, Windows x64. From the example folder:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python verify.py
```

The script uses the parser ASN.1 of asn1tools to read also the `hello` value,
fill out the type and check the codifica/decodifica DER cycle. Expected result:

```text
DER: 0c0b48656c6c6f20576f726c64
Decoded: Hello World
PASS: parse, compile, encode and decode
```

syntax and behavior verified: **sì**, vedere `verification.log`.
The verification concerns the subset ASN.1 used by the module and the codec DER.

Riferimenti primari: [documentazione asn1tools](https://asn1tools.readthedocs.io/en/latest/)
e [codice/documentazione del progetto](https://github.com/eerimoq/asn1tools).

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.asn` | [hello.asn](hello.asn) verified |
| `.asn1` | [hello.asn1](variants/ext-asn1-2e61736e31/hello.asn1) created; verification pending |
