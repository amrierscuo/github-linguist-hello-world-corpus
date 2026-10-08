# #745 Vala

Compilare Vala in C e stampare il saluto.

Tipo canonico `programming`, language_id `386`.

Toolchain prevista: Vala 0.56.16; GLib2.80.0; GCC13.3.0; WSL Ubuntu24.04.

Dalla cartella dell’esempio:

```sh
mkdir -p build
valac --directory=build -o hello hello.vala
./build/hello
```

Risultato atteso: stdout Hello, World! e newline.

Il controllo deve includere valac; compilare un C scritto a mano non verifica Vala.

Stato registrato: sintassi verificata; semantica verificata. Toolchain: Vala 0.56.16; GLib2.80.0; GCC13.3.0; WSL Ubuntu24.04. [Log](verification/result.json). 

Fonti:

- [Vala tutorial](https://docs.vala.dev/tutorials/programming-language/main.html)

La verifica reale usa pacchetti Ubuntu originali estratti sotto `work/tools_741_760/ubuntu` e directory di build separate sotto `work/tools_741_760`; gli artefatti compilati non fanno parte del corpus. I comandi e gli environment effettivi sono nel log.

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.vala` | [hello.vala](hello.vala), [main.vala](variants/vapi-45f688d8/main.vala) creato, verifiche pendenti |
| `.vapi` | [hello.vapi](variants/vapi-45f688d8/hello.vapi) creato, verifiche pendenti |
