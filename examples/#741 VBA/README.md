# #741 VBA

Run a macro VBA and write greetings in the Immediate Window.

Canonical type `programming`, language_id `399230729`.

Suggested toolchain: Microsoft Office VBA host.

From the example directory:

```sh
Importare hello.bas, eseguire HelloWorld e leggere la Immediate Window.
```

Expected result: Hello, World! in the immediate window.

Requires a VBA host; the code does not automate user documents.

Stato iniziale: creato; sintassi e semantica in attesa. Host VBA di prova non predisposto.

Sources:

- [VBA Debug.Print](https://learn.microsoft.com/en-us/office/vba/language/reference/user-interface-help/print-method)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.bas` | [hello.bas](hello.bas) created; verification pending |
| `.cls` | [hello.cls](variants/cls-699ea095/hello.cls) created; verification pending |
| `.frm` | artefatto da generare Un UserForm VBA esportato normalmente richiede il corrispondente stream binario .frx/OleObjectBlob generato da Office. Non viene inventato quel payload. |
| `.vba` | [hello.vba](variants/vba-e8141d49/hello.vba) created; verification pending |
