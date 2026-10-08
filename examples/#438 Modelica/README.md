# #438 Modelica

Simulare un modello Modelica che stampa il saluto nell’algoritmo iniziale.

Tipo canonico `programming`, language_id `233`.

Toolchain prevista: OpenModelica omc e Modelica Standard Library.

Dalla cartella dell’esempio:

```sh
omc run.mos
```

Risultato atteso: modello caricato e simulato; stdout/log contiene Hello, World!.

Streams.print è eseguito durante l’inizializzazione. Il modello non modifica dispositivi esterni.

Stato iniziale: creato; sintassi e semantica in attesa. Toolchain non ancora eseguita: sintassi e semantica restano pendenti.

Fonti:

- [Modelica — linguaggio e specifica](https://specification.modelica.org/maint/3.6/)
- [OpenModelica — scripting](https://openmodelica.org/doc/OpenModelicaUsersGuide/latest/scripting_api.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.mo` | [Hello.mo](Hello.mo) creato, verifiche pendenti |
