# #095 COLLADA

Rappresentare in COLLADA 1.4.1 un asset dal titolo Hello, World!, con scena GreetingScene e nodo HelloWorld senza spostamento; validare XSD e caricare la scena.

## Toolchain

Python 3.13.9; pycollada 0.9.3; lxml 6.0.2; Khronos COLLADA 1.4.1 XSD

## Comandi e procedura

Scaricare lo schema 1.4.1 dalla fonte Khronos indicata sotto e mantenerlo in
una cartella di tool esterna. Dalla cartella dell'esempio:

```sh
python -m pip install -r requirements.txt
python verify.py /percorso/collada_schema_1_4_1.xsd
```

Prima lxml valida il documento contro lo schema ufficiale completo; poi
pycollada lo carica e risolve il collegamento della scena e la matrice del
nodo. Una sola verifica XML di buona formazione non sarebbe sufficiente.

## Risultato atteso

XSD valida il documento; parser COLLADA restituisce il titolo esatto, scena attiva GreetingScene, nodo GreetingNode/name HelloWorld e matrice identità.

## Stato

Sintassi e semantica verificate.

Il titolo contiene il saluto; i nomi XML di scena e nodo sono identificatori NCName validi. Si verifica il modello dati e la trasformazione, non una resa grafica 3D. L'hash dello schema ufficiale scaricato è nel log; lo schema non è duplicato nel corpus.

Verifica effettiva del 2026-10-08T11:35:41.649498+00:00 su Windows x64: [log](verification/result.json).
Il log include hash SHA-256 della sorgente e dei checker, versioni, comandi, codici di uscita, stdout, stderr e limiti della prova.

## Fonti primarie

- [https://www.khronos.org/collada/](https://www.khronos.org/collada/)
- [https://www.khronos.org/files/collada_schema_1_4_1.xsd](https://www.khronos.org/files/collada_schema_1_4_1.xsd)
- [https://pycollada.readthedocs.io/](https://pycollada.readthedocs.io/)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.dae` | [hello.dae](hello.dae) verificato |
