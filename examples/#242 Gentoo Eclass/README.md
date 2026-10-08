# #242 Gentoo Eclass

Esportare src_install da un eclass EAPI 8 e installare lo script hello-world nel suo ebuild consumatore.

## Toolchain

GNU bash, version 5.2.21(1)-release (x86_64-pc-linux-gnu)

## Comandi e procedura

bash -n hello-world.eclass; bash -n hello-world-1.0.ebuild; inserire l’eclass in eclass/ di un overlay temporaneo; ebuild hello-world-1.0.ebuild install

## Risultato atteso

Portage risolve inherit hello-world ed EXPORT_FUNCTIONS; immagine contiene hello-world che stampa il saluto.

## Stato

Sintassi verificata; semantica in attesa.

L’eclass originale gestisce EAPI 8 ed esporta hello-world_src_install. Il consumer è incluso per rendere concreta la verifica futura. Bash -n verifica il linguaggio ospite; inheritance, metadata e newbin richiedono Portage reale e restano da provare.

Verifica effettiva del 2026-10-08T12:15:43.041537+00:00 su WSL Ubuntu 24.04.3 x86_64: [log](verification/result.json).
Il log conserva SHA-256 delle sorgenti/checker, versioni/comandi reali, codici di uscita, stdout/stderr e limiti della prova.

Requisiti residui:
- Gentoo Portage package environment not available: native install/inherit phases pending.

## Fonti primarie

- [https://devmanual.gentoo.org/eclass-writing/index.html](https://devmanual.gentoo.org/eclass-writing/index.html)
- [https://projects.gentoo.org/pms/latest/pms.html](https://projects.gentoo.org/pms/latest/pms.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.eclass` | [hello-world.eclass](hello-world.eclass) sintassi verificata |
