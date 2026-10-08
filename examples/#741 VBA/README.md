# #741 VBA

Eseguire una macro VBA e scrivere il saluto nella Immediate Window.

Tipo canonico `programming`, language_id `399230729`.

Toolchain prevista: Microsoft Office VBA host.

Dalla cartella dell’esempio:

```sh
Importare hello.bas, eseguire HelloWorld e leggere la Immediate Window.
```

Risultato atteso: Hello, World! nella finestra immediata.

Richiede un host VBA; il codice non automatizza documenti dell’utente.

Stato iniziale: creato; sintassi e semantica in attesa. Host VBA di prova non predisposto.

Fonti:

- [VBA Debug.Print](https://learn.microsoft.com/en-us/office/vba/language/reference/user-interface-help/print-method)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bas` | [hello.bas](hello.bas) creato, verifiche pendenti |
| `.cls` | [hello.cls](variants/cls-699ea095/hello.cls) creato, verifiche pendenti |
| `.frm` | artefatto da generare Un UserForm VBA esportato normalmente richiede il corrispondente stream binario .frx/OleObjectBlob generato da Office. Non viene inventato quel payload. |
| `.vba` | [hello.vba](variants/vba-e8141d49/hello.vba) creato, verifiche pendenti |
