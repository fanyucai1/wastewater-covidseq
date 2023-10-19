import os
import sys
import subprocess
import argparse
import time
import re
import csv

parser=argparse.ArgumentParser("")
parser.add_argument("-g","--gis",help="meta file from GISAID",required=True)
parser.add_argument("-u","--ucsc",help="meta file from ucsc",required=True)#http://hgdownload.soe.ucsc.edu/goldenPath/wuhCor1/UShER_SARS-CoV-2/
parser.add_argument("-o","--outdir",help="output directory",default=os.getcwd())
parser.add_argument("-p","--prefix",help="prefix of output",default=time.strftime("%Y-%m-%d"))
parser.add_argument("-c","--core",help="manually curated sequences ID")
args=parser.parse_args()

args.outdir=os.path.abspath(args.outdir)
if not os.path.exists(args.outdir):
    subprocess.check_call("mkdir -p %s"%(args.outdir),shell=True)
start=time.time()
#############################
seq_id=[]
if args.core:
    infile=open(args.core,"r")
    for line in infile:
        if not line.startswith("#"):
            seq_id.append(line)
    infile.close()
#############################read meta file from ucsc
strains=[]
infile=open(args.ucsc,"r")
for line in infile:
    line=line.strip()
    if line.split("\t")[-1]==line.split("\t")[-3] and re.search("/",line.split("|")[0]):##pango_lineage_usher==pangolin_lineage
        strains.append("hCoV-19/"+line.split("|")[0])
infile.close()
#############################read meta file from GISAID
num,GISAID,clades=0,{},{}
out=args.outdir+"/"+args.prefix
infile=open(args.gis,"r")
outfile=open("%s.metadata.csv"%(out),"w")
for line in infile:
    line=line.strip("\n")
    array = line.split("\t")
    num += 1
    if num==1:######输出表头
        outfile.write("%s\n" % line)
    elif array[4] in seq_id:
        outfile.write("%s\n" %line)
    else:
        GISAID[array[0]]=line
        if array[13] != "":
            if array[13] in clades:
                clades[array[13]]+=1
            else:
                clades[array[13]]= 1
print("There total clades:%s"%len(clades))
infile.close()
##########################################################
for key in strains:
    if key in GISAID:
        if re.search("China", GISAID[key]):##输出中国
            outfile.write("%s\n" % GISAID[key])
            if GISAID[key].split("\t")[13] in clades:
                del clades[GISAID[key].split("\t")[13]]
            del GISAID[key]
        else:
            if GISAID[key].split("\t")[13] in clades:
                outfile.write("%s\n" % GISAID[key])
                del clades[GISAID[key].split("\t")[13]]
                del GISAID[key]
##########################################################分类至少在GISAID出现50次以上
if clades!={}:
    for key in clades.copy():
        if clades[key]<50:
            del clades[key]
    print("pangolin_lineage and pango_lineage_usher not consensus clades(>=50 starins):%s"%len(clades))
##########################################################
if clades!={}:
    for key in GISAID:
        array=GISAID[key].split("\t")
        if clades=={}:
            break
        elif re.search("China", GISAID[key]) and int(array[8]) >= 29700 and array[13] != "" and array[22] != "" and array[13] != "Unassigned" and float(array[22]) <= 0.01 and array[13] in clades:
            outfile.write("%s\n" % GISAID[key])
            del clades[array[13]]
##########################################################
if clades!={}:
    for key in GISAID:
        array=GISAID[key].split("\t")
        if clades=={}:
            break
        elif int(array[8]) >= 29700 and array[13] != "" and array[22] != "" and array[13] != "Unassigned" and float(array[22]) <= 0.01 and array[13] in clades:
            outfile.write("%s\n" % GISAID[key])
            del clades[array[13]]
##########################################################
if clades!={}:
    for key in GISAID:
        array=GISAID[key].split("\t")
        if clades=={}:
            break
        elif int(array[8]) >= 29400 and array[13] != "" and array[22] != "" and array[13] != "Unassigned" and float(array[22]) <= 0.05 and array[13] in clades:
            outfile.write("%s\n" % GISAID[key])
            del clades[array[13]]
##########################################################
if clades!={}:
    print("Not find clade:")
    for key in clades:
        print (key,clades[key])
outfile.close()
end=time.time()
cmd='awk -F\"\\t\" \'{if($9!="Sequence length")print $5}\' %s.metadata.csv >%s.sequence_ID.txt'%(out,out)
subprocess.check_call(cmd,shell=True)
print("Total elapsed time:%s"%(end-start))