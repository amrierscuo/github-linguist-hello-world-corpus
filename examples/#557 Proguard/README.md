# #557 Proguard

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Applicare regole ProGuard a una fixture Java reale e conservare il saluto Hello, World!.

hello.pro è il file principale di configurazione. Il driver compila Hello.java e un jar originale, invoca ProGuard con le regole keep e poi esegue il jar processato. L’ottimizzazione/offuscamento sono disabilitati per rendere esplicito il goal della regola keep; binari restano in work.

## Toolchain e riproduzione

ProGuard7.10.0 ufficiale, JDK21 Microsoft

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
javac Hello.java; jar --create --file input.jar --main-class Hello Hello.class; java -jar proguard.jar @hello.pro
```

```text
java -cp output.jar Hello
```

## Risultato atteso e stato

Hello, World! seguito da newline; exit0.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://www.guardsquare.com/manual/configuration/usage
- https://github.com/Guardsquare/proguard/releases/tag/v7.10.0

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pro` | [hello.pro](hello.pro) verificato |
