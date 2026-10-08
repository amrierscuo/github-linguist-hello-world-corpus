# #041 Assembly

Voce canonica: `Assembly`, tipo `programming`, `language_id: 24`.

Stampare esattamente Hello, World! con syscall Linux x86_64 write, poi terminare con stato 0.

## Toolchain e riproduzione

GNU GAS and ld, Linux x86_64 syscall ABI — GNU assembler (GNU Binutils for Ubuntu) 2.42. Ambiente della prova: **Ubuntu 24.04 WSL2/Linux x86_64**.

Eseguire in Linux x86_64 con GNU Binutils. In Windows usare Ubuntu WSL2; questo sorgente usa GAS in sintassi Intel e ABI Linux, non il formato PE Windows.

Comando/procedura dalla directory dell’esempio:

```text
as --64 -o hello.o hello.s; ld -o hello hello.o; ./hello
```

Risultato atteso: Exit 0; stdout esattamente Hello, World! seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

La prova assembla i byte originali, collega un ELF in una directory isolata ed esegue quell’ELF. Non serve libc.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain e SHA-256 degli artefatti. `path_normalization` descrive le sostituzioni dei
percorsi della macchina; i byte dei sorgenti restano quelli identificati dai checksum.
Se il log registra solo disponibilità degli strumenti, nessun parsing o runtime è attestato.
Gli strumenti, le dipendenze e i prodotti di verifica restano nella directory di lavoro.

## Fonti primarie

- [https://sourceware.org/binutils/docs/as/i386_002dSyntax.html](https://sourceware.org/binutils/docs/as/i386_002dSyntax.html)
- [https://sourceware.org/binutils/docs/as/i386_002dOptions.html](https://sourceware.org/binutils/docs/as/i386_002dOptions.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.asm` | [hello.asm](variants/ext-asm-2e61736d/hello.asm) creato, verifiche pendenti |
| `.a51` | [hello.a51](variants/ext-a51-2e613531/hello.a51) creato, verifiche pendenti |
| `.i` | [hello.i](variants/ext-i-2e69/hello.i) creato, verifiche pendenti |
| `.inc` | [hello.inc](variants/ext-inc-2e696e63/hello.inc) creato, verifiche pendenti |
| `.nas` | [hello.nas](variants/ext-nas-2e6e6173/hello.nas) creato, verifiche pendenti |
| `.nasm` | [hello.nasm](variants/ext-nasm-2e6e61736d/hello.nasm) creato, verifiche pendenti |
| `.s` | [hello.s](hello.s), [consumer.s](variants/ext-inc-2e696e63/consumer.s) creato, verifiche pendenti |
