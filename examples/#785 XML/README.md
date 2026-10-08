# #785 XML

Voce e ordine canonici di reference/languages.yml. Sorgente e fixture originali.

## Obiettivo

Analizzare XML e leggere il testo Hello, World!.

Parser XML con rete ed espansione di entità disabilitate; il driver legge elemento, attributo e contenuto.

## Toolchain e riproduzione

lxml6.1.3 con libxml2 originale

Comandi dalla cartella dell’esempio; usare strumenti installati nel PATH e una copia temporanea per build/output. Le dipendenze della prova sono isolate in work.

```text
python verify.py
```

## Risultato atteso e stato

Elemento greeting, audience World, contenuto Hello, World!.

Artefatto creato: sì. Sintassi verificata: sì. Semantica verificata: sì.

Il log verification/toolchain.json registra SHA-256 dei sorgenti, provenienza/versioni, comandi effettivi, exit/stdout/stderr e ambito della prova.

## Fonti primarie

- https://www.w3.org/TR/xml/

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.xml` | [hello.xml](hello.xml), [greeting.xml](variants/mod-282b9d03/greeting.xml), [greeting.xml](variants/sch-5766dac2/greeting.xml), [greeting.xml](variants/xsd-e7933ad0/greeting.xml) creato, verifiche pendenti |
| `.adml` | [hello.adml](variants/adml-46dc3558/hello.adml) creato, verifiche pendenti |
| `.admx` | [hello.admx](variants/admx-0548ed07/hello.admx) creato, verifiche pendenti |
| `.ant` | [hello.ant](variants/ant-a1e16eb5/hello.ant) creato, verifiche pendenti |
| `.axaml` | [hello.axaml](variants/axaml-2a49e0e8/hello.axaml) creato, verifiche pendenti |
| `.axml` | [hello.axml](variants/axml-7bb948ba/hello.axml) creato, verifiche pendenti |
| `.builds` | [hello.builds](variants/builds-14c8c2e5/hello.builds) creato, verifiche pendenti |
| `.ccproj` | [hello.ccproj](variants/ccproj-c2916c70/hello.ccproj) creato, verifiche pendenti |
| `.ccxml` | [hello.ccxml](variants/ccxml-75a495c9/hello.ccxml) creato, verifiche pendenti |
| `.clixml` | [hello.clixml](variants/clixml-f6080012/hello.clixml) creato, verifiche pendenti |
| `.cproject` | [hello.cproject](variants/cproject-1ebe600e/hello.cproject) creato, verifiche pendenti |
| `.cscfg` | [hello.cscfg](variants/cscfg-de5a032d/hello.cscfg) creato, verifiche pendenti |
| `.csdef` | [hello.csdef](variants/csdef-999ec91d/hello.csdef) creato, verifiche pendenti |
| `.csl` | [hello.csl](variants/csl-341667e5/hello.csl) creato, verifiche pendenti |
| `.csproj` | [hello.csproj](variants/csproj-c8fb684d/hello.csproj) creato, verifiche pendenti |
| `.ct` | [hello.ct](variants/ct-cf5694ce/hello.ct) creato, verifiche pendenti |
| `.depproj` | [hello.depproj](variants/depproj-b8e1f116/hello.depproj) creato, verifiche pendenti |
| `.dita` | [hello.dita](variants/dita-d69b8c61/hello.dita) creato, verifiche pendenti |
| `.ditamap` | [hello.ditamap](variants/ditamap-bf34a4fc/hello.ditamap) creato, verifiche pendenti |
| `.ditaval` | [hello.ditaval](variants/ditaval-171fd0e9/hello.ditaval) creato, verifiche pendenti |
| `.dll.config` | [hello.dll.config](variants/dll-config-9ffdf19b/hello.dll.config) creato, verifiche pendenti |
| `.dotsettings` | [hello.dotsettings](variants/dotsettings-0bc341c3/hello.dotsettings) creato, verifiche pendenti |
| `.filters` | [hello.filters](variants/filters-32be12c1/hello.filters) creato, verifiche pendenti |
| `.fsproj` | [hello.fsproj](variants/fsproj-88391edf/hello.fsproj) creato, verifiche pendenti |
| `.fxml` | [hello.fxml](variants/fxml-eb650f95/hello.fxml) creato, verifiche pendenti |
| `.glade` | [hello.glade](variants/glade-4f198e5e/hello.glade) creato, verifiche pendenti |
| `.gml` | [hello.gml](variants/gml-098725fd/hello.gml) creato, verifiche pendenti |
| `.gmx` | [hello.gmx](variants/gmx-eb1b5e23/hello.gmx) creato, verifiche pendenti |
| `.gpx` | [hello.gpx](variants/gpx-26da0cc3/hello.gpx) creato, verifiche pendenti |
| `.grxml` | [hello.grxml](variants/grxml-89e50f7a/hello.grxml) creato, verifiche pendenti |
| `.gst` | [hello.gst](variants/gst-7fb857dd/hello.gst) creato, verifiche pendenti |
| `.hzp` | [hello.hzp](variants/hzp-e1b0b97d/hello.hzp) creato, verifiche pendenti |
| `.icls` | [hello.icls](variants/icls-fc92fcca/hello.icls) creato, verifiche pendenti |
| `.iml` | [hello.iml](variants/iml-32c4fd41/hello.iml) creato, verifiche pendenti |
| `.ivy` | [hello.ivy](variants/ivy-a48ad6c0/hello.ivy) creato, verifiche pendenti |
| `.jelly` | [hello.jelly](variants/jelly-137dfe6a/hello.jelly) creato, verifiche pendenti |
| `.jsproj` | [hello.jsproj](variants/jsproj-4a03cba5/hello.jsproj) creato, verifiche pendenti |
| `.kml` | [hello.kml](variants/kml-ea546317/hello.kml) creato, verifiche pendenti |
| `.launch` | [hello.launch](variants/launch-a111fb5d/hello.launch) creato, verifiche pendenti |
| `.mdpolicy` | [hello.mdpolicy](variants/mdpolicy-130ff745/hello.mdpolicy) creato, verifiche pendenti |
| `.meta4` | [hello.meta4](variants/meta4-255640ee/hello.meta4) creato, verifiche pendenti |
| `.mjml` | [hello.mjml](variants/mjml-ecfe81f3/hello.mjml) creato, verifiche pendenti |
| `.mm` | [hello.mm](variants/mm-1354547c/hello.mm) creato, verifiche pendenti |
| `.mod` | [hello.mod](variants/mod-282b9d03/hello.mod) creato, verifiche pendenti |
| `.mojo` | [hello.mojo](variants/mojo-af65e82b/hello.mojo) creato, verifiche pendenti |
| `.mxml` | [hello.mxml](variants/mxml-f7008a87/hello.mxml) creato, verifiche pendenti |
| `.natvis` | [hello.natvis](variants/natvis-141b89bb/hello.natvis) creato, verifiche pendenti |
| `.ncl` | [hello.ncl](variants/ncl-381c21d0/hello.ncl) creato, verifiche pendenti |
| `.ndproj` | [hello.ndproj](variants/ndproj-700c55a6/hello.ndproj) creato, verifiche pendenti |
| `.nproj` | [hello.nproj](variants/nproj-86104a21/hello.nproj) creato, verifiche pendenti |
| `.nuspec` | [hello.nuspec](variants/nuspec-a8a3258d/hello.nuspec) creato, verifiche pendenti |
| `.odd` | [hello.odd](variants/odd-d1e2aae1/hello.odd) creato, verifiche pendenti |
| `.osm` | [hello.osm](variants/osm-f6d9c802/hello.osm) creato, verifiche pendenti |
| `.pkgproj` | [hello.pkgproj](variants/pkgproj-401ae7dc/hello.pkgproj) creato, verifiche pendenti |
| `.pluginspec` | [hello.pluginspec](variants/pluginspec-34c2c898/hello.pluginspec) creato, verifiche pendenti |
| `.proj` | [hello.proj](variants/proj-cab74e0c/hello.proj) creato, verifiche pendenti |
| `.props` | [hello.props](variants/props-9ee050f6/hello.props) creato, verifiche pendenti |
| `.ps1xml` | [hello.ps1xml](variants/ps1xml-09e83984/hello.ps1xml) creato, verifiche pendenti |
| `.psc1` | [hello.psc1](variants/psc1-a69b79ce/hello.psc1) creato, verifiche pendenti |
| `.pt` | [hello.pt](variants/pt-e566345e/hello.pt) creato, verifiche pendenti |
| `.pubxml` | [hello.pubxml](variants/pubxml-c1e93c09/hello.pubxml) creato, verifiche pendenti |
| `.qhelp` | [hello.qhelp](variants/qhelp-b2335ca8/hello.qhelp) creato, verifiche pendenti |
| `.rbxmx` | [hello.rbxmx](variants/rbxmx-9c1dfdc9/hello.rbxmx) creato, verifiche pendenti |
| `.rdf` | [hello.rdf](variants/rdf-51d7c4fe/hello.rdf) creato, verifiche pendenti |
| `.res` | [hello.res](variants/res-93ede235/hello.res) creato, verifiche pendenti |
| `.resx` | [hello.resx](variants/resx-7d4ecbae/hello.resx) creato, verifiche pendenti |
| `.rs` | [hello.rs](variants/rs-fbdde0c3/hello.rs) creato, verifiche pendenti |
| `.rss` | [hello.rss](variants/rss-e389da7b/hello.rss) creato, verifiche pendenti |
| `.sch` | [hello.sch](variants/sch-5766dac2/hello.sch) creato, verifiche pendenti |
| `.scxml` | [hello.scxml](variants/scxml-4ab24e2f/hello.scxml) creato, verifiche pendenti |
| `.sfproj` | [hello.sfproj](variants/sfproj-0a8b1485/hello.sfproj) creato, verifiche pendenti |
| `.shproj` | [hello.shproj](variants/shproj-1e30c6ee/hello.shproj) creato, verifiche pendenti |
| `.slnx` | [hello.slnx](variants/slnx-80464f8e/hello.slnx) creato, verifiche pendenti |
| `.srdf` | [hello.srdf](variants/srdf-e2c0f37e/hello.srdf) creato, verifiche pendenti |
| `.storyboard` | [hello.storyboard](variants/storyboard-e404945f/hello.storyboard) creato, verifiche pendenti |
| `.sublime-snippet` | [hello.sublime-snippet](variants/sublime-snippet-26117df4/hello.sublime-snippet) creato, verifiche pendenti |
| `.sw` | [hello.sw](variants/sw-a70f7da6/hello.sw) creato, verifiche pendenti |
| `.targets` | [hello.targets](variants/targets-350b67c2/hello.targets) creato, verifiche pendenti |
| `.tml` | [hello.tml](variants/tml-20a68624/hello.tml) creato, verifiche pendenti |
| `.ts` | [hello.ts](variants/ts-538a6c01/hello.ts) creato, verifiche pendenti |
| `.tsx` | [hello.tsx](variants/tsx-98711b97/hello.tsx) creato, verifiche pendenti |
| `.typ` | [hello.typ](variants/typ-1a9210cc/hello.typ) creato, verifiche pendenti |
| `.ui` | [hello.ui](variants/ui-b4a1142c/hello.ui) creato, verifiche pendenti |
| `.urdf` | [hello.urdf](variants/urdf-9b84ed91/hello.urdf) creato, verifiche pendenti |
| `.ux` | [hello.ux](variants/ux-b49ae1c8/hello.ux) creato, verifiche pendenti |
| `.vbproj` | [hello.vbproj](variants/vbproj-d85ff9d3/hello.vbproj) creato, verifiche pendenti |
| `.vcxproj` | [hello.vcxproj](variants/vcxproj-68931e67/hello.vcxproj) creato, verifiche pendenti |
| `.vsixmanifest` | [hello.vsixmanifest](variants/vsixmanifest-267ff99d/hello.vsixmanifest) creato, verifiche pendenti |
| `.vssettings` | [hello.vssettings](variants/vssettings-d1365d8a/hello.vssettings) creato, verifiche pendenti |
| `.vstemplate` | [hello.vstemplate](variants/vstemplate-164b322c/hello.vstemplate) creato, verifiche pendenti |
| `.vxml` | [hello.vxml](variants/vxml-aae052f7/hello.vxml) creato, verifiche pendenti |
| `.wixproj` | [hello.wixproj](variants/wixproj-881a9958/hello.wixproj) creato, verifiche pendenti |
| `.workflow` | [hello.workflow](variants/workflow-17728b44/hello.workflow) creato, verifiche pendenti |
| `.wsdl` | [hello.wsdl](variants/wsdl-3735f2b7/hello.wsdl) creato, verifiche pendenti |
| `.wsf` | [hello.wsf](variants/wsf-e45d2642/hello.wsf) creato, verifiche pendenti |
| `.wxi` | [hello.wxi](variants/wxi-83752bb1/hello.wxi) creato, verifiche pendenti |
| `.wxl` | [hello.wxl](variants/wxl-b636afaf/hello.wxl) creato, verifiche pendenti |
| `.wxs` | [hello.wxs](variants/wxs-c87e94fa/hello.wxs) creato, verifiche pendenti |
| `.x3d` | [hello.x3d](variants/x3d-3a1c006e/hello.x3d) creato, verifiche pendenti |
| `.xacro` | [hello.xacro](variants/xacro-a4317059/hello.xacro) creato, verifiche pendenti |
| `.xaml` | [hello.xaml](variants/xaml-14ebb983/hello.xaml) creato, verifiche pendenti |
| `.xib` | [hello.xib](variants/xib-12b224f8/hello.xib) creato, verifiche pendenti |
| `.xlf` | [hello.xlf](variants/xlf-ee454d21/hello.xlf) creato, verifiche pendenti |
| `.xliff` | [hello.xliff](variants/xliff-5829fedb/hello.xliff) creato, verifiche pendenti |
| `.xmi` | [hello.xmi](variants/xmi-6edb7c99/hello.xmi) creato, verifiche pendenti |
| `.xml.dist` | [hello.xml.dist](variants/xml-dist-b06126e8/hello.xml.dist) creato, verifiche pendenti |
| `.xmp` | [hello.xmp](variants/xmp-5abdb317/hello.xmp) creato, verifiche pendenti |
| `.xproj` | [hello.xproj](variants/xproj-9c5ebfdf/hello.xproj) creato, verifiche pendenti |
| `.xsd` | [hello.xsd](variants/xsd-e7933ad0/hello.xsd) creato, verifiche pendenti |
| `.xspec` | [hello.xspec](variants/xspec-9187de7b/hello.xspec) creato, verifiche pendenti |
| `.xul` | [hello.xul](variants/xul-916fc60e/hello.xul) creato, verifiche pendenti |
| `.zcml` | [hello.zcml](variants/zcml-defc4407/hello.zcml) creato, verifiche pendenti |
