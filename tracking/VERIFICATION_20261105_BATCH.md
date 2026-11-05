# Headless native verification batch: November 5, 2026

The batch used console or headless tools and did not invoke .NET. Verification applies to the exact inputs and scope in each receipt. The prior report remains available.

## Main sample checks

- **#023 Agda**: Syntax and behavior verified. Agda typechecked the unchanged main : IO declaration; its GHC backend compiled the FFI putLine implementation and the resulting executable printed exactly Hello, World!. [Evidence](../examples/%23023%20Agda/verification/native_20261105_batch_main.json).
- **#043 Asymptote**: Syntax and behavior verified. The native Asymptote interpreter loaded its matching standard modules and concatenated/printed the exact greeting. Console I/O only; no graphics or viewer. [Evidence](../examples/%23043%20Asymptote/verification/native_20261105_batch_main.json).
- **#204 Factor**: Syntax and behavior verified. Authentic Factor VM loaded the unchanged script, concatenated the two stack strings and printed exactly Hello, World!. No listener or UI was started. [Evidence](../examples/%23204%20Factor/verification/native_20261105_batch_main.json).
- **#265 Grace**: Syntax and behavior verified. The official Minigrace compiler parsed and compiled the unchanged Grace source with its standard dialect. The official Grace command-line runner, invoked through the pinned Node runtime rather than its machine-specific shebang, executed the resulting module and printed exactly Hello, World!. [Evidence](../examples/%23265%20Grace/verification/native_20261105_batch_main.json).
- **#388 Linux Kernel Module**: Syntax and behavior verified. Native Kbuild compiled the original external module, regenerated the canonical .mod object list modulo its temporary directory prefix, and embedded both greeting and module description. No module was loaded or kernel init executed. [Evidence](../examples/%23388%20Linux%20Kernel%20Module/verification/native_20261105_batch_main.json).
- **#403 M**: Syntax and behavior verified. Native FIS-GT.M compiled and ran the exact M bytes after the documented HELLO.m filename staging. No database access or server was used. [Evidence](../examples/%23403%20M/verification/native_20261105_batch_main.json).
- **#439 Modula-2**: Syntax and behavior verified. GNU Modula-2 compiled the exact PIM module and its native executable printed the exact greeting with LF. [Evidence](../examples/%23439%20Modula-2/verification/native_20261105_batch_main.json).
- **#454 NASL**: Syntax and behavior verified. Original NASL parsed and display() emitted the exact greeting through Greenbone GLib message logging on stderr using a disposable Unix-socket Redis knowledge base. TCP was disabled; no vulnerability scans, probe scripts or remote targets were used. [Evidence](../examples/%23454%20NASL/verification/native_20261105_batch_main.json).
- **#469 Nextflow**: Syntax and behavior verified. Nextflow parsed and scheduled the exact original DSL2 workflow offline, completed the local Bash task and emitted the exact stdout greeting. No remote workflow, container or external service. [Evidence](../examples/%23469%20Nextflow/verification/native_20261105_batch_main.json).
- **#576 Qt Script**: Syntax and behavior verified. The unchanged C++ QCoreApplication consumer loaded the exact hello.qs into the native Qt5 QScriptEngine and printed its final value, Hello, World!, with exit0 and no exceptions. No display variables were supplied, and no QtGui/QtWidgets libraries or GUI processes were used. [Evidence](../examples/%23576%20Qt%20Script/verification/native_20261105_batch_main.json).
- **#608 Redcode**: Syntax and behavior verified. The genuine pMARS assembler accepted the original warrior. Its generated load listing contained the thirteen ASCII data fields decoding to Hello, World!, and a bounded native battle ran its JMP loop. This Redcode sample encodes data, does not print text. Display updates were disabled and no display environment was supplied. [Evidence](../examples/%23608%20Redcode/verification/native_20261105_batch_main.json).
- **#653 Scilab**: Syntax and behavior verified. The minimal native Scilab command-line interpreter ran the original .sce script; separately loaded and called the original .sci function through its original companion driver; and executed the .tst assertion. Each emitted the exact greeting. The nwni mode uses GUI/graphics/JVM-disabled libraries, with no display supplied and no GUI library linkage. [Evidence](../examples/%23653%20Scilab/verification/native_20261105_batch_main.json).
- **#665 Slice**: Syntax and behavior verified. The genuine ZeroC Slice compiler accepted the exact original definition, generated its C++ constant, and a native C++ program compiled against the genuine Ice SDK read Greeting::message and printed the exact greeting. The definition contains no server or proxy; no network or daemon was started. [Evidence](../examples/%23665%20Slice/verification/native_20261105_batch_main.json).
- **#808 Zimpl**: Syntax and behavior verified. After explicitly binding the indexed-variable iterator in the three declared sources, native Zimpl generated each LP and GLPK solved it to optimality. The thirteen native solution variables decode to exactly Hello, World!. Each suffix was compiled and solved separately. [Evidence](../examples/%23808%20Zimpl/verification/native_20261105_batch_main.json).

## Extension checks

- **#023 Agda**, `.agda`: Syntax and behavior verified. [Evidence](../examples/%23023%20Agda/verification/native_20261105_batch_main.json).
- **#043 Asymptote**, `.asy`: Syntax and behavior verified. [Evidence](../examples/%23043%20Asymptote/verification/native_20261105_batch_main.json).
- **#048 Awk**, `.auk`: Syntax and behavior verified. [Evidence](../examples/%23048%20Awk/verification/native_20261105_batch_2e61756b.json).
- **#048 Awk**, `.gawk`: Syntax and behavior verified. [Evidence](../examples/%23048%20Awk/verification/native_20261105_batch_2e6761776b.json).
- **#048 Awk**, `.mawk`: Syntax and behavior verified. [Evidence](../examples/%23048%20Awk/verification/native_20261105_batch_2e6d61776b.json).
- **#048 Awk**, `.nawk`: Syntax and behavior verified. [Evidence](../examples/%23048%20Awk/verification/native_20261105_batch_2e6e61776b.json).
- **#083 C**, `.c`: Syntax and behavior verified. [Evidence](../examples/%23083%20C/verification/native_20261105_batch_2e63.json).
- **#083 C**, `.h.in`: Syntax and behavior verified. [Evidence](../examples/%23083%20C/verification/native_20261105_batch_2e682e696e.json).
- **#085 C++**, `.cpp`: Syntax and behavior verified. [Evidence](../examples/%23085%20C%2B%2B/verification/native_20261105_batch_2e637070.json).
- **#085 C++**, `.cppm`: Syntax and behavior verified. [Evidence](../examples/%23085%20C%2B%2B/verification/native_20261105_batch_2e6370706d.json).
- **#085 C++**, `.ixx`: Syntax and behavior verified. [Evidence](../examples/%23085%20C%2B%2B/verification/native_20261105_batch_2e697878.json).
- **#092 CMake**, `.cmake`: Syntax and behavior verified. [Evidence](../examples/%23092%20CMake/verification/native_20261105_batch_2e636d616b65.json).
- **#092 CMake**, `.cmake.in`: Syntax and behavior verified. [Evidence](../examples/%23092%20CMake/verification/native_20261105_batch_2e636d616b652e696e.json).
- **#133 Common Lisp**, `.asd`: Syntax and behavior verified. [Evidence](../examples/%23133%20Common%20Lisp/verification/native_20261105_batch_2e617364.json).
- **#133 Common Lisp**, `.cl`: Syntax and behavior verified. [Evidence](../examples/%23133%20Common%20Lisp/verification/native_20261105_batch_2e636c.json).
- **#133 Common Lisp**, `.l`: Syntax and behavior verified. [Evidence](../examples/%23133%20Common%20Lisp/verification/native_20261105_batch_2e6c.json).
- **#133 Common Lisp**, `.lisp`: Syntax and behavior verified. [Evidence](../examples/%23133%20Common%20Lisp/verification/native_20261105_batch_2e6c697370.json).
- **#133 Common Lisp**, `.lsp`: Syntax and behavior verified. [Evidence](../examples/%23133%20Common%20Lisp/verification/native_20261105_batch_2e6c7370.json).
- **#133 Common Lisp**, `.sexp`: Syntax and behavior verified. [Evidence](../examples/%23133%20Common%20Lisp/verification/native_20261105_batch_2e73657870.json).
- **#166 Diff**, `.patch`: Syntax and behavior verified. [Evidence](../examples/%23166%20Diff/verification/native_20261105_batch_2e7061746368.json).
- **#204 Factor**, `.factor`: Syntax and behavior verified. [Evidence](../examples/%23204%20Factor/verification/native_20261105_batch_main.json).
- **#215 Forth**, `.4th`: Syntax and behavior verified. [Evidence](../examples/%23215%20Forth/verification/native_20261105_batch_2e347468.json).
- **#215 Forth**, `.f`: Syntax and behavior verified. [Evidence](../examples/%23215%20Forth/verification/native_20261105_batch_2e66.json).
- **#215 Forth**, `.for`: Syntax and behavior verified. [Evidence](../examples/%23215%20Forth/verification/native_20261105_batch_2e666f72.json).
- **#215 Forth**, `.forth`: Syntax and behavior verified. [Evidence](../examples/%23215%20Forth/verification/native_20261105_batch_2e666f727468.json).
- **#215 Forth**, `.fr`: Syntax and behavior verified. [Evidence](../examples/%23215%20Forth/verification/native_20261105_batch_2e6672.json).
- **#215 Forth**, `.frt`: Syntax and behavior verified. [Evidence](../examples/%23215%20Forth/verification/native_20261105_batch_2e667274.json).
- **#215 Forth**, `.fs`: Syntax and behavior verified. [Evidence](../examples/%23215%20Forth/verification/native_20261105_batch_2e6673.json).
- **#244 Gettext Catalog**, `.pot`: Syntax and behavior verified. [Evidence](../examples/%23244%20Gettext%20Catalog/verification/native_20261105_batch_2e706f74.json).
- **#256 Gnuplot**, `.gnu`: Syntax and behavior verified. [Evidence](../examples/%23256%20Gnuplot/verification/native_20261105_batch_2e676e75.json).
- **#256 Gnuplot**, `.gp`: Syntax and behavior verified. [Evidence](../examples/%23256%20Gnuplot/verification/native_20261105_batch_2e6770.json).
- **#256 Gnuplot**, `.p`: Syntax and behavior verified. [Evidence](../examples/%23256%20Gnuplot/verification/native_20261105_batch_2e70.json).
- **#256 Gnuplot**, `.plot`: Syntax and behavior verified. [Evidence](../examples/%23256%20Gnuplot/verification/native_20261105_batch_2e706c6f74.json).
- **#256 Gnuplot**, `.plt`: Syntax and behavior verified. [Evidence](../examples/%23256%20Gnuplot/verification/native_20261105_batch_2e706c74.json).
- **#265 Grace**, `.grace`: Syntax and behavior verified. [Evidence](../examples/%23265%20Grace/verification/native_20261105_batch_main.json).
- **#271 Graphviz (DOT)**, `.gv`: Syntax and behavior verified. [Evidence](../examples/%23271%20Graphviz%20%28DOT%29/verification/native_20261105_batch_2e6776.json).
- **#345 Jsonnet**, `.jsonnet`: Syntax and behavior verified. [Evidence](../examples/%23345%20Jsonnet/verification/native_20261105_batch_2e6a736f6e6e6574.json).
- **#345 Jsonnet**, `.libsonnet`: Syntax and behavior verified. [Evidence](../examples/%23345%20Jsonnet/verification/native_20261105_batch_2e6c6962736f6e6e6574.json).
- **#388 Linux Kernel Module**, `.mod`: Syntax and behavior verified. [Evidence](../examples/%23388%20Linux%20Kernel%20Module/verification/native_20261105_batch_main.json).
- **#403 M**, `.mumps`: Syntax and behavior verified. [Evidence](../examples/%23403%20M/verification/native_20261105_batch_main.json).
- **#416 Makefile**, `.mak`: Syntax and behavior verified. [Evidence](../examples/%23416%20Makefile/verification/native_20261105_batch_2e6d616b.json).
- **#416 Makefile**, `.make`: Syntax and behavior verified. [Evidence](../examples/%23416%20Makefile/verification/native_20261105_batch_2e6d616b65.json).
- **#416 Makefile**, `.makefile`: Syntax and behavior verified. [Evidence](../examples/%23416%20Makefile/verification/native_20261105_batch_2e6d616b6566696c65.json).
- **#416 Makefile**, `.mk`: Syntax and behavior verified. [Evidence](../examples/%23416%20Makefile/verification/native_20261105_batch_2e6d6b.json).
- **#439 Modula-2**, `.mod`: Syntax and behavior verified. [Evidence](../examples/%23439%20Modula-2/verification/native_20261105_batch_main.json).
- **#454 NASL**, `.nasl`, `.inc`: Syntax and behavior verified. [Evidence](../examples/%23454%20NASL/verification/native_20261105_batch_main.json).
- **#469 Nextflow**, `.nf`: Syntax and behavior verified. [Evidence](../examples/%23469%20Nextflow/verification/native_20261105_batch_main.json).
- **#576 Qt Script**, `.qs`: Syntax and behavior verified. [Evidence](../examples/%23576%20Qt%20Script/verification/native_20261105_batch_main.json).
- **#588 REXX**, `.pprx`: Syntax and behavior verified. [Evidence](../examples/%23588%20REXX/verification/native_20261105_batch_2e70707278.json).
- **#588 REXX**, `.rex`: Syntax and behavior verified. [Evidence](../examples/%23588%20REXX/verification/native_20261105_batch_2e726578.json).
- **#608 Redcode**, `.cw`: Syntax and behavior verified. [Evidence](../examples/%23608%20Redcode/verification/native_20261105_batch_main.json).
- **#623 Roff**, `.1`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e31.json).
- **#623 Roff**, `.1in`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e31696e.json).
- **#623 Roff**, `.1m`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e316d.json).
- **#623 Roff**, `.1x`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e3178.json).
- **#623 Roff**, `.2`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e32.json).
- **#623 Roff**, `.3`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e33.json).
- **#623 Roff**, `.3in`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e33696e.json).
- **#623 Roff**, `.3m`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e336d.json).
- **#623 Roff**, `.3p`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e3370.json).
- **#623 Roff**, `.3pm`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e33706d.json).
- **#623 Roff**, `.3qt`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e337174.json).
- **#623 Roff**, `.3x`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e3378.json).
- **#623 Roff**, `.4`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e34.json).
- **#623 Roff**, `.5`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e35.json).
- **#623 Roff**, `.6`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e36.json).
- **#623 Roff**, `.7`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e37.json).
- **#623 Roff**, `.8`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e38.json).
- **#623 Roff**, `.9`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e39.json).
- **#623 Roff**, `.l`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e6c.json).
- **#623 Roff**, `.man`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e6d616e.json).
- **#623 Roff**, `.mdoc`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e6d646f63.json).
- **#623 Roff**, `.me`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e6d65.json).
- **#623 Roff**, `.ms`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e6d73.json).
- **#623 Roff**, `.n`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e6e.json).
- **#623 Roff**, `.nr`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e6e72.json).
- **#623 Roff**, `.rno`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e726e6f.json).
- **#623 Roff**, `.roff`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e726f6666.json).
- **#623 Roff**, `.tmac`: Syntax and behavior verified. [Evidence](../examples/%23623%20Roff/verification/native_20261105_batch_2e746d6163.json).
- **#624 Roff Manpage**, `.1in`: Syntax and behavior verified. [Evidence](../examples/%23624%20Roff%20Manpage/verification/native_20261105_batch_2e31696e.json).
- **#624 Roff Manpage**, `.1m`: Syntax and behavior verified. [Evidence](../examples/%23624%20Roff%20Manpage/verification/native_20261105_batch_2e316d.json).
- **#624 Roff Manpage**, `.1x`: Syntax and behavior verified. [Evidence](../examples/%23624%20Roff%20Manpage/verification/native_20261105_batch_2e3178.json).
- **#624 Roff Manpage**, `.2`: Syntax and behavior verified. [Evidence](../examples/%23624%20Roff%20Manpage/verification/native_20261105_batch_2e32.json).
- **#624 Roff Manpage**, `.3`: Syntax and behavior verified. [Evidence](../examples/%23624%20Roff%20Manpage/verification/native_20261105_batch_2e33.json).
- **#624 Roff Manpage**, `.3in`: Syntax and behavior verified. [Evidence](../examples/%23624%20Roff%20Manpage/verification/native_20261105_batch_2e33696e.json).
- **#624 Roff Manpage**, `.3m`: Syntax and behavior verified. [Evidence](../examples/%23624%20Roff%20Manpage/verification/native_20261105_batch_2e336d.json).
- **#624 Roff Manpage**, `.3p`: Syntax and behavior verified. [Evidence](../examples/%23624%20Roff%20Manpage/verification/native_20261105_batch_2e3370.json).
- **#624 Roff Manpage**, `.3pm`: Syntax and behavior verified. [Evidence](../examples/%23624%20Roff%20Manpage/verification/native_20261105_batch_2e33706d.json).
- **#624 Roff Manpage**, `.3qt`: Syntax and behavior verified. [Evidence](../examples/%23624%20Roff%20Manpage/verification/native_20261105_batch_2e337174.json).
- **#624 Roff Manpage**, `.3x`: Syntax and behavior verified. [Evidence](../examples/%23624%20Roff%20Manpage/verification/native_20261105_batch_2e3378.json).
- **#624 Roff Manpage**, `.4`: Syntax and behavior verified. [Evidence](../examples/%23624%20Roff%20Manpage/verification/native_20261105_batch_2e34.json).
- **#624 Roff Manpage**, `.5`: Syntax and behavior verified. [Evidence](../examples/%23624%20Roff%20Manpage/verification/native_20261105_batch_2e35.json).
- **#624 Roff Manpage**, `.6`: Syntax and behavior verified. [Evidence](../examples/%23624%20Roff%20Manpage/verification/native_20261105_batch_2e36.json).
- **#624 Roff Manpage**, `.7`: Syntax and behavior verified. [Evidence](../examples/%23624%20Roff%20Manpage/verification/native_20261105_batch_2e37.json).
- **#624 Roff Manpage**, `.8`: Syntax and behavior verified. [Evidence](../examples/%23624%20Roff%20Manpage/verification/native_20261105_batch_2e38.json).
- **#624 Roff Manpage**, `.9`: Syntax and behavior verified. [Evidence](../examples/%23624%20Roff%20Manpage/verification/native_20261105_batch_2e39.json).
- **#624 Roff Manpage**, `.man`: Syntax and behavior verified. [Evidence](../examples/%23624%20Roff%20Manpage/verification/native_20261105_batch_2e6d616e.json).
- **#624 Roff Manpage**, `.mdoc`: Syntax and behavior verified. [Evidence](../examples/%23624%20Roff%20Manpage/verification/native_20261105_batch_2e6d646f63.json).
- **#653 Scilab**, `.sci`, `.sce`, `.tst`: Syntax and behavior verified. [Evidence](../examples/%23653%20Scilab/verification/native_20261105_batch_main.json).
- **#665 Slice**, `.ice`: Syntax and behavior verified. [Evidence](../examples/%23665%20Slice/verification/native_20261105_batch_main.json).
- **#716 Texinfo**, `.texinfo`: Syntax and behavior verified. [Evidence](../examples/%23716%20Texinfo/verification/native_20261105_batch_2e746578696e666f.json).
- **#716 Texinfo**, `.txi`: Syntax and behavior verified. [Evidence](../examples/%23716%20Texinfo/verification/native_20261105_batch_2e747869.json).
- **#808 Zimpl**, `.zimpl`, `.zmpl`, `.zpl`: Syntax and behavior verified. [Evidence](../examples/%23808%20Zimpl/verification/native_20261105_batch_main.json).
- **#828 pkg-config**, `.pc.in`: Syntax and behavior verified. [Evidence](../examples/%23828%20pkg-config/verification/native_20261105_batch_2e70632e696e.json).

## Attempts still pending

**#182 Easybuild**: Native EasyBuild toolchain preparation timed out before the easyconfig could be executed; syntax and behavior remain pending. [Attempt evidence](../examples/%23182%20Easybuild/verification/native_20261105_batch_blocked_main.json).

**#565 Puppet**: The prepared Puppet command line timed out during initialization, including the bounded extended attempt; the original manifest was not verified. [Attempt evidence](../examples/%23565%20Puppet/verification/native_20261105_batch_blocked_main.json).

**#085 C++ `.re`**: The genuine re2c generator accepted the original .re source, but the generated C++ failed to compile because YYLIMIT and YYFILL were not defined. This variant remains unverified and needs a source correction. [Attempt evidence](../examples/%23085%20C%2B%2B/verification/native_20261105_batch_blocked_2e7265.json).


Main samples: 563/836 syntax and 536/836 behavior verified.
Language and extension pairs: 780/1749 syntax and 706/1749 behavior verified.
