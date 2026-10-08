# #138 Cpp-ObjDump

Voce canonica: `Cpp-ObjDump`, tipo `data`, `language_id: 70`.

Produrre un autentico dump GNU objdump di un eseguibile C++ Hello World, conservando disassemblaggio main e byte delle sezioni.

## Toolchain e riproduzione

GNU G++ and GNU objdump genuine C++ ELF disassembly — GNU objdump (GNU Binutils for Ubuntu) 2.42. Ambiente della prova: **Ubuntu 24.04 WSL2/Linux x86_64**.

GNU G++ 13.3.0 e Binutils objdump/strings 2.42 su Ubuntu 24.04 x86_64. hello.cpp è il sorgente di provenienza; hello.cppobjdump è il vero output del tool ed è la voce dati canonica. Eseguire dalla directory build con un nome binario relativo corto per evitare percorsi personali nel dump.

Comando/procedura dalla directory dell’esempio, salvo la directory build esplicitamente indicata:

```text
In una directory build isolata: g++ -std=c++17 -O0 <example>/hello.cpp -o hello; objdump -drwC -s hello > hello.cppobjdump; strings -a hello; ./hello
```

Risultato atteso: Dump ELF x86_64 con <main>: e sezione .rodata; strings individua Hello, World!; l’eseguibile termina 0 con il saluto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Cpp-ObjDump è un formato di dati generati. Sintassi positiva indica generazione nativa del formato; semantica positiva associa il dump alla vera compilazione, al simbolo main, alla stringa incorporata e alla esecuzione del binario. Il binario non è incluso nel corpus. Gli indirizzi e l’ordine delle sezioni possono differire con compilatori diversi.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
versioni/toolchain e SHA-256 degli artefatti. La proprietà `path_normalization` documenta
le sostituzioni dei percorsi locali. `<corpus>` identifica i file relativi inclusi nel
corpus finale, che sono stati verificati prima nella directory di staging. I byte dei
sorgenti restano quelli identificati dai checksum. I soli probe di disponibilità degli
strumenti non attestano parsing o esecuzione. Dipendenze e prodotti compilati restano
nella directory di lavoro e non sono inclusi nel corpus.

## Fonti primarie

- [https://sourceware.org/binutils/docs/binutils/objdump.html](https://sourceware.org/binutils/docs/binutils/objdump.html)
- [https://sourceware.org/binutils/docs/binutils/strings.html](https://sourceware.org/binutils/docs/binutils/strings.html)
- [https://gcc.gnu.org/onlinedocs/gcc/Invoking-G_002b_002b.html](https://gcc.gnu.org/onlinedocs/gcc/Invoking-G_002b_002b.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.cppobjdump` | [hello.cppobjdump](hello.cppobjdump) verificato |
| `.c++-objdump` | [hello.c++-objdump](variants/ext-c-objdump-2e632b2b2d6f626a64756d70/hello.c%2B%2B-objdump) creato, verifiche pendenti |
| `.c++objdump` | [hello.c++objdump](variants/ext-c-objdump-2e632b2b6f626a64756d70/hello.c%2B%2Bobjdump) creato, verifiche pendenti |
| `.cpp-objdump` | [hello.cpp-objdump](variants/ext-cpp-objdump-2e6370702d6f626a64756d70/hello.cpp-objdump) creato, verifiche pendenti |
| `.cxx-objdump` | [hello.cxx-objdump](variants/ext-cxx-objdump-2e6378782d6f626a64756d70/hello.cxx-objdump) creato, verifiche pendenti |
