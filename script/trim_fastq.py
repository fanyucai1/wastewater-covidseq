##  S Martínez-Puchol,  Itarte M ,  Rusiol M , et al. Exploring the diversity of coronavirus in sewage during COVID-19 pandemic: Don't miss the forest for the trees[J]. Science of The Total Environment, 2021, 800:149562.
##  Fontenele R S, Kraberger S, Hadfield J, et al. High-throughput sequencing of SARS-CoV-2 in wastewater provides insights into circulating variants[J]. Water Research, 2021, 205: 117710.
##  Baaijens J A, Zulli A, Ott I M, et al. Lineage abundance estimation for SARS-CoV-2 in wastewater using transcriptome quantification techniques[J]. Genome biology, 2022, 23(1): 236.
##  Email:yucai.fan@illumina.com
##  2023.03.31 version:1.0

import os
import subprocess
import argparse
import time

parser=argparse.ArgumentParser("A pipeline for lineage abundance estimation from wastewater sequencing data.\nEmail:yucai.fan@illumina.com\n\n")
parser.add_argument("-p1","--pe1",help="R1 fastq",required=True)
parser.add_argument("-p2","--pe2",help="R2 fastq",required=True)
parser.add_argument("-a","--adapter",help="fasta file adapter sequence",required=True)
parser.add_argument("-i","--index",help="prefix of covidRefSequences wuhan bowtie2 index",required=True)
parser.add_argument("-r","--reference",help="reference fasta sequence:NC_045512.2")
parser.add_argument("-g","--gff",help="gff file:NC_045512.2")
parser.add_argument("-t","--thread",help="number threads",type=int,default=24)
parser.add_argument("-b","--bed",help="primer bed file",required=True)
parser.add_argument('--min_base_qual', required=False, type=int, help="Minimum Base Quality for consensus sequence",default=20)
parser.add_argument("-p","--prefix",help="prefix of output",default=time.strftime("%Y-%m-%d"))
parser.add_argument("-o","--outdir",help="output directory",default=os.getcwd())
args=parser.parse_args()

args.outdir=os.path.abspath(args.outdir)
args.adapter=os.path.abspath(args.adapter)
args.pe1=os.path.abspath(args.pe1)
args.pe2=os.path.abspath(args.pe2)
args.bed=os.path.abspath(args.bed)
args.reference=os.path.abspath(args.reference)
args.gff=os.path.abspath(args.gff)

out=args.outdir+"/"+args.prefix
if not os.path.exists(args.outdir):
    subprocess.check_call("mkdir -p %s"%(args.outdir),shell=True)

# http://www.usadellab.org/cms/?page=trimmomatic
# https://github.com/usadellab/Trimmomatic
# trim adapters with trimmomatic
# https://github.com/baymlab/wastewater_analysis/blob/main/pipeline/trim_reads.sh
# https://github.com/CFSAN-Biostatistics/C-WAP/blob/main/startWorkflow.nf
# https://github.com/niemasd/SD-COVID-Sequencing/blob/main/scripts/pipeline.sh
# https://github.com/niemasd/ViReflow/blob/main/ViReflow.py

#输出最短序列30bp
cmd="fastp --in1 %s --in2 %s --out1 %s_1.fastq.gz --out2 %s_2.fastq.gz " \
    "--html %s.html --json %s.json --report_title %s " \
    "--thread 8 --adapter_fasta %s --length_required 30 --qualified_quality_phred 20"%(args.pe1,args.pe2,out,out,out,out,out,args.adapter)
print(cmd)
subprocess.check_call(cmd,shell=True)

# align reads with bowtie2 and sort bam with samtools
cmd="bowtie2 --threads %s -x %s -1 %s_1.fastq.gz -2 %s_2.fastq.gz |samtools view -bh |samtools sort > %s.bam && samtools index %s.bam && rm -rf %s_1.fastq.gz %s_2.fastq.gz"%(args.thread,args.index,out,out,out,out,out,out)
print(cmd)
subprocess.check_call(cmd,shell=True)

# trim primers with ivar (soft clipping)
# https://andersen-lab.github.io/ivar/html/manualpage.html
# -e    Include reads with no primers
cmd="ivar trim -e -i %s.bam -b %s -p %s.soft.clipped | tee %s.ivar.stdout && rm -rf %s.bam %s.bam.bai"%(out,args.bed,out,out,out,out)
print(cmd)
subprocess.check_call(cmd,shell=True)

## remove soft-clipped primers
#https://jvarkit.readthedocs.io/en/latest/Biostar84452/
# source activate && conda deactivate
cmd ="/software/samtools-v1.17/bin/samtools sort %s.soft.clipped.bam -o %s.soft.clipped.sort.bam"%(out,out)
print(cmd)
subprocess.check_call(cmd,shell=True)

cmd="java -jar /software/jvarkit.jar biostar84452 --samoutputformat BAM %s.soft.clipped.sort.bam |samtools sort >%s.trimmed.bam " \
    "&& cd %s && samtools index %s.trimmed.bam"%(out,out,args.outdir,out)
print(cmd)
subprocess.check_call(cmd,shell=True)

# extract fastqs
# https://www.htslib.org/doc/samtools-fasta.html
cmd="/software/samtools-v1.17/bin/samtools fastq %s.trimmed.bam >%s.resorted.fastq"%(out,out)
print(cmd)
subprocess.check_call(cmd,shell=True)

# Generate Pile-Up and variantCalling
# https://github.com/CFSAN-Biostatistics/C-WAP/blob/main/startWorkflow.nf
# -m    Minimum read depth to call variants (Default: 10)
cmd="/software/samtools-v1.17/bin/samtools mpileup -A -aa -d 0 -Q 0 -o %s.pile.up --reference %s %s.trimmed.bam"%(out,args.reference,out)
print(cmd)
subprocess.check_call(cmd,shell=True)
cmd="cat %s.pile.up | ivar variants -p %s.rawVarCalls -g %s -r %s -m 10"%(out,out,args.gff,args.reference)
print(cmd)
subprocess.check_call(cmd,shell=True)

# Calculation of the consensus sequence using bcftools
# https://github.com/niemasd/ViReflow/blob/main/ViReflow.py
# https://github.com/CFSAN-Biostatistics/C-WAP/blob/main/startWorkflow.nf
cmd="bcftools mpileup -Ou -f %s %s.trimmed.bam | bcftools call --ploidy 1 -mv -Oz -o %s.calls.vcf.gz"%(args.reference,out,out)
cmd+=" && bcftools index %s.calls.vcf.gz"%(out)
cmd+=" && cat %s | bcftools consensus %s.calls.vcf.gz -p %s > %s.consensus.fa"%(args.reference,out,args.prefix,out)
print(cmd)
subprocess.check_call(cmd,shell=True)
subprocess.check_call('sed -i \'1s/.*/>%s/\' %s.consensus.fa'%(args.prefix,out),shell=True)

# Calculation of the consensus sequence is used to determine the predominant lineage
cmd="pangolin --alignment %s.consensus.fa --threads 2 --outdir %s --outfile %s.lineage_report.csv --alignment-file %s.alignment.fasta"%(out,args.outdir,args.prefix,args.prefix)
print(cmd)
subprocess.check_call(cmd,shell=True)

# Calculate depth from the trimmed mapped reads
# http://www.htslib.org/doc/samtools-depth.html
# "-J Include reads with deletions in depth computation."
# "-q only count reads with base quality greater than or equal to INT"
# https://github.com/niemasd/ViReflow/blob/main/ViReflow.py
cmd="/software/samtools-v1.17/bin/samtools depth -J -d 0 -Q 0 -q %s -aa %s.trimmed.bam >%s.depth.txt"%(args.min_base_qual,out,out)
subprocess.check_call(cmd,shell=True)
