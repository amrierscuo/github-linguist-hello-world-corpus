# #785 XML

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Analyze XML and read the text Hello, World!.

The XML parser disables networking and entity expansion. The driver reads the element, attribute, and content.

## Toolchain and reproduction

lxml 6.1.3 with native libxml2

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
python verify.py
```

## Expected result and status

The greeting element has audience World and contains Hello, World!.

Artifact created: yes. syntax verified: yes. behavior verified: yes.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

## Primary sources

- https://www.w3.org/TR/xml/

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.xml` | [hello.xml](hello.xml), [greeting.xml](variants/mod-282b9d03/greeting.xml), [greeting.xml](variants/sch-5766dac2/greeting.xml), [greeting.xml](variants/xsd-e7933ad0/greeting.xml) created; verification pending |
| `.adml` | [hello.adml](variants/adml-46dc3558/hello.adml) created; verification pending |
| `.admx` | [hello.admx](variants/admx-0548ed07/hello.admx) created; verification pending |
| `.ant` | [hello.ant](variants/ant-a1e16eb5/hello.ant) created; verification pending |
| `.axaml` | [hello.axaml](variants/axaml-2a49e0e8/hello.axaml) created; verification pending |
| `.axml` | [hello.axml](variants/axml-7bb948ba/hello.axml) created; verification pending |
| `.builds` | [hello.builds](variants/builds-14c8c2e5/hello.builds) created; verification pending |
| `.ccproj` | [hello.ccproj](variants/ccproj-c2916c70/hello.ccproj) created; verification pending |
| `.ccxml` | [hello.ccxml](variants/ccxml-75a495c9/hello.ccxml) created; verification pending |
| `.clixml` | [hello.clixml](variants/clixml-f6080012/hello.clixml) created; verification pending |
| `.cproject` | [hello.cproject](variants/cproject-1ebe600e/hello.cproject) created; verification pending |
| `.cscfg` | [hello.cscfg](variants/cscfg-de5a032d/hello.cscfg) created; verification pending |
| `.csdef` | [hello.csdef](variants/csdef-999ec91d/hello.csdef) created; verification pending |
| `.csl` | [hello.csl](variants/csl-341667e5/hello.csl) created; verification pending |
| `.csproj` | [hello.csproj](variants/csproj-c8fb684d/hello.csproj) created; verification pending |
| `.ct` | [hello.ct](variants/ct-cf5694ce/hello.ct) created; verification pending |
| `.depproj` | [hello.depproj](variants/depproj-b8e1f116/hello.depproj) created; verification pending |
| `.dita` | [hello.dita](variants/dita-d69b8c61/hello.dita) created; verification pending |
| `.ditamap` | [hello.ditamap](variants/ditamap-bf34a4fc/hello.ditamap) created; verification pending |
| `.ditaval` | [hello.ditaval](variants/ditaval-171fd0e9/hello.ditaval) created; verification pending |
| `.dll.config` | [hello.dll.config](variants/dll-config-9ffdf19b/hello.dll.config) created; verification pending |
| `.dotsettings` | [hello.dotsettings](variants/dotsettings-0bc341c3/hello.dotsettings) created; verification pending |
| `.filters` | [hello.filters](variants/filters-32be12c1/hello.filters) created; verification pending |
| `.fsproj` | [hello.fsproj](variants/fsproj-88391edf/hello.fsproj) created; verification pending |
| `.fxml` | [hello.fxml](variants/fxml-eb650f95/hello.fxml) created; verification pending |
| `.glade` | [hello.glade](variants/glade-4f198e5e/hello.glade) created; verification pending |
| `.gml` | [hello.gml](variants/gml-098725fd/hello.gml) created; verification pending |
| `.gmx` | [hello.gmx](variants/gmx-eb1b5e23/hello.gmx) created; verification pending |
| `.gpx` | [hello.gpx](variants/gpx-26da0cc3/hello.gpx) created; verification pending |
| `.grxml` | [hello.grxml](variants/grxml-89e50f7a/hello.grxml) created; verification pending |
| `.gst` | [hello.gst](variants/gst-7fb857dd/hello.gst) created; verification pending |
| `.hzp` | [hello.hzp](variants/hzp-e1b0b97d/hello.hzp) created; verification pending |
| `.icls` | [hello.icls](variants/icls-fc92fcca/hello.icls) created; verification pending |
| `.iml` | [hello.iml](variants/iml-32c4fd41/hello.iml) created; verification pending |
| `.ivy` | [hello.ivy](variants/ivy-a48ad6c0/hello.ivy) created; verification pending |
| `.jelly` | [hello.jelly](variants/jelly-137dfe6a/hello.jelly) created; verification pending |
| `.jsproj` | [hello.jsproj](variants/jsproj-4a03cba5/hello.jsproj) created; verification pending |
| `.kml` | [hello.kml](variants/kml-ea546317/hello.kml) created; verification pending |
| `.launch` | [hello.launch](variants/launch-a111fb5d/hello.launch) created; verification pending |
| `.mdpolicy` | [hello.mdpolicy](variants/mdpolicy-130ff745/hello.mdpolicy) created; verification pending |
| `.meta4` | [hello.meta4](variants/meta4-255640ee/hello.meta4) created; verification pending |
| `.mjml` | [hello.mjml](variants/mjml-ecfe81f3/hello.mjml) created; verification pending |
| `.mm` | [hello.mm](variants/mm-1354547c/hello.mm) created; verification pending |
| `.mod` | [hello.mod](variants/mod-282b9d03/hello.mod) created; verification pending |
| `.mojo` | [hello.mojo](variants/mojo-af65e82b/hello.mojo) created; verification pending |
| `.mxml` | [hello.mxml](variants/mxml-f7008a87/hello.mxml) created; verification pending |
| `.natvis` | [hello.natvis](variants/natvis-141b89bb/hello.natvis) created; verification pending |
| `.ncl` | [hello.ncl](variants/ncl-381c21d0/hello.ncl) created; verification pending |
| `.ndproj` | [hello.ndproj](variants/ndproj-700c55a6/hello.ndproj) created; verification pending |
| `.nproj` | [hello.nproj](variants/nproj-86104a21/hello.nproj) created; verification pending |
| `.nuspec` | [hello.nuspec](variants/nuspec-a8a3258d/hello.nuspec) created; verification pending |
| `.odd` | [hello.odd](variants/odd-d1e2aae1/hello.odd) created; verification pending |
| `.osm` | [hello.osm](variants/osm-f6d9c802/hello.osm) created; verification pending |
| `.pkgproj` | [hello.pkgproj](variants/pkgproj-401ae7dc/hello.pkgproj) created; verification pending |
| `.pluginspec` | [hello.pluginspec](variants/pluginspec-34c2c898/hello.pluginspec) created; verification pending |
| `.proj` | [hello.proj](variants/proj-cab74e0c/hello.proj) created; verification pending |
| `.props` | [hello.props](variants/props-9ee050f6/hello.props) created; verification pending |
| `.ps1xml` | [hello.ps1xml](variants/ps1xml-09e83984/hello.ps1xml) created; verification pending |
| `.psc1` | [hello.psc1](variants/psc1-a69b79ce/hello.psc1) created; verification pending |
| `.pt` | [hello.pt](variants/pt-e566345e/hello.pt) created; verification pending |
| `.pubxml` | [hello.pubxml](variants/pubxml-c1e93c09/hello.pubxml) created; verification pending |
| `.qhelp` | [hello.qhelp](variants/qhelp-b2335ca8/hello.qhelp) created; verification pending |
| `.rbxmx` | [hello.rbxmx](variants/rbxmx-9c1dfdc9/hello.rbxmx) created; verification pending |
| `.rdf` | [hello.rdf](variants/rdf-51d7c4fe/hello.rdf) created; verification pending |
| `.res` | [hello.res](variants/res-93ede235/hello.res) created; verification pending |
| `.resx` | [hello.resx](variants/resx-7d4ecbae/hello.resx) created; verification pending |
| `.rs` | [hello.rs](variants/rs-fbdde0c3/hello.rs) created; verification pending |
| `.rss` | [hello.rss](variants/rss-e389da7b/hello.rss) created; verification pending |
| `.sch` | [hello.sch](variants/sch-5766dac2/hello.sch) created; verification pending |
| `.scxml` | [hello.scxml](variants/scxml-4ab24e2f/hello.scxml) created; verification pending |
| `.sfproj` | [hello.sfproj](variants/sfproj-0a8b1485/hello.sfproj) created; verification pending |
| `.shproj` | [hello.shproj](variants/shproj-1e30c6ee/hello.shproj) created; verification pending |
| `.slnx` | [hello.slnx](variants/slnx-80464f8e/hello.slnx) created; verification pending |
| `.srdf` | [hello.srdf](variants/srdf-e2c0f37e/hello.srdf) created; verification pending |
| `.storyboard` | [hello.storyboard](variants/storyboard-e404945f/hello.storyboard) created; verification pending |
| `.sublime-snippet` | [hello.sublime-snippet](variants/sublime-snippet-26117df4/hello.sublime-snippet) created; verification pending |
| `.sw` | [hello.sw](variants/sw-a70f7da6/hello.sw) created; verification pending |
| `.targets` | [hello.targets](variants/targets-350b67c2/hello.targets) created; verification pending |
| `.tml` | [hello.tml](variants/tml-20a68624/hello.tml) created; verification pending |
| `.ts` | [hello.ts](variants/ts-538a6c01/hello.ts) created; verification pending |
| `.tsx` | [hello.tsx](variants/tsx-98711b97/hello.tsx) created; verification pending |
| `.typ` | [hello.typ](variants/typ-1a9210cc/hello.typ) created; verification pending |
| `.ui` | [hello.ui](variants/ui-b4a1142c/hello.ui) created; verification pending |
| `.urdf` | [hello.urdf](variants/urdf-9b84ed91/hello.urdf) created; verification pending |
| `.ux` | [hello.ux](variants/ux-b49ae1c8/hello.ux) created; verification pending |
| `.vbproj` | [hello.vbproj](variants/vbproj-d85ff9d3/hello.vbproj) created; verification pending |
| `.vcxproj` | [hello.vcxproj](variants/vcxproj-68931e67/hello.vcxproj) created; verification pending |
| `.vsixmanifest` | [hello.vsixmanifest](variants/vsixmanifest-267ff99d/hello.vsixmanifest) created; verification pending |
| `.vssettings` | [hello.vssettings](variants/vssettings-d1365d8a/hello.vssettings) created; verification pending |
| `.vstemplate` | [hello.vstemplate](variants/vstemplate-164b322c/hello.vstemplate) created; verification pending |
| `.vxml` | [hello.vxml](variants/vxml-aae052f7/hello.vxml) created; verification pending |
| `.wixproj` | [hello.wixproj](variants/wixproj-881a9958/hello.wixproj) created; verification pending |
| `.workflow` | [hello.workflow](variants/workflow-17728b44/hello.workflow) created; verification pending |
| `.wsdl` | [hello.wsdl](variants/wsdl-3735f2b7/hello.wsdl) created; verification pending |
| `.wsf` | [hello.wsf](variants/wsf-e45d2642/hello.wsf) created; verification pending |
| `.wxi` | [hello.wxi](variants/wxi-83752bb1/hello.wxi) created; verification pending |
| `.wxl` | [hello.wxl](variants/wxl-b636afaf/hello.wxl) created; verification pending |
| `.wxs` | [hello.wxs](variants/wxs-c87e94fa/hello.wxs) created; verification pending |
| `.x3d` | [hello.x3d](variants/x3d-3a1c006e/hello.x3d) created; verification pending |
| `.xacro` | [hello.xacro](variants/xacro-a4317059/hello.xacro) created; verification pending |
| `.xaml` | [hello.xaml](variants/xaml-14ebb983/hello.xaml) created; verification pending |
| `.xib` | [hello.xib](variants/xib-12b224f8/hello.xib) created; verification pending |
| `.xlf` | [hello.xlf](variants/xlf-ee454d21/hello.xlf) created; verification pending |
| `.xliff` | [hello.xliff](variants/xliff-5829fedb/hello.xliff) created; verification pending |
| `.xmi` | [hello.xmi](variants/xmi-6edb7c99/hello.xmi) created; verification pending |
| `.xml.dist` | [hello.xml.dist](variants/xml-dist-b06126e8/hello.xml.dist) created; verification pending |
| `.xmp` | [hello.xmp](variants/xmp-5abdb317/hello.xmp) created; verification pending |
| `.xproj` | [hello.xproj](variants/xproj-9c5ebfdf/hello.xproj) created; verification pending |
| `.xsd` | [hello.xsd](variants/xsd-e7933ad0/hello.xsd) created; verification pending |
| `.xspec` | [hello.xspec](variants/xspec-9187de7b/hello.xspec) created; verification pending |
| `.xul` | [hello.xul](variants/xul-916fc60e/hello.xul) created; verification pending |
| `.zcml` | [hello.zcml](variants/zcml-defc4407/hello.zcml) created; verification pending |
