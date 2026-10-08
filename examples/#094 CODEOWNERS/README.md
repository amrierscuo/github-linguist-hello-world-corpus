# #094 CODEOWNERS

Associare in un esempio CODEOWNERS il percorso /hello.txt al proprietario illustrativo hello@example.invalid, e verificare il match con un parser locale.

## Toolchain

Python 3.13.9; codeowners 0.9.0 community parser

## Comandi e procedura

Da questa cartella:

```sh
python -m pip install -r requirements.txt
python verify.py
```

Il parser locale legge la sintassi e applica la regola di percorso. L'indirizzo
rimane illustrativo e non corrisponde a un account GitHub. Questo file sta
nel campione individuale, non in .github/CODEOWNERS: non assegna revisori
al repository del corpus.

## Risultato atteso

Parser locale: hello.txt -> EMAIL hello@example.invalid, other.txt -> nessun proprietario. La risoluzione GitHub richiederebbe un account idoneo reale.

## Stato

Sintassi verificata; semantica in attesa.

Email illustrativa sul dominio riservato example.invalid; non indica un utente reale e non produce richieste di revisione. Non usare questo file come CODEOWNERS effettivo del repository pubblico. La prova locale del match non attesta idoneità del proprietario su GitHub.

Verifica effettiva del 2026-10-08T11:33:36.889535+00:00 su Windows x64: [log](verification/result.json).
Il log include hash SHA-256 della sorgente e dei checker, versioni, comandi, codici di uscita, stdout, stderr e limiti della prova.

Requisiti residui:
- GitHub eligibility and review assignment not verifiable with an illustrative address.

## Fonti primarie

- [https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
- [https://github.com/sbdchd/codeowners](https://github.com/sbdchd/codeowners)
