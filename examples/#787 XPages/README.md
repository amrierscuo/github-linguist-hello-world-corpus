# #787 XPages

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Upload a custom XPages control configured to show Hello, World!.

L’artefatto canonico .xsp-config registra il controllo, namespace, tag e file composito. La fixture .xsp contiene il valore da renderizzare. Non si attribuisce una verifica XPages alla sola buona formazione XML.

## Toolchain and reproduction

HCL Domino Designer/XPages, versione da registrare

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
Domino Designer: importare Greeting.xsp-config e Greeting.xsp nella cartella CustomControls, compilare e inserire il controllo Greeting in una pagina di prova
```

## Expected result and status

Controllo Greeting renderizzato con Hello, World!.

Artifact created: yes. syntax verified: no. behavior verified: no.

Documented source; no original parser/compiler/runtime performed for this item.

Commitments: Domino Designer/XPages unavailable; component parser and hanging renderings.

## Primary sources

- https://help.hcl-software.com/dom_designer/10.0.1/basic/H_CUSTOM_CONTROLS_IN_ECLIPSE.html

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.xsp-config` | [Greeting.xsp-config](Greeting.xsp-config) created; verification pending |
| `.xsp.metadata` | artifact to generate Designer XPages metadata with schema/versione unidentified owners: there is a reliable structure for this compound suffix and no .xsp. control is renamed |
