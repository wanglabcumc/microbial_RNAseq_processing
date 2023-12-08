# microbial_RNAseq_processing

Design tools for Mutagenesis by Template-guided Amplicon Assembly (MEGAA)

We have tested these scripts on Linux and MacOS.

<p align="center">
  <img src="https://github.com/hym0405/MEGAdt/blob/main/misc/MEGAAdt_pipeline.png" width="842" title="hover text">
</p>

## Dependencies

* Python 3.9.7
	- os
	- sys
	- argparse
	- [Biopython](https://biopython.org/) - for melting temperature calculation

### Description
```
usage: MEGAAdt.py [-f FASTA] [-i VARIANT] [-o OUTPUT] [Optional arguments]

Design tools for Mutagenesis by Template-guided Amplicon Assembly (MEGAA). See details in https://github.com/hym0405/MEGAAdt

Input and output [Required]:
  -f FASTA, --fasta FASTA
                        Input template sequences in FASTA format (See example: ./test_input/input_seq.fasta)
  -i VARIANT, --variant VARIANT
                        Input variants information in tab-separated table (See example: ./test_input/variant_info.tsv)
  -o OUTPUT, --output OUTPUT
                        Prefix of output files; [output].variant.fasta and [output].oligo.tsv will be generated

Oligo design [Optional]:
  -el END_LENGTH, --end_length END_LENGTH
                        Minimum number of perfectly matched bases (nt) at the end of mutagenesis oligo (both 3' and 5')' [default: 10]
  -gc3 {0,1}, --gc_clamp3 {0,1}
                        # of GC bases (nt) required at 3' end of mutagenesis oligo. The value should be either 1 or 0 [default: 1]
  -Tm5 MELTING5, --melting5 MELTING5
                        Minimum melting temperature (°C) at 5' end of mutagenesis oligos [default: 35]
  -Tm3h MELTING3_HIGH, --melting3_high MELTING3_HIGH
                        Upper limit of gradient melting temperature (°C) at 3' end of mutagenesis oligos [default: 65]
  -Tm3l MELTING3_LOW, --melting3_low MELTING3_LOW
                        Lower limit of gradient melting temperature (°C) at 3' end of mutagenesis oligos [default: 50]

Warning information [Optional]:
  -wg WARNING_GAP, --warning_gap WARNING_GAP
                        Minimum number of gaps (nt) between oligo to print warnings [default: 5]
  -wl WARNING_LENGTH, --warning_length WARNING_LENGTH
                        Minimum length of oligos to print warnings [default: 60]
  -h, --help            show this help message and exit
```

### Input format

**Input template sequences:** Input template sequences in FASTA format.

****[example: ./test_input/input_seq.fasta]****

```
>rsgA
CCATTGTTTTGTCGTTCCTGAT...
...
>pheS
ATGTCACATCTCGCAGAACTGG...
...
>AAVcap
ATGGCTGCCGATGGTTATCTTC...
...
```

**Input variants information:** Information of desired mutations of each variant. Variants can be SNPs, multiple-SNPs, insertions or deletions but at least one base is required in Reference_base (column-4) and Alternative_base (column-5).

****[Important] Positions of mutations (column-3) are 1-based****

****[Important] Template of variants (column-2) should match with input template sequences****

****[example: ./test_input/variant_info.tsv]****

```
Variant		Template	Position	Reference_base	Alternative_base
## single-site mutations
pheS_variant	pheS		397		A		G
pheS_variant	pheS		559		A		G
...
## multiple-sites mutations
rsgA_variant	rsgA		255		TAA		GAG
rsgA_variant	rsgA		408		CGA		GCT
...
## insertion and deletion
AAVcap_variant	AAVcap		416		C		CTGA
AAVcap_variant	AAVcap		570		GCCA		G
...
```

### Output format

****Results of mutagensis oligo designs ([output_prefix].oligo.tsv) and final sequences of desired variants ([output_prefix].variant.fasta)****

****[example of mutagensis oligo designs: ./test_output/output.oligo.tsv]****
```
Variant		Template	Primer			Start_site	Sequence				Length	Tm_5p	Tm_3p	Mutations	Notes				Warnings
rsgA_variant	rsgA		rsgA_variant-P0		1		CCATTGTTTTGTCGTTC			17	0	51.5			Extension F-primer	
rsgA_variant	rsgA		rsgA_variant-P1		244		TTACACAGACCgagATAGTCATGGAATTCGAC	32	35.4	55.3	255_TAA_GAG		
rsgA_variant	rsgA		rsgA_variant-P2		398		GACCGAGCCCgctGTTGTCAGAGATATCGTTG	32	43.8	57.3	408_CGA_GCT			
...
pheS_variant	pheS		pheS_variant-P5		326		TTACCCGTACCgTCGACCGTgTCGAAAGTTTCTTCGGTG	39	38.9	59.2	337_A_G;346_A_G	Contains multiple mutations	
pheS_variant	pheS		pheS_variant-P6		387		CGGGCCGGAAgTCGAAGACGATTATCATAACTTC	34	47.6	61	397_A_G		
...
AAVcap_variant	AAVcap		AAVcap_variant-P2	405		TGTTAAGACGGctgaTCCGGGAAAAAAGAGG		31	36.5	56.5	416_C_CTGA
AAVcap_variant	AAVcap		AAVcap_variant-P3	560		CTCTCGGACAgCCAGCAGCCCCCTC		25	36	61.4	570_GCCA_G
...
```

****[example of final sequences of desired variants: ./test_output/output.variant.fasta]****
```
>rsgA_variant
CCATTGTTTTGTCGTTCCTGAT...
...
>pheS_variant
ATGTCACATCTCGCAGAACTGG...
...
>AAVcap_variant
ATGGCTGCCGATGGTTATCTTC...
...
```

### Script example
```
python3 ./MEGAAdt.py -f ./test_input/input_seq.fasta \
		-i ./test_input/variant_info.tsv \
		-o ./test_output/output
```



### Optional parameters

****Oligo design****

* ****end_length****: Minimum number of perfectly matched bases (nt) at the 3' end and 5' end of mutagenesis oligo. 10nt is recommended in most cases and desired mutations with less than 2x [end_length] gap (nt) will be covered by the same mutagensis oligo.
* ****gc_clamp3****: # of GC bases (nt) required at 3' end of mutagenesis oligo. value 1 means 3' end of the oligo need to be a G or C (We found 1nt 3' GC clamp will yield higher MEGAA efficiency)
* ****melting5****: Minimum melting temperature (°C) at 5' end of mutagenesis oligos. 35°C is recommended in most cases 
* ****melting3_low and melting3_high****: Lower limit and Upper limit of gradient melting temperature (°C) at 3' end of mutagenesis oligos. 50°C and 65°C is default value and the limit can be optimized if there are >20 desired mutations but melting3_low need to be greater than 45°C.

****Warning information****
* ****warning_gap****: print this warning if the gaps (nt) between mutagenesis oligo and the upstream oligo is less than [warning_gap]
* ****warning_length****: print this warning if mutagenesis oligo is longer than [warning_length]nt

<br>
<br>


****For academic use only****

Patent Pending

Copyright © [2022] The Trustees of Columbia University in the City of New York. All Rights Reserved.

Use is subject to the terms of the License Agreement. 
