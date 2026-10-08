# #661 Simple File Verification

La fixture originale `greeting.txt` contiene `Hello, World!` seguito da LF.
`hello.sfv` dichiara il suo checksum CRC32 `B4E89E84`.

## Toolchain e riproduzione

RHash 1.4.3, pacchetti Ubuntu amd64 `rhash` e `librhash0` 1.4.3-3build1.
La prova è eseguita con i pacchetti originali estratti in una directory di lavoro,
senza installazione globale, su Ubuntu 24.04 tramite WSL2.

Dalla directory dell’esempio, con il vero RHash disponibile:

```sh
rhash --version
rhash -c hello.sfv
```

Per un prefisso estratto esterno, il comando equivalente è:

```sh
LD_LIBRARY_PATH=<prefisso>/usr/lib/x86_64-linux-gnu <prefisso>/usr/bin/rhash -c hello.sfv
```

Risultato reale: `greeting.txt OK`, riepilogo `Everything OK`, exit code 0.
Il checker interpreta il file SFV e calcola il CRC32 del payload originale.
Sintassi e semantica sono verificate per l’integrità dei byte di questa fixture.
CRC32 non attesta autenticità o sicurezza crittografica.

## Evidenza

[Log nativo](verification/native.json): versione, comandi, cwd, stdout/stderr,
exit code e SHA-256 dei due artefatti originali e dei pacchetti del tool.
La nota `path_normalization` descrive le sostituzioni dei soli percorsi locali.
Nessuna modifica è stata apportata ai byte del payload o del file SFV.
Dipendenze e binari sono conservati solo nella directory di lavoro.

## Fonti primarie

- [Progetto RHash](https://github.com/rhash/RHash)
- [Manuale del progetto](https://github.com/rhash/RHash/blob/master/docs/rhash.1)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.sfv` | [hello.sfv](hello.sfv) verificato |
