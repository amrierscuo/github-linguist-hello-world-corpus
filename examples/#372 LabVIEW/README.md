# #372 LabVIEW

The example includes three **XML container templates** with the canonical extensions `.lvproj`, `.lvlib`, and `.lvclass`. The root elements `Project`, `Library`, and `LVClass`, and the LVVersion field, follow NI's public examples. These templates need to be completed and saved in LabVIEW; they are not executable graphical VIs.

`Hello.vi` is a dependency that **still needs to be created**. No placeholder VI file is included. The project and library references therefore remain intentionally unresolved. The `.lvclass` contains no private data or methods and needs to be completed in the native editor.

## User-requested procedure

1. Open or recreate the project in LabVIEW and create `Hello.vi` in the same folder.
2. Add a string indicator to the Front Panel.
3. Add a `Hello, World!` string constant to the Block Diagram and wire it to the indicator.
4. Save the VI and the containers in the IDE, then run the VI and check the greeting.
5. If the VI belongs to the library, confirm that the project includes it through the library, then save the resolved references.

The container files were created as templates. **LabVIEW syntax and semantics remain unverified.** Reading the XML alone does not count as LabVIEW verification.

Sources: user-provided material and NI container structures at https://github.com/ni/labview-memory-management-tools ; https://www.ni.com/en/support/documentation/supplemental/07/labview-project-file-format.html

## Extension coverage

Checks for the main example and its variants are recorded separately.

| Extension | File / status |
| --- | --- |
| `.lvproj` | [Hello.lvproj](Hello.lvproj) created, verification pending |
| `.lvclass` | [Hello.lvclass](Hello.lvclass) created, verification pending |
| `.lvlib` | [Hello.lvlib](Hello.lvlib) created, verification pending |
