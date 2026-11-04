# Headless verification follow-up: November 4, 2026

The batch used console or headless tools and did not invoke .NET. Verification applies to the exact inputs and scope in each receipt. The prior report remains available.

## Main sample checks

- **#008 AIDL**: Syntax and behavior verified. Native AOSP compiler generated the intended Binder constant, method signature, Stub and Proxy. No Android IPC or service execution was tested. [Evidence](../examples/%23008%20AIDL/verification/native_20261104_followup_main.json).
- **#424 MeTTa**: Syntax and behavior verified. The official native Hyperon Python binding evaluated the exact MeTTa program, with the exact greeting and LF and no stderr. [Evidence](../examples/%23424%20MeTTa/verification/native_20261104_followup_main.json).
- **#475 Nix**: Syntax and behavior verified. Original Nix evaluator returned exactly the intended string. No derivations, builds, system configuration or network evaluation. [Evidence](../examples/%23475%20Nix/verification/native_20261104_followup_main.json).
- **#505 OpenRC runscript**: Syntax and behavior verified. Native OpenRC start invoked the original script and ebegin emitted its greeting. Only a disposable Alpine fixture was modified; no host service was started. [Evidence](../examples/%23505%20OpenRC%20runscript/verification/native_20261104_followup_main.json).
- **#511 OverPy**: Syntax verified; behavior pending. The genuine OverPy compiler emitted an Ongoing - Each Player rule with Big Message for Event Player and the exact greeting. The original member invocation was rejected. Execution in Overwatch remains unverified. [Evidence](../examples/%23511%20OverPy/verification/native_20261104_followup_main.json).
- **#575 QMake**: Syntax and behavior verified. The original qmake project was generated and compiled by Qt; its console-only program printed the exact greeting. No GUI was used. [Evidence](../examples/%23575%20QMake/verification/native_20261104_followup_main.json).
- **#589 RMarkdown**: Syntax and behavior verified. The original R Markdown chunk executed with knitr; Pandoc rendered HTML containing the greeting in the chunk output. Quarto .qmd was not exercised. [Evidence](../examples/%23589%20RMarkdown/verification/native_20261104_followup_main.json).
- **#594 RPM Spec**: Syntax and behavior verified. The native RPM parser accepted the spec and rpmbuild ran %prep, printing the exact greeting. No packages were installed and no RPM was built. [Evidence](../examples/%23594%20RPM%20Spec/verification/native_20261104_followup_main.json).
- **#660 Sieve**: Syntax and behavior verified. Pigeonhole compiled the filter and the offline dry run planned fileinto INBOX.CorpusGreeting for the original .eml. No mail delivered. [Evidence](../examples/%23660%20Sieve/verification/native_20261104_followup_main.json).
- **#678 Spline Font Database**: Syntax and behavior verified. Native FontForge loaded the original SFD and reported its exact FullName. No glyph or font rendering was tested. [Evidence](../examples/%23678%20Spline%20Font%20Database/verification/native_20261104_followup_main.json).

## Extension checks

- **#008 AIDL**, `.aidl`: Syntax and behavior verified. [Evidence](../examples/%23008%20AIDL/verification/native_20261104_followup_main.json).
- **#083 C**, `.cats`: Syntax and behavior verified. [Evidence](../examples/%23083%20C/verification/native_20261104_followup_2e63617473.json).
- **#083 C**, `.h`: Syntax and behavior verified. [Evidence](../examples/%23083%20C/verification/native_20261104_followup_2e68.json).
- **#085 C++**, `.c++`: Syntax and behavior verified. [Evidence](../examples/%23085%20C%2B%2B/verification/native_20261104_followup_2e632b2b.json).
- **#085 C++**, `.cc`: Syntax and behavior verified. [Evidence](../examples/%23085%20C%2B%2B/verification/native_20261104_followup_2e6363.json).
- **#085 C++**, `.cp`: Syntax and behavior verified. [Evidence](../examples/%23085%20C%2B%2B/verification/native_20261104_followup_2e6370.json).
- **#085 C++**, `.cxx`: Syntax and behavior verified. [Evidence](../examples/%23085%20C%2B%2B/verification/native_20261104_followup_2e637878.json).
- **#085 C++**, `.h`: Syntax and behavior verified. [Evidence](../examples/%23085%20C%2B%2B/verification/native_20261104_followup_2e68.json).
- **#085 C++**, `.h++`: Syntax and behavior verified. [Evidence](../examples/%23085%20C%2B%2B/verification/native_20261104_followup_2e682b2b.json).
- **#085 C++**, `.hh`: Syntax and behavior verified. [Evidence](../examples/%23085%20C%2B%2B/verification/native_20261104_followup_2e6868.json).
- **#085 C++**, `.hpp`: Syntax and behavior verified. [Evidence](../examples/%23085%20C%2B%2B/verification/native_20261104_followup_2e687070.json).
- **#085 C++**, `.hxx`: Syntax and behavior verified. [Evidence](../examples/%23085%20C%2B%2B/verification/native_20261104_followup_2e687878.json).
- **#085 C++**, `.inc`: Syntax and behavior verified. [Evidence](../examples/%23085%20C%2B%2B/verification/native_20261104_followup_2e696e63.json).
- **#085 C++**, `.inl`: Syntax and behavior verified. [Evidence](../examples/%23085%20C%2B%2B/verification/native_20261104_followup_2e696e6c.json).
- **#085 C++**, `.ipp`: Syntax and behavior verified. [Evidence](../examples/%23085%20C%2B%2B/verification/native_20261104_followup_2e697070.json).
- **#085 C++**, `.tcc`: Syntax and behavior verified. [Evidence](../examples/%23085%20C%2B%2B/verification/native_20261104_followup_2e746363.json).
- **#085 C++**, `.tpp`: Syntax and behavior verified. [Evidence](../examples/%23085%20C%2B%2B/verification/native_20261104_followup_2e747070.json).
- **#085 C++**, `.txx`: Syntax and behavior verified. [Evidence](../examples/%23085%20C%2B%2B/verification/native_20261104_followup_2e747878.json).
- **#130 CoffeeScript**, `._coffee`: Syntax and behavior verified. [Evidence](../examples/%23130%20CoffeeScript/verification/native_20261104_followup_2e5f636f66666565.json).
- **#130 CoffeeScript**, `.cake`: Syntax and behavior verified. [Evidence](../examples/%23130%20CoffeeScript/verification/native_20261104_followup_2e63616b65.json).
- **#216 Fortran**, `.f77`: Syntax and behavior verified. [Evidence](../examples/%23216%20Fortran/verification/native_20261104_followup_2e663737.json).
- **#216 Fortran**, `.for`: Syntax and behavior verified. [Evidence](../examples/%23216%20Fortran/verification/native_20261104_followup_2e666f72.json).
- **#216 Fortran**, `.fpp`: Syntax and behavior verified. [Evidence](../examples/%23216%20Fortran/verification/native_20261104_followup_2e667070.json).
- **#217 Fortran Free Form**, `.f03`: Syntax and behavior verified. [Evidence](../examples/%23217%20Fortran%20Free%20Form/verification/native_20261104_followup_2e663033.json).
- **#217 Fortran Free Form**, `.f08`: Syntax and behavior verified. [Evidence](../examples/%23217%20Fortran%20Free%20Form/verification/native_20261104_followup_2e663038.json).
- **#217 Fortran Free Form**, `.f95`: Syntax and behavior verified. [Evidence](../examples/%23217%20Fortran%20Free%20Form/verification/native_20261104_followup_2e663935.json).
- **#280 HTML**, `.htm`: Syntax and behavior verified. [Evidence](../examples/%23280%20HTML/verification/native_20261104_followup_2e68746d.json).
- **#304 INI**, `.cfg`: Syntax and behavior verified. [Evidence](../examples/%23304%20INI/verification/native_20261104_followup_2e636667.json).
- **#304 INI**, `.properties`: Syntax and behavior verified. [Evidence](../examples/%23304%20INI/verification/native_20261104_followup_2e70726f70657274696573.json).
- **#324 JSON**, `.jsonl`: Syntax and behavior verified. [Evidence](../examples/%23324%20JSON/verification/native_20261104_followup_2e6a736f6e6c.json).
- **#324 JSON**, `.tfstate`: Syntax and behavior verified. [Evidence](../examples/%23324%20JSON/verification/native_20261104_followup_2e74667374617465.json).
- **#324 JSON**, `.tfstate.backup`: Syntax and behavior verified. [Evidence](../examples/%23324%20JSON/verification/native_20261104_followup_2e746673746174652e6261636b7570.json).
- **#418 Markdown**, `.markdown`: Syntax and behavior verified. [Evidence](../examples/%23418%20Markdown/verification/native_20261104_followup_2e6d61726b646f776e.json).
- **#418 Markdown**, `.mdown`: Syntax and behavior verified. [Evidence](../examples/%23418%20Markdown/verification/native_20261104_followup_2e6d646f776e.json).
- **#418 Markdown**, `.mdwn`: Syntax and behavior verified. [Evidence](../examples/%23418%20Markdown/verification/native_20261104_followup_2e6d64776e.json).
- **#418 Markdown**, `.mkd`: Syntax and behavior verified. [Evidence](../examples/%23418%20Markdown/verification/native_20261104_followup_2e6d6b64.json).
- **#418 Markdown**, `.mkdn`: Syntax and behavior verified. [Evidence](../examples/%23418%20Markdown/verification/native_20261104_followup_2e6d6b646e.json).
- **#418 Markdown**, `.mkdown`: Syntax and behavior verified. [Evidence](../examples/%23418%20Markdown/verification/native_20261104_followup_2e6d6b646f776e.json).
- **#424 MeTTa**, `.metta`: Syntax and behavior verified. [Evidence](../examples/%23424%20MeTTa/verification/native_20261104_followup_main.json).
- **#463 Nearley**, `.nearley`: Syntax and behavior verified. [Evidence](../examples/%23463%20Nearley/verification/native_20261104_followup_2e6e6561726c6579.json).
- **#475 Nix**, `.nix`: Syntax and behavior verified. [Evidence](../examples/%23475%20Nix/verification/native_20261104_followup_main.json).
- **#482 OASv2-yaml**, `.yml`: Syntax and behavior verified. [Evidence](../examples/%23482%20OASv2-yaml/verification/native_20261104_followup_2e796d6c.json).
- **#484 OASv3-yaml**, `.yml`: Syntax and behavior verified. [Evidence](../examples/%23484%20OASv3-yaml/verification/native_20261104_followup_2e796d6c.json).
- **#511 OverPy**, `.opy`: Syntax verified; behavior pending. [Evidence](../examples/%23511%20OverPy/verification/native_20261104_followup_main.json).
- **#518 PEG.js**, `.peggy`: Syntax and behavior verified. [Evidence](../examples/%23518%20PEG.js/verification/native_20261104_followup_2e7065676779.json).
- **#547 PostCSS**, `.postcss`: Syntax and behavior verified. [Evidence](../examples/%23547%20PostCSS/verification/native_20261104_followup_2e706f7374637373.json).
- **#564 Pug**, `.jade`: Syntax and behavior verified. [Evidence](../examples/%23564%20Pug/verification/native_20261104_followup_2e6a616465.json).
- **#570 Python**, `.cgi`: Syntax and behavior verified. [Evidence](../examples/%23570%20Python/verification/native_20261104_followup_2e636769.json).
- **#570 Python**, `.py3`: Syntax and behavior verified. [Evidence](../examples/%23570%20Python/verification/native_20261104_followup_2e707933.json).
- **#570 Python**, `.pyw`: Syntax and behavior verified. [Evidence](../examples/%23570%20Python/verification/native_20261104_followup_2e707977.json).
- **#570 Python**, `.wsgi`: Syntax and behavior verified. [Evidence](../examples/%23570%20Python/verification/native_20261104_followup_2e77736769.json).
- **#575 QMake**, `.pro`, `.pri`: Syntax and behavior verified. [Evidence](../examples/%23575%20QMake/verification/native_20261104_followup_2e70726f.json).
- **#589 RMarkdown**, `.qmd`: Syntax and behavior verified. [Evidence](../examples/%23589%20RMarkdown/verification/native_20261104_followup_2e716d64.json).
- **#589 RMarkdown**, `.rmd`: Syntax and behavior verified. [Evidence](../examples/%23589%20RMarkdown/verification/native_20261104_followup_main.json).
- **#594 RPM Spec**, `.spec`: Syntax and behavior verified. [Evidence](../examples/%23594%20RPM%20Spec/verification/native_20261104_followup_main.json).
- **#605 Rebol**, `.r`: Syntax and behavior verified. [Evidence](../examples/%23605%20Rebol/verification/native_20261104_followup_2e72.json).
- **#605 Rebol**, `.r2`: Syntax and behavior verified. [Evidence](../examples/%23605%20Rebol/verification/native_20261104_followup_2e7232.json).
- **#605 Rebol**, `.r3`: Syntax and behavior verified. [Evidence](../examples/%23605%20Rebol/verification/native_20261104_followup_2e7233.json).
- **#605 Rebol**, `.rebol`: Syntax and behavior verified. [Evidence](../examples/%23605%20Rebol/verification/native_20261104_followup_2e7265626f6c.json).
- **#611 Regular Expression**, `.regex`: Syntax and behavior verified. [Evidence](../examples/%23611%20Regular%20Expression/verification/native_20261104_followup_2e7265676578.json).
- **#634 SPARQL**, `.sparql`: Syntax and behavior verified. [Evidence](../examples/%23634%20SPARQL/verification/native_20261104_followup_2e73706172716c.json).
- **#636 SQL**, `.ddl`: Syntax and behavior verified. [Evidence](../examples/%23636%20SQL/verification/native_20261104_followup_2e64646c.json).
- **#636 SQL**, `.inc`: Syntax and behavior verified. [Evidence](../examples/%23636%20SQL/verification/native_20261104_followup_2e696e63.json).
- **#636 SQL**, `.tab`: Syntax and behavior verified. [Evidence](../examples/%23636%20SQL/verification/native_20261104_followup_2e746162.json).
- **#636 SQL**, `.viw`: Syntax and behavior verified. [Evidence](../examples/%23636%20SQL/verification/native_20261104_followup_2e766977.json).
- **#656 Shell**, `.bash`: Syntax and behavior verified. [Evidence](../examples/%23656%20Shell/verification/native_20261104_followup_2e62617368.json).
- **#656 Shell**, `.cgi`: Syntax and behavior verified. [Evidence](../examples/%23656%20Shell/verification/native_20261104_followup_2e636769.json).
- **#656 Shell**, `.command`: Syntax and behavior verified. [Evidence](../examples/%23656%20Shell/verification/native_20261104_followup_2e636f6d6d616e64.json).
- **#656 Shell**, `.sh.in`: Syntax and behavior verified. [Evidence](../examples/%23656%20Shell/verification/native_20261104_followup_2e73682e696e.json).
- **#656 Shell**, `.tool`: Syntax and behavior verified. [Evidence](../examples/%23656%20Shell/verification/native_20261104_followup_2e746f6f6c.json).
- **#656 Shell**, `.trigger`: Syntax and behavior verified. [Evidence](../examples/%23656%20Shell/verification/native_20261104_followup_2e74726967676572.json).
- **#660 Sieve**, `.sieve`: Syntax and behavior verified. [Evidence](../examples/%23660%20Sieve/verification/native_20261104_followup_main.json).
- **#678 Spline Font Database**, `.sfd`: Syntax and behavior verified. [Evidence](../examples/%23678%20Spline%20Font%20Database/verification/native_20261104_followup_main.json).
- **#700 TOML**, `.toml.example`: Syntax and behavior verified. [Evidence](../examples/%23700%20TOML/verification/native_20261104_followup_2e746f6d6c2e6578616d706c65.json).
- **#709 Tcl**, `.tcl.in`: Syntax and behavior verified. [Evidence](../examples/%23709%20Tcl/verification/native_20261104_followup_2e74636c2e696e.json).
- **#744 VHDL**, `.vhd`: Syntax and behavior verified. [Evidence](../examples/%23744%20VHDL/verification/native_20261104_followup_2e766864.json).
- **#744 VHDL**, `.vhf`: Syntax and behavior verified. [Evidence](../examples/%23744%20VHDL/verification/native_20261104_followup_2e766866.json).
- **#744 VHDL**, `.vho`: Syntax and behavior verified. [Evidence](../examples/%23744%20VHDL/verification/native_20261104_followup_2e76686f.json).
- **#744 VHDL**, `.vhs`: Syntax and behavior verified. [Evidence](../examples/%23744%20VHDL/verification/native_20261104_followup_2e766873.json).
- **#744 VHDL**, `.vht`: Syntax and behavior verified. [Evidence](../examples/%23744%20VHDL/verification/native_20261104_followup_2e766874.json).
- **#744 VHDL**, `.vhw`: Syntax and behavior verified. [Evidence](../examples/%23744%20VHDL/verification/native_20261104_followup_2e766877.json).
- **#771 Wikitext**, `.wiki`: Syntax and behavior verified. [Evidence](../examples/%23771%20Wikitext/verification/native_20261104_followup_2e77696b69.json).
- **#771 Wikitext**, `.wikitext`: Syntax and behavior verified. [Evidence](../examples/%23771%20Wikitext/verification/native_20261104_followup_2e77696b6974657874.json).
- **#791 XSLT**, `.xslt`: Syntax and behavior verified. [Evidence](../examples/%23791%20XSLT/verification/native_20261104_followup_2e78736c74.json).
- **#796 YAML**, `.yaml`: Syntax and behavior verified. [Evidence](../examples/%23796%20YAML/verification/native_20261104_followup_2e79616d6c.json).
- **#798 YARA**, `.yara`: Syntax and behavior verified. [Evidence](../examples/%23798%20YARA/verification/native_20261104_followup_2e79617261.json).
- **#818 iCalendar**, `.ical`: Syntax and behavior verified. [Evidence](../examples/%23818%20iCalendar/verification/native_20261104_followup_2e6963616c.json).
- **#830 reStructuredText**, `.rest`: Syntax and behavior verified. [Evidence](../examples/%23830%20reStructuredText/verification/native_20261104_followup_2e72657374.json).
- **#830 reStructuredText**, `.rest.txt`: Syntax and behavior verified. [Evidence](../examples/%23830%20reStructuredText/verification/native_20261104_followup_2e726573742e747874.json).
- **#830 reStructuredText**, `.rst.txt`: Syntax and behavior verified. [Evidence](../examples/%23830%20reStructuredText/verification/native_20261104_followup_2e7273742e747874.json).

Main samples: 548/836 syntax and 521/836 behavior verified.
Language and extension pairs: 671/1749 syntax and 597/1749 behavior verified.
