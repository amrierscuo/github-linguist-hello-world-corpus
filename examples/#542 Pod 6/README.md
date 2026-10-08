# #542 Pod 6

Voce e ordine canonici di reference/languages.yml. Documento originale.

## Obiettivo

Analizzare e renderizzare un documento Pod6/Rakudoc con Hello, World!.

Documento Pod6 originale realmente analizzato e renderizzato da Rakudo. Il driver usa il runtime MoarVM relocato; la verifica riguarda documentazione Pod6, non POD5 Perl.

## Toolchain e riproduzione

Rakudo/MoarVM2022.12 originale, parser Pod6 e renderer Pod::To::Text. Versioni/provenienza e SHA-256 nel log; dipendenze isolate in work.

```text
raku --doc=Text hello.pod6
```

## Risultato atteso e stato

Testo renderizzato contiene Hello, World!.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

verification/toolchain.json registra sorgente SHA-256, comando effettivo, exit/stdout/stderr e runtime originale. La chiamata diretta a MoarVM nel log serve a relocare Rakudo senza installazione globale.

## Fonti primarie

- https://docs.raku.org/language/pod
- https://rakudo.org/

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.pod` | [hello.pod](variants/pod-539ee4a9/hello.pod) creato, verifiche pendenti |
| `.pod6` | [hello.pod6](hello.pod6) verificato |
