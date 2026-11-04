# #594 RPM Spec

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
| `.spec` | [hello.spec](hello.spec) created; verification pending |
