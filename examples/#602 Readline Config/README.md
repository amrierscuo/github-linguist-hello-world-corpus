# #602 Readline Config

Voce canonica `Readline Config`, tipo `data`, language_id `538732839`.

Decodificare un inputrc che associa una sequenza escape al testo del saluto.

## Toolchain e riproduzione

Authentic GNU Bash Readline inputrc reader/bind macro listing — GNU bash, version 5.2.21(1)-release (x86_64-pc-linux-gnu). Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Bash 5.2.21 con GNU Readline; il file contiene editing-mode e macro keybinding originali.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
bash --noprofile --norc -c 'bind -f "$1"; bind -S' bash .inputrc
```

Risultato atteso: Hello, World! nell’output o nel dato conforme, secondo l’ambito descritto.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Parsing e lookup della macro reali: bind -S mostra il valore Hello, World!. L’ambito verificato eÌ€ la lettura della configurazione; la pressione fisica del tasto non eÌ€ provata.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.gnu.org/software/bash/manual/html_node/Readline-Init-File.html](https://www.gnu.org/software/bash/manual/html_node/Readline-Init-File.html)
