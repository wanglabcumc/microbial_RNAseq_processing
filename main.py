#!/usr/bin/env python
import os
import sys
def main():
    print "start!"
    config = sys.argv[1]
    configPara = readConfigure(config)

    
#############################
###  Process script files ###
############################# 
       
    os.system("python " + configPara["pipeline_bin_PATH"] + "/script/modifyrnammerLoc.py " + configPara["pipeline_bin_PATH"] + "/" + \
                "rnammer-1.2/rnammer " + configPara["pipeline_bin_PATH"] + "/rnammer-1.2/rnammer " + \
                configPara["pipeline_bin_PATH"] + "/rnammer-1.2 " + configPara["pipeline_bin_PATH"] + "/hmmer-2.3.1/bin/hmmsearch")
    os.system("python " + configPara["pipeline_bin_PATH"] + "/script/modifyPythonProgramLoc.py " + configPara["pipeline_bin_PATH"] + \
                "/anaconda2/bin/poretools " + configPara["pipeline_bin_PATH"] + "/anaconda2/bin/poretools " + \
                configPara["pipeline_bin_PATH"] + "/anaconda2/bin/python2")
    os.system("python " + configPara["pipeline_bin_PATH"] + "/script/modifyPythonProgramLoc.py " + configPara["pipeline_bin_PATH"] + \
                "/anaconda2/bin/ipdSummary " + configPara["pipeline_bin_PATH"] + "/anaconda2/bin/ipdSummary " + \
                configPara["pipeline_bin_PATH"] + "/anaconda2/bin/python2")
    os.system("python " + configPara["pipeline_bin_PATH"] + "/script/modifyPythonProgramLoc.py " + configPara["pipeline_bin_PATH"] + \
                "/binary/unicycler " + configPara["pipeline_bin_PATH"] + "/binary/unicycler " + \
                configPara["pipeline_bin_PATH"] + "/anaconda3/bin/python")
    os.system("python " + configPara["pipeline_bin_PATH"] + "/script/modifyPythonProgramLoc.py " + configPara["pipeline_bin_PATH"] + \
                "/anaconda3/bin/unicycler " + configPara["pipeline_bin_PATH"] + "/anaconda3/bin/unicycler " + \
                configPara["pipeline_bin_PATH"] + "/anaconda3/bin/python")
    os.system("python " + configPara["pipeline_bin_PATH"] + "/script/modifyPythonProgramLoc.py " + configPara["pipeline_bin_PATH"] + \
                "/anaconda3/bin/cutadapt " + configPara["pipeline_bin_PATH"] + "/anaconda3/bin/cutadapt " + \
                configPara["pipeline_bin_PATH"] + "/anaconda3/bin/python")
    os.system("chmod +x " + configPara["house_bin_PATH"] + "/*")
    
    
    os.system("mkdir -p " + configPara["output_temp_PATH"])
    os.system("mkdir -p " + configPara["output_script_PATH"])
    os.system("mkdir -p " + configPara["output_PATH"])

    
###############################
### Process configure Files ###
###############################
    """
    os.system("python " + configPara["house_bin_PATH"] + "/adatperTxt2Fa.py " + configPara["adapter_file"] + \
                " " + configPara["output_temp_PATH"] + "/adapter.fa")
    for i in range(int(configPara["num_of_pool"])):
        os.system("python " + configPara["house_bin_PATH"] + "/SampleInfo2BCTag.py " + configPara["sample_info_dir"] + \
                    "/sampleInfo_p" + str(i + 1) + ".txt " + configPara["adapter_file"] + " " + \
                    configPara["output_temp_PATH"] + "/barcodeTag_p" + str(i + 1) + ".txt")
    os.system("rm -f " + configPara["output_temp_PATH"] + "/barcodeTag_merge.txt")
    for i in range(int(configPara["num_of_pool"])):
        os.system("cat " + configPara["output_temp_PATH"] + "/barcodeTag_p" + str(i + 1) + ".txt >> " + \
                    configPara["output_temp_PATH"] + "/barcodeTag_merge.txt")
    """

#####################################################################
### Extract annotation file of genomes and gather CDS information ###
#####################################################################

    """
    strainList = readStrainList(configPara["strain_list"])    
    for eachStrain in strainList:

        f = open(configPara["output_script_PATH"] + "/referenceBuild." + eachStrain + ".sh","w")
        writeHeader(f,configPara["pipeline_bin_PATH"],"reference." + eachStrain, configPara["number_of_core"])
        

        f.writelines(["bowtie2-build " + configPara["output_PATH"] + "/reference_genome/" + eachStrain + ".rename.fa " + \
                    configPara["output_PATH"] + "/reference_genome/" + eachStrain + ".rename" + os.linesep])

        f.close()
        os.system("bash " + configPara["output_script_PATH"] + "/referenceBuild." + eachStrain + ".sh")
    """

#############################################################
### Demultiplex Reads for different condition using sabre ###
#############################################################
    
    """
    os.system("mkdir -p " + configPara["output_PATH"] + "/0.barcodeDemultiplex")
    for i in range(int(configPara["num_of_pool"])):
        os.system("python " + configPara["house_bin_PATH"] + "/makeBarcodeTag.py " + configPara["output_temp_PATH"] + \
                    "/barcodeTag_p" + str(i + 1) + ".txt " + configPara["output_PATH"] + "/0.barcodeDemultiplex/" + \
                    configPara["label"] + ".p" + str(i + 1) + ".txt " + configPara["output_PATH"] + \
                    "/0.barcodeDemultiplex/" + configPara["label"]) 
    
    for i in range(int(configPara["num_of_pool"])):
        f = open(configPara["output_script_PATH"] + "/demultiplex.p" + str(i + 1) + ".sh","w")
        writeHeader(f,configPara["pipeline_bin_PATH"],"demultiplex.p" + str(i + 1), configPara["number_of_core"])
        f.writelines([configPara["house_bin_PATH"] + "/sabre pe -f " + configPara["readsPrefix"] + "/" + configPara["reads2_p" + str(i + 1)] + \
                    " -r " + configPara["readsPrefix"] + "/" + configPara["reads1_p" + str(i + 1)] + " -b " + configPara["output_PATH"] + \
                    "/0.barcodeDemultiplex/" + configPara["label"] + ".p" + str(i + 1) + ".txt" + \
                    " -u " + configPara["output_PATH"] + "/0.barcodeDemultiplex/" + configPara["label"] + \
                    "_unknown.p" + str(i + 1) + ".R2.fq -w " + configPara["output_PATH"] + "/0.barcodeDemultiplex/" + \
                    configPara["label"] + "_unknown.p" + str(i + 1) + ".R1.fq -m 1 &> " + configPara["output_PATH"] +\
                    "/0.barcodeDemultiplex/log.p" + str(i + 1) + os.linesep])
        f.close()
        os.system("bash " + configPara["output_script_PATH"] + "/demultiplex.p" + str(i + 1) + ".sh")
    

#    os.system("rm -f " + configPara["output_PATH"] + "/0.barcodeDemultiplex/" + configPara["label"] + ".*.R2.fq")
#    os.system("rm -f " + configPara["output_PATH"] + "/0.barcodeDemultiplex/" + configPara["label"] + "_unknown.*.fq")
    """

    """
    strainList = readStrainList(configPara["strain_list"])
    sampleList = readBarcodeTag(configPara["output_temp_PATH"] + "/barcodeTag_merge.txt")
    
    os.system("mkdir -p " + configPara["output_PATH"] + "/1.phixRemove")    
    os.system("mkdir -p " + configPara["output_PATH"] + "/2.adatperTrimAndQC")
    os.system("mkdir -p " + configPara["output_PATH"] + "/3.rRNAremoval")
    os.system("mkdir -p " + configPara["output_PATH"] + "/4.bowtieMap")
    os.system("mkdir -p " + configPara["output_PATH"] + "/5.expression/count")
    os.system("mkdir -p " + configPara["output_PATH"] + "/6.genomicCov")

    for eachSample in sampleList:
        tmpSample = eachSample.split("_")
        sample_ref = tmpSample[0]

        f = open(configPara["output_script_PATH"] + "/filterMap." + eachSample + ".sh","w")
        writeHeader(f,configPara["pipeline_bin_PATH"],"filterMap." + eachSample, configPara["number_of_core"])
          
        ###################################
        ### Remove reads mapped to PhiX ###
        ###################################
        f.writelines(["cutadapt --max-n 0 -o " + configPara["output_PATH"] + "/1.phixRemove/" + configPara["label"] + "." + \
                    eachSample + ".N_filtered.fq " + configPara["output_PATH"] + "/0.barcodeDemultiplex/" + configPara["label"] + \
                    "." + eachSample + ".R1.fq -j " + configPara["number_of_core"] + " &> " + configPara["output_PATH"] + "/1.phixRemove/" + \
                    eachSample + ".N_filtered.log" + os.linesep])
        f.writelines(["bowtie2 --very-sensitive -x " + configPara["phiX"] + " -U " + configPara["output_PATH"] + "/1.phixRemove/" + \
                    configPara["label"] + "." + eachSample + ".N_filtered.fq -S " + configPara["output_PATH"] + "/1.phixRemove/" + \
                    configPara["label"] + "." + eachSample + ".phiX_map.sam --un " + configPara["output_PATH"] + "/1.phixRemove/" + \
                    configPara["label"] + "." + eachSample + ".phiX_filtered.fq -p " + configPara["number_of_core"] + " &> " + \
                    configPara["output_PATH"] + "/1.phixRemove/" + eachSample + ".phiX_filter.log" + os.linesep])
        f.writelines(["rm -f " + configPara["output_PATH"] + "/1.phixRemove/" + configPara["label"] + "." + eachSample + ".phiX_map.sam" + os.linesep])
        f.writelines(["rm -f " + configPara["output_PATH"] + "/1.phixRemove/" + configPara["label"] + "." + eachSample + ".N_filtered.fq" + os.linesep])
        
        ##################################################################
        ### Trim adapter from reads and remove reads with poor quality ###
        ##################################################################
        
        f.writelines(["cutadapt -a GGGGGGGGGGGGGGGGGGGG -m 20 -o " + configPara["output_PATH"] + "/2.adatperTrimAndQC/" + configPara["label"] + \
                    "." + eachSample + ".polyG_filtered.fq " + configPara["output_PATH"] + "/1.phixRemove/" + configPara["label"] + "." + \
                    eachSample + ".phiX_filtered.fq -j " + configPara["number_of_core"] + " --discard-trimmed &> " + configPara["output_PATH"] + \
                    "/2.adatperTrimAndQC/" + eachSample + ".polyG_filter.log" + os.linesep])
        f.writelines(["cutadapt -a file:" + configPara["output_temp_PATH"] + "/adapter.fa -m 20 -e 0.2 --nextseq-trim=20 -j " + 
                    configPara["number_of_core"] + " -u 5 -o " + configPara["output_PATH"] + "/2.adatperTrimAndQC/" + configPara["label"] + \
                    "." + eachSample + ".qc.fq " + configPara["output_PATH"] + "/2.adatperTrimAndQC/" + configPara["label"] + "." + \
                    eachSample + ".polyG_filtered.fq -j " + configPara["number_of_core"] + " &> " + configPara["output_PATH"] + \
                    "/2.adatperTrimAndQC/" + eachSample + ".adapter_remove_QC.log" + os.linesep])
        f.writelines(["rm -f " + configPara["output_PATH"] + "/2.adatperTrimAndQC/" + configPara["label"] + "." + eachSample + \
                    ".polyG_filtered.fq" + os.linesep])
        

        ######################################################
        ### Remove rRNA from processed reads using Bowtie2 ###
        ######################################################

        f.writelines(["bowtie2 --very-sensitive -x " + configPara["output_PATH"] + "/reference_genome/" + sample_ref + ".rRNA -U " + \
                    configPara["output_PATH"] + "/2.adatperTrimAndQC/" + configPara["label"] + "." + eachSample + ".qc.fq -S " + \
                    configPara["output_PATH"] + "/3.rRNAremoval/" + configPara["label"] + "." + eachSample + ".rRNA_map.sam --un " + \
                    configPara["output_PATH"] + "/3.rRNAremoval/" + configPara["label"] + "." + eachSample + ".rRNA_filtered.fq -p " + \
                    configPara["number_of_core"] + " &> " + configPara["output_PATH"] + "/3.rRNAremoval/" + eachSample + \
                    ".rRNA_filter.log" + os.linesep])  

        f.writelines(["python " + configPara["house_bin_PATH"] + "/statrRNAtypes.py " + configPara["output_PATH"] + "/3.rRNAremoval/" + \
                    configPara["label"] + "." + eachSample + ".rRNA_map.sam " + configPara["output_PATH"] + "/reference_genome/" + \
                    sample_ref + ".rRNA.fa " + configPara["output_PATH"] + "/3.rRNAremoval/" + eachSample + ".rRNA_filter_detail.log" + os.linesep])
             
        f.writelines(["rm -f " + configPara["output_PATH"] + "/3.rRNAremoval/" + configPara["label"] + "." + eachSample + ".rRNA_map.sam" + os.linesep])
        
        ###################################################
        ### Map non-rRNA reads to corresponding genomes ###
        ###################################################
        
        f.writelines(["bowtie2 -x " + configPara["output_PATH"] + "/reference_genome/" + sample_ref + ".rename -U " + configPara["output_PATH"] + \
                    "/3.rRNAremoval/" + configPara["label"] + "." + eachSample + ".rRNA_filtered.fq -S " + configPara["output_PATH"] + \
                    "/4.bowtieMap/" + configPara["label"] + "." + eachSample + ".map.sam -p " + configPara["number_of_core"] + \
                    " &> " + configPara["output_PATH"] + "/4.bowtieMap/" + eachSample + ".map.log" + os.linesep]) 

        f.writelines(["samtools view -b -@ " + configPara["number_of_core"] + " " + configPara["output_PATH"] + "/4.bowtieMap/" + \
                    configPara["label"] + "." + eachSample + ".map.sam > " + configPara["output_PATH"] + "/4.bowtieMap/" + \
                    configPara["label"] + "." + eachSample + ".map.bam" + os.linesep])
        f.writelines(["rm -f " + configPara["output_PATH"] + "/4.bowtieMap/" + configPara["label"] + "." + eachSample + ".map.sam" + os.linesep])
        f.writelines(["samtools sort -@ " + configPara["number_of_core"] + " " + configPara["output_PATH"] + "/4.bowtieMap/" + \
                    configPara["label"] + "." + eachSample + ".map.bam > " + configPara["output_PATH"] + "/4.bowtieMap/" + \
                    configPara["label"] + "." + eachSample + ".map.sort.bam" + os.linesep]) 
        f.writelines(["rm -f " + configPara["output_PATH"] + "/4.bowtieMap/" + configPara["label"] + "." + eachSample + ".map.bam" + os.linesep])
        f.writelines(["samtools index -@ " + configPara["number_of_core"] + " " + configPara["output_PATH"] + "/4.bowtieMap/" + \
                    configPara["label"] + "." + eachSample + ".map.sort.bam" + os.linesep])
        f.writelines(["samtools rmdup -s " + configPara["output_PATH"] + "/4.bowtieMap/" + configPara["label"] + "." + eachSample + \
                    ".map.sort.bam " + configPara["output_PATH"] + "/4.bowtieMap/" + configPara["label"] + "." + eachSample + \
                    ".map.sort.rmdup.bam" + os.linesep])
        f.writelines(["samtools index -@ " + configPara["number_of_core"] + " " + configPara["output_PATH"] + "/4.bowtieMap/" + \
                    configPara["label"] + "." + eachSample + ".map.sort.rmdup.bam" + os.linesep])
        f.writelines(["totalAlign=`samtools view -c -q 1 -@ " + configPara["number_of_core"] + " " + configPara["output_PATH"] + \
                    "/4.bowtieMap/" + configPara["label"] + "." + eachSample + ".map.sort.bam`" + os.linesep])
        f.writelines(["alignRMdup=`samtools view -c -q 1 -@ " + configPara["number_of_core"] + " " + configPara["output_PATH"] + \
                    "/4.bowtieMap/" + configPara["label"] + "." + eachSample + ".map.sort.rmdup.bam`" + os.linesep])
        f.writelines(["echo \"Total mapped reads: $totalAlign\" > " + configPara["output_PATH"] + "/4.bowtieMap/" + eachSample + \
                    ".PCRdup.log" + os.linesep])
        f.writelines(["echo \"Total reads after PCR duplication removal: $alignRMdup\" >> " + configPara["output_PATH"] + \
                    "/4.bowtieMap/" + eachSample + ".PCRdup.log" + os.linesep])
        
        ##########################################################
        ### Count reads for CDS and calculate expression level ###
        ##########################################################


        f.writelines(["featureCounts -a " + configPara["output_PATH"] + "/reference_genome/" + sample_ref + ".rename.prokka/" + \
                    sample_ref + ".gff -o " + configPara["output_PATH"] + "/5.expression/count/" + configPara["label"] + "." + \
                    eachSample + ".featureCount.all.txt " + configPara["output_PATH"] + "/4.bowtieMap/" + configPara["label"] + "." + \
                    eachSample + ".map.sort.bam -t CDS -g ID -T " + configPara["number_of_core"] + " -s 0" + os.linesep])
        f.writelines(["python " + configPara["house_bin_PATH"] + "/calculateExp.py " + configPara["output_PATH"] + "/5.expression/count/" + \
                    configPara["label"] + "." + eachSample + ".featureCount.all.txt " + configPara["output_PATH"] + "/5.expression/" + \
                    configPara["label"] + "." + eachSample + ".all.exp" + os.linesep])


        f.writelines(["bamToBed -i " + configPara["output_PATH"] + "/4.bowtieMap/" + configPara["label"] + "." + eachSample + \
                    ".map.sort.bam > " + configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + "." + eachSample + \
                    ".bed" + os.linesep])
        f.writelines(["sort -k1,1 " + configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + "." + eachSample + ".bed > " + \
                    configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + "." + eachSample + ".sorted.bed" + os.linesep])
        f.writelines(["genomeCoverageBed -bga -i " +  configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + "." + eachSample + \
                    ".sorted.bed -g " + configPara["output_PATH"] + "/reference_genome/" + sample_ref + ".chrom.size > " + \
                    configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + "." + eachSample + ".bedGraph" + os.linesep])
        f.writelines(["sort -k1,1 -k2,2n " + configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + "." + eachSample + \
                    ".bedGraph > " + configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + "." + eachSample + ".sort.bedGraph" + os.linesep])
        f.writelines([configPara["house_bin_PATH"] + "/bedGraphToBigWig " + configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + \
                    "." + eachSample + ".sort.bedGraph " + configPara["output_PATH"] + "/reference_genome/" + sample_ref + ".chrom.size " + \
                    configPara["output_PATH"] + "/6.genomicCov/" +  configPara["label"] + "." + eachSample + ".bw" + os.linesep])

        f.writelines(["python " + configPara["house_bin_PATH"] + "/normalizeBedGraph.py " + configPara["output_PATH"] + "/6.genomicCov/" + \
                    configPara["label"] + "." + eachSample + ".sort.bedGraph " + configPara["output_PATH"] + "/4.bowtieMap/" + eachSample + \
                    ".PCRdup.log " + configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + "." + eachSample + \
                    ".sort.normalized.bedGraph" + os.linesep])
        f.writelines([configPara["house_bin_PATH"] + "/bedGraphToBigWig " + configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + \
                    "." + eachSample + ".sort.normalized.bedGraph " + configPara["output_PATH"] + "/reference_genome/" + sample_ref + ".chrom.size " + \
                    configPara["output_PATH"] + "/6.genomicCov/" +  configPara["label"] + "." + eachSample + ".normalized.bw" + os.linesep])

        f.writelines(["genomeCoverageBed -bga -i " +  configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + "." + eachSample + \
                    ".sorted.bed -g " + configPara["output_PATH"] + "/reference_genome/" + sample_ref + ".chrom.size -strand + > " + \
                    configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + "." + eachSample + ".plus.bedGraph" + os.linesep])
        f.writelines(["sort -k1,1 -k2,2n " + configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + "." + eachSample + \
                    ".plus.bedGraph > " + configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + "." + eachSample + \
                    ".sort.plus.bedGraph" + os.linesep])
        f.writelines([configPara["house_bin_PATH"] + "/bedGraphToBigWig " + configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + \
                    "." + eachSample + ".sort.plus.bedGraph " + configPara["output_PATH"] + "/reference_genome/" + sample_ref + ".chrom.size " + \
                    configPara["output_PATH"] + "/6.genomicCov/" +  configPara["label"] + "." + eachSample + ".plus.bw" + os.linesep])

        f.writelines(["genomeCoverageBed -bga -i " +  configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + "." + eachSample + \
                    ".sorted.bed -g " + configPara["output_PATH"] + "/reference_genome/" + sample_ref + ".chrom.size -strand - > " + \
                    configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + "." + eachSample + ".minus.bedGraph" + os.linesep])
        f.writelines(["sort -k1,1 -k2,2n " + configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + "." + eachSample + \
                    ".minus.bedGraph > " + configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + "." + eachSample + \
                    ".sort.minus.bedGraph" + os.linesep])
        f.writelines([configPara["house_bin_PATH"] + "/bedGraphToBigWig " + configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + \
                    "." + eachSample + ".sort.minus.bedGraph " + configPara["output_PATH"] + "/reference_genome/" + sample_ref + ".chrom.size " + \
                    configPara["output_PATH"] + "/6.genomicCov/" +  configPara["label"] + "." + eachSample + ".minus.bw" + os.linesep])

        f.writelines(["genomeCoverageBed -d -i " + configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + \
                     "." + eachSample + ".sorted.bed -g " + \
                     configPara["output_PATH"] + "/reference_genome/" + sample_ref + ".chrom.size > " + configPara["output_PATH"] + "/6.genomicCov/" + \
                     configPara["label"] + "." + eachSample + ".baseCov" + os.linesep])
        f.writelines(["python " + configPara["house_bin_PATH"] + "/extractDepthPerElement.py " + configPara["output_PATH"] + "/6.genomicCov/" + \
                    configPara["label"] + "." + eachSample + ".baseCov " + configPara["output_PATH"] + "/reference_genome/" + sample_ref + \
                    ".mRNA.bed " +  configPara["output_PATH"] + "/reference_genome/" + sample_ref + ".chrom.size " + configPara["output_PATH"] + \
                    "/6.genomicCov/" + configPara["label"] + "." + eachSample + ".mRNA.baseCov" + os.linesep])

        f.writelines(["rm -f " + configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + "." + eachSample + ".bed" + os.linesep])
        f.writelines(["rm -f " + configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + "." + eachSample + ".sorted.bed" + os.linesep])
        f.writelines(["mv " + configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + "." + eachSample + ".sort.bedGraph " + 
                    configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + "." + eachSample + ".bedGraph" + os.linesep])
        f.writelines(["mv " + configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + "." + eachSample + ".sort.normalized.bedGraph " + 
                    configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + "." + eachSample + ".normalized.bedGraph" + os.linesep])
        f.writelines(["mv " + configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + "." + eachSample + ".sort.plus.bedGraph " + 
                    configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + "." + eachSample + ".plus.bedGraph" + os.linesep])
        f.writelines(["mv " + configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + "." + eachSample + ".sort.minus.bedGraph " + 
                    configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + "." + eachSample + ".minus.bedGraph" + os.linesep])
        f.writelines(["rm -f " + configPara["output_PATH"] + "/6.genomicCov/" + configPara["label"] + "." + eachSample + ".baseCov" + os.linesep])
            
        f.close()
        os.system("bash " + configPara["output_script_PATH"] + "/filterMap." + eachSample + ".sh")
    """

    
    sampleStat = readSampleInfoTotal(configPara["sample_info_dir"], int(configPara["num_of_pool"]))
    totalReads = statTotalReads(configPara["output_PATH"] + "/1.phixRemove", [e[0] for e in sampleStat])
    Nremoval = statNremoval(configPara["output_PATH"] + "/1.phixRemove", [e[0] for e in sampleStat])    
    phiXremoval = statPhiXremoval(configPara["output_PATH"] + "/1.phixRemove", [e[0] for e in sampleStat])
    polyGremoval = statpolyG(configPara["output_PATH"] + "/2.adatperTrimAndQC", [e[0] for e in sampleStat])
    qcReads = statQC(configPara["output_PATH"] + "/2.adatperTrimAndQC", [e[0] for e in sampleStat])
    rRNAremoval = statrRNA(configPara["output_PATH"] + "/3.rRNAremoval", [e[0] for e in sampleStat])
    rRNAdetail = readrRNAdetail(configPara["output_PATH"] + "/3.rRNAremoval", [e[0] for e in sampleStat])
    genomeReads = statGenome_all(configPara["output_PATH"] + "/4.bowtieMap", [e[0] for e in sampleStat])
    PCRdupReads = statPCRdup(configPara["output_PATH"] + "/4.bowtieMap", [e[0] for e in sampleStat])
    CDSreads = statCDS(configPara["output_PATH"] + "/5.expression/count", [e[0] for e in sampleStat], configPara["label"])
    
    f = open(configPara["output_Stat_PATH"],"w")
    f.writelines(["label\tstrain\tcondition\tbio_rep\ttech_rep\tpoolID\tadapterID\ttotal reads\treads with N\tphiX reads\t" + \
                "poly-G reads\treads passing all filters\treads passing all filters (ratio)\treads mapped to rRNA\t" + \
                "rRNA mapping ratio\treads mapped to 23S\t23S mapping ratio\treads mapped to 16S\t16S mapping ratio\t" + \
                "reads mapped to 5S\t5S mapping ratio\treads mapped to genome\tratio of reads mapped to genome + rRNA\tgenome mapping ratio\t" + \
                "reads after PCR removal\tunique reads ratio\treads mapped to CDS\tCDS mapping ratio" + os.linesep])
    for i in range(len(sampleStat)):
        if rRNAremoval[i] == 0:
            rRNAremoval[i] += 1
        f.writelines(["\t".join(sampleStat[i]) + "\t"])
        f.writelines([str(totalReads[i]) + "\t" + str(Nremoval[i]) + "\t" + str(phiXremoval[i]) + "\t" + \
                    str(polyGremoval[i]) + "\t" + str(qcReads[i]) + "\t" + str(1.0 * qcReads[i] / totalReads[i]) + "\t" + \
                    str(rRNAremoval[i]) + "\t" + str(1.0 * rRNAremoval[i] / qcReads[i]) + "\t" + str(rRNAdetail[i][0]) + "\t" + \
                    str(1.0 * rRNAdetail[i][0] / rRNAremoval[i]) + "\t" + str(rRNAdetail[i][1]) + "\t" + \
                    str(1.0 * rRNAdetail[i][1] / rRNAremoval[i]) + "\t" + str(rRNAdetail[i][2]) + "\t" + \
                    str(1.0 * rRNAdetail[i][2] / rRNAremoval[i]) + "\t" + str(genomeReads[i]) + "\t" + \
                    str(1.0 * (genomeReads[i] + rRNAremoval[i]) / qcReads[i]) + "\t" + str(1.0 * genomeReads[i] / (qcReads[i] - rRNAremoval[i])) + "\t" + \
                    str(PCRdupReads[i]) + "\t" + str(1.0 * PCRdupReads[i] / genomeReads[i]) + "\t" + str(CDSreads[i]) + "\t" + \
                    str(1.0 * CDSreads[i] / genomeReads[i]) + os.linesep])
    f.close()

    strainList = readStrainList(configPara["strain_list"])
    for eachStrain in strainList:
        print eachStrain
        os.system("python " + configPara["house_bin_PATH"] + "/mergeExp.py " + configPara["output_temp_PATH"] + "/barcodeTag_merge.txt " + \
                configPara["output_PATH"] + "/5.expression " + configPara["label"] + " " + eachStrain + " " + configPara["output_PATH"] + "/" + \
                "5.expression/" + configPara["label"] + "." + eachStrain + ".RPKM RPKM") 
        os.system("python " + configPara["house_bin_PATH"] + "/mergeExp.py " + configPara["output_temp_PATH"] + "/barcodeTag_merge.txt " + \
                configPara["output_PATH"] + "/5.expression " + configPara["label"] + " " + eachStrain + " " + configPara["output_PATH"] + "/" + \
                "5.expression/" + configPara["label"] + "." + eachStrain + ".FPKMO FPKMO") 
        os.system("python " + configPara["house_bin_PATH"] + "/mergeExp.py " + configPara["output_temp_PATH"] + "/barcodeTag_merge.txt " + \
                configPara["output_PATH"] + "/5.expression " + configPara["label"] + " " + eachStrain + " " + configPara["output_PATH"] + "/" + \
                "5.expression/" + configPara["label"] + "." + eachStrain + ".TPM TPM")
        os.system("mkdir -p " + configPara["output_PATH"] + "/5.expression/" + eachStrain + "_archive")
        os.system("mv " + configPara["output_PATH"] + "/5.expression/" + configPara["label"] + "." + eachStrain + "_*.all.exp " + \
                configPara["output_PATH"] + "/5.expression/" + eachStrain + "_archive")
        os.system("python " + configPara["house_bin_PATH"] + "/mergeCount.py " + configPara["output_temp_PATH"] + "/barcodeTag_merge.txt " + \
                configPara["output_PATH"] + "/5.expression/count " + configPara["label"] + " " + eachStrain + " " + configPara["output_PATH"] + "/" + \
                "5.expression/" + configPara["label"] + "." + eachStrain + ".count")


def readrRNAdetail(Indir, SampleList):
    tmpPool = []
    for each in SampleList:
        f = open(Indir + "/" + each + ".rRNA_filter_detail.log","rb")
        data = f.readlines()
        f.close()
        n16S = 0
        n23S = 0
        n5S = 0
        for e in data:
            e = e[:-1]
            tmp = e.split("\t")
            tmpNum = int(tmp[1])
            if "16S" in tmp[0]:
                n16S += tmpNum
            elif "23S" in tmp[0]:
                n23S += tmpNum
            elif "5S" in tmp[0]:
                n5S += tmpNum
        tmpPool.append([n23S, n16S, n5S])
    return tmpPool   
def statCDS(Indir,SampleList,label):
    tmpPool = []
    for each in SampleList:
        f = open(Indir + "/" + label + "." + each + ".featureCount.all.txt.summary","rb")
        data = f.readlines()
        f.close()
        tmp = data[1][:-1]
        tmp2 = tmp.split("\t")
        tmpPool.append(int(tmp2[-1]))
    return tmpPool
def statPCRdup(Indir,SampleList):
    tmpPool = []
    for each in SampleList:
        f = open(Indir + "/" + each + ".PCRdup.log","rb")
        data = f.readlines()
        f.close()
        tmp = data[1][:-1]
        tmp2 = tmp.split(" ")
        tmpPool.append(int(tmp2[-1]))
    return tmpPool
def statGenome(Indir,SampleList):
    tmpPool = []
    for each in SampleList:
        f = open(Indir + "/" + each + ".map.log","rb")
        data = f.readlines()
        f.close()
        tmp = data[-1][:-1]
        tmp2 = tmp.split(" ")
        tmpPool.append(int(tmp2[1]))
    return tmpPool
def statGenome_all(Indir,SampleList):
    tmpPool = []
    for each in SampleList:
        f = open(Indir + "/" + each + ".map.log","rb")
        data = f.readlines()
        f.close()
        tmp = data[3][:-1]
        tmp2 = tmp.split(" ")
        unique = int(tmp2[4])
        tmp = data[4][:-1]
        tmp2 = tmp.split(" ")
        noun = int(tmp2[4])
        tmpPool.append(unique + noun)
    return tmpPool

def statrRNA(Indir,SampleList):
    tmpPool = []
    for each in SampleList:
        f = open(Indir + "/" + each + ".rRNA_filter.log","rb")
        data = f.readlines()
        f.close()
        tmp = data[3][:-1]
        tmp2 = tmp.split("(")
        num1 = int(tmp2[0])
        tmp = data[4][:-1]
        tmp2 = tmp.split("(")
        num2 = int(tmp2[0])
        tmpPool.append(num1 + num2)
    return tmpPool
def statQC(Indir,SampleList):
    tmpPool = []
    for each in SampleList:
        f = open(Indir + "/" + each + ".adapter_remove_QC.log","rb")
        data = f.readlines()
        f.close()
        tmp = data[10][:-1]
        tmp2 = tmp.split(" ")
        tmp3 = tmp2[-2].split(",")
        tmpPool.append(int("".join(tmp3)))
    return tmpPool
def statTotalReads(Indir,SampleList):
    tmpPool = []
    for each in SampleList:
        f = open(Indir + "/" + each + ".N_filtered.log","rb")
        data = f.readlines()
        f.close()
        tmp = data[7][:-1]
        tmp2 = tmp.split(" ")
        tmp3 = tmp2[-1].split(",")
        tmpPool.append(int("".join(tmp3)))
    return tmpPool
def statNremoval(Indir,SampleList):
    tmpPool = []
    for each in SampleList:
        f = open(Indir + "/" + each + ".N_filtered.log","rb")
        data = f.readlines()
        f.close()
        tmp = data[9][:-1]
        tmp2 = tmp.split(" ")
        tmp3 = tmp2[-2].split(",")
        tmpPool.append(int("".join(tmp3)))
    return tmpPool
def statPhiXremoval(Indir,SampleList):
    tmpPool = []
    for each in SampleList:
        f = open(Indir + "/" + each + ".phiX_filter.log","rb")
        data = f.readlines()
        f.close()
        data2 = []
        tmp = data[3][:-1]
        tmp2 = tmp.split("(")
        num1 = int(tmp2[0])
        tmp = data[4][:-1]
        tmp2 = tmp.split("(")
        num2 = int(tmp2[0])
        tmpPool.append(num1 + num2)
    return tmpPool
def statpolyG(Indir,SampleList):
    tmpPool = []
    for each in SampleList:
        f = open(Indir + "/" + each + ".polyG_filter.log","rb")
        data = f.readlines()
        f.close()
        tmp = data[8][:-1]
        tmp2 = tmp.split(" ")
        tmp3 = tmp2[-2].split(",")
        tmpPool.append(int("".join(tmp3)))
    return tmpPool
def readConfigure(path):
    f = open(path,"rb")
    data = f.readlines()
    f.close()
    Pool = {}
    for each in data:
        if each[0] != "#" and len(each) > 1:
            each = each[:-1]
            tmp = each.split("=")
            Pool[tmp[0]] = tmp[1]
    return Pool
def readBarcodeTag(path):
    f = open(path,"rb")
    data = f.readlines()
    f.close()
    Pool = []
    for each in data:
        each = each[:-1]
        tmp = each.split("\t")
        Pool.append(tmp[0])
    return Pool
def readStrainList(path):
    f = open(path,"rb")
    data = f.readlines()
    f.close()
    Pool = [e[:-1] for e in data]
    return Pool
def readSampleInfoTotal(path, num):
    Pool = []
    for i in range(num):
        f = open(path + "/sampleInfo_p" + str(i + 1) + ".txt","rb")
        data = f.readlines()
        f.close()
        for each in data:
            each = each[:-1]
            tmp = each.split("\t")
            label = tmp[0] + "_" + tmp[1] + "_" + tmp[2] + "_" + tmp[3]
            Pool.append([label,] + tmp)
    return Pool
def writeHeader(f,unicyclerBin,label,core):

    f.writelines(["#!/bin/bash -l" + os.linesep])
    f.writelines(["#SBATCH --job-name=" + label + os.linesep])
    f.writelines(["#SBATCH -n " + str(core) + os.linesep])
    f.writelines(["#SBATCH --nodes=1" + os.linesep])
    f.writelines(["#SBATCH --ntasks=1" + os.linesep])
    f.writelines(["#SBATCH --cpus-per-task=" + str(core) + os.linesep])
    f.writelines(["#SBATCH --mem=0" + os.linesep])
    f.writelines(["#SBATCH -o /dev/null" + os.linesep])
    f.writelines(["#SBATCH -e /dev/null" + os.linesep])
    f.writelines(["source ~/.bashrc" + os.linesep])
    f.writelines(["source " + unicyclerBin + "/source " + unicyclerBin + os.linesep])

if __name__ == "__main__":
    main()
