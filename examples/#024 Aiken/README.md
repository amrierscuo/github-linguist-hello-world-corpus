# #024 Aiken

Voce canonica: `Aiken`, tipo `programming`, `language_id: 899409497`.
`lib/hello.ak` espone `greeting() -> ByteArray` e restituisce i byte UTF-8 di
`Hello, World!`. Due test Aiken confrontano il risultato con i tredici byte
attesi e con un testo diverso. `aiken.toml` descrive il progetto senza dipendenze.

## Toolchain e riproduzione

Verificato su Windows x64 con il binario ufficiale **Aiken v1.1.23+8949565**.
Installare la distribuzione 1.1.23 ufficiale, poi dalla directory di questo esempio:

```powershell
aiken --version
aiken check --skip-tests .
aiken check .
```

Risultato atteso: typecheck con codice 0 e due test superati —
`greeting_has_exact_bytes`, `greeting_rejects_other_text` — senza fallimenti.
I test sono eseguiti dalla VM Plutus integrata in Aiken. La stringa tra virgolette
nel tipo `ByteArray` rappresenta byte UTF-8; non è un messaggio stampato su console.

## Stato ed evidenza

Artefatto creato; sintassi **verificata**; semantica **verificata** nella VM.
Controllo negativo: parentesi incompleta nella firma di `greeting` rifiutata dal
compilatore con codice 1. La prova usa una copia isolata del progetto con i medesimi
byte degli artefatti; non aggiunge prodotti di build al corpus. Nessun requisito
residuo per questi test; non sono richiesti wallet o transazioni.

Log: [aiken.json](verification/aiken.json), con comandi, report completo dei due
test e SHA-256. L'archivio ufficiale Windows ha SHA-256
`8f91dfea06a80ddab139db6bce788c7f1a6cc3850c21b44ae6350afe181239ee`,
confrontato nel runner con il checksum della distribuzione. `path_normalization`
descrive i percorsi normalizzati; sorgenti e risultati sono invariati.

## Fonti ufficiali

- [ByteArray e notazioni letterali](https://aiken-lang.org/language-tour/primitive-types).
- [Test Aiken e VM](https://aiken-lang.org/language-tour/tests).
- [Distribuzione v1.1.23 e checksum](https://github.com/aiken-lang/aiken/releases/tag/v1.1.23).

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.ak` | [hello.ak](lib/hello.ak) verificato |
