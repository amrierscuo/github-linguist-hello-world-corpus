# 0711 — TeX — `.aux`

Controllo ausiliario TeX originale scritto a mano: definisce una macro persistente per il documento companion. Non dichiarato come output di una compilazione LaTeX precedente.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.aux`.

Controllo previsto, dalla cartella della variante:

```text
${WORKSPACE_WSL}/work/tools_701_720/ubuntu/usr/bin/tex --version
${WORKSPACE_WSL}/work/tools_701_720/ubuntu/usr/bin/tex --ini --interaction=nonstopmode --halt-on-error generate.tex
```

Risultato atteso: documento legge hello.aux e visualizza Hello, World!.

Stato: creato; sintassi verificata; semantica verificata.

Toolchain osservata: TeX 3.141592653 (TeX Live 2023/Debian).

Ambito reale: Motore originale TeX crea un vero file ausiliario e lo rilegge; espansione della macro osservata nel log console. Nessun formato LaTeX simulato.

Log: `verification/result.json`; SHA-256 di ogni sorgente/supporto della variante, comandi, exit code e output effettivi. Build/cache restano sotto `work/verify_extensions_561_836`.

Fonti primarie:

- [https://www.latex-project.org/help/documentation/](https://www.latex-project.org/help/documentation/)
- [https://ctan.org/pkg/biblatex](https://ctan.org/pkg/biblatex)
- [https://wiki.contextgarden.net/ConTeXt_and_Lua_programming](https://wiki.contextgarden.net/ConTeXt_and_Lua_programming)
