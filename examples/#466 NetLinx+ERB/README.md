# #466 NetLinx+ERB

Canonical entry and order from reference/languages.yml. The source and fixtures are original.

## Goal

Render NetLinx+ ERB and get the startup program with Hello, World!.

ERB.new /result(binding) interpolates audience in .axs.erb template and produces NetLinx source. The test really checks the ERB renderr; the compilazione/esecuzione NetLinx of the result remains pending.

## Toolchain and reproduction

ERB original Ruby3.2.3; compiler/runtime NetLinx not prepared

Commands from the example folder; use tools installed in PATH and a temporary copy for build/output. The test dependencies are isolated in work.

```text
ruby render.rb
```

## Expected result and status

Source rendered contains SEND_STRING0 with Hello, World!.

Artifact created: yes. syntax verified: yes. behavior verified: no.

The verification/toolchain.json log records SHA-256 of the sources, provenance and versions, actual commands, exit/stdout/stderr and test scope.

Commitments: Compiler/runtime NetLinx not available; behavior of target pendant.

## Primary sources

- https://docs.ruby-lang.org/en/3.2/ERB.html
- https://www.amx.com/ko/site_elements/amx-language-reference-guide-netlinx-programming-language

## Extension coverage

Verification of the main sample and each variant is recorded separately.

| Extension | File / status |
| --- | --- |
| `.axs.erb` | [hello.axs.erb](hello.axs.erb) syntax verified |
| `.axi.erb` | [hello.axi.erb](variants/axi-erb-3273de56/hello.axi.erb) created; verification pending |
