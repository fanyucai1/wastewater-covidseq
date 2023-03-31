# Email:yucai.fan@illumina.com
# 2023.03.30

import os
import subprocess
import argparse
import time
parser=argparse.ArgumentParser("")
parser.add_argument("-b","--bam",help="bam file(trimed primer)",required=True)
parser.add_argument("-r","--ref",help="reference sequence,fasta",required=True)
parser.add_argument("-p","--prefix",help="prefix of output",default=time.strftime("%Y-%m-%d"))
parser.add_argument("-o","--outdir",help="output directory",default=os.getcwd())
parser.add_argument("--barcode",help="usher_barcodes.csv,download:https://github.com/andersen-lab/Freyja-data",required=True)
parser.add_argument("--meta",help="curated_lineages.json,download:https://github.com/andersen-lab/Freyja-data",required=True)
parser.add_argument("--minq",help="Minimum base quality score",default=20,type=int)
parser.add_argument("--eps",help="minimum abundance to include",default=0.001,type=float)
parser.add_argument("--nb",help="number of bootstraps",default=1000,type=int)
args=parser.parse_args()

args.ref=os.path.abspath(args.ref)
args.bam=os.path.abspath(args.bam)
args.barcode=os.path.abspath(args.barcode)
args.meta=os.path.abspath(args.meta)

args.outdir=os.path.abspath(args.outdir)
if not os.path.exists(args.outdir):
    subprocess.check_call("mkdir -p %s"%(args.outdir),shell=True)
out=args.outdir+"/"+args.prefix


# freyjaVariantCaller
# https://github.com/CFSAN-Biostatistics/C-WAP/blob/main/startWorkflow.nf
# barcode and meta file download link:https://github.com/andersen-lab/Freyja-data

#Usage: freyja variants [OPTIONS] BAMFILE
'''

Options:
  --ref PATH       Reference
  --variants PATH  Variant call output file
  --depths PATH    Sequencing depth output file
  --refname TEXT   Ref name (for bams with multiple sequences)
  --minq INTEGER   Minimum base quality score
  --help           Show this message and exit.
'''

cmd="freyja variants %s --variants %s.freyja.variants.tsv --depths %s.freyja.depths.tsv --ref %s --minq %s"%(args.bam,out,out,args.ref,args.minq)
print(cmd)
subprocess.check_call(cmd,shell=True)

#Usage: freyja demix [OPTIONS] VARIANTS DEPTHS
'''

Options:
  --eps FLOAT       minimum abundance to include
  --barcodes TEXT   custom barcode file
  --meta TEXT       custom lineage metadata file
  --output PATH     Output file
  --covcut INTEGER  depth cutoff for
                    coverage estimate
  --confirmedonly
  --wgisaid         larger library with non-public lineages
  --help            Show this message and exit.
'''

cmd="freyja demix %s.freyja.variants.tsv %s.freyja.depths.tsv --barcodes %s --meta %s --eps %s --output %s.freyja.demix --confirmedonly"%(out,out,args.barcode,args.meta,args.eps,out)
subprocess.check_call(cmd,shell=True)

#Usage: freyja boot [OPTIONS] VARIANTS DEPTHS
'''
Options:
  --nb INTEGER        number of bootstraps
  --nt INTEGER        max number of cpus to use
  --eps FLOAT         minimum abundance to include
  --barcodes TEXT     custom barcode file
  --meta TEXT         custom lineage metadata file
  --output_base PATH  Output file basename
  --boxplot TEXT      file format of boxplot output (e.g. pdf or png)
  --confirmedonly
  --wgisaid           larger library with non-public lineages
  --help              Show this message and exit.
'''
cmd="freyja boot %s.freyja.variants.tsv %s.freyja.depths.tsv --nt 24 --nb %s --boxplot pdf --output_base %s.freyja_boot --eps %s"%(out,out,args.nb,out,args.eps)
print(cmd)
subprocess.check_call(cmd,shell=True)

cmd="python3 /script/parseFreyjaBootstraps.py %.freyja.demix %s.freyja_boot_lineages.csv %s.freyja_bootstrap.png"%(out,out,out)
print(cmd)
subprocess.check_call(cmd,shell=True)
