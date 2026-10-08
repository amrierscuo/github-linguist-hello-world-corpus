# #516 P4

Creare un header P4 di 104 bit con il payload ASCII del saluto e inviarlo alla porta di prova 1.

Tipo canonico `programming`, language_id `348895984`.

Toolchain prevista: p4c bmv2 backend e BMv2 simple_switch in rete di prova.

Dalla cartella dell’esempio:

```sh
p4c --target bmv2 --arch v1model hello.p4
```

Risultato atteso: compilazione riuscita; pacchetto emesso contiene Hello, World!.

Non configura switch o interfacce reali; semantica richiede un harness BMv2 isolato.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain non ancora eseguita: sintassi e semantica restano pendenti.

Fonti:

- [P4 specification](https://p4.org/p4-spec/docs/P4-16-v1.2.5.html)
- [p4c v1model](https://github.com/p4lang/p4c/blob/main/p4include/v1model.p4)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.p4` | [hello.p4](hello.p4) creato, verifiche pendenti |
