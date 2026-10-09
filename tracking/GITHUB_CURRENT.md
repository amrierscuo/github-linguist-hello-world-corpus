# GitHub Languages attuali

Osservazione REST e GraphQL del 2026-10-09T09:00:19.237648+00:00, dopo il push del commit `a664768c794aa6d6a5ded3a412e748c58939fd31`. Repository privata, GitHub Pages disabilitato e loghi esclusi dall'export.

GitHub riporta **575 nomi su 578 attesi** e **273374 byte**. Lean conserva 13966 byte, il 5.10875%.

B4X ora compare grazie all'override esatto per il vero modulo B4J `examples/#051 B4X/Main.bas`. Il suffisso ambiguo non era distinto senza l'header di export IDE. Sorgente, prove e verifiche native restano invariati. [Diagnosi B4X](B4X_RECOGNITION.json).

Restano ArkTS, Bend e LLVM TableGen. Sono nel main ufficiale, il cui YAML corrisponde byte per byte al riferimento ricevuto, ma mancano nella release pubblicata v9.7.0. Gli override non possono registrare nomi nuovi nel servizio. La versione di Linguist distribuita da GitHub non e' accertata; il raggiungimento di 578 dipende dall'adozione di questi nomi e va verificato nuovamente sul servizio. Nessuna falsa etichetta o formato di dati e' stato aggiunto per cambiare il conteggio.

[Risposta REST](github_languages_current.json), [colori e ID effettivi GraphQL](github_catalog_live.json), [mappatura dei 578 nomi](GITHUB_RECOGNITION_TARGETS.json).

La dashboard locale mostra solo i nomi aggregati programming/markup, con nuova numerazione #001..#578. Dati, prosa, varianti, estensioni e verifiche restano negli archivi tecnici. I numeri delle 836 cartelle canoniche non cambiano. Le statistiche aggregate non provano il riconoscimento di ogni singolo file.

I colori GraphQL e gli ID globali GitHub sono dati osservati del servizio. I `language_id` numerici del YAML e i numeri del catalogo hanno ruoli diversi. Per `color: null` la UI usa un colore neutro. La barra compatta puo' raccogliere alcuni nomi sotto Other. REST/GraphQL non espongono il commit della cache.

Fonti: [override ufficiali](https://github.com/github-linguist/linguist/blob/main/docs/overrides.md#detectable), [release v9.7.0](https://github.com/github-linguist/linguist/releases/tag/v9.7.0), [oggetto Language GraphQL](https://docs.github.com/en/graphql/reference/objects#language).
