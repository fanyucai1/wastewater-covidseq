# Email:yucai.fan@illumina.com
# 2023.03.31-2023.04.3 version:1.0

import os
import subprocess
import argparse
import time

parser=argparse.ArgumentParser("predict abundance per lineage using kallisto\n")
parser.add_argument("-p1","--pe1",help="R1 fastq files not contains primer",required=True)
parser.add_argument("-p2","--pe2",help="R2 fastq files not contains primer",required=True)
parser.add_argument("-p","--prefix",help="prefix of output",default=time.strftime("%Y-%m-%d"))
parser.add_argument("-o","--outdir",help="output directory",required=True)
parser.add_argument("--meta",help="meta file download from GIS",required=True)
parser.add_argument("--fna",help="fasta file download from fasta",required=True)
parser.add_argument("-i","--index",help="kallisto index",required=True)
args=parser.parse_args()

args.pe1=os.path.abspath(args.pe1)
args.pe2=os.path.abspath(args.pe2)
args.outdir=os.path.abspath(args.outdir)
args.meta=os.path.abspath(args.meta)
args.fna=os.path.abspath(args.fna)
args.index=os.path.abspath(args.index)

if not os.path.exists(args.outdir):
    subprocess.check_call("mkdir -p %s"%(args.outdir),shell=True)
out=args.outdir+"/"+args.prefix

#https://pachterlab.github.io/kallisto/manual
#output name: abundance.tsv
cmd="kallisto quant --plaintext -t 36 -i %s -o %s %s %s"%(args.index,args.outdir,args.pe1,args.pe2)
subprocess.check_call(cmd,shell=True)

########################Keep meta and fasta consistent
seq_id={}
infile=open(args.fna,"r")
for line in infile:
    line=line.strip()
    array=line.split("\t")
    if line.startswith(">"):
        array = line.split("|")
        seq_id[array[1]]=array[0][1:]
infile.close()

infile=open(args.meta,"r")
outfile=open("%s.kallisto.meta.csv"%(out),"w")
for line in infile:
    line=line.strip()
    array=line.split("\t")
    if array[4] in seq_id:
        for i in range(0,len(array)):
            if i==0:
                outfile.write("\n%s"%(seq_id[array[4]]))
            else:
                outfile.write("\t%s"%(array[i]))
    else:
        outfile.write("%s\n"%line)
infile.close()
outfile.close()
###################
cmd="python3 /script/output_abundances.py -o %s/predictions.tsv " \
    "--metadata %s.kallisto.meta.csv %s/abundance.tsv"%(args.outdir,out,args.outdir)
subprocess.check_call(cmd,shell=True)
print("\nRun Done.")