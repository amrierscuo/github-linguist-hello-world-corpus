# #560 Propeller Spin

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Compilare Propeller Spin e rendere disponibile la stringa DAT Hello, World! a main.

DAT definisce13byte ASCII e il terminatore NUL; PUB main restituisce il puntatore alla stringa. Il compiler autentico genera un binario44byte. L’esecuzione del target e la lettura del dato non vengono attribuite alla sola compilazione.

## Toolchain e riproduzione

OpenSpin1.00.81 originale Parallax; costruito con GCC/G++

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
openspin -b -o hello.binary hello.spin
```

```text
Caricare/eseguire hello.binary su un runtime Propeller appropriato.
```

## Risultato atteso e stato

Compilazione accettata; main restituisce l’indirizzo dei byte Hello, World! NUL.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: no.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

Impedimenti: Runtime/emulatore Propeller non preparato; semantica pendente.

## Fonti primarie

- https://github.com/parallaxinc/OpenSpin

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.spin` | [hello.spin](hello.spin) sintassi verificata |
