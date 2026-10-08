# #152 D-ObjDump

Voce canonica e ordine del `reference/languages.yml` del corpus. I sorgenti e fixture sono originali; eventuali dump/bundle provengono dagli strumenti indicati.

## Obiettivo

Produrre un disassemblato autentico di un oggetto D originale associato a un programma Hello, World!.

hello.d-objdump è output testuale originale del vero objdump, non assembly scritto a mano. hello.d è la fixture da cui nasce l’oggetto. Il log conserva SHA-256 dell’oggetto e dei sorgenti, output del tool e esecuzione del programma. La semantica verificata è provenienza e associazione al programma; il dump non si esegue direttamente.

## Toolchain e riproduzione

LDC 1.43.0 BetterC; GNU objdump/Binutils 2.42; Linux ELF x86_64

Comandi nella cartella dell’esempio con la toolchain disponibile nel PATH. Usare una copia temporanea: database, oggetti, audio e altri output di prova non appartengono al corpus.

```text
ldc2 -betterC -c hello.d -of=hello.o
objdump -d -r -s hello.o > hello.d-objdump
```

```text
ldc2 -betterC hello.d -of=hello
./hello
Confrontare il dump rigenerato con hello.d-objdump.
```

## Risultato atteso e stato

Oggetto ELF x86_64 reale, sezioni e simbolo D greeting presenti, literal Hello, World! nei dati; programma associato emette il saluto.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra versioni e provenienza, SHA-256 dei sorgenti, comandi effettivi, exit, stdout e stderr normalizzati.

## Fonti primarie

- https://sourceware.org/binutils/docs/binutils/objdump.html
- https://dlang.org/spec/betterc.html
- https://github.com/ldc-developers/ldc/releases/tag/v1.43.0

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.d-objdump` | [hello.d-objdump](hello.d-objdump) verificato |
