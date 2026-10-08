# #587 REALbasic

Importare un modulo REALbasic esportato che restituisce il saluto da Message.

Tipo canonico `programming`, language_id `310`.

Toolchain prevista: REALbasic/Xojo con import text project.

Dalla cartella dell’esempio:

```sh
Importare Greeting.rbbas e chiamare Greeting.Message in un progetto console di prova.
```

Risultato atteso: compilazione del modulo; Message restituisce Hello, World!.

Il file è un modulo esportato; l’applicazione host e il compiler sono requisiti ancora aperti.

Stato iniziale: creato; sintassi e semantica in attesa. Compiler REALbasic/Xojo e progetto host non disponibili.

Fonti:

- [Xojo text project format](https://documentation.xojo.com/topics/projects/version_control.html)
- [Xojo modules](https://documentation.xojo.com/topics/code_management/modules.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.rbbas` | [Greeting.rbbas](Greeting.rbbas) creato, verifiche pendenti |
| `.rbfrm` | [hello.rbfrm](variants/rbfrm-d996a914/hello.rbfrm) creato, verifiche pendenti |
| `.rbmnu` | [hello.rbmnu](variants/rbmnu-7e96a970/hello.rbmnu) creato, verifiche pendenti |
| `.rbres` | artefatto da generare Formato componente/progetto REALbasic specifico: occorre un export reale dell’IDE storico e, per risorse/stato UI, eventuali dati binari associati; un modulo .rbbas non è un sostituto. |
| `.rbtbar` | [hello.rbtbar](variants/rbtbar-bfa28cac/hello.rbtbar) creato, verifiche pendenti |
| `.rbuistate` | artefatto da generare Formato componente/progetto REALbasic specifico: occorre un export reale dell’IDE storico e, per risorse/stato UI, eventuali dati binari associati; un modulo .rbbas non è un sostituto. |
