# 0703: TSV: `.vcf`

Variant Call Format: Synthetic data in TSV columns with VCF header and GREETING field; not a vCard.

Provenience: original example written for the role of this suffix.

Artefatto principale: `hello.vcf`.

Control provided, from the folder of the variant:

```text
bcftools view hello.vcf -Ov -o work/parsed.vcf
```

Expected result: VCF accepted and INFO.GREETING decoding Hello, World!.

Status: created; syntax and behavior not verified.

This variant has not yet been subjected to its original parser/compiler/host.

Primary sources:

- [https://samtools.github.io/hts-specs/VCFv4.3.pdf](https://samtools.github.io/hts-specs/VCFv4.3.pdf)
