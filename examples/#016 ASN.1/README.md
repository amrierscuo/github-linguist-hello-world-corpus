# #016 ASN.1

`hello.asn` dichiara il tipo `Greeting` (`UTF8String`) e il valore `hello`,
uguale a `Hello World`. ASN.1 descrive dati: l'equivalente di Hello World è
compilare la specifica, codificare il valore dichiarato e recuperarlo identico.

Toolchain verificata: Python **3.13.9**, asn1tools **0.167.0**, bitstruct **8.23.0**,
pyparsing **3.3.3**, Windows x64. Dalla cartella dell'esempio:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python verify.py
```

Lo script usa il parser ASN.1 di asn1tools per leggere anche il valore `hello`,
compila il tipo e controlla il ciclo codifica/decodifica DER. Risultato atteso:

```text
DER: 0c0b48656c6c6f20576f726c64
Decoded: Hello World
PASS: parse, compile, encode and decode
```

Sintassi e semantica verificate: **sì**, vedere `verification.log`.
La verifica riguarda il sottoinsieme ASN.1 usato dal modulo e il codec DER.

Riferimenti primari: [documentazione asn1tools](https://asn1tools.readthedocs.io/en/latest/)
e [codice/documentazione del progetto](https://github.com/eerimoq/asn1tools).

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.asn` | [hello.asn](hello.asn) verificato |
| `.asn1` | [hello.asn1](variants/ext-asn1-2e61736e31/hello.asn1) creato, verifiche pendenti |
