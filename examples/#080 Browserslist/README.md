# #080 Browserslist

Voce canonica del `reference/languages.yml` del corpus. Il riferimento e il suo ordine restano invariati. Il sorgente è originale di questo esempio.

## Obiettivo

Risolvere una configurazione Browserslist in due target espliciti e deterministici.

Browserslist è un formato di configurazione di target, quindi il risultato pertinente è la selezione di browser. .browserslistrc è letto e risolto dalla libreria Browserslist autentica; verify.cjs controlla soltanto l’elenco prodotto. Versioni esplicite evitano query dipendenti dalla data.

## Toolchain e riproduzione

Browserslist 4.29.3; Node.js 22.20.0

Comandi dalla cartella dell’esempio, con la toolchain indicata disponibile nel PATH. Eseguire la build in una copia temporanea per mantenere fuori dal corpus i file generati.

```text
node verify.cjs <directory-node_modules-con-browserslist>
```

## Risultato atteso e stato

chrome 100
firefox 100
PASS: expected explicit browser targets

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log `verification/toolchain.json` registra comandi effettivi, versioni/provenienza della toolchain, codici di uscita, stdout/stderr e SHA-256 dei sorgenti provati. I percorsi della macchina sono normalizzati.

## Fonti primarie

- https://github.com/browserslist/browserslist
