# #218 FreeBASIC

Voce canonica `FreeBASIC`, tipo `programming`, language_id `472896659`.

Concatenare stringhe FreeBASIC e stamparle con Print.

## Toolchain e riproduzione

Required authentic toolchain not available/configured — non disponibile / non verificata. Ambiente della prova: **Windows x64**.

Richiede il compilatore FreeBASIC fbc e il suo runtime compatibile. Il compilatore non è presente in questo ambiente.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
fbc hello.bas -x build/hello; ./build/hello
```

Risultato atteso: Exit 0; Hello, World! seguito da newline.

## Stato ed evidenza

Artefatto **creato**; sintassi **in attesa**; semantica **in attesa**.

Dim As String, concatenazione + e End 0 sono sorgente FreeBASIC originale; una esecuzione con un diverso BASIC non è attestata.

Requisiti residui:

- FreeBASIC native fbc compiler is unavailable.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica la collocazione finale dei
sorgenti verificati in staging. I soli probe di disponibilità non attestano parsing
o esecuzione. Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.freebasic.net/wiki/KeyPgPrint](https://www.freebasic.net/wiki/KeyPgPrint)
- [https://www.freebasic.net/wiki/KeyPgString](https://www.freebasic.net/wiki/KeyPgString)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.bi` | [hello.bi](variants/ext-bi-2e6269/hello.bi) creato, verifiche pendenti |
| `.bas` | [hello.bas](hello.bas), [consumer.bas](variants/ext-bi-2e6269/consumer.bas) creato, verifiche pendenti |
