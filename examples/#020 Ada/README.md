# #020 Ada

`hello.adb` contiene la procedura `Hello`, che chiama `Ada.Text_IO.Put_Line`
per scrivere `Hello World` seguito da un a capo.

Toolchain richiesta: GNAT, incluso `gnatmake`, binder, linker e runtime Ada.
Dalla cartella dell'esempio, con GNAT nel PATH:

```powershell
gnatmake hello.adb
.\hello.exe
```

Su Unix il secondo comando è `./hello`. Risultato atteso: una riga
`Hello World` e terminazione senza errori.

Sintassi e semantica verificate: **no**. Blocco attuale: `gnatmake` e la
toolchain Ada non sono disponibili nell'ambiente Windows usato. Il file
è stato confrontato con il modello documentato, senza dichiarare una
compilazione o un'esecuzione mai effettuata.

Riferimenti primari: [primo programma GNAT, GCC](https://gcc.gnu.org/onlinedocs/gnat_ugn/Running-a-Simple-Ada-Program.html)
e [introduzione ad Ada, AdaCore](https://learn.adacore.com/courses/intro-to-ada/chapters/imperative_language.html).

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.adb` | [hello.adb](hello.adb), [consumer.adb](variants/ext-ads-2e616473/consumer.adb) creato, verifiche pendenti |
| `.ada` | [hello.ada](variants/ext-ada-2e616461/hello.ada) creato, verifiche pendenti |
| `.ads` | [greeting.ads](variants/ext-ads-2e616473/greeting.ads) creato, verifiche pendenti |
