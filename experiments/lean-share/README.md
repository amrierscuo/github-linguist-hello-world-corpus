# Esperimento quota Lean

Questo campione aggiuntivo serve a osservare come cambia la barra Languages aumentando la quantità di sorgente Lean. L’obiettivo richiesto è almeno il 5% Lean.

Il file Lean 4 contiene prove elementari numerate e un main che stampa Hello, World!. Le ripetizioni sono intenzionali per questo esperimento; la quota Languages misura i byte del sorgente, non il lavoro funzionale o la complessità del progetto.

Il corpus originale con 836 voci e le sue verifiche restano invariati. I contatori del corpus non includono questo esperimento.

Baseline GitHub: 569 linguaggi, 259622 byte totali, 375 byte Lean. Dopo il push, l’API GitHub Languages ha misurato **13966 byte Lean su 273213 byte**, cioè **5,11176%**. I linguaggi rilevati restano **569**; solo i byte di Lean sono cambiati. Il [risultato completo](verification/github_languages.json) conserva commit e momento della misurazione.

Verifica eseguita con Lean 4.0.0: `lean LeanShare.lean` termina con codice 0; `lean --run LeanShare.lean` termina con codice 0 e stampa `Hello, World!`. La [prova registrata](verification/lean4.json) include versione, output e SHA-256 del sorgente.
