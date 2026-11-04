# #126 Cloud Firestore Security Rules

Voce canonica: `Cloud Firestore Security Rules`, tipo `data`, `language_id: 407996372`.

Allow public reading of the greetings/hello document only and authenticated creation of the message= Hello, World! field only; deny other scriptures.

## Toolchain and reproduction

Required native toolchain unavailable or not configured, unavailable version / not verified. Test environment: **Windows x64**.

package.json fissa firebase 13.0.0, @firebase/rules-unit-testing 6.0.0 e firebase-tools 15.33.0. firebase.json configura Firestore su 127.0.0.1:8788. Eseguire in una copia di lavoro con Node compatibile e JDK richiesto dal Firebase Emulator Suite. Il project ID demo-corpus è locale; nessun account o deployment cloud è necessario.

Comando/procedura from the example directory, except the build directory explicitly indicated:

```text
npm install; npx firebase emulators:exec --only firestore --project demo-corpus "node verify.mjs"
```

Expected result: Local emulator charge firestore.rules; test pass by greeting, authorization, fields, path, update and delete.

## Status and evidence

Artifact **created**; syntax verification **pending**; behavioral verification **pending**.

verify.mjs uses the true SDK of test and the true emulator: it distinguishes authenticated and anonymous users and includes negative controls. Here the dipendenze/emulatore are not configured and the tests have not been performed; no positive flags are attributed to the rules only.

Remaining requirements:

- Firebase Firestore rules emulator and unit test client are not installed/configured; no cloud deployment is needed.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
toolchain versions and SHA-256 values for the artifacts. The `path_normalization` property documents
local route replacements. `<corpus>` identifies the relative files included in
final corpus, which were first verified in the staging directory.
sources remain those identified by checksums. The only offspring of availability
instruments do not attest parsing or execution.
in the work directory and are not included in the corpus.

## Primary sources

- [https://firebase.google.com/docs/firestore/security/get-started](https://firebase.google.com/docs/firestore/security/get-started)
- [https://firebase.google.com/docs/rules/unit-tests](https://firebase.google.com/docs/rules/unit-tests)
- [https://firebase.google.com/docs/emulator-suite/connect_firestore](https://firebase.google.com/docs/emulator-suite/connect_firestore)
