# microbial_RNAseq_processing

Script to process raw data in FASTQ format for microbial RNA-seq (RNAtag-seq)

We have tested these scripts on Linux.

## Dependencies

* Python 2.7.15
	- os
	- sys
* rnammer 1.2
* cutadapt

### Description
```
usage: main.py ./configure.txt

Script to process raw data in FASTQ format for microbial RNA-seq (RNAtag-seq).

All Input Parameters can be found and changed in configure.txt:

run_on_cluster:	TRUE or FALSE
	- if the program is running on a ParallelCluster (Amazon Web Services) or local computer 

number_of_core:	48 (numbers between 1 to 96)
	- numbers of CPU cores used for processing

pipeline_bin_PATH: [path to folder]
	- path to the master folder for all binaries

house_bin_PATH: ./bin
	- local Python script for processing


output_script_PATH: ./script
	- path to output script files

output_temp_PATH: ./temp
	- path to temporary files

output_Stat_PATH: ./summary.txt
	- path to output stastics file

output_PATH: ./output
	- path to output folder containing results

num_of_pool: 2
	- number of pooled RNAtag-seq library

label: temp
	- prefix of output files

sample_info_dir: ./sampleInfo
	- path to sample information files

adapter_file: ./adapter.txt
	- path to adapter file

genome_dir: ./assembled_genome
	- path to reference genomes

strain_list: ./strainTotal
	- path to list of strains used in the processing

readsPrefix: ./rawdata
	- path to raw reads in FASTQ format

reads1_p1: Pool1.R1.fastq.gz
reads2_p1: Pool1.R2.fastq.gz
	- file name of reads-1&2 for Pool1

reads1_p2: Pool1.R1.fastq.gz
reads2_p2: Pool1.R2.fastq.gz
	- file name of reads-1&2 for Pool2

```

### Output format

****[example of output stastics]****

```
label	strain	condition	bio_rep	tech_rep	poolID	adapterID	total reads	reads with N	phiX reads	poly-G reads	reads passing all filters	reads passing all filters (ratio)	reads mapped to rRNA	rRNA mapping ratio	reads mapped to 23S	23S mapping ratio	reads mapped to 16S	16S mapping ratio	reads mapped to 5S	5S mapping ratio	reads mapped to genome	ratio of reads mapped to genome + rRNA	genome mapping ratio	reads after PCR removal	unique reads ratio	reads mapped to CDS	CDS mapping ratio
P3wC11_Tet_1_1	P3wC11	Tet	1	1	pool1	adap1	1793144	524	2004	10177	1779506	0.992394364	3201	0.001798814	1870	0.58419244	863	0.269603249	468	0.146204311	1742304	0.980893012	0.98085858	96314	0.055279676	1593872	0.91480706
P3wC11_Tet_2_1	P3wC11	Tet	2	1	pool1	adap2	1516919	404	1708	8895	1505522	0.992486745	2578	0.001712363	1699	0.659038014	573	0.222265322	306	0.118696664	1477327	0.982984639	0.982955453	88087	0.059625933	1357253	0.918722124
P3wC11_Tet_3_1	P3wC11	Tet	3	1	pool1	adap3	1337086	365	1301	7607	1326942	0.992413353	1688	0.001272098	958	0.567535545	510	0.302132701	220	0.130331754	1300943	0.981678928	0.981655592	80452	0.061841295	1199997	0.922405517
...
```

****[example of reads count: ./output/5.expression]****
```
Geneid	Chr	Start	End	Strand	Length	P3wC11_Tet_1_1	P3wC11_Tet_2_1	P3wC11_Tet_3_1	P3wC11_Strep_1_1	P3wC11_Strep_2_1	P3wC11_Strep_3_1	P3wC11_Cefox_1_1
AJKBPMOI_00001	P3wC11.0	279	1859	+	1581	266	311	226	905	740	730	133
AJKBPMOI_00002	P3wC11.0	1973	3304	+	1332	35	49	21	19	46	66	0
AJKBPMOI_00003	P3wC11.0	3301	3858	+	558	37	17	15	1	5	35	0
...
```

****[example of TPM calulation: ./output/5.expression]****
```
geneID	P3wC11_Tet_1_1	P3wC11_Tet_2_1	P3wC11_Tet_3_1	P3wC11_Strep_1_1	P3wC11_Strep_2_1	P3wC11_Strep_3_1	P3wC11_Cefox_1_1
AJKBPMOI_00001	69.72698148	96.2463551	79.34530236	238.5121144	175.4835885	178.7589387	227.1148468
AJKBPMOI_00002	10.88967498	17.99896894	8.751041031	5.943511527	12.94762951	19.18299829	0
AJKBPMOI_00003	27.4801199	14.90632188	14.92112987	0.74672301	3.359483113	24.28346314	0
...
```

****For academic use only****
