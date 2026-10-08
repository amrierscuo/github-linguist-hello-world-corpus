# #719 TextMate Properties

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Caricare una proprietà TextMate contenente Hello, World!.

Fixture .tm_properties originale con selettore glob e valore stringa; il file non viene installato nella configurazione dell’editor.

## Toolchain e riproduzione

TextMate2 originale su macOS, versione da registrare

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
TextMate: aprire un file .txt nel progetto e leggere GREETING dalle variabili di un comando bundle
```

## Risultato atteso e stato

GREETING = Hello, World! per i file *.txt.

Artefatto creato: sì. Sintassi verificata: no. Semantica verificata: no.

Sorgente documentato; nessun parser/compiler/runtime originale eseguito per questa voce.

Impedimenti: TextMate/macOS non disponibili; parser delle proprietà ed effettiva variabile pendenti.

## Fonti primarie

- https://macromates.com/textmate/manual/settings
