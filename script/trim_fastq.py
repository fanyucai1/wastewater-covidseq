##  S Martínez-Puchol,  Itarte M ,  Rusiol M , et al. Exploring the diversity of coronavirus in sewage during COVID-19 pandemic: Don't miss the forest for the trees[J]. Science of The Total Environment, 2021, 800:149562.
##  Fontenele R S, Kraberger S, Hadfield J, et al. High-throughput sequencing of SARS-CoV-2 in wastewater provides insights into circulating variants[J]. Water Research, 2021, 205: 117710.
##  Baaijens J A, Zulli A, Ott I M, et al. Lineage abundance estimation for SARS-CoV-2 in wastewater using transcriptome quantification techniques[J]. Genome biology, 2022, 23(1): 236.
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
parser.add_argument("-t","--thread",help="number threads",type=int,default=20)
parser.add_argument("-b","--bed",help="primer bed file",required=True)
parser.add_argument('--min_base_qual', required=False, type=int, help="Minimum Base Quality for consensus sequence",default=30)
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
'''
#输出最短序列30bp
cmd="trimmomatic PE -threads 20 %s %s %s_1.fastq.gz %s_1_unpaired.fastq.gz " \
    "%s_2.fastq.gz %s_2_unpaired.fastq.gz " \
    "ILLUMINACLIP:%s:2:30:10:2:keepBothReads " \
    "SLIDINGWINDOW:4:20 MINLEN:30 LEADING:3 TRAILING:3 && rm -rf %s*unpaired.fastq.gz"%(args.pe1,args.pe2,out,out,out,out,args.adapter,out)
print(cmd)
subprocess.check_call(cmd,shell=True)

# align reads with bowtie2 and sort bam with samtools
cmd="bowtie2 --no-unal --threads %s -x %s -1 %s_1.fastq.gz -2 %s_2.fastq.gz -S %s_aligned.sam"%(args.thread,args.index,out,out,out)
print(cmd)
subprocess.check_call(cmd,shell=True)

cmd="samtools sort %s_aligned.sam -o %s_sorted.bam -@ %s && samtools index %s_sorted.bam && rm -rf %s_aligned.sam"%(out,out,args.thread,out,out)
print(cmd)
subprocess.check_call(cmd,shell=True)

# trim primers with ivar (soft clipping)
# https://andersen-lab.github.io/ivar/html/manualpage.html
# -e    Include reads with no primers
cmd="source activate && conda deactivate && conda activate ivar-env && ivar trim -e -i %s_sorted.bam -b %s -p %s.soft.clipped | tee %s.ivar.stdout && rm -rf %s_sorted.bam"%(out,args.bed,out,out,out)
print(cmd)
subprocess.check_call(cmd,shell=True)
# Generate a tsv file tabulating the number of reads vs trimmer primer name in the bed file
cmd="cat %s.ivar.stdout | grep -A 10000 \"Primer Name\" | head -n -5 > %s.primer_hit_counts.tsv"%(out,out)
print(cmd)
subprocess.check_call(cmd,shell=True)

## remove soft-clipped primers
#https://jvarkit.readthedocs.io/en/latest/Biostar84452/
cmd="source activate && conda deactivate && samtools sort -o %s.soft.clipped.sort.bam %s.soft.clipped.bam && " \
    "java -jar /software/jvarkit.jar biostar84452 --samoutputformat BAM %s.soft.clipped.sort.bam -o %s.clipped.bam && " \
    "samtools sort -o %s.trimmed.bam %s.clipped.bam && rm -rf %s.clipped.bam"%(out,out,out,out,out,out,out)
print(cmd)
subprocess.check_call(cmd,shell=True)

# extract fastqs
# https://www.htslib.org/doc/samtools-fasta.html
cmd="samtools fastq %s.trimmed.bam >%s.all_reads.fq"%(out,out)
print(cmd)
subprocess.check_call(cmd,shell=True)
'''
# Generate Pile-Up and variantCalling
# https://github.com/CFSAN-Biostatistics/C-WAP/blob/main/startWorkflow.nf
# -m    Minimum read depth to call variants (Default: 10)
cmd="samtools mpileup -A -aa -d 0 -Q 0 -o %s.pile.up --reference %s %s.soft.clipped.sort.bam"%(out,args.reference,out)
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
cmd+=" && cat %s | bcftools consensus %s.calls.vcf.gz > %s.consensus.fa"%(args.reference,out,out)
print(cmd)
subprocess.check_call(cmd,shell=True)

# Calculation of the consensus sequence is used to determine the predominant lineage
cmd="pangolin --alignment %s.consensus.fa --threads 2 --outdir %s"%(out,args.outdir)
print(cmd)
subprocess.check_call(cmd,shell=True)

# Calculate depth from the trimmed mapped reads
# http://www.htslib.org/doc/samtools-depth.html
# "-J Include reads with deletions in depth computation."
# "-q only count reads with base quality greater than or equal to INT"
# https://github.com/niemasd/ViReflow/blob/main/ViReflow.py
cmd="samtools depth -J -d 0 -Q 0 -q %s -aa %s.soft.clipped.sort.bam"%(args.min_base_qual,out)
subprocess.check_call(cmd,shell=True)



