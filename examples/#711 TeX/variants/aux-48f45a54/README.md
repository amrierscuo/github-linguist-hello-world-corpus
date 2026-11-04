# 0711: TeX: `.aux`

Original handwritten TeX auxiliary control: defines a persistent macro for the companion document. Not declared as output of a previous LaTeX compilation.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.aux`.

Control provided, from the folder of the variant:

```text
${WORKSPACE_WSL}/work/tools_701_720/ubuntu/usr/bin/tex --version
${WORKSPACE_WSL}/work/tools_701_720/ubuntu/usr/bin/tex --ini --interaction=nonstopmode --halt-on-error generate.tex
```

Expected result: law document hello.aux and display Hello, World!.

Status: created; syntax verified; behavior verified.

Toolchain osservata: TeX 3.141592653 (TeX Live 2023/Debian).

Ambito reale: Motore originale TeX crea un vero file ausiliario e lo rilegge; espansione della macro osservata nel log console. Nessun formato LaTeX simulato.

Log: `verification/result.json`; SHA-256 of each sorgente/supporto of the variant, commands, exit code and actual output. Build/cache remain under `work/verify_extensions_561_836`.

Primary sources:

- [https://www.latex-project.org/help/documentation/](https://www.latex-project.org/help/documentation/)
- [https://ctan.org/pkg/biblatex](https://ctan.org/pkg/biblatex)
- [https://wiki.contextgarden.net/ConTeXt_and_Lua_programming](https://wiki.contextgarden.net/ConTeXt_and_Lua_programming)
