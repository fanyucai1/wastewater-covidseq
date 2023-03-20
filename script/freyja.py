# Email:yucai.fan@illumina.com
# 2023.03.20

import os
import sys
import subprocess
import argparse
import time
parser=argparse.ArgumentParser("")
parser.add_argument()
parser.add_argument("-p","--prefix",help="prefix of output",default=time.strftime("%Y-%m-%d"))
parser.add_argument("-o",help="output directory",default=os.getcwd())

# freyjaVariantCaller
# https://github.com/CFSAN-Biostatistics/C-WAP/blob/main/startWorkflow.nf
cmd="freyja variants %s.trimmed.bam --variants %s.freyja.variants.tsv --depths %s.freyja.depths.tsv --ref %s"%(out,out,out,args.reference)
print(cmd)
subprocess.check_call(cmd,shell=True)
cmd="freyja demix %s.freyja.variants.tsv %s.freyja.depths.tsv --output %s.freyja.demix --confirmedonly"%(out,out,out)
print(cmd)
subprocess.check_call(cmd,shell=True)
cmd="freyja boot %s.freyja.variants.tsv %s.freyja.depths.tsv --nt 24 --nb 1000 --output_base %s.freyja_boot"%(out,out,out)
print(cmd)
subprocess.check_call(cmd,shell=True)

