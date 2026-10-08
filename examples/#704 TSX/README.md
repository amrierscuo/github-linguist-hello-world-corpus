# #704 TSX

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Compilare TSX e renderizzare un componente React con Hello, World!.

Il typechecker TSX compila il componente tipizzato; React server renderer valuta il prop audience e produce markup statico.

## Toolchain e riproduzione

TypeScript, React e react-dom originali; versioni e lock SHA nel log

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
tsc --jsx react-jsx --module commonjs --target es2020 --skipLibCheck --outDir build hello.tsx; node render.cjs
```

## Risultato atteso e stato

<p>Hello, World!</p> su stdout.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://www.typescriptlang.org/docs/handbook/jsx.html

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.tsx` | [hello.tsx](hello.tsx) verificato |
