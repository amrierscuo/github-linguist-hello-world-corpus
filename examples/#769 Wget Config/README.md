# #769 Wget Config

Voce canonica `Wget Config`, tipo `data`, language_id `668457123`.

Configurazione GNU Wget originale che imposta User-Agent su `Hello, World!`, con timeout e numero di tentativi limitati; una risorsa locale restituisce lo stesso saluto.

## Toolchain e riproduzione

GNU Wget — GNU Wget 1.21.4 built on linux-gnu.. Ambiente della prova: **Windows x64, Ubuntu 24.04 WSL2 for Linux tools**.

Linux: GNU Wget 1.21.4 e Python 3.12; avviare il comando nella directory dell’esempio. Il driver imposta WGETRC sul .wgetrc locale, apre una porta loopback temporanea e chiude il server a fine prova.

Comando/procedura dalla directory dell’esempio, salvo indicazioni esplicite:

```text
python3 verify.py
```

Risultato atteso: Risposta Hello, World!, User-Agent osservato Hello, World! e PASS.

## Stato ed evidenza

Artefatto **creato**; sintassi **verificata**; semantica **verificata**.

Il comando wget reale legge il config e invia la richiesta HTTP. Il server osserva il valore User-Agent, mentre il driver controlla anche il body ricevuto. Nessuna richiesta a un host esterno è necessaria.

Requisiti residui:

Nessun requisito residuo per l’ambito dichiarato.

Log reale: [native.json](verification/native.json), con comandi, versioni, exit code,
stdout/stderr e SHA-256 degli artefatti. `path_normalization` descrive le sole
sostituzioni dei percorsi locali; `<corpus>` identifica i sorgenti finali verificati
prima in staging. I soli probe di disponibilità non attestano parsing o esecuzione.
Dipendenze e prodotti compilati rimangono nella directory di lavoro.

## Fonti primarie

- [https://www.gnu.org/software/wget/manual/html_node/Wgetrc-Commands.html](https://www.gnu.org/software/wget/manual/html_node/Wgetrc-Commands.html)
