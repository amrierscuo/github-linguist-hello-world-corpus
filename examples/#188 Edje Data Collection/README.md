# #188 Edje Data Collection

Compilare un gruppo Edje con una parte testuale che mostra Hello, World!.

Tipo canonico `data`, language_id `342840478`.

Toolchain prevista: EFL/Edje con edje_cc e viewer edje_player o applicazione Edje.

Dalla cartella dell’esempio:

```sh
edje_cc hello.edc hello.edj
edje_player hello.edj -g greeting
```

Risultato atteso: collezione greeting compilata; nella parte label compare Hello, World!.

La compilazione della collezione e l’osservazione del testo nel viewer sono controlli distinti; serve un ambiente grafico EFL con font Sans disponibile.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain nativa non ancora eseguita: le verifiche di sintassi e semantica restano pendenti.

Fonti del linguaggio/formato e implementazioni originali:

- [Edje — riferimento EDC originale](https://github.com/Enlightenment/efl/blob/master/doc/edcref.dox)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.edc` | [hello.edc](hello.edc) creato, verifiche pendenti |
