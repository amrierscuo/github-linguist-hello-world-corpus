# Obiettivo delle statistiche GitHub

L’obiettivo primario è massimizzare i linguaggi correttamente rilevati negli esempi del repository. Le 836 voci del catalogo rappresentano l’intero snapshot YAML e non il numero di nomi che compariranno nella barra Languages.

Riferimento canonico SHA-256: `183243e30496ba53f5f8743b0e39c9f0e0bccc5a32639f7b541cc2285db0e043`.
Analisi locale aggiornata: `2026-10-08T22:04:25.589921+00:00`.

| Tipo nel YAML | Voci | Partecipazione predefinita alle statistiche |
| --- | ---: | --- |
| programming | 563 | Candidati |
| markup | 71 | Candidati |
| data | 184 | Esclusi |
| prose | 18 | Esclusi |

Sono quindi 634 voci candidate, aggregate in 578 nomi di gruppo nello snapshot. Il campo `group` fa confluire dialetti o varianti nel linguaggio principale. Questi sono obiettivi teorici: il riconoscimento effettivo dipende dai file, dalle esclusioni, dai formati binari e dalla versione Linguist usata da GitHub.

La barra compatta di GitHub raggruppa i linguaggi meno rappresentati in `Other`. Non elenca centinaia di nomi. La lista completa dei linguaggi rilevati e dei byte è disponibile tramite l’API Languages del repository.

Le percentuali dipendono dai byte rilevati, non dal numero di file, cartelle, loghi o programmi. La sola presenza di un’estensione non prova il corretto riconoscimento.

`.gitattributes` esclude dalle statistiche il catalogo HTML, le icone, i riferimenti, i tracker, gli strumenti del corpus, la documentazione e i log di verifica. I file conservano i propri byte e il catalogo resta utilizzabile con GitHub Pages.
I tipi data e prose conservano il comportamento predefinito. Non sono stati applicati override `linguist-language` agli esempi. Il passo successivo è una prova con il vero GitHub Linguist, seguita dalla correzione delle classificazioni ambigue con attributi specifici e documentati.

La sintassi e la semantica registrate riguardano le toolchain dei campioni; non costituiscono una prova delle statistiche GitHub. Nessun repository è stato pubblicato e non è ancora disponibile un risultato Languages su GitHub per questo corpus.

Nelle 634 voci candidate ci sono 352 campioni con sintassi verificata e 313 con semantica verificata. Le verifiche restanti dei candidati hanno priorità rispetto ai formati data e prose per questo obiettivo.

Fonti primarie: [funzionamento Linguist](https://github.com/github-linguist/linguist/blob/main/docs/how-linguist-works.md), [attributi](https://github.com/github-linguist/linguist/blob/main/docs/overrides.md#detectable), [gruppi](https://github.com/github-linguist/linguist/blob/5fbdfcb8133be2bed88bf3ce62b2335f50474525/lib/linguist/repository.rb#L182), [API completa](https://docs.github.com/en/rest/repos/repos#list-repository-languages). Esempio pubblico della barra con `Other`: [RosettaCodeData](https://github.com/acmeism/RosettaCodeData).

## Voci candidate

| Numero | Nome canonico | Tipo | Nome del gruppo nelle statistiche | Sintassi | Semantica |
| --- | --- | --- | --- | --- | --- |
| #001 | 1C Enterprise | programming | 1C Enterprise | Verificata | Verificata |
| #003 | 4D | programming | 4D | Da verificare | Da verificare |
| #004 | ABAP | programming | ABAP | Verificata | Da verificare |
| #005 | ABAP CDS | programming | ABAP CDS | Verificata | Da verificare |
| #007 | AGS Script | programming | AGS Script | Da verificare | Da verificare |
| #008 | AIDL | programming | AIDL | Da verificare | Da verificare |
| #009 | AL | programming | AL | Da verificare | Da verificare |
| #010 | ALGOL | programming | ALGOL | Da verificare | Da verificare |
| #011 | AMPL | programming | AMPL | Verificata | Verificata |
| #012 | ANTLR | programming | ANTLR | Verificata | Verificata |
| #013 | API Blueprint | markup | API Blueprint | Verificata | Verificata |
| #014 | APL | programming | APL | Verificata | Verificata |
| #015 | ASL | programming | ASL | Verificata | Verificata |
| #017 | ASP.NET | programming | ASP.NET | Verificata | Verificata |
| #018 | ATS | programming | ATS | Da verificare | Da verificare |
| #019 | ActionScript | programming | ActionScript | Da verificare | Da verificare |
| #020 | Ada | programming | Ada | Da verificare | Da verificare |
| #023 | Agda | programming | Agda | Da verificare | Da verificare |
| #024 | Aiken | programming | Aiken | Verificata | Verificata |
| #025 | Aleo | programming | Aleo | Verificata | Da verificare |
| #026 | Alloy | programming | Alloy | Verificata | Verificata |
| #027 | Alpine Abuild | programming | Shell | Da verificare | Da verificare |
| #029 | AngelScript | programming | AngelScript | Verificata | Verificata |
| #030 | Answer Set Programming | programming | Answer Set Programming | Verificata | Verificata |
| #032 | Antlers | markup | Antlers | Da verificare | Da verificare |
| #034 | Apex | programming | Apex | Verificata | Da verificare |
| #035 | Apollo Guidance Computer | programming | Assembly | Verificata | Da verificare |
| #036 | AppleScript | programming | AppleScript | Da verificare | Da verificare |
| #037 | Arc | programming | Arc | Verificata | Verificata |
| #038 | ArkTS | programming | ArkTS | Da verificare | Da verificare |
| #040 | AspectJ | programming | AspectJ | Verificata | Verificata |
| #041 | Assembly | programming | Assembly | Verificata | Verificata |
| #042 | Astro | markup | Astro | Verificata | Da verificare |
| #043 | Asymptote | programming | Asymptote | Da verificare | Da verificare |
| #044 | Augeas | programming | Augeas | Verificata | Verificata |
| #045 | AutoHotkey | programming | AutoHotkey | Verificata | Verificata |
| #046 | AutoIt | programming | AutoIt | Verificata | Verificata |
| #048 | Awk | programming | Awk | Verificata | Verificata |
| #049 | B | programming | B | Da verificare | Da verificare |
| #050 | B (Formal Method) | programming | B (Formal Method) | Da verificare | Da verificare |
| #051 | B4X | programming | B4X | Da verificare | Da verificare |
| #052 | BAML | programming | BAML | Verificata | Da verificare |
| #053 | BASIC | programming | BASIC | Verificata | Verificata |
| #054 | BBCode | markup | BBCode | Verificata | Verificata |
| #056 | BQN | programming | BQN | Verificata | Verificata |
| #057 | Ballerina | programming | Ballerina | Da verificare | Da verificare |
| #058 | Batchfile | programming | Batchfile | Verificata | Verificata |
| #059 | Beef | programming | Beef | Da verificare | Da verificare |
| #060 | Befunge | programming | Befunge | Verificata | Verificata |
| #061 | Bend | programming | Bend | Verificata | Verificata |
| #062 | Berry | programming | Berry | Verificata | Verificata |
| #063 | BibTeX | markup | TeX | Verificata | Verificata |
| #064 | BibTeX Style | programming | BibTeX Style | Verificata | Verificata |
| #065 | Bicep | programming | Bicep | Verificata | Verificata |
| #066 | Bikeshed | markup | Bikeshed | Da verificare | Da verificare |
| #067 | Bison | programming | Yacc | Verificata | Verificata |
| #068 | BitBake | programming | BitBake | Da verificare | Da verificare |
| #069 | Blade | markup | Blade | Da verificare | Da verificare |
| #070 | BlitzBasic | programming | BlitzBasic | Da verificare | Da verificare |
| #071 | BlitzMax | programming | BlitzMax | Da verificare | Da verificare |
| #072 | Blueprint | markup | Blueprint | Da verificare | Da verificare |
| #073 | Bluespec | programming | Bluespec | Verificata | Verificata |
| #074 | Bluespec BH | programming | Bluespec | Verificata | Verificata |
| #075 | Boo | programming | Boo | Da verificare | Da verificare |
| #076 | Boogie | programming | Boogie | Verificata | Verificata |
| #077 | Brainfuck | programming | Brainfuck | Verificata | Verificata |
| #078 | BrighterScript | programming | BrighterScript | Verificata | Verificata |
| #079 | Brightscript | programming | Brightscript | Verificata | Verificata |
| #081 | Bru | markup | Bru | Verificata | Verificata |
| #083 | C | programming | C | Verificata | Verificata |
| #084 | C# | programming | C# | Verificata | Verificata |
| #085 | C++ | programming | C++ | Verificata | Verificata |
| #087 | C2hs Haskell | programming | Haskell | Verificata | Da verificare |
| #088 | C3 | programming | C3 | Verificata | Verificata |
| #089 | CAP CDS | programming | CAP CDS | Verificata | Verificata |
| #091 | CLIPS | programming | CLIPS | Verificata | Verificata |
| #092 | CMake | programming | CMake | Verificata | Verificata |
| #093 | COBOL | programming | COBOL | Verificata | Verificata |
| #096 | CQL | programming | CQL | Da verificare | Da verificare |
| #098 | CSS | markup | CSS | Verificata | Verificata |
| #100 | CUE | programming | CUE | Verificata | Verificata |
| #101 | CWeb | programming | CWeb | Verificata | Verificata |
| #104 | Cadence | programming | Cadence | Da verificare | Da verificare |
| #105 | Cairo | programming | Cairo | Da verificare | Da verificare |
| #106 | Cairo Zero | programming | Cairo | Da verificare | Da verificare |
| #107 | CameLIGO | programming | LigoLANG | Da verificare | Da verificare |
| #108 | Cangjie | programming | Cangjie | Da verificare | Da verificare |
| #109 | Cap'n Proto | programming | Cap'n Proto | Verificata | Verificata |
| #110 | Carbon | programming | Carbon | Da verificare | Da verificare |
| #111 | CartoCSS | programming | CartoCSS | Verificata | Verificata |
| #112 | Ceylon | programming | Ceylon | Da verificare | Da verificare |
| #113 | Chapel | programming | Chapel | Da verificare | Da verificare |
| #114 | Charity | programming | Charity | Da verificare | Da verificare |
| #116 | ChucK | programming | ChucK | Da verificare | Da verificare |
| #117 | Circom | programming | Circom | Verificata | Verificata |
| #118 | Cirru | programming | Cirru | Verificata | Verificata |
| #119 | Clarion | programming | Clarion | Da verificare | Da verificare |
| #120 | Clarity | programming | Clarity | Verificata | Verificata |
| #121 | Classic ASP | programming | Classic ASP | Da verificare | Da verificare |
| #122 | Clean | programming | Clean | Verificata | Verificata |
| #123 | Click | programming | Click | Da verificare | Da verificare |
| #124 | Clojure | programming | Clojure | Verificata | Verificata |
| #125 | Closure Templates | markup | Closure Templates | Verificata | Verificata |
| #127 | Clue | programming | Clue | Verificata | Verificata |
| #129 | CodeQL | programming | CodeQL | Da verificare | Da verificare |
| #130 | CoffeeScript | programming | CoffeeScript | Verificata | Verificata |
| #131 | ColdFusion | programming | ColdFusion | Da verificare | Da verificare |
| #132 | ColdFusion CFC | programming | ColdFusion | Da verificare | Da verificare |
| #133 | Common Lisp | programming | Common Lisp | Verificata | Verificata |
| #134 | Common Workflow Language | programming | Common Workflow Language | Da verificare | Da verificare |
| #135 | Component Pascal | programming | Component Pascal | Da verificare | Da verificare |
| #136 | Cooklang | markup | Cooklang | Verificata | Verificata |
| #137 | Cool | programming | Cool | Da verificare | Da verificare |
| #140 | Crystal | programming | Crystal | Da verificare | Da verificare |
| #141 | Csound | programming | Csound | Verificata | Verificata |
| #142 | Csound Document | programming | Csound Document | Verificata | Verificata |
| #143 | Csound Score | programming | Csound Score | Verificata | Verificata |
| #144 | Cuda | programming | Cuda | Da verificare | Da verificare |
| #146 | Curry | programming | Curry | Da verificare | Da verificare |
| #147 | Cycript | programming | Cycript | Da verificare | Da verificare |
| #149 | Cypher | programming | Cypher | Verificata | Verificata |
| #150 | Cython | programming | Cython | Verificata | Verificata |
| #151 | D | programming | D | Verificata | Verificata |
| #153 | D2 | markup | D2 | Verificata | Verificata |
| #154 | DIGITAL Command Language | programming | DIGITAL Command Language | Da verificare | Da verificare |
| #155 | DM | programming | DM | Da verificare | Da verificare |
| #157 | DTrace | programming | DTrace | Da verificare | Da verificare |
| #158 | Dafny | programming | Dafny | Verificata | Verificata |
| #160 | Dart | programming | Dart | Verificata | Verificata |
| #161 | Daslang | programming | Daslang | Verificata | Verificata |
| #162 | DataWeave | programming | DataWeave | Verificata | Verificata |
| #164 | DenizenScript | programming | DenizenScript | Da verificare | Da verificare |
| #165 | Dhall | programming | Dhall | Verificata | Verificata |
| #168 | Dockerfile | programming | Dockerfile | Verificata | Da verificare |
| #169 | Dogescript | programming | Dogescript | Verificata | Verificata |
| #171 | Dune | programming | Dune | Verificata | Verificata |
| #172 | Dylan | programming | Dylan | Da verificare | Da verificare |
| #173 | E | programming | E | Da verificare | Da verificare |
| #176 | ECL | programming | ECL | Da verificare | Da verificare |
| #177 | ECLiPSe | programming | Prolog | Verificata | Verificata |
| #178 | EJS | markup | EJS | Verificata | Verificata |
| #179 | EQ | programming | EQ | Da verificare | Da verificare |
| #181 | Earthly | programming | Earthly | Da verificare | Da verificare |
| #184 | Ecmarkup | markup | HTML | Verificata | Verificata |
| #185 | Edge | markup | Edge | Verificata | Verificata |
| #186 | EdgeQL | programming | EdgeQL | Da verificare | Da verificare |
| #189 | Eiffel | programming | Eiffel | Da verificare | Da verificare |
| #190 | Elixir | programming | Elixir | Verificata | Verificata |
| #191 | Elm | programming | Elm | Da verificare | Da verificare |
| #192 | Elvish | programming | Elvish | Verificata | Verificata |
| #193 | Elvish Transcript | programming | Elvish | Verificata | Verificata |
| #194 | Emacs Lisp | programming | Emacs Lisp | Da verificare | Da verificare |
| #195 | EmberScript | programming | EmberScript | Verificata | Verificata |
| #196 | Erlang | programming | Erlang | Verificata | Verificata |
| #197 | Euphoria | programming | Euphoria | Verificata | Verificata |
| #198 | F# | programming | F# | Verificata | Verificata |
| #199 | F* | programming | F* | Da verificare | Da verificare |
| #201 | FIRRTL | programming | FIRRTL | Da verificare | Da verificare |
| #202 | FLUX | programming | FLUX | Da verificare | Da verificare |
| #203 | FPP | programming | FPP | Da verificare | Da verificare |
| #204 | Factor | programming | Factor | Da verificare | Da verificare |
| #205 | Fancy | programming | Fancy | Da verificare | Da verificare |
| #206 | Fantom | programming | Fantom | Verificata | Verificata |
| #207 | Faust | programming | Faust | Verificata | Verificata |
| #208 | Fennel | programming | Fennel | Verificata | Verificata |
| #209 | Filebench WML | programming | Filebench WML | Da verificare | Da verificare |
| #210 | Filterscript | programming | RenderScript | Da verificare | Da verificare |
| #212 | Flix | programming | Flix | Verificata | Verificata |
| #213 | Fluent | programming | Fluent | Verificata | Verificata |
| #215 | Forth | programming | Forth | Verificata | Verificata |
| #216 | Fortran | programming | Fortran | Verificata | Verificata |
| #217 | Fortran Free Form | programming | Fortran | Verificata | Verificata |
| #218 | FreeBASIC | programming | FreeBASIC | Da verificare | Da verificare |
| #219 | FreeMarker | programming | FreeMarker | Verificata | Verificata |
| #220 | Frege | programming | Frege | Verificata | Verificata |
| #221 | Futhark | programming | Futhark | Verificata | Verificata |
| #222 | G-code | programming | G-code | Da verificare | Da verificare |
| #223 | GAML | programming | GAML | Da verificare | Da verificare |
| #224 | GAMS | programming | GAMS | Da verificare | Da verificare |
| #225 | GAP | programming | GAP | Verificata | Verificata |
| #226 | GCC Machine Description | programming | GCC Machine Description | Da verificare | Da verificare |
| #227 | GDB | programming | GDB | Verificata | Verificata |
| #228 | GDScript | programming | GDScript | Verificata | Verificata |
| #229 | GDShader | programming | GDShader | Verificata | Da verificare |
| #231 | GLSL | programming | GLSL | Verificata | Da verificare |
| #233 | GSC | programming | GSC | Verificata | Da verificare |
| #234 | Game Maker Language | programming | Game Maker Language | Da verificare | Da verificare |
| #237 | Genero 4gl | programming | Genero 4gl | Da verificare | Da verificare |
| #238 | Genero per | markup | Genero per | Da verificare | Da verificare |
| #239 | Genie | programming | Genie | Verificata | Verificata |
| #240 | Genshi | programming | Genshi | Verificata | Verificata |
| #241 | Gentoo Ebuild | programming | Shell | Verificata | Da verificare |
| #242 | Gentoo Eclass | programming | Shell | Verificata | Da verificare |
| #245 | Gherkin | programming | Gherkin | Verificata | Verificata |
| #250 | Gleam | programming | Gleam | Verificata | Verificata |
| #251 | Glimmer JS | programming | JavaScript | Verificata | Da verificare |
| #252 | Glimmer TS | programming | TypeScript | Verificata | Da verificare |
| #253 | Glyph | programming | Glyph | Da verificare | Da verificare |
| #255 | Gno | programming | Gno | Verificata | Verificata |
| #256 | Gnuplot | programming | Gnuplot | Verificata | Verificata |
| #257 | Go | programming | Go | Verificata | Verificata |
| #260 | Go Template | markup | Go Template | Verificata | Verificata |
| #263 | Golo | programming | Golo | Verificata | Verificata |
| #264 | Gosu | programming | Gosu | Da verificare | Da verificare |
| #265 | Grace | programming | Grace | Da verificare | Da verificare |
| #268 | Grammatical Framework | programming | Grammatical Framework | Da verificare | Da verificare |
| #272 | Groovy | programming | Groovy | Verificata | Verificata |
| #273 | Groovy Server Pages | programming | Groovy | Da verificare | Da verificare |
| #276 | HCL | programming | HCL | Verificata | Verificata |
| #277 | HIP | programming | HIP | Da verificare | Da verificare |
| #278 | HLSL | programming | HLSL | Verificata | Da verificare |
| #280 | HTML | markup | HTML | Verificata | Verificata |
| #281 | HTML+ECR | markup | HTML | Verificata | Verificata |
| #282 | HTML+EEX | markup | HTML | Verificata | Verificata |
| #283 | HTML+ERB | markup | HTML | Verificata | Verificata |
| #284 | HTML+PHP | markup | HTML | Verificata | Verificata |
| #285 | HTML+Razor | markup | HTML | Da verificare | Da verificare |
| #288 | Hack | programming | Hack | Da verificare | Da verificare |
| #289 | Haml | markup | Haml | Verificata | Verificata |
| #290 | Handlebars | markup | Handlebars | Verificata | Verificata |
| #291 | Harbour | programming | Harbour | Da verificare | Da verificare |
| #292 | Hare | programming | Hare | Da verificare | Da verificare |
| #293 | Haskell | programming | Haskell | Verificata | Verificata |
| #294 | Haxe | programming | Haxe | Verificata | Verificata |
| #295 | HiveQL | programming | HiveQL | Verificata | Da verificare |
| #296 | HolyC | programming | HolyC | Da verificare | Da verificare |
| #298 | Hurl | programming | Hurl | Verificata | Verificata |
| #299 | Hy | programming | Hy | Verificata | Verificata |
| #300 | HyPhy | programming | HyPhy | Verificata | Verificata |
| #301 | IDL | programming | IDL | Da verificare | Da verificare |
| #302 | IGOR Pro | programming | IGOR Pro | Da verificare | Da verificare |
| #303 | IL Assembly | programming | IL Assembly | Verificata | Verificata |
| #306 | ISPC | programming | ISPC | Verificata | Verificata |
| #307 | Idris | programming | Idris | Da verificare | Da verificare |
| #309 | ImHex Pattern Language | programming | ImHex Pattern Language | Da verificare | Da verificare |
| #310 | ImageJ Macro | programming | ImageJ Macro | Verificata | Verificata |
| #311 | Imba | programming | Imba | Verificata | Verificata |
| #312 | Inform 7 | programming | Inform 7 | Verificata | Verificata |
| #313 | Ink | programming | Ink | Verificata | Verificata |
| #314 | Inno Setup | programming | Inno Setup | Da verificare | Da verificare |
| #315 | Io | programming | Io | Da verificare | Da verificare |
| #316 | Ioke | programming | Ioke | Da verificare | Da verificare |
| #317 | Isabelle | programming | Isabelle | Da verificare | Da verificare |
| #318 | Isabelle ROOT | programming | Isabelle | Da verificare | Da verificare |
| #319 | J | programming | J | Verificata | Verificata |
| #321 | JASS | programming | JASS | Da verificare | Da verificare |
| #322 | JCL | programming | JCL | Da verificare | Da verificare |
| #323 | JFlex | programming | Lex | Verificata | Verificata |
| #328 | JSONiq | programming | JSONiq | Da verificare | Da verificare |
| #329 | Jac | programming | Jac | Verificata | Verificata |
| #330 | Jai | programming | Jai | Da verificare | Da verificare |
| #331 | Janet | programming | Janet | Verificata | Verificata |
| #332 | Jasmin | programming | Jasmin | Verificata | Verificata |
| #333 | Java | programming | Java | Verificata | Verificata |
| #335 | Java Server Pages | programming | Java | Verificata | Verificata |
| #336 | Java Template Engine | programming | Java | Verificata | Verificata |
| #337 | JavaScript | programming | JavaScript | Verificata | Verificata |
| #338 | JavaScript+ERB | programming | JavaScript | Verificata | Verificata |
| #340 | JetBrains MPS | programming | JetBrains MPS | Da verificare | Da verificare |
| #341 | Jinja | markup | Jinja | Verificata | Verificata |
| #342 | Jison | programming | Yacc | Verificata | Verificata |
| #343 | Jison Lex | programming | Lex | Verificata | Verificata |
| #344 | Jolie | programming | Jolie | Da verificare | Da verificare |
| #345 | Jsonnet | programming | Jsonnet | Verificata | Verificata |
| #346 | Julia | programming | Julia | Verificata | Verificata |
| #347 | Julia REPL | programming | Julia | Verificata | Verificata |
| #348 | Jupyter Notebook | markup | Jupyter Notebook | Verificata | Verificata |
| #349 | Just | programming | Just | Verificata | Verificata |
| #350 | KCL | programming | KCL | Verificata | Verificata |
| #352 | KFramework | programming | KFramework | Da verificare | Da verificare |
| #353 | KRL | programming | KRL | Verificata | Da verificare |
| #354 | Kaitai Struct | programming | Kaitai Struct | Verificata | Verificata |
| #355 | KakouneScript | programming | KakouneScript | Verificata | Verificata |
| #356 | KerboScript | programming | KerboScript | Da verificare | Da verificare |
| #361 | Kit | markup | Kit | Da verificare | Da verificare |
| #362 | KoLmafia ASH | programming | KoLmafia ASH | Da verificare | Da verificare |
| #363 | Koka | programming | Koka | Verificata | Verificata |
| #364 | Kotlin | programming | Kotlin | Verificata | Verificata |
| #366 | LFE | programming | LFE | Verificata | Verificata |
| #367 | LLVM | programming | LLVM | Verificata | Verificata |
| #368 | LLVM TableGen | programming | LLVM TableGen | Verificata | Verificata |
| #369 | LOLCODE | programming | LOLCODE | Verificata | Verificata |
| #370 | LSL | programming | LSL | Da verificare | Da verificare |
| #372 | LabVIEW | programming | LabVIEW | Da verificare | Da verificare |
| #373 | Lambdapi | programming | Lambdapi | Da verificare | Da verificare |
| #374 | Langium | programming | Langium | Verificata | Verificata |
| #376 | Lasso | programming | Lasso | Da verificare | Da verificare |
| #377 | Latte | markup | Latte | Verificata | Verificata |
| #378 | Lean | programming | Lean | Verificata | Verificata |
| #379 | Lean 4 | programming | Lean | Verificata | Verificata |
| #380 | Leo | programming | Leo | Da verificare | Da verificare |
| #381 | Less | markup | Less | Verificata | Verificata |
| #382 | Lex | programming | Lex | Verificata | Verificata |
| #383 | LigoLANG | programming | LigoLANG | Da verificare | Da verificare |
| #384 | LilyPond | programming | LilyPond | Da verificare | Da verificare |
| #385 | Limbo | programming | Limbo | Da verificare | Da verificare |
| #386 | Linear Programming | programming | Linear Programming | Verificata | Verificata |
| #387 | Linker Script | programming | Linker Script | Verificata | Verificata |
| #389 | Liquid | markup | Liquid | Verificata | Verificata |
| #390 | Liquidsoap | programming | Liquidsoap | Da verificare | Da verificare |
| #391 | Literate Agda | programming | Agda | Da verificare | Da verificare |
| #392 | Literate CoffeeScript | programming | CoffeeScript | Verificata | Verificata |
| #393 | Literate Haskell | programming | Haskell | Verificata | Verificata |
| #394 | LiveCode Script | programming | LiveCode Script | Da verificare | Da verificare |
| #395 | LiveScript | programming | LiveScript | Verificata | Verificata |
| #396 | Lobster | programming | Lobster | Verificata | Verificata |
| #397 | Logos | programming | Logos | Verificata | Da verificare |
| #398 | Logtalk | programming | Logtalk | Verificata | Verificata |
| #399 | LookML | programming | LookML | Verificata | Da verificare |
| #400 | LoomScript | programming | LoomScript | Da verificare | Da verificare |
| #401 | Lua | programming | Lua | Verificata | Verificata |
| #402 | Luau | programming | Luau | Verificata | Verificata |
| #403 | M | programming | M | Da verificare | Da verificare |
| #405 | M4 | programming | M4 | Verificata | Verificata |
| #406 | M4Sugar | programming | M4 | Verificata | Verificata |
| #407 | MATLAB | programming | MATLAB | Da verificare | Da verificare |
| #408 | MAXScript | programming | MAXScript | Da verificare | Da verificare |
| #409 | MDX | markup | MDX | Verificata | Verificata |
| #410 | MLIR | programming | MLIR | Verificata | Verificata |
| #411 | MQL4 | programming | MQL4 | Da verificare | Da verificare |
| #412 | MQL5 | programming | MQL5 | Da verificare | Da verificare |
| #413 | MTML | markup | MTML | Da verificare | Da verificare |
| #414 | MUF | programming | Forth | Da verificare | Da verificare |
| #415 | Macaulay2 | programming | Macaulay2 | Da verificare | Da verificare |
| #416 | Makefile | programming | Makefile | Verificata | Verificata |
| #417 | Mako | programming | Mako | Verificata | Verificata |
| #419 | Marko | markup | Marko | Verificata | Verificata |
| #420 | Mask | markup | Mask | Verificata | Verificata |
| #421 | Mathematical Programming System | programming | Mathematical Programming System | Verificata | Verificata |
| #423 | Max | programming | Max | Da verificare | Da verificare |
| #424 | MeTTa | programming | MeTTa | Da verificare | Da verificare |
| #425 | Mercury | programming | Mercury | Da verificare | Da verificare |
| #426 | Mermaid | markup | Mermaid | Verificata | Verificata |
| #427 | Meson | programming | Meson | Verificata | Verificata |
| #428 | Metal | programming | Metal | Da verificare | Da verificare |
| #431 | MiniD | programming | MiniD | Da verificare | Da verificare |
| #432 | MiniScript | programming | MiniScript | Verificata | Verificata |
| #434 | MiniZinc | programming | MiniZinc | Verificata | Verificata |
| #436 | Mint | programming | Mint | Da verificare | Da verificare |
| #437 | Mirah | programming | Mirah | Da verificare | Da verificare |
| #438 | Modelica | programming | Modelica | Da verificare | Da verificare |
| #439 | Modula-2 | programming | Modula-2 | Da verificare | Da verificare |
| #440 | Modula-3 | programming | Modula-3 | Da verificare | Da verificare |
| #441 | Module Management System | programming | Module Management System | Da verificare | Da verificare |
| #442 | Mojo | programming | Mojo | Da verificare | Da verificare |
| #443 | Monkey | programming | Monkey | Da verificare | Da verificare |
| #444 | Monkey C | programming | Monkey C | Da verificare | Da verificare |
| #445 | Moocode | programming | Moocode | Da verificare | Da verificare |
| #446 | MoonBit | programming | MoonBit | Verificata | Verificata |
| #447 | MoonScript | programming | MoonScript | Verificata | Verificata |
| #448 | Motoko | programming | Motoko | Verificata | Verificata |
| #449 | Motorola 68K Assembly | programming | Assembly | Verificata | Da verificare |
| #450 | Move | programming | Move | Da verificare | Da verificare |
| #452 | Mustache | markup | Mustache | Verificata | Verificata |
| #453 | Myghty | programming | Myghty | Da verificare | Da verificare |
| #454 | NASL | programming | NASL | Da verificare | Da verificare |
| #455 | NCL | programming | NCL | Da verificare | Da verificare |
| #458 | NMODL | programming | NMODL | Verificata | Da verificare |
| #460 | NSIS | programming | NSIS | Verificata | Da verificare |
| #461 | NWScript | programming | NWScript | Da verificare | Da verificare |
| #462 | Nasal | programming | Nasal | Da verificare | Da verificare |
| #463 | Nearley | programming | Nearley | Verificata | Verificata |
| #464 | Nemerle | programming | Nemerle | Da verificare | Da verificare |
| #465 | NetLinx | programming | NetLinx | Da verificare | Da verificare |
| #466 | NetLinx+ERB | programming | NetLinx+ERB | Verificata | Da verificare |
| #467 | NetLogo | programming | NetLogo | Da verificare | Da verificare |
| #468 | NewLisp | programming | NewLisp | Verificata | Verificata |
| #469 | Nextflow | programming | Nextflow | Da verificare | Da verificare |
| #471 | Nickel | programming | Nickel | Verificata | Verificata |
| #472 | Nim | programming | Nim | Verificata | Verificata |
| #474 | Nit | programming | Nit | Da verificare | Da verificare |
| #475 | Nix | programming | Nix | Da verificare | Da verificare |
| #476 | Noir | programming | Noir | Da verificare | Da verificare |
| #477 | Nu | programming | Nu | Da verificare | Da verificare |
| #478 | NumPy | programming | Python | Verificata | Verificata |
| #479 | Nunjucks | markup | Nunjucks | Verificata | Verificata |
| #480 | Nushell | programming | Nushell | Verificata | Verificata |
| #485 | OCaml | programming | OCaml | Verificata | Verificata |
| #486 | OMNeT++ MSG | programming | OMNeT++ MSG | Da verificare | Da verificare |
| #487 | OMNeT++ NED | programming | OMNeT++ NED | Da verificare | Da verificare |
| #488 | Oberon | programming | Oberon | Da verificare | Da verificare |
| #491 | ObjectScript | programming | ObjectScript | Da verificare | Da verificare |
| #492 | Objective-C | programming | Objective-C | Verificata | Verificata |
| #493 | Objective-C++ | programming | Objective-C++ | Verificata | Verificata |
| #494 | Objective-J | programming | Objective-J | Verificata | Da verificare |
| #495 | Odin | programming | Odin | Verificata | Verificata |
| #496 | Omgrofl | programming | Omgrofl | Verificata | Verificata |
| #497 | Opa | programming | Opa | Da verificare | Da verificare |
| #498 | Opal | programming | Opal | Da verificare | Da verificare |
| #499 | Open Policy Agent | programming | Open Policy Agent | Verificata | Verificata |
| #502 | OpenCL | programming | C | Verificata | Da verificare |
| #503 | OpenEdge ABL | programming | OpenEdge ABL | Da verificare | Da verificare |
| #504 | OpenQASM | programming | OpenQASM | Verificata | Verificata |
| #505 | OpenRC runscript | programming | Shell | Verificata | Da verificare |
| #506 | OpenSCAD | programming | OpenSCAD | Da verificare | Da verificare |
| #511 | OverPy | programming | OverPy | Da verificare | Da verificare |
| #512 | OverpassQL | programming | OverpassQL | Da verificare | Da verificare |
| #513 | Ox | programming | Ox | Da verificare | Da verificare |
| #514 | Oxygene | programming | Oxygene | Da verificare | Da verificare |
| #515 | Oz | programming | Oz | Da verificare | Da verificare |
| #516 | P4 | programming | P4 | Da verificare | Da verificare |
| #517 | PDDL | programming | PDDL | Verificata | Verificata |
| #518 | PEG.js | programming | PEG.js | Verificata | Verificata |
| #519 | PHP | programming | PHP | Verificata | Verificata |
| #520 | PLSQL | programming | PLSQL | Da verificare | Da verificare |
| #521 | PLpgSQL | programming | PLpgSQL | Verificata | Verificata |
| #522 | POV-Ray SDL | programming | POV-Ray SDL | Verificata | Verificata |
| #523 | Pact | programming | Pact | Da verificare | Da verificare |
| #524 | Pan | programming | Pan | Verificata | Verificata |
| #525 | Papyrus | programming | Papyrus | Da verificare | Da verificare |
| #526 | Parrot | programming | Parrot | Da verificare | Da verificare |
| #527 | Parrot Assembly | programming | Parrot | Da verificare | Da verificare |
| #528 | Parrot Internal Representation | programming | Parrot | Da verificare | Da verificare |
| #529 | Pascal | programming | Pascal | Verificata | Verificata |
| #530 | Pawn | programming | Pawn | Da verificare | Da verificare |
| #531 | Pep8 | programming | Pep8 | Da verificare | Da verificare |
| #532 | Perl | programming | Perl | Verificata | Verificata |
| #533 | Pic | markup | Roff | Verificata | Verificata |
| #535 | PicoLisp | programming | PicoLisp | Verificata | Verificata |
| #536 | PigLatin | programming | PigLatin | Da verificare | Da verificare |
| #537 | Pike | programming | Pike | Verificata | Verificata |
| #539 | Pkl | programming | Pkl | Verificata | Verificata |
| #543 | PogoScript | programming | PogoScript | Verificata | Verificata |
| #544 | Polar | programming | Polar | Verificata | Verificata |
| #545 | Pony | programming | Pony | Da verificare | Da verificare |
| #546 | Portugol | programming | Portugol | Da verificare | Da verificare |
| #547 | PostCSS | markup | CSS | Verificata | Verificata |
| #548 | PostScript | markup | PostScript | Verificata | Verificata |
| #549 | Power Query | programming | Power Query | Da verificare | Da verificare |
| #550 | PowerBuilder | programming | PowerBuilder | Da verificare | Da verificare |
| #551 | PowerShell | programming | PowerShell | Verificata | Verificata |
| #552 | Praat | programming | Praat | Verificata | Verificata |
| #554 | Pro*C | programming | Pro*C | Da verificare | Da verificare |
| #555 | Processing | programming | Processing | Da verificare | Da verificare |
| #556 | Procfile | programming | Procfile | Verificata | Verificata |
| #558 | Prolog | programming | Prolog | Verificata | Verificata |
| #559 | Promela | programming | Promela | Verificata | Verificata |
| #560 | Propeller Spin | programming | Propeller Spin | Verificata | Da verificare |
| #564 | Pug | markup | Pug | Verificata | Verificata |
| #565 | Puppet | programming | Puppet | Da verificare | Da verificare |
| #567 | PureBasic | programming | PureBasic | Da verificare | Da verificare |
| #568 | PureScript | programming | PureScript | Da verificare | Da verificare |
| #569 | Pyret | programming | Pyret | Da verificare | Da verificare |
| #570 | Python | programming | Python | Verificata | Verificata |
| #571 | Python console | programming | Python | Verificata | Verificata |
| #573 | Q# | programming | Q# | Da verificare | Da verificare |
| #574 | QML | programming | QML | Da verificare | Da verificare |
| #575 | QMake | programming | QMake | Da verificare | Da verificare |
| #576 | Qt Script | programming | Qt Script | Da verificare | Da verificare |
| #577 | Quake | programming | Quake | Da verificare | Da verificare |
| #578 | QuakeC | programming | QuakeC | Verificata | Da verificare |
| #580 | QuickBASIC | programming | QuickBASIC | Da verificare | Da verificare |
| #581 | Quint | programming | Quint | Verificata | Verificata |
| #582 | R | programming | R | Verificata | Verificata |
| #583 | RAML | markup | RAML | Verificata | Verificata |
| #584 | RAScript | programming | RAScript | Da verificare | Da verificare |
| #587 | REALbasic | programming | REALbasic | Da verificare | Da verificare |
| #588 | REXX | programming | REXX | Verificata | Verificata |
| #592 | RPC | programming | RPC | Verificata | Verificata |
| #593 | RPGLE | programming | RPGLE | Da verificare | Da verificare |
| #595 | RUNOFF | markup | RUNOFF | Da verificare | Da verificare |
| #596 | Racket | programming | Racket | Verificata | Verificata |
| #597 | Ragel | programming | Ragel | Verificata | Verificata |
| #598 | Raku | programming | Raku | Verificata | Verificata |
| #599 | Rascal | programming | Rascal | Da verificare | Da verificare |
| #601 | ReScript | programming | ReScript | Verificata | Verificata |
| #603 | Reason | programming | Reason | Verificata | Verificata |
| #604 | ReasonLIGO | programming | LigoLANG | Da verificare | Da verificare |
| #605 | Rebol | programming | Rebol | Verificata | Verificata |
| #607 | Red | programming | Red | Da verificare | Da verificare |
| #608 | Redcode | programming | Redcode | Da verificare | Da verificare |
| #610 | Redscript | programming | Redscript | Da verificare | Da verificare |
| #612 | Ren'Py | programming | Ren'Py | Da verificare | Da verificare |
| #613 | RenderScript | programming | RenderScript | Da verificare | Da verificare |
| #614 | Rez | programming | Rez | Da verificare | Da verificare |
| #615 | Rhai | programming | Rhai | Verificata | Verificata |
| #616 | Rich Text Format | markup | Rich Text Format | Verificata | Verificata |
| #617 | Ring | programming | Ring | Da verificare | Da verificare |
| #618 | Riot | markup | Riot | Verificata | Verificata |
| #619 | RobotFramework | programming | RobotFramework | Verificata | Verificata |
| #621 | Roc | programming | Roc | Da verificare | Da verificare |
| #622 | Rocq Prover | programming | Rocq Prover | Verificata | Verificata |
| #623 | Roff | markup | Roff | Verificata | Verificata |
| #624 | Roff Manpage | markup | Roff | Verificata | Verificata |
| #625 | Rouge | programming | Rouge | Verificata | Verificata |
| #626 | RouterOS Script | programming | RouterOS Script | Da verificare | Da verificare |
| #627 | Ruby | programming | Ruby | Verificata | Verificata |
| #628 | Rust | programming | Rust | Verificata | Verificata |
| #629 | SAS | programming | SAS | Da verificare | Da verificare |
| #630 | SCSS | markup | SCSS | Verificata | Verificata |
| #632 | SIP | programming | SIP | Verificata | Da verificare |
| #633 | SMT | programming | SMT | Verificata | Verificata |
| #635 | SQF | programming | SQF | Da verificare | Da verificare |
| #637 | SQLPL | programming | SQLPL | Da verificare | Da verificare |
| #638 | SRecode Template | markup | SRecode Template | Da verificare | Da verificare |
| #644 | SWIG | programming | SWIG | Verificata | Verificata |
| #645 | Sage | programming | Sage | Da verificare | Da verificare |
| #646 | Sail | programming | Sail | Da verificare | Da verificare |
| #647 | Salt | programming | Salt | Da verificare | Da verificare |
| #648 | Sass | markup | Sass | Verificata | Verificata |
| #649 | Scala | programming | Scala | Verificata | Verificata |
| #650 | Scaml | markup | Scaml | Da verificare | Da verificare |
| #651 | Scenic | programming | Scenic | Da verificare | Da verificare |
| #652 | Scheme | programming | Scheme | Verificata | Verificata |
| #653 | Scilab | programming | Scilab | Da verificare | Da verificare |
| #654 | Self | programming | Self | Da verificare | Da verificare |
| #655 | ShaderLab | programming | ShaderLab | Da verificare | Da verificare |
| #656 | Shell | programming | Shell | Verificata | Verificata |
| #658 | ShellSession | programming | ShellSession | Verificata | Verificata |
| #659 | Shen | programming | Shen | Da verificare | Da verificare |
| #660 | Sieve | programming | Sieve | Da verificare | Da verificare |
| #662 | Singularity | programming | Singularity | Da verificare | Da verificare |
| #663 | Slang | programming | Slang | Verificata | Da verificare |
| #664 | Slash | programming | Slash | Da verificare | Da verificare |
| #665 | Slice | programming | Slice | Da verificare | Da verificare |
| #666 | Slim | markup | Slim | Verificata | Verificata |
| #667 | Slint | markup | Slint | Da verificare | Da verificare |
| #668 | SmPL | programming | SmPL | Verificata | Verificata |
| #669 | Smali | programming | Smali | Da verificare | Da verificare |
| #670 | Smalltalk | programming | Smalltalk | Da verificare | Da verificare |
| #671 | Smarty | programming | Smarty | Verificata | Verificata |
| #672 | Smithy | programming | Smithy | Verificata | Verificata |
| #673 | Snakemake | programming | Python | Verificata | Verificata |
| #674 | Solidity | programming | Solidity | Verificata | Verificata |
| #676 | SourcePawn | programming | SourcePawn | Da verificare | Da verificare |
| #679 | Squirrel | programming | Squirrel | Verificata | Verificata |
| #680 | Stan | programming | Stan | Da verificare | Da verificare |
| #681 | Standard ML | programming | Standard ML | Verificata | Verificata |
| #682 | Starlark | programming | Starlark | Verificata | Verificata |
| #683 | Stata | programming | Stata | Da verificare | Da verificare |
| #684 | StringTemplate | markup | StringTemplate | Verificata | Verificata |
| #685 | Stylus | markup | Stylus | Verificata | Verificata |
| #687 | SugarSS | markup | SugarSS | Verificata | Verificata |
| #688 | SuperCollider | programming | SuperCollider | Da verificare | Da verificare |
| #689 | SurrealQL | programming | SurrealQL | Da verificare | Da verificare |
| #691 | Svelte | markup | Svelte | Verificata | Verificata |
| #692 | Sway | programming | Sway | Da verificare | Da verificare |
| #694 | Swift | programming | Swift | Da verificare | Da verificare |
| #695 | SystemVerilog | programming | SystemVerilog | Verificata | Verificata |
| #696 | TI Program | programming | TI Program | Da verificare | Da verificare |
| #697 | TL-Verilog | programming | TL-Verilog | Da verificare | Da verificare |
| #698 | TLA | programming | TLA | Verificata | Verificata |
| #702 | TSQL | programming | TSQL | Da verificare | Da verificare |
| #704 | TSX | programming | TypeScript | Verificata | Verificata |
| #705 | TXL | programming | TXL | Da verificare | Da verificare |
| #706 | Tact | programming | Tact | Verificata | Da verificare |
| #707 | Talon | programming | Talon | Da verificare | Da verificare |
| #708 | Tape | programming | Tape | Verificata | Da verificare |
| #709 | Tcl | programming | Tcl | Verificata | Verificata |
| #710 | Tcsh | programming | Shell | Verificata | Verificata |
| #711 | TeX | markup | TeX | Verificata | Verificata |
| #712 | Tea | markup | Tea | Da verificare | Da verificare |
| #713 | Teal | programming | Teal | Verificata | Verificata |
| #714 | Terra | programming | Terra | Da verificare | Da verificare |
| #715 | Terraform Template | markup | HCL | Verificata | Verificata |
| #721 | Thrift | programming | Thrift | Verificata | Verificata |
| #722 | Toit | programming | Toit | Da verificare | Da verificare |
| #723 | Tolk | programming | Tolk | Verificata | Da verificare |
| #725 | Tree-sitter Query | programming | Tree-sitter Query | Verificata | Verificata |
| #726 | Turing | programming | Turing | Da verificare | Da verificare |
| #728 | Twig | markup | Twig | Da verificare | Da verificare |
| #730 | TypeScript | programming | TypeScript | Verificata | Verificata |
| #731 | TypeSpec | programming | TypeSpec | Verificata | Verificata |
| #732 | Typst | programming | Typst | Verificata | Verificata |
| #733 | Unified Parallel C | programming | C | Da verificare | Da verificare |
| #735 | Unix Assembly | programming | Assembly | Verificata | Verificata |
| #736 | Uno | programming | Uno | Da verificare | Da verificare |
| #737 | UnrealScript | programming | UnrealScript | Da verificare | Da verificare |
| #738 | Untyped Plutus Core | programming | Untyped Plutus Core | Da verificare | Da verificare |
| #739 | UrWeb | programming | UrWeb | Da verificare | Da verificare |
| #740 | V | programming | V | Da verificare | Da verificare |
| #741 | VBA | programming | VBA | Da verificare | Da verificare |
| #742 | VBScript | programming | VBScript | Verificata | Verificata |
| #743 | VCL | programming | VCL | Da verificare | Da verificare |
| #744 | VHDL | programming | VHDL | Verificata | Verificata |
| #745 | Vala | programming | Vala | Verificata | Verificata |
| #747 | Velocity Template Language | markup | Velocity Template Language | Verificata | Verificata |
| #748 | Vento | markup | Vento | Verificata | Verificata |
| #749 | Verilog | programming | Verilog | Verificata | Verificata |
| #750 | Verse | programming | Verse | Da verificare | Da verificare |
| #753 | Vim Snippet | markup | Vim Snippet | Da verificare | Da verificare |
| #754 | Vim script | programming | Vim script | Verificata | Verificata |
| #755 | Visual Basic .NET | programming | Visual Basic .NET | Verificata | Verificata |
| #756 | Visual Basic 6.0 | programming | Visual Basic 6.0 | Da verificare | Da verificare |
| #757 | Volt | programming | Volt | Da verificare | Da verificare |
| #758 | Vue | markup | Vue | Verificata | Verificata |
| #759 | Vyper | programming | Vyper | Verificata | Verificata |
| #760 | WDL | programming | WDL | Verificata | Da verificare |
| #761 | WGSL | programming | WGSL | Verificata | Da verificare |
| #765 | WebAssembly | programming | WebAssembly | Verificata | Verificata |
| #767 | WebIDL | programming | WebIDL | Verificata | Verificata |
| #770 | Whiley | programming | Whiley | Da verificare | Da verificare |
| #774 | Witcher Script | programming | Witcher Script | Da verificare | Da verificare |
| #775 | Wolfram Language | programming | Wolfram Language | Verificata | Verificata |
| #776 | Wollok | programming | Wollok | Verificata | Verificata |
| #778 | Wren | programming | Wren | Verificata | Verificata |
| #782 | X10 | programming | X10 | Da verificare | Da verificare |
| #783 | XC | programming | XC | Da verificare | Da verificare |
| #788 | XProc | programming | XProc | Da verificare | Da verificare |
| #789 | XQuery | programming | XQuery | Verificata | Verificata |
| #790 | XS | programming | XS | Verificata | Verificata |
| #791 | XSLT | programming | XSLT | Verificata | Verificata |
| #792 | Xmake | programming | Xmake | Verificata | Verificata |
| #793 | Xojo | programming | Xojo | Da verificare | Da verificare |
| #794 | Xonsh | programming | Xonsh | Verificata | Verificata |
| #795 | Xtend | programming | Xtend | Da verificare | Da verificare |
| #798 | YARA | programming | YARA | Verificata | Verificata |
| #799 | YASnippet | markup | YASnippet | Da verificare | Da verificare |
| #800 | Yacc | programming | Yacc | Verificata | Verificata |
| #801 | Yul | programming | Yul | Verificata | Da verificare |
| #802 | ZAP | programming | ZAP | Verificata | Verificata |
| #803 | ZIL | programming | ZIL | Verificata | Verificata |
| #804 | Zeek | programming | Zeek | Da verificare | Da verificare |
| #805 | ZenScript | programming | ZenScript | Da verificare | Da verificare |
| #806 | Zephir | programming | Zephir | Da verificare | Da verificare |
| #807 | Zig | programming | Zig | Verificata | Verificata |
| #808 | Zimpl | programming | Zimpl | Da verificare | Da verificare |
| #814 | eC | programming | eC | Da verificare | Da verificare |
| #816 | fish | programming | Shell | Verificata | Verificata |
| #817 | hoon | programming | hoon | Da verificare | Da verificare |
| #819 | jq | programming | jq | Verificata | Verificata |
| #820 | kvlang | markup | kvlang | Verificata | Da verificare |
| #821 | mIRC Script | programming | mIRC Script | Da verificare | Da verificare |
| #822 | mcfunction | programming | mcfunction | Da verificare | Da verificare |
| #823 | mdsvex | markup | mdsvex | Verificata | Verificata |
| #824 | mupad | programming | mupad | Da verificare | Da verificare |
| #826 | nesC | programming | nesC | Da verificare | Da verificare |
| #827 | ooc | programming | ooc | Da verificare | Da verificare |
| #829 | q | programming | q | Da verificare | Da verificare |
| #831 | sed | programming | sed | Verificata | Verificata |
| #832 | templ | markup | templ | Verificata | Verificata |
| #833 | ucode | programming | ucode | Verificata | Verificata |
| #835 | wisp | programming | wisp | Verificata | Verificata |
| #836 | xBase | programming | xBase | Da verificare | Da verificare |
