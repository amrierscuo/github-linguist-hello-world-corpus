# #354 Kaitai Struct

Voce canonica `Kaitai Struct`, tipo `programming`, language_id `818804755`.

Compilare una specifica Kaitai Struct e leggere una fixture binaria originale con magic, lunghezza e stringa UTF-8.

## Toolchain e riproduzione

Official Kaitai Struct Scala compiler JavaScript build and Python runtime — compiler 0.11.0; kaitaistruct 0.11. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Compiler Kaitai Struct ufficiale 0.11.0, build JavaScript del compiler Scala originale, e runtime Python kaitaistruct 0.11. greeting.bin contiene i byte originali HW, 0x0d e tredici caratteri del saluto.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
npm install --prefix .tools kaitai-struct-compiler@0.11.0 js-yaml@4.1.0; python -m pip install kaitaistruct==0.11; node compile.cjs .tools build; python verify.py build greeting.bin
```

Risultato atteso: Magic HW, length=13, message=Hello, World!, stream consumato; controllo negativo e PASS.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

La specifica è compilata dal vero compiler. Il helper importa solo il Python realmente generato in build, legge la fixture, verifica posizione finale e rifiuto di magic errato. Il parser generato e le dipendenze non sono inclusi nel corpus.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://doc.kaitai.io/user_guide.html](https://doc.kaitai.io/user_guide.html)
- [https://github.com/kaitai-io/kaitai_struct_compiler](https://github.com/kaitai-io/kaitai_struct_compiler)
- [https://doc.kaitai.io/lang_python.html](https://doc.kaitai.io/lang_python.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ksy` | [greeting.ksy](greeting.ksy) verificato |
