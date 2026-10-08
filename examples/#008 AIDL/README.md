# #008 AIDL

`corpus/hello/IHello.aidl` dichiara un contratto Android Binder: una costante
`GREETING` con valore `Hello, World!` e un metodo che restituisce una stringa.
Un contratto AIDL non implementa il servizio e non stampa un messaggio da solo.
L'obiettivo semantico di questo esempio è generare l'interfaccia Binder con
quella costante e quella firma.

## Toolchain e comando

Serve il compilatore ufficiale `aidl` degli Android SDK Build Tools. Dalla
cartella dell'esempio, con `aidl` nel PATH:

```powershell
New-Item -ItemType Directory -Force -Path .build | Out-Null
aidl --lang=java -I. -o .build corpus/hello/IHello.aidl
```

Risultato atteso: `.build/corpus/hello/IHello.java`, senza errori; la classe
generata deve contenere `GREETING` e `getGreeting()` insieme a `Stub`/`Proxy`.
Per il comportamento IPC serve inoltre implementare `IHello.Stub`, restituire
`GREETING`, esporlo da un servizio e chiamarlo da un client Android.

## Stato

Creato; sintassi e semantica **non verificate**. Il comando `aidl` non è presente
nel PATH dell'ambiente di lavoro. Il controllo di esistenza dei file non viene
contato come validazione del linguaggio. Vedere `verification.log`.

## Fonti primarie

- [Android Developers: definizione e implementazione AIDL](https://developer.android.com/develop/background-work/services/aidl)
- [Android SDK Build Tools](https://developer.android.com/tools/releases/build-tools)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.aidl` | [IHello.aidl](corpus/hello/IHello.aidl) creato, verifiche pendenti |
