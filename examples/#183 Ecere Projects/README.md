# #183 Ecere Projects

Descrivere un progetto Ecere console con un sorgente eC che stampa Hello, World!.

Tipo canonico `data`, language_id `98`.

Toolchain prevista: Ecere SDK con Ecere IDE, ecereCOM ed epj2make.

Dalla cartella dell’esempio:

```sh
epj2make greeting.epj
make
./greeting
```

Risultato atteso: progetto accettato e programma console che stampa `Hello, World!` seguito da newline.

Il .epj conserva la struttura documentata della versione 0.2; il sorgente di supporto è eC. La sola lettura del JSON non prova il formato progetto o il linking Ecere.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain nativa non ancora eseguita: le verifiche di sintassi e semantica restano pendenti.

Fonti del linguaggio/formato e implementazioni originali:

- [Ecere — progetto console originale](https://github.com/ecere/ecere-sdk/blob/master/samples/eC/HelloWorld/HelloWorld.epj)
- [Ecere SDK](https://github.com/ecere/ecere-sdk)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.epj` | [greeting.epj](greeting.epj) creato, verifiche pendenti |
