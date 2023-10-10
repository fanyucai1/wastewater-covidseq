import os
import sys
import subprocess
import argparse
import time
parser=argparse.ArgumentParser("")
parser.add_argument("-p1","--pe1",help="R1 fastq",required=True)
parser.add_argument("-p2","--pe2",help="R2 fastq",required=True)
parser.add_argument("-o","--outdir",help="output directory",default=os.getcwd())
parser.add_argument("-r","--ref",help="database directory",required=True)
parser.add_argument("-s","--script",help="script directory",required=True)
parser.add_argument("-a","--adapter",help="adapter sequence fasta",required=True)
parser.add_argument("-b","--bed",help="bed file",required=True)
parser.add_argument("-i","--index",help="kallisto idx",required=True)
parser.add_argument("-f","--fna",help="GISAID database",required=True)
parser.add_argument("-m","--meta",help="GISAID meta file",required=True)
parser.add_argument("-p","--prefix",help="prefix of output",required=True)
args=parser.parse_args()

start=time.time()
args.outdir=os.path.abspath(args.outdir)
args.script=os.path.abspath(args.script)
args.ref=os.path.abspath(args.ref)
out=args.outdir+"/"+args.prefix
if not os.path.exists(args.outdir):
    subprocess.check_call('mkdir -p %s'%args.outdir,shell=True)

subprocess.check_call("mkdir -p %s/pre_process"%(args.outdir),shell=True)
subprocess.check_call("mkdir -p %s/kallisto"%(args.outdir),shell=True)
subprocess.check_call("mkdir -p %s/freyja"%(args.outdir),shell=True)
args.pe1=os.path.abspath(args.pe1)
args.pe2=os.path.abspath(args.pe2)

raw_data=os.path.dirname(args.pe1)
script=os.path.abspath(os.path.abspath(args.script))

R1=args.pe1.split("/")[-1]
R2=args.pe2.split("/")[-1]

adapter_name=os.path.abspath(args.adapter).split("/")[-1]
if not os.path.exists(args.ref+"/"+adapter_name):
    subprocess.check_call("cp %s %s"%(args.adapter,args.ref),shell=True)

bed_name=os.path.abspath(args.bed).split("/")[-1]
if not os.path.exists(args.ref+"/"+bed_name):
    subprocess.check_call("cp %s %s"%(args.bed,args.ref),shell=True)

cmd="docker run -v %s:/reference -v %s:/script \
  -v %s:/raw_data/ -v %s/pre_process/:/outdir/ \
  waste_water:latest python3 /script/trim_fastq.py \
  -p1 /raw_data/%s -p2 /raw_data/%s \
  -a /reference/%s \
  -i /reference/NC_045512.2 -b /reference/%s -r /reference/NC_045512.2.fa \
  -g /reference/NC_045512.2.gff3 -o /outdir/ -p %s"%(args.ref,args.script,
                                                     raw_data,args.outdir,
                                                     R1,R2,adapter_name,bed_name,args.prefix)
print(cmd)
subprocess.check_call(cmd,shell=True)

kallisto_name=os.path.abspath(args.index).split("/")[-1]
meta_name=os.path.abspath(args.meta).split("/")[-1]
fasta_name=os.path.abspath(args.fna).split("/")[-1]

if not os.path.exists(args.ref+"/"+kallisto_name):
    subprocess.check_call("cp %s %s"%(args.index,args.ref),shell=True)

if not os.path.exists(args.ref+"/"+meta_name):
    subprocess.check_call("cp %s %s"%(args.meta,args.ref),shell=True)

if not os.path.exists(args.ref+"/"+fasta_name):
    subprocess.check_call("cp %s %s"%(args.fna,args.ref),shell=True)

cmd="docker run -v %s/:/reference -v %s:/script \
	-v %s/freyja/:/outdir/ -v %s/pre_process/:/raw_data/ \
    waste_water:latest  python3 /script/freyja.py -b /raw_data/%s.soft.clipped.sort.bam \
    -r /reference/NC_045512.2.fa --barcode /reference/usher_barcodes.csv  --meta /reference/curated_lineages.json \
    -o /outdir/ -p %s"%(args.ref,args.script,args.outdir,args.outdir,args.prefix,args.prefix)
print(cmd)
if not os.path.exists("%s/freyja/%s.freyja_bootstrap.png"%(args.outdir,args.prefix)):
    subprocess.check_call(cmd,shell=True)

cmd="docker run -v %s:/reference -v %s:/script \
    -v %s/kallisto/:/outdir/ -v %s/pre_process:/raw_data/ \
    waste_water:latest python3 /script/kallisto.py \
	-p1 /raw_data/%s.R1.fq -p2 /raw_data/%s.R2.fq \
    -i /reference/%s \
    -o /outdir/ -p %s --fna /reference/%s --meta /reference/%s"%(args.ref,args.script,
                                                 args.outdir,args.outdir,
                                                 args.prefix,args.prefix,kallisto_name,
                                                 args.prefix,fasta_name,meta_name)
print(cmd)
if not os.path.exists("%s/kallisto/%s.pieChart_kallisto.png"%(args.outdir,args.prefix)):
    subprocess.check_call(cmd,shell=True)
end=time.time()
print("Elapse time is %g seconds" % (end - start))