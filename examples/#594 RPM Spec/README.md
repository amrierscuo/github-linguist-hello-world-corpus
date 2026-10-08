# #594 RPM Spec

Analizzare un RPM spec ed eseguire la fase prep per stampare il saluto.

Tipo canonico `data`, language_id `314`.

Toolchain prevista: RPM rpmbuild.

Dalla cartella dell’esempio:

```sh
rpmbuild -bp --nodeps --define "_topdir /percorso/work/rpm" hello.spec
```

Risultato atteso: spec accettato e fase prep produce Hello, World!.

Il fixture non installa file o pacchetti nel sistema; l’obiettivo è prep e non la distribuzione di un RPM.

Stato registrato: sintassi in attesa; semantica in attesa. Toolchain: RPM4.18.2 original rpmbuild native prep. [Log](verification/result.json). exit 127: ${WORKSPACE_WSL}/work/tools_581_600/ubuntu/usr/bin/rpmbuild: error while loading shared libraries: librpm.so.9: cannot open shared object file: No such file or directory


Fonti:

- [RPM spec](https://rpm.org/docs/4.20.x/manual/spec.html)

## Copertura delle estensioni

Le verifiche del campione principale e delle varianti sono registrate separatamente.

| Estensione | File / stato |
| --- | --- |
| `.spec` | [hello.spec](hello.spec) creato, verifiche pendenti |
