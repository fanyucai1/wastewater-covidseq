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
parser.add_argument("--barcode",help="usher_barcodes.csv,download:https://github.com/andersen-lab/Freyja-data",required=True)
parser.add_argument("--meta",help="curated_lineages.json,download:https://github.com/andersen-lab/Freyja-data",required=True)
parser.add_argument("-o",help="output directory",default=os.getcwd())
args=parser.parse_args()

args.reference=os.path.abspath(args.reference)
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
'''
Usage: freyja variants [OPTIONS] BAMFILE

Options:
  --ref PATH       Reference
  --variants PATH  Variant call output file
  --depths PATH    Sequencing depth output file
  --refname TEXT   Ref name (for bams with multiple sequences)
  --minq INTEGER   Minimum base quality score
  --help           Show this message and exit.
'''

cmd="freyja variants %s --variants %s.freyja.variants.tsv --depths %s.freyja.depths.tsv --ref %s"%(args.bam,out,out,args.reference)
print(cmd)
subprocess.check_call(cmd,shell=True)

'''
Usage: freyja demix [OPTIONS] VARIANTS DEPTHS

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

cmd="freyja demix %s.freyja.variants.tsv %s.freyja.depths.tsv --output %s.freyja.demix --confirmedonly"%(out,out,out)
cmd+="--barcodes %s --meta %s --eps 0.0001 && "%(args.barcode,args.meta)

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
cmd+="freyja boot %s.freyja.variants.tsv %s.freyja.depths.tsv --nt 24 --nb 1000 --boxplot pdf --output_base %s.freyja_boot"%(out,out,out)
print(cmd)
subprocess.check_call(cmd,shell=True)

'''
Usage: freyja aggregate [OPTIONS] RESULTS

Options:
  --ext TEXT     file extension option
  --output PATH  Output file
  --help         Show this message and exit.
'''

'''
Usage: freyja plot [OPTIONS] AGG_RESULTS

Options:
  --lineages
  --times TEXT
  --interval TEXT
  --colors TEXT         path to csv of hex codes
  --mincov FLOAT        min genome coverage included
  --output TEXT         Output file
  --windowsize INTEGER
  --help                Show this message and exit.
'''
