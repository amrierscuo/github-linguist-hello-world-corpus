# #162 DataWeave

Comporre Hello, World! in DataWeave 2 ed esportare un oggetto JSON con greeting.

## Toolchain

Python 3.13.9; DataWeave native 2.12.2 genuine MuleSoft engine binding

## Comandi e procedura

python -m pip install -r requirements.txt; python verify.py

## Risultato atteso

Motore senza errori; risultato JSON esattamente {"greeting":"Hello, World!"}.

## Stato

Sintassi e semantica verificate.

verify.py usa il binding Python ufficiale del motore nativo MuleSoft. Il saluto deriva dalla concatenazione DataWeave di target, non da Python. Non serve un server Mule per questa prova.

Verifica effettiva del 2026-10-08T11:56:15.339726+00:00 su Windows x64: [log](verification/result.json).
Hash delle sorgenti/checker, versioni e comandi reali, codici di uscita, stdout/stderr e limiti della prova sono nel log.

## Fonti primarie e riferimento di formato

- [https://docs.mulesoft.com/dataweave/latest/dataweave-language-introduction](https://docs.mulesoft.com/dataweave/latest/dataweave-language-introduction)
- [https://github.com/mulesoft/data-weave-cli](https://github.com/mulesoft/data-weave-cli)
- [https://pypi.org/project/dataweave-native/2.12.2/](https://pypi.org/project/dataweave-native/2.12.2/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.dwl` | [hello.dwl](hello.dwl) verificato |
