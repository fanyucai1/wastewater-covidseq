# Email:yucai.fan@illumina.com
# 2023.03.31 version:1.0

import os
import subprocess
import argparse


parser=argparse.ArgumentParser("predict abundance per lineage using kallisto\n")
parser.add_argument("-f","--fastq",help="fastq files not contains primer",required=True)
parser.add_argument("-p","--prefix",help="prefix of output",required=True)
parser.add_argument("-o","--outdir",help="output directory",required=True)
parser.add_argument("-i","--index",help="kallisto index",required=True)
args=parser.parse_args()

args.fastq=os.path.abspath(args.fastq)
args.outdir=os.path.abspath(args.outdir)
out=args.outdir+"/qc/"+args.prefix
if not os.path.exists(args.outdir):
    subprocess.check_call("mkdir -p %s"%(args.outdir),shell=True)

args.index=os.path.abspath(args.index)

#https://pachterlab.github.io/kallisto/manual
#output name: abundance.tsv
cmd="kallisto quant --plaintext -t 24 -i %s -o %s --single -l 300 -s 50  %s"%(args.index,args.outdir,args.fastq)
subprocess.check_call(cmd,shell=True)
print("\nRun Done.")

#####