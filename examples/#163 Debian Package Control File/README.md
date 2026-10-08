# #163 Debian Package Control File

Descrivere ed estrarre un piccolo pacchetto sorgente Debian nativo 1.0; hello.txt estratto deve contenere Hello, World!.

## Toolchain

Debian dpkg-source version 1.22.6.

## Comandi e procedura

dpkg-source --version; dpkg-source -x hello-world-corpus_1.0.dsc build/source; cat build/source/hello.txt

## Risultato atteso

Descrittore e checksum accettati; estrazione exit 0; hello.txt contiene il saluto più newline.

## Stato

Sintassi e semantica verificate.

Il .dsc è un descrittore di pacchetto sorgente, con MD5, SHA-1 e SHA-256 reali del tar.gz originale incluso. L’archivio deterministico contiene solo hello.txt, senza eseguibili. È unsigned e dimostra estrazione del sorgente: non è una prova di pacchetto binario installabile. Il warning di firma assente è conservato nel log.

Verifica effettiva del 2026-10-08T11:56:17.956022+00:00 su WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
Hash delle sorgenti/checker, versioni e comandi reali, codici di uscita, stdout/stderr e limiti della prova sono nel log.

## Fonti primarie e riferimento di formato

- [https://www.debian.org/doc/debian-policy/ch-controlfields.html#debian-source-control-files-dsc](https://www.debian.org/doc/debian-policy/ch-controlfields.html#debian-source-control-files-dsc)
- [https://manpages.debian.org/dpkg-dev/dpkg-source.1.en.html](https://manpages.debian.org/dpkg-dev/dpkg-source.1.en.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.dsc` | [hello-world-corpus_1.0.dsc](hello-world-corpus_1.0.dsc) verificato |
