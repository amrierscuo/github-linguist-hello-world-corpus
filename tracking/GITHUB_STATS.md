# GitHub language statistics goals

The main goal is to maximize the languages correctly recognized in the repository's examples. The 836 catalog entries represent the entire YAML snapshot. The GitHub Languages bar counts a different set of names.

Canonical reference SHA-256: `183243e30496ba53f5f8743b0e39c9f0e0bccc5a32639f7b541cc2285db0e043`.

Local analysis timestamp: `2026-10-08T22:04:25.589921+00:00`.

| YAML type | Entries | Default participation in statistics |
| --- | ---: | --- |
| programming | 563 | Candidates |
| markup | 71 | Candidates |
| data | 184 | Excluded |
| prose | 18 | Excluded |

The 634 candidate entries aggregate into 578 group names in this snapshot. The `group` field groups dialects or variants under their parent language. These are theoretical targets. Actual recognition depends on the files, exclusions, binary formats and the Linguist version deployed by GitHub.

GitHub's compact bar groups less represented languages under `Other`. The repository's Languages API returns the full list of detected languages and byte counts.

Percentages depend on detected bytes. The number of files, folders, logos or programs does not determine the percentages. A file extension alone does not establish that GitHub recognized the file correctly.

At this historical checkpoint, `.gitattributes` excluded references, trackers, corpus tools, documentation and verification logs from the statistics. The rule `/examples/** linguist-documentation=false` treated the samples as repository source, overriding the default documentation classification of `examples/`. This private export excluded the logos and HTML catalog, and GitHub Pages was disabled.
Data and prose retained their default behavior. No `linguist-language` overrides had been applied to examples at this checkpoint.

The recorded syntax and semantic checks concern the samples' toolchains. GitHub recognition is a separate observation. While the repository was private, the Languages API detected **569 languages** and **259622 bytes** at commit `05dfed82885e7a03369f8d1b8a30a84831cf1e70`. The [full baseline](github_languages_baseline.json) preserves the results before the Lean experiment, including the 375 bytes attributed to Lean.

Of the 634 candidate entries, 352 had syntax verified and 313 had semantics verified at this checkpoint. For this goal, the remaining candidate checks take priority over data and prose formats.

Primary sources: [how Linguist works](https://github.com/github-linguist/linguist/blob/main/docs/how-linguist-works.md), [attributes](https://github.com/github-linguist/linguist/blob/main/docs/overrides.md#detectable), [groups](https://github.com/github-linguist/linguist/blob/5fbdfcb8133be2bed88bf3ce62b2335f50474525/lib/linguist/repository.rb#L182), [Languages API](https://docs.github.com/en/rest/repos/repos#list-repository-languages). Public example of the bar with `Other`: [RosettaCodeData](https://github.com/acmeism/RosettaCodeData).

## Candidate entries

| Number | Canonical name | Type | Group name in statistics | Syntax | Semantics |
| ---: | --- | --- | --- | --- | --- |
| #001 | 1C Enterprise | programming | 1C Enterprise | Verified | Verified |
| #003 | 4D | programming | 4D | Pending | Pending |
| #004 | ABAP | programming | ABAP | Verified | Pending |
| #005 | ABAP CDS | programming | ABAP CDS | Verified | Pending |
| #007 | AGS Script | programming | AGS Script | Pending | Pending |
| #008 | AIDL | programming | AIDL | Pending | Pending |
| #009 | AL | programming | AL | Pending | Pending |
| #010 | ALGOL | programming | ALGOL | Pending | Pending |
| #011 | AMPL | programming | AMPL | Verified | Verified |
| #012 | ANTLR | programming | ANTLR | Verified | Verified |
| #013 | API Blueprint | markup | API Blueprint | Verified | Verified |
| #014 | APL | programming | APL | Verified | Verified |
| #015 | ASL | programming | ASL | Verified | Verified |
| #017 | ASP.NET | programming | ASP.NET | Verified | Verified |
| #018 | ATS | programming | ATS | Pending | Pending |
| #019 | ActionScript | programming | ActionScript | Pending | Pending |
| #020 | Ada | programming | Ada | Pending | Pending |
| #023 | Agda | programming | Agda | Pending | Pending |
| #024 | Aiken | programming | Aiken | Verified | Verified |
| #025 | Aleo | programming | Aleo | Verified | Pending |
| #026 | Alloy | programming | Alloy | Verified | Verified |
| #027 | Alpine Abuild | programming | Shell | Pending | Pending |
| #029 | AngelScript | programming | AngelScript | Verified | Verified |
| #030 | Answer Set Programming | programming | Answer Set Programming | Verified | Verified |
| #032 | Antlers | markup | Antlers | Pending | Pending |
| #034 | Apex | programming | Apex | Verified | Pending |
| #035 | Apollo Guidance Computer | programming | Assembly | Verified | Pending |
| #036 | AppleScript | programming | AppleScript | Pending | Pending |
| #037 | Arc | programming | Arc | Verified | Verified |
| #038 | ArkTS | programming | ArkTS | Pending | Pending |
| #040 | AspectJ | programming | AspectJ | Verified | Verified |
| #041 | Assembly | programming | Assembly | Verified | Verified |
| #042 | Astro | markup | Astro | Verified | Pending |
| #043 | Asymptote | programming | Asymptote | Pending | Pending |
| #044 | Augeas | programming | Augeas | Verified | Verified |
| #045 | AutoHotkey | programming | AutoHotkey | Verified | Verified |
| #046 | AutoIt | programming | AutoIt | Verified | Verified |
| #048 | Awk | programming | Awk | Verified | Verified |
| #049 | B | programming | B | Pending | Pending |
| #050 | B (Formal Method) | programming | B (Formal Method) | Pending | Pending |
| #051 | B4X | programming | B4X | Pending | Pending |
| #052 | BAML | programming | BAML | Verified | Pending |
| #053 | BASIC | programming | BASIC | Verified | Verified |
| #054 | BBCode | markup | BBCode | Verified | Verified |
| #056 | BQN | programming | BQN | Verified | Verified |
| #057 | Ballerina | programming | Ballerina | Pending | Pending |
| #058 | Batchfile | programming | Batchfile | Verified | Verified |
| #059 | Beef | programming | Beef | Pending | Pending |
| #060 | Befunge | programming | Befunge | Verified | Verified |
| #061 | Bend | programming | Bend | Verified | Verified |
| #062 | Berry | programming | Berry | Verified | Verified |
| #063 | BibTeX | markup | TeX | Verified | Verified |
| #064 | BibTeX Style | programming | BibTeX Style | Verified | Verified |
| #065 | Bicep | programming | Bicep | Verified | Verified |
| #066 | Bikeshed | markup | Bikeshed | Pending | Pending |
| #067 | Bison | programming | Yacc | Verified | Verified |
| #068 | BitBake | programming | BitBake | Pending | Pending |
| #069 | Blade | markup | Blade | Pending | Pending |
| #070 | BlitzBasic | programming | BlitzBasic | Pending | Pending |
| #071 | BlitzMax | programming | BlitzMax | Pending | Pending |
| #072 | Blueprint | markup | Blueprint | Pending | Pending |
| #073 | Bluespec | programming | Bluespec | Verified | Verified |
| #074 | Bluespec BH | programming | Bluespec | Verified | Verified |
| #075 | Boo | programming | Boo | Pending | Pending |
| #076 | Boogie | programming | Boogie | Verified | Verified |
| #077 | Brainfuck | programming | Brainfuck | Verified | Verified |
| #078 | BrighterScript | programming | BrighterScript | Verified | Verified |
| #079 | Brightscript | programming | Brightscript | Verified | Verified |
| #081 | Bru | markup | Bru | Verified | Verified |
| #083 | C | programming | C | Verified | Verified |
| #084 | C# | programming | C# | Verified | Verified |
| #085 | C++ | programming | C++ | Verified | Verified |
| #087 | C2hs Haskell | programming | Haskell | Verified | Pending |
| #088 | C3 | programming | C3 | Verified | Verified |
| #089 | CAP CDS | programming | CAP CDS | Verified | Verified |
| #091 | CLIPS | programming | CLIPS | Verified | Verified |
| #092 | CMake | programming | CMake | Verified | Verified |
| #093 | COBOL | programming | COBOL | Verified | Verified |
| #096 | CQL | programming | CQL | Pending | Pending |
| #098 | CSS | markup | CSS | Verified | Verified |
| #100 | CUE | programming | CUE | Verified | Verified |
| #101 | CWeb | programming | CWeb | Verified | Verified |
| #104 | Cadence | programming | Cadence | Pending | Pending |
| #105 | Cairo | programming | Cairo | Pending | Pending |
| #106 | Cairo Zero | programming | Cairo | Pending | Pending |
| #107 | CameLIGO | programming | LigoLANG | Pending | Pending |
| #108 | Cangjie | programming | Cangjie | Pending | Pending |
| #109 | Cap'n Proto | programming | Cap'n Proto | Verified | Verified |
| #110 | Carbon | programming | Carbon | Pending | Pending |
| #111 | CartoCSS | programming | CartoCSS | Verified | Verified |
| #112 | Ceylon | programming | Ceylon | Pending | Pending |
| #113 | Chapel | programming | Chapel | Pending | Pending |
| #114 | Charity | programming | Charity | Pending | Pending |
| #116 | ChucK | programming | ChucK | Pending | Pending |
| #117 | Circom | programming | Circom | Verified | Verified |
| #118 | Cirru | programming | Cirru | Verified | Verified |
| #119 | Clarion | programming | Clarion | Pending | Pending |
| #120 | Clarity | programming | Clarity | Verified | Verified |
| #121 | Classic ASP | programming | Classic ASP | Pending | Pending |
| #122 | Clean | programming | Clean | Verified | Verified |
| #123 | Click | programming | Click | Pending | Pending |
| #124 | Clojure | programming | Clojure | Verified | Verified |
| #125 | Closure Templates | markup | Closure Templates | Verified | Verified |
| #127 | Clue | programming | Clue | Verified | Verified |
| #129 | CodeQL | programming | CodeQL | Pending | Pending |
| #130 | CoffeeScript | programming | CoffeeScript | Verified | Verified |
| #131 | ColdFusion | programming | ColdFusion | Pending | Pending |
| #132 | ColdFusion CFC | programming | ColdFusion | Pending | Pending |
| #133 | Common Lisp | programming | Common Lisp | Verified | Verified |
| #134 | Common Workflow Language | programming | Common Workflow Language | Pending | Pending |
| #135 | Component Pascal | programming | Component Pascal | Pending | Pending |
| #136 | Cooklang | markup | Cooklang | Verified | Verified |
| #137 | Cool | programming | Cool | Pending | Pending |
| #140 | Crystal | programming | Crystal | Pending | Pending |
| #141 | Csound | programming | Csound | Verified | Verified |
| #142 | Csound Document | programming | Csound Document | Verified | Verified |
| #143 | Csound Score | programming | Csound Score | Verified | Verified |
| #144 | Cuda | programming | Cuda | Pending | Pending |
| #146 | Curry | programming | Curry | Pending | Pending |
| #147 | Cycript | programming | Cycript | Pending | Pending |
| #149 | Cypher | programming | Cypher | Verified | Verified |
| #150 | Cython | programming | Cython | Verified | Verified |
| #151 | D | programming | D | Verified | Verified |
| #153 | D2 | markup | D2 | Verified | Verified |
| #154 | DIGITAL Command Language | programming | DIGITAL Command Language | Pending | Pending |
| #155 | DM | programming | DM | Pending | Pending |
| #157 | DTrace | programming | DTrace | Pending | Pending |
| #158 | Dafny | programming | Dafny | Verified | Verified |
| #160 | Dart | programming | Dart | Verified | Verified |
| #161 | Daslang | programming | Daslang | Verified | Verified |
| #162 | DataWeave | programming | DataWeave | Verified | Verified |
| #164 | DenizenScript | programming | DenizenScript | Pending | Pending |
| #165 | Dhall | programming | Dhall | Verified | Verified |
| #168 | Dockerfile | programming | Dockerfile | Verified | Pending |
| #169 | Dogescript | programming | Dogescript | Verified | Verified |
| #171 | Dune | programming | Dune | Verified | Verified |
| #172 | Dylan | programming | Dylan | Pending | Pending |
| #173 | E | programming | E | Pending | Pending |
| #176 | ECL | programming | ECL | Pending | Pending |
| #177 | ECLiPSe | programming | Prolog | Verified | Verified |
| #178 | EJS | markup | EJS | Verified | Verified |
| #179 | EQ | programming | EQ | Pending | Pending |
| #181 | Earthly | programming | Earthly | Pending | Pending |
| #184 | Ecmarkup | markup | HTML | Verified | Verified |
| #185 | Edge | markup | Edge | Verified | Verified |
| #186 | EdgeQL | programming | EdgeQL | Pending | Pending |
| #189 | Eiffel | programming | Eiffel | Pending | Pending |
| #190 | Elixir | programming | Elixir | Verified | Verified |
| #191 | Elm | programming | Elm | Pending | Pending |
| #192 | Elvish | programming | Elvish | Verified | Verified |
| #193 | Elvish Transcript | programming | Elvish | Verified | Verified |
| #194 | Emacs Lisp | programming | Emacs Lisp | Pending | Pending |
| #195 | EmberScript | programming | EmberScript | Verified | Verified |
| #196 | Erlang | programming | Erlang | Verified | Verified |
| #197 | Euphoria | programming | Euphoria | Verified | Verified |
| #198 | F# | programming | F# | Verified | Verified |
| #199 | F* | programming | F* | Pending | Pending |
| #201 | FIRRTL | programming | FIRRTL | Pending | Pending |
| #202 | FLUX | programming | FLUX | Pending | Pending |
| #203 | FPP | programming | FPP | Pending | Pending |
| #204 | Factor | programming | Factor | Pending | Pending |
| #205 | Fancy | programming | Fancy | Pending | Pending |
| #206 | Fantom | programming | Fantom | Verified | Verified |
| #207 | Faust | programming | Faust | Verified | Verified |
| #208 | Fennel | programming | Fennel | Verified | Verified |
| #209 | Filebench WML | programming | Filebench WML | Pending | Pending |
| #210 | Filterscript | programming | RenderScript | Pending | Pending |
| #212 | Flix | programming | Flix | Verified | Verified |
| #213 | Fluent | programming | Fluent | Verified | Verified |
| #215 | Forth | programming | Forth | Verified | Verified |
| #216 | Fortran | programming | Fortran | Verified | Verified |
| #217 | Fortran Free Form | programming | Fortran | Verified | Verified |
| #218 | FreeBASIC | programming | FreeBASIC | Pending | Pending |
| #219 | FreeMarker | programming | FreeMarker | Verified | Verified |
| #220 | Frege | programming | Frege | Verified | Verified |
| #221 | Futhark | programming | Futhark | Verified | Verified |
| #222 | G-code | programming | G-code | Pending | Pending |
| #223 | GAML | programming | GAML | Pending | Pending |
| #224 | GAMS | programming | GAMS | Pending | Pending |
| #225 | GAP | programming | GAP | Verified | Verified |
| #226 | GCC Machine Description | programming | GCC Machine Description | Pending | Pending |
| #227 | GDB | programming | GDB | Verified | Verified |
| #228 | GDScript | programming | GDScript | Verified | Verified |
| #229 | GDShader | programming | GDShader | Verified | Pending |
| #231 | GLSL | programming | GLSL | Verified | Pending |
| #233 | GSC | programming | GSC | Verified | Pending |
| #234 | Game Maker Language | programming | Game Maker Language | Pending | Pending |
| #237 | Genero 4gl | programming | Genero 4gl | Pending | Pending |
| #238 | Genero per | markup | Genero per | Pending | Pending |
| #239 | Genie | programming | Genie | Verified | Verified |
| #240 | Genshi | programming | Genshi | Verified | Verified |
| #241 | Gentoo Ebuild | programming | Shell | Verified | Pending |
| #242 | Gentoo Eclass | programming | Shell | Verified | Pending |
| #245 | Gherkin | programming | Gherkin | Verified | Verified |
| #250 | Gleam | programming | Gleam | Verified | Verified |
| #251 | Glimmer JS | programming | JavaScript | Verified | Pending |
| #252 | Glimmer TS | programming | TypeScript | Verified | Pending |
| #253 | Glyph | programming | Glyph | Pending | Pending |
| #255 | Gno | programming | Gno | Verified | Verified |
| #256 | Gnuplot | programming | Gnuplot | Verified | Verified |
| #257 | Go | programming | Go | Verified | Verified |
| #260 | Go Template | markup | Go Template | Verified | Verified |
| #263 | Golo | programming | Golo | Verified | Verified |
| #264 | Gosu | programming | Gosu | Pending | Pending |
| #265 | Grace | programming | Grace | Pending | Pending |
| #268 | Grammatical Framework | programming | Grammatical Framework | Pending | Pending |
| #272 | Groovy | programming | Groovy | Verified | Verified |
| #273 | Groovy Server Pages | programming | Groovy | Pending | Pending |
| #276 | HCL | programming | HCL | Verified | Verified |
| #277 | HIP | programming | HIP | Pending | Pending |
| #278 | HLSL | programming | HLSL | Verified | Pending |
| #280 | HTML | markup | HTML | Verified | Verified |
| #281 | HTML+ECR | markup | HTML | Verified | Verified |
| #282 | HTML+EEX | markup | HTML | Verified | Verified |
| #283 | HTML+ERB | markup | HTML | Verified | Verified |
| #284 | HTML+PHP | markup | HTML | Verified | Verified |
| #285 | HTML+Razor | markup | HTML | Pending | Pending |
| #288 | Hack | programming | Hack | Pending | Pending |
| #289 | Haml | markup | Haml | Verified | Verified |
| #290 | Handlebars | markup | Handlebars | Verified | Verified |
| #291 | Harbour | programming | Harbour | Pending | Pending |
| #292 | Hare | programming | Hare | Pending | Pending |
| #293 | Haskell | programming | Haskell | Verified | Verified |
| #294 | Haxe | programming | Haxe | Verified | Verified |
| #295 | HiveQL | programming | HiveQL | Verified | Pending |
| #296 | HolyC | programming | HolyC | Pending | Pending |
| #298 | Hurl | programming | Hurl | Verified | Verified |
| #299 | Hy | programming | Hy | Verified | Verified |
| #300 | HyPhy | programming | HyPhy | Verified | Verified |
| #301 | IDL | programming | IDL | Pending | Pending |
| #302 | IGOR Pro | programming | IGOR Pro | Pending | Pending |
| #303 | IL Assembly | programming | IL Assembly | Verified | Verified |
| #306 | ISPC | programming | ISPC | Verified | Verified |
| #307 | Idris | programming | Idris | Pending | Pending |
| #309 | ImHex Pattern Language | programming | ImHex Pattern Language | Pending | Pending |
| #310 | ImageJ Macro | programming | ImageJ Macro | Verified | Verified |
| #311 | Imba | programming | Imba | Verified | Verified |
| #312 | Inform 7 | programming | Inform 7 | Verified | Verified |
| #313 | Ink | programming | Ink | Verified | Verified |
| #314 | Inno Setup | programming | Inno Setup | Pending | Pending |
| #315 | Io | programming | Io | Pending | Pending |
| #316 | Ioke | programming | Ioke | Pending | Pending |
| #317 | Isabelle | programming | Isabelle | Pending | Pending |
| #318 | Isabelle ROOT | programming | Isabelle | Pending | Pending |
| #319 | J | programming | J | Verified | Verified |
| #321 | JASS | programming | JASS | Pending | Pending |
| #322 | JCL | programming | JCL | Pending | Pending |
| #323 | JFlex | programming | Lex | Verified | Verified |
| #328 | JSONiq | programming | JSONiq | Pending | Pending |
| #329 | Jac | programming | Jac | Verified | Verified |
| #330 | Jai | programming | Jai | Pending | Pending |
| #331 | Janet | programming | Janet | Verified | Verified |
| #332 | Jasmin | programming | Jasmin | Verified | Verified |
| #333 | Java | programming | Java | Verified | Verified |
| #335 | Java Server Pages | programming | Java | Verified | Verified |
| #336 | Java Template Engine | programming | Java | Verified | Verified |
| #337 | JavaScript | programming | JavaScript | Verified | Verified |
| #338 | JavaScript+ERB | programming | JavaScript | Verified | Verified |
| #340 | JetBrains MPS | programming | JetBrains MPS | Pending | Pending |
| #341 | Jinja | markup | Jinja | Verified | Verified |
| #342 | Jison | programming | Yacc | Verified | Verified |
| #343 | Jison Lex | programming | Lex | Verified | Verified |
| #344 | Jolie | programming | Jolie | Pending | Pending |
| #345 | Jsonnet | programming | Jsonnet | Verified | Verified |
| #346 | Julia | programming | Julia | Verified | Verified |
| #347 | Julia REPL | programming | Julia | Verified | Verified |
| #348 | Jupyter Notebook | markup | Jupyter Notebook | Verified | Verified |
| #349 | Just | programming | Just | Verified | Verified |
| #350 | KCL | programming | KCL | Verified | Verified |
| #352 | KFramework | programming | KFramework | Pending | Pending |
| #353 | KRL | programming | KRL | Verified | Pending |
| #354 | Kaitai Struct | programming | Kaitai Struct | Verified | Verified |
| #355 | KakouneScript | programming | KakouneScript | Verified | Verified |
| #356 | KerboScript | programming | KerboScript | Pending | Pending |
| #361 | Kit | markup | Kit | Pending | Pending |
| #362 | KoLmafia ASH | programming | KoLmafia ASH | Pending | Pending |
| #363 | Koka | programming | Koka | Verified | Verified |
| #364 | Kotlin | programming | Kotlin | Verified | Verified |
| #366 | LFE | programming | LFE | Verified | Verified |
| #367 | LLVM | programming | LLVM | Verified | Verified |
| #368 | LLVM TableGen | programming | LLVM TableGen | Verified | Verified |
| #369 | LOLCODE | programming | LOLCODE | Verified | Verified |
| #370 | LSL | programming | LSL | Pending | Pending |
| #372 | LabVIEW | programming | LabVIEW | Pending | Pending |
| #373 | Lambdapi | programming | Lambdapi | Pending | Pending |
| #374 | Langium | programming | Langium | Verified | Verified |
| #376 | Lasso | programming | Lasso | Pending | Pending |
| #377 | Latte | markup | Latte | Verified | Verified |
| #378 | Lean | programming | Lean | Verified | Verified |
| #379 | Lean 4 | programming | Lean | Verified | Verified |
| #380 | Leo | programming | Leo | Pending | Pending |
| #381 | Less | markup | Less | Verified | Verified |
| #382 | Lex | programming | Lex | Verified | Verified |
| #383 | LigoLANG | programming | LigoLANG | Pending | Pending |
| #384 | LilyPond | programming | LilyPond | Pending | Pending |
| #385 | Limbo | programming | Limbo | Pending | Pending |
| #386 | Linear Programming | programming | Linear Programming | Verified | Verified |
| #387 | Linker Script | programming | Linker Script | Verified | Verified |
| #389 | Liquid | markup | Liquid | Verified | Verified |
| #390 | Liquidsoap | programming | Liquidsoap | Pending | Pending |
| #391 | Literate Agda | programming | Agda | Pending | Pending |
| #392 | Literate CoffeeScript | programming | CoffeeScript | Verified | Verified |
| #393 | Literate Haskell | programming | Haskell | Verified | Verified |
| #394 | LiveCode Script | programming | LiveCode Script | Pending | Pending |
| #395 | LiveScript | programming | LiveScript | Verified | Verified |
| #396 | Lobster | programming | Lobster | Verified | Verified |
| #397 | Logos | programming | Logos | Verified | Pending |
| #398 | Logtalk | programming | Logtalk | Verified | Verified |
| #399 | LookML | programming | LookML | Verified | Pending |
| #400 | LoomScript | programming | LoomScript | Pending | Pending |
| #401 | Lua | programming | Lua | Verified | Verified |
| #402 | Luau | programming | Luau | Verified | Verified |
| #403 | M | programming | M | Pending | Pending |
| #405 | M4 | programming | M4 | Verified | Verified |
| #406 | M4Sugar | programming | M4 | Verified | Verified |
| #407 | MATLAB | programming | MATLAB | Pending | Pending |
| #408 | MAXScript | programming | MAXScript | Pending | Pending |
| #409 | MDX | markup | MDX | Verified | Verified |
| #410 | MLIR | programming | MLIR | Verified | Verified |
| #411 | MQL4 | programming | MQL4 | Pending | Pending |
| #412 | MQL5 | programming | MQL5 | Pending | Pending |
| #413 | MTML | markup | MTML | Pending | Pending |
| #414 | MUF | programming | Forth | Pending | Pending |
| #415 | Macaulay2 | programming | Macaulay2 | Pending | Pending |
| #416 | Makefile | programming | Makefile | Verified | Verified |
| #417 | Mako | programming | Mako | Verified | Verified |
| #419 | Marko | markup | Marko | Verified | Verified |
| #420 | Mask | markup | Mask | Verified | Verified |
| #421 | Mathematical Programming System | programming | Mathematical Programming System | Verified | Verified |
| #423 | Max | programming | Max | Pending | Pending |
| #424 | MeTTa | programming | MeTTa | Pending | Pending |
| #425 | Mercury | programming | Mercury | Pending | Pending |
| #426 | Mermaid | markup | Mermaid | Verified | Verified |
| #427 | Meson | programming | Meson | Verified | Verified |
| #428 | Metal | programming | Metal | Pending | Pending |
| #431 | MiniD | programming | MiniD | Pending | Pending |
| #432 | MiniScript | programming | MiniScript | Verified | Verified |
| #434 | MiniZinc | programming | MiniZinc | Verified | Verified |
| #436 | Mint | programming | Mint | Pending | Pending |
| #437 | Mirah | programming | Mirah | Pending | Pending |
| #438 | Modelica | programming | Modelica | Pending | Pending |
| #439 | Modula-2 | programming | Modula-2 | Pending | Pending |
| #440 | Modula-3 | programming | Modula-3 | Pending | Pending |
| #441 | Module Management System | programming | Module Management System | Pending | Pending |
| #442 | Mojo | programming | Mojo | Pending | Pending |
| #443 | Monkey | programming | Monkey | Pending | Pending |
| #444 | Monkey C | programming | Monkey C | Pending | Pending |
| #445 | Moocode | programming | Moocode | Pending | Pending |
| #446 | MoonBit | programming | MoonBit | Verified | Verified |
| #447 | MoonScript | programming | MoonScript | Verified | Verified |
| #448 | Motoko | programming | Motoko | Verified | Verified |
| #449 | Motorola 68K Assembly | programming | Assembly | Verified | Pending |
| #450 | Move | programming | Move | Pending | Pending |
| #452 | Mustache | markup | Mustache | Verified | Verified |
| #453 | Myghty | programming | Myghty | Pending | Pending |
| #454 | NASL | programming | NASL | Pending | Pending |
| #455 | NCL | programming | NCL | Pending | Pending |
| #458 | NMODL | programming | NMODL | Verified | Pending |
| #460 | NSIS | programming | NSIS | Verified | Pending |
| #461 | NWScript | programming | NWScript | Pending | Pending |
| #462 | Nasal | programming | Nasal | Pending | Pending |
| #463 | Nearley | programming | Nearley | Verified | Verified |
| #464 | Nemerle | programming | Nemerle | Pending | Pending |
| #465 | NetLinx | programming | NetLinx | Pending | Pending |
| #466 | NetLinx+ERB | programming | NetLinx+ERB | Verified | Pending |
| #467 | NetLogo | programming | NetLogo | Pending | Pending |
| #468 | NewLisp | programming | NewLisp | Verified | Verified |
| #469 | Nextflow | programming | Nextflow | Pending | Pending |
| #471 | Nickel | programming | Nickel | Verified | Verified |
| #472 | Nim | programming | Nim | Verified | Verified |
| #474 | Nit | programming | Nit | Pending | Pending |
| #475 | Nix | programming | Nix | Pending | Pending |
| #476 | Noir | programming | Noir | Pending | Pending |
| #477 | Nu | programming | Nu | Pending | Pending |
| #478 | NumPy | programming | Python | Verified | Verified |
| #479 | Nunjucks | markup | Nunjucks | Verified | Verified |
| #480 | Nushell | programming | Nushell | Verified | Verified |
| #485 | OCaml | programming | OCaml | Verified | Verified |
| #486 | OMNeT++ MSG | programming | OMNeT++ MSG | Pending | Pending |
| #487 | OMNeT++ NED | programming | OMNeT++ NED | Pending | Pending |
| #488 | Oberon | programming | Oberon | Pending | Pending |
| #491 | ObjectScript | programming | ObjectScript | Pending | Pending |
| #492 | Objective-C | programming | Objective-C | Verified | Verified |
| #493 | Objective-C++ | programming | Objective-C++ | Verified | Verified |
| #494 | Objective-J | programming | Objective-J | Verified | Pending |
| #495 | Odin | programming | Odin | Verified | Verified |
| #496 | Omgrofl | programming | Omgrofl | Verified | Verified |
| #497 | Opa | programming | Opa | Pending | Pending |
| #498 | Opal | programming | Opal | Pending | Pending |
| #499 | Open Policy Agent | programming | Open Policy Agent | Verified | Verified |
| #502 | OpenCL | programming | C | Verified | Pending |
| #503 | OpenEdge ABL | programming | OpenEdge ABL | Pending | Pending |
| #504 | OpenQASM | programming | OpenQASM | Verified | Verified |
| #505 | OpenRC runscript | programming | Shell | Verified | Pending |
| #506 | OpenSCAD | programming | OpenSCAD | Pending | Pending |
| #511 | OverPy | programming | OverPy | Pending | Pending |
| #512 | OverpassQL | programming | OverpassQL | Pending | Pending |
| #513 | Ox | programming | Ox | Pending | Pending |
| #514 | Oxygene | programming | Oxygene | Pending | Pending |
| #515 | Oz | programming | Oz | Pending | Pending |
| #516 | P4 | programming | P4 | Pending | Pending |
| #517 | PDDL | programming | PDDL | Verified | Verified |
| #518 | PEG.js | programming | PEG.js | Verified | Verified |
| #519 | PHP | programming | PHP | Verified | Verified |
| #520 | PLSQL | programming | PLSQL | Pending | Pending |
| #521 | PLpgSQL | programming | PLpgSQL | Verified | Verified |
| #522 | POV-Ray SDL | programming | POV-Ray SDL | Verified | Verified |
| #523 | Pact | programming | Pact | Pending | Pending |
| #524 | Pan | programming | Pan | Verified | Verified |
| #525 | Papyrus | programming | Papyrus | Pending | Pending |
| #526 | Parrot | programming | Parrot | Pending | Pending |
| #527 | Parrot Assembly | programming | Parrot | Pending | Pending |
| #528 | Parrot Internal Representation | programming | Parrot | Pending | Pending |
| #529 | Pascal | programming | Pascal | Verified | Verified |
| #530 | Pawn | programming | Pawn | Pending | Pending |
| #531 | Pep8 | programming | Pep8 | Pending | Pending |
| #532 | Perl | programming | Perl | Verified | Verified |
| #533 | Pic | markup | Roff | Verified | Verified |
| #535 | PicoLisp | programming | PicoLisp | Verified | Verified |
| #536 | PigLatin | programming | PigLatin | Pending | Pending |
| #537 | Pike | programming | Pike | Verified | Verified |
| #539 | Pkl | programming | Pkl | Verified | Verified |
| #543 | PogoScript | programming | PogoScript | Verified | Verified |
| #544 | Polar | programming | Polar | Verified | Verified |
| #545 | Pony | programming | Pony | Pending | Pending |
| #546 | Portugol | programming | Portugol | Pending | Pending |
| #547 | PostCSS | markup | CSS | Verified | Verified |
| #548 | PostScript | markup | PostScript | Verified | Verified |
| #549 | Power Query | programming | Power Query | Pending | Pending |
| #550 | PowerBuilder | programming | PowerBuilder | Pending | Pending |
| #551 | PowerShell | programming | PowerShell | Verified | Verified |
| #552 | Praat | programming | Praat | Verified | Verified |
| #554 | Pro*C | programming | Pro*C | Pending | Pending |
| #555 | Processing | programming | Processing | Pending | Pending |
| #556 | Procfile | programming | Procfile | Verified | Verified |
| #558 | Prolog | programming | Prolog | Verified | Verified |
| #559 | Promela | programming | Promela | Verified | Verified |
| #560 | Propeller Spin | programming | Propeller Spin | Verified | Pending |
| #564 | Pug | markup | Pug | Verified | Verified |
| #565 | Puppet | programming | Puppet | Pending | Pending |
| #567 | PureBasic | programming | PureBasic | Pending | Pending |
| #568 | PureScript | programming | PureScript | Pending | Pending |
| #569 | Pyret | programming | Pyret | Pending | Pending |
| #570 | Python | programming | Python | Verified | Verified |
| #571 | Python console | programming | Python | Verified | Verified |
| #573 | Q# | programming | Q# | Pending | Pending |
| #574 | QML | programming | QML | Pending | Pending |
| #575 | QMake | programming | QMake | Pending | Pending |
| #576 | Qt Script | programming | Qt Script | Pending | Pending |
| #577 | Quake | programming | Quake | Pending | Pending |
| #578 | QuakeC | programming | QuakeC | Verified | Pending |
| #580 | QuickBASIC | programming | QuickBASIC | Pending | Pending |
| #581 | Quint | programming | Quint | Verified | Verified |
| #582 | R | programming | R | Verified | Verified |
| #583 | RAML | markup | RAML | Verified | Verified |
| #584 | RAScript | programming | RAScript | Pending | Pending |
| #587 | REALbasic | programming | REALbasic | Pending | Pending |
| #588 | REXX | programming | REXX | Verified | Verified |
| #592 | RPC | programming | RPC | Verified | Verified |
| #593 | RPGLE | programming | RPGLE | Pending | Pending |
| #595 | RUNOFF | markup | RUNOFF | Pending | Pending |
| #596 | Racket | programming | Racket | Verified | Verified |
| #597 | Ragel | programming | Ragel | Verified | Verified |
| #598 | Raku | programming | Raku | Verified | Verified |
| #599 | Rascal | programming | Rascal | Pending | Pending |
| #601 | ReScript | programming | ReScript | Verified | Verified |
| #603 | Reason | programming | Reason | Verified | Verified |
| #604 | ReasonLIGO | programming | LigoLANG | Pending | Pending |
| #605 | Rebol | programming | Rebol | Verified | Verified |
| #607 | Red | programming | Red | Pending | Pending |
| #608 | Redcode | programming | Redcode | Pending | Pending |
| #610 | Redscript | programming | Redscript | Pending | Pending |
| #612 | Ren'Py | programming | Ren'Py | Pending | Pending |
| #613 | RenderScript | programming | RenderScript | Pending | Pending |
| #614 | Rez | programming | Rez | Pending | Pending |
| #615 | Rhai | programming | Rhai | Verified | Verified |
| #616 | Rich Text Format | markup | Rich Text Format | Verified | Verified |
| #617 | Ring | programming | Ring | Pending | Pending |
| #618 | Riot | markup | Riot | Verified | Verified |
| #619 | RobotFramework | programming | RobotFramework | Verified | Verified |
| #621 | Roc | programming | Roc | Pending | Pending |
| #622 | Rocq Prover | programming | Rocq Prover | Verified | Verified |
| #623 | Roff | markup | Roff | Verified | Verified |
| #624 | Roff Manpage | markup | Roff | Verified | Verified |
| #625 | Rouge | programming | Rouge | Verified | Verified |
| #626 | RouterOS Script | programming | RouterOS Script | Pending | Pending |
| #627 | Ruby | programming | Ruby | Verified | Verified |
| #628 | Rust | programming | Rust | Verified | Verified |
| #629 | SAS | programming | SAS | Pending | Pending |
| #630 | SCSS | markup | SCSS | Verified | Verified |
| #632 | SIP | programming | SIP | Verified | Pending |
| #633 | SMT | programming | SMT | Verified | Verified |
| #635 | SQF | programming | SQF | Pending | Pending |
| #637 | SQLPL | programming | SQLPL | Pending | Pending |
| #638 | SRecode Template | markup | SRecode Template | Pending | Pending |
| #644 | SWIG | programming | SWIG | Verified | Verified |
| #645 | Sage | programming | Sage | Pending | Pending |
| #646 | Sail | programming | Sail | Pending | Pending |
| #647 | Salt | programming | Salt | Pending | Pending |
| #648 | Sass | markup | Sass | Verified | Verified |
| #649 | Scala | programming | Scala | Verified | Verified |
| #650 | Scaml | markup | Scaml | Pending | Pending |
| #651 | Scenic | programming | Scenic | Pending | Pending |
| #652 | Scheme | programming | Scheme | Verified | Verified |
| #653 | Scilab | programming | Scilab | Pending | Pending |
| #654 | Self | programming | Self | Pending | Pending |
| #655 | ShaderLab | programming | ShaderLab | Pending | Pending |
| #656 | Shell | programming | Shell | Verified | Verified |
| #658 | ShellSession | programming | ShellSession | Verified | Verified |
| #659 | Shen | programming | Shen | Pending | Pending |
| #660 | Sieve | programming | Sieve | Pending | Pending |
| #662 | Singularity | programming | Singularity | Pending | Pending |
| #663 | Slang | programming | Slang | Verified | Pending |
| #664 | Slash | programming | Slash | Pending | Pending |
| #665 | Slice | programming | Slice | Pending | Pending |
| #666 | Slim | markup | Slim | Verified | Verified |
| #667 | Slint | markup | Slint | Pending | Pending |
| #668 | SmPL | programming | SmPL | Verified | Verified |
| #669 | Smali | programming | Smali | Pending | Pending |
| #670 | Smalltalk | programming | Smalltalk | Pending | Pending |
| #671 | Smarty | programming | Smarty | Verified | Verified |
| #672 | Smithy | programming | Smithy | Verified | Verified |
| #673 | Snakemake | programming | Python | Verified | Verified |
| #674 | Solidity | programming | Solidity | Verified | Verified |
| #676 | SourcePawn | programming | SourcePawn | Pending | Pending |
| #679 | Squirrel | programming | Squirrel | Verified | Verified |
| #680 | Stan | programming | Stan | Pending | Pending |
| #681 | Standard ML | programming | Standard ML | Verified | Verified |
| #682 | Starlark | programming | Starlark | Verified | Verified |
| #683 | Stata | programming | Stata | Pending | Pending |
| #684 | StringTemplate | markup | StringTemplate | Verified | Verified |
| #685 | Stylus | markup | Stylus | Verified | Verified |
| #687 | SugarSS | markup | SugarSS | Verified | Verified |
| #688 | SuperCollider | programming | SuperCollider | Pending | Pending |
| #689 | SurrealQL | programming | SurrealQL | Pending | Pending |
| #691 | Svelte | markup | Svelte | Verified | Verified |
| #692 | Sway | programming | Sway | Pending | Pending |
| #694 | Swift | programming | Swift | Pending | Pending |
| #695 | SystemVerilog | programming | SystemVerilog | Verified | Verified |
| #696 | TI Program | programming | TI Program | Pending | Pending |
| #697 | TL-Verilog | programming | TL-Verilog | Pending | Pending |
| #698 | TLA | programming | TLA | Verified | Verified |
| #702 | TSQL | programming | TSQL | Pending | Pending |
| #704 | TSX | programming | TypeScript | Verified | Verified |
| #705 | TXL | programming | TXL | Pending | Pending |
| #706 | Tact | programming | Tact | Verified | Pending |
| #707 | Talon | programming | Talon | Pending | Pending |
| #708 | Tape | programming | Tape | Verified | Pending |
| #709 | Tcl | programming | Tcl | Verified | Verified |
| #710 | Tcsh | programming | Shell | Verified | Verified |
| #711 | TeX | markup | TeX | Verified | Verified |
| #712 | Tea | markup | Tea | Pending | Pending |
| #713 | Teal | programming | Teal | Verified | Verified |
| #714 | Terra | programming | Terra | Pending | Pending |
| #715 | Terraform Template | markup | HCL | Verified | Verified |
| #721 | Thrift | programming | Thrift | Verified | Verified |
| #722 | Toit | programming | Toit | Pending | Pending |
| #723 | Tolk | programming | Tolk | Verified | Pending |
| #725 | Tree-sitter Query | programming | Tree-sitter Query | Verified | Verified |
| #726 | Turing | programming | Turing | Pending | Pending |
| #728 | Twig | markup | Twig | Pending | Pending |
| #730 | TypeScript | programming | TypeScript | Verified | Verified |
| #731 | TypeSpec | programming | TypeSpec | Verified | Verified |
| #732 | Typst | programming | Typst | Verified | Verified |
| #733 | Unified Parallel C | programming | C | Pending | Pending |
| #735 | Unix Assembly | programming | Assembly | Verified | Verified |
| #736 | Uno | programming | Uno | Pending | Pending |
| #737 | UnrealScript | programming | UnrealScript | Pending | Pending |
| #738 | Untyped Plutus Core | programming | Untyped Plutus Core | Pending | Pending |
| #739 | UrWeb | programming | UrWeb | Pending | Pending |
| #740 | V | programming | V | Pending | Pending |
| #741 | VBA | programming | VBA | Pending | Pending |
| #742 | VBScript | programming | VBScript | Verified | Verified |
| #743 | VCL | programming | VCL | Pending | Pending |
| #744 | VHDL | programming | VHDL | Verified | Verified |
| #745 | Vala | programming | Vala | Verified | Verified |
| #747 | Velocity Template Language | markup | Velocity Template Language | Verified | Verified |
| #748 | Vento | markup | Vento | Verified | Verified |
| #749 | Verilog | programming | Verilog | Verified | Verified |
| #750 | Verse | programming | Verse | Pending | Pending |
| #753 | Vim Snippet | markup | Vim Snippet | Pending | Pending |
| #754 | Vim script | programming | Vim script | Verified | Verified |
| #755 | Visual Basic .NET | programming | Visual Basic .NET | Verified | Verified |
| #756 | Visual Basic 6.0 | programming | Visual Basic 6.0 | Pending | Pending |
| #757 | Volt | programming | Volt | Pending | Pending |
| #758 | Vue | markup | Vue | Verified | Verified |
| #759 | Vyper | programming | Vyper | Verified | Verified |
| #760 | WDL | programming | WDL | Verified | Pending |
| #761 | WGSL | programming | WGSL | Verified | Pending |
| #765 | WebAssembly | programming | WebAssembly | Verified | Verified |
| #767 | WebIDL | programming | WebIDL | Verified | Verified |
| #770 | Whiley | programming | Whiley | Pending | Pending |
| #774 | Witcher Script | programming | Witcher Script | Pending | Pending |
| #775 | Wolfram Language | programming | Wolfram Language | Verified | Verified |
| #776 | Wollok | programming | Wollok | Verified | Verified |
| #778 | Wren | programming | Wren | Verified | Verified |
| #782 | X10 | programming | X10 | Pending | Pending |
| #783 | XC | programming | XC | Pending | Pending |
| #788 | XProc | programming | XProc | Pending | Pending |
| #789 | XQuery | programming | XQuery | Verified | Verified |
| #790 | XS | programming | XS | Verified | Verified |
| #791 | XSLT | programming | XSLT | Verified | Verified |
| #792 | Xmake | programming | Xmake | Verified | Verified |
| #793 | Xojo | programming | Xojo | Pending | Pending |
| #794 | Xonsh | programming | Xonsh | Verified | Verified |
| #795 | Xtend | programming | Xtend | Pending | Pending |
| #798 | YARA | programming | YARA | Verified | Verified |
| #799 | YASnippet | markup | YASnippet | Pending | Pending |
| #800 | Yacc | programming | Yacc | Verified | Verified |
| #801 | Yul | programming | Yul | Verified | Pending |
| #802 | ZAP | programming | ZAP | Verified | Verified |
| #803 | ZIL | programming | ZIL | Verified | Verified |
| #804 | Zeek | programming | Zeek | Pending | Pending |
| #805 | ZenScript | programming | ZenScript | Pending | Pending |
| #806 | Zephir | programming | Zephir | Pending | Pending |
| #807 | Zig | programming | Zig | Verified | Verified |
| #808 | Zimpl | programming | Zimpl | Pending | Pending |
| #814 | eC | programming | eC | Pending | Pending |
| #816 | fish | programming | Shell | Verified | Verified |
| #817 | hoon | programming | hoon | Pending | Pending |
| #819 | jq | programming | jq | Verified | Verified |
| #820 | kvlang | markup | kvlang | Verified | Pending |
| #821 | mIRC Script | programming | mIRC Script | Pending | Pending |
| #822 | mcfunction | programming | mcfunction | Pending | Pending |
| #823 | mdsvex | markup | mdsvex | Verified | Verified |
| #824 | mupad | programming | mupad | Pending | Pending |
| #826 | nesC | programming | nesC | Pending | Pending |
| #827 | ooc | programming | ooc | Pending | Pending |
| #829 | q | programming | q | Pending | Pending |
| #831 | sed | programming | sed | Verified | Verified |
| #832 | templ | markup | templ | Verified | Verified |
| #833 | ucode | programming | ucode | Verified | Verified |
| #835 | wisp | programming | wisp | Verified | Verified |
| #836 | xBase | programming | xBase | Pending | Pending |
