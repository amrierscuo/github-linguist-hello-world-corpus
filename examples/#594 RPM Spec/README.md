# #594 RPM Spec

## Latest recorded verification

**Syntax and behavior verified** on November 4, 2026.

The native RPM parser accepted the spec and rpmbuild ran %prep, printing the exact greeting. No packages were installed and no RPM was built.

[Native commands, versions, outputs and SHA-256](verification/native_20261104_followup_main.json). [Earlier evidence](verification/result.json).

## Extension results

- `.spec`: syntax and behavior verified.

<details>
<summary>Original instructions and earlier status</summary>

Analyze a RPM spec and perform the prep phase to print the greeting.

Canonical type `data`, language_id `314`.

Suggested toolchain: RPM rpmbuild.

From the example directory:

```sh
rpmbuild -bp --nodeps --define "_topdir /percorso/work/rpm" hello.spec
```

Expected result: accepted spec and prep phase produces Hello, World!.

The fixture does not install files or packages in the system; the target is prep and not the distribution of a RPM.

Registered state: syntax and behavioral verification pending. Toolchain: RPM4.18.2 original rpmbuild native prep. [Log](verification/result.json). exit 127: ${WORKSPACE_WSL}/work/tools_581_600/ubuntu/usr/bin/rpmbuild: error while loading shared libraries: librpm.so.9: cannot open shared object file: No such file or directory


Sources:

- [RPM spec](https://rpm.org/docs/4.20.x/manual/spec.html)

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.spec` | [hello.spec](hello.spec) syntax and behavior verified |

</details>
