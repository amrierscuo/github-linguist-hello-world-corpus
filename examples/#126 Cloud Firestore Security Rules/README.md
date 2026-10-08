# #126 Cloud Firestore Security Rules

Voce canonica: `Cloud Firestore Security Rules`, tipo `data`, `language_id: 407996372`.

Consentire lettura pubblica del solo documento greetings/hello e creazione autenticata del solo campo message=Hello, World!; negare altre scritture.

## Toolchain e riproduzione

Required native toolchain unavailable or not configured — versione non disponibile / non verificata. Ambiente della prova: **Windows x64**.

package.json fissa firebase 13.0.0, @firebase/rules-unit-testing 6.0.0 e firebase-tools 15.33.0. firebase.json configura Firestore su 127.0.0.1:8788. Eseguire in una copia di lavoro con Node compatibile e JDK richiesto dal Firebase Emulator Suite. Il project ID demo-corpus è locale; nessun account o deployment cloud è necessario.

Comando/procedura dalla directory dell’esempio, salvo la directory build esplicitamente indicata:

```text
npm install; npx firebase emulators:exec --only firestore --project demo-corpus "node verify.mjs"
```

Risultato atteso: Emulatore locale carica firestore.rules; test passano per saluto, autorizzazione, campi, path, update e delete.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

verify.mjs usa il vero SDK di test e il vero emulatore: distingue utenti autenticati e anonimi e include controlli negativi. Qui le dipendenze/emulatore non sono configurati e i test non sono stati eseguiti; non vengono attribuiti flag positivi al solo testo delle regole.

Requisiti residui:

- Firebase Firestore rules emulator and unit test client are not installed/configured; no cloud deployment is needed.

Log reale: [native.json](verification/native.json), con comandi, exit code, stdout/stderr,
versioni/toolchain e SHA-256 degli artefatti. La proprietà `path_normalization` documenta
le sostituzioni dei percorsi locali. `<corpus>` identifica i file relativi inclusi nel
corpus finale, che sono stati verificati prima nella directory di staging. I byte dei
sorgenti restano quelli identificati dai checksum. I soli probe di disponibilità degli
strumenti non attestano parsing o esecuzione. Dipendenze e prodotti compilati restano
nella directory di lavoro e non sono inclusi nel corpus.

## Fonti primarie

- [https://firebase.google.com/docs/firestore/security/get-started](https://firebase.google.com/docs/firestore/security/get-started)
- [https://firebase.google.com/docs/rules/unit-tests](https://firebase.google.com/docs/rules/unit-tests)
- [https://firebase.google.com/docs/emulator-suite/connect_firestore](https://firebase.google.com/docs/emulator-suite/connect_firestore)
