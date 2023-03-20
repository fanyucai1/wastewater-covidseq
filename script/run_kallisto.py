import os
import sys
import subprocess
import argparse
import re

parser=argparse.ArgumentParser("")
parser.add_argument("-p1","--pe1",help="forward fastq not contains primer",required=True)
parser.add_argument("-p2","--pe2",help="reverse fastq not contains primer",required=True)
parser.add_argument("-p","--prefix",help="prefix of output",required=True)
parser.add_argument("-o","--outdir",help="output directory",required=True)
parser.add_argument("-i","--index",help="kallisto index",required=True)
args=parser.parse_args()

args.pe1=os.path.abspath(args.pe1)
args.pe2=os.path.abspath(args.pe2)
args.outdir=os.path.abspath(args.outdir)
out=args.outdir+"/qc/"+args.prefix
if not os.path.exists(args.outdir):
    subprocess.check_call("mkdir -p %s"%(args.outdir),shell=True)

args.index=os.path.abspath(args.index)

#https://pachterlab.github.io/kallisto/manual
#output name: abundance.tsv
cmd="kallisto quant --plaintext -t 20 -b $num_bootstraps -i %s -o %s %s %s"%(args.index,args.outdir,args.pe1,args.pe2)
subprocess.check_call(cmd,shell=True)
