# 0703 — TSV — `.vcf`

Variant Call Format: dati sintetici in colonne TSV con header VCF e campo GREETING; non una vCard.

Provenienza: esempio originale scritto per il ruolo di questo suffisso.

Artefatto principale: `hello.vcf`.

Controllo previsto, dalla cartella della variante:

```text
bcftools view hello.vcf -Ov -o work/parsed.vcf
```

Risultato atteso: VCF accettato e INFO.GREETING decodifica Hello, World!.

Stato: creato; sintassi e semantica non verificate.

Questa variante non è ancora stata sottoposta al suo parser/compiler/host originale.

Fonti primarie:

- [https://samtools.github.io/hts-specs/VCFv4.3.pdf](https://samtools.github.io/hts-specs/VCFv4.3.pdf)
