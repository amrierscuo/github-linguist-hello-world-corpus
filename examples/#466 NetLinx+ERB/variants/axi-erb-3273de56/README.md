# 0466: NetLinx+ERB: `.axi.erb`

Role: ERB Template includes NetLinx with greeting function and audience assignment, not .axs. program

Origin: Original source written for the specific role of the variant, using the mentioned documentation.

Required toolchain: ERB originale Ruby3.2.3; compiler/runtime NetLinx non preparati. The exact toolchain version for this variant was not verified in this batch.

Proposed verification procedure, not performed, by the directory of the variant:

```text
ruby render.rb; poi NetLinx Studio include di hello.axi nel progetto di test
```

Expected result: Includes generated with Hello, World!; runtime hanging controller

Individual status: artifact created `true`, syntax verified `false`, behavior verified `false`. Greeting data or configuration alone does not establish execution.

Blockers:

- The variant has not been subject to a new test of the original parser/compiler/runtime; the verifications of the main source are not inherited.

SHA-256 of variant files:

- `hello.axi.erb`: `8c2441b28ea9f2841dbd7201f8b3b2d25a62270aaa3d78f438f0ab89d80c24f5`
- `render.rb`: `710ac885e567c3889f2fb6584fc759c193dd42d50c243cd2feaae3f6ff7df69e`

Primary sources:

- https://docs.ruby-lang.org/en/3.2/ERB.html
- https://www.amx.com/ko/site_elements/amx-language-reference-guide-netlinx-programming-language
