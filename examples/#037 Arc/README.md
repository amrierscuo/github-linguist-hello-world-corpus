# #037 Arc

Stampare esattamente Hello, World! seguito da newline con prn in Arc.

## File

- `hello.arc`

## Toolchain e verifica

Anarki stable (Arc 3.2 con patch comunitarie), commit 8421605f4a75a0f7fc9a0bed83a87affa1137fab; Racket 8.18 [cs].

Installare Racket 8.18 e ottenere Anarki al commit utilizzato:

```sh
git clone https://github.com/arclanguage/anarki.git anarki
git -C anarki checkout 8421605f4a75a0f7fc9a0bed83a87affa1137fab
```

Il commit appartiene al ramo `stable`, basato su Arc 3.2. Dalla cartella
dell'esempio, adattare il percorso di Anarki e avviare il loader ufficiale:

```sh
racket --version
racket -f /percorso/anarki/as.scm hello.arc
```

Su Windows il medesimo comando accetta un percorso quotato verso `as.scm`.
La distribuzione minima di Racket deve avere anche i pacchetti richiesti da
Anarki (ad esempio `mzscheme`, `compatibility-lib` e `net-lib`). Il loader
esegue il file e termina; non apre il ciclo interattivo quando riceve un file.

## Risultato atteso

Exit 0; stdout esattamente Hello, World! seguito da newline; stderr vuoto.

## Stato della prova

Sintassi verificata. Semantica verificata.

Esecuzione reale con Anarki stable su Racket; carica e valuta la sorgente Arc, nessuna emulazione del linguaggio in Python.

Prova effettiva Windows x64 del 2026-10-08T11:01:56.068379+00:00: [log](verification/result.json).
Il log include hash SHA-256 della sorgente, versioni osservate, comandi, codici di uscita, stdout e stderr.

## Fonti primarie

- [https://arclanguage.github.io/](https://arclanguage.github.io/)
- [https://github.com/arclanguage/anarki/tree/8421605f4a75a0f7fc9a0bed83a87affa1137fab](https://github.com/arclanguage/anarki/tree/8421605f4a75a0f7fc9a0bed83a87affa1137fab)
- [https://github.com/arclanguage/anarki/blob/8421605f4a75a0f7fc9a0bed83a87affa1137fab/arc.arc](https://github.com/arclanguage/anarki/blob/8421605f4a75a0f7fc9a0bed83a87affa1137fab/arc.arc)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.arc` | [hello.arc](hello.arc) verificato |
