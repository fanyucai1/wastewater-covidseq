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
strains,clades={},{}
infile=open(args.ucsc,"r")
for line in infile:
    line=line.strip()
    if line.split("\t")[-1]==line.split("\t")[-3] and re.search("/",line.split("|")[0]):##pango_lineage_usher==pangolin_lineage
        strains[("hCoV-19/"+line.split("|")[0])]=line.split("\t")[-1]
        clades[line.split("\t")[-3]]=1
infile.close()
print("There total clades:%s in ucsc"%len(clades))
#############################read meta file from GISAID
num,GISAID=0,{}
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
        if array[13] != "" and array[13] != "Unassigned" and re.search('Human',line):###只考虑有明确分类,来自于固定宿州
            GISAID[array[0]]=line
infile.close()
############################################################输出中国
for key in strains.copy():
    if key in GISAID:
        array = GISAID[key].split("\t")
        if re.search("China", GISAID[key]) and strains[key] in clades:
            for i in range(0,len(array)):###GISAID meta提供的分类为pangolin_lineage比较落后，修改为最新的分类结果
                if i==13:
                    outfile.write("%s\t" % strains[key])
                elif i==len(array)-1:
                    outfile.write("%s\n" % array[i])
                else:
                    outfile.write("%s\t"%array[i])
            del GISAID[key]
            del clades[strains[key]]
            del strains[key]
print("step1:%s"%len(clades))
##########################################################输出其它国家
if len(clades)!=0:
    for key in strains.copy():
        if key in GISAID:
            array = GISAID[key].split("\t")
            if strains[key] in clades:
                for i in range(0,len(array)):
                    if i==13:
                        outfile.write("%s\t" % strains[key])
                    elif i==len(array)-1:
                        outfile.write("%s\n" % array[i])
                    else:
                        outfile.write("%s\t"%array[i])
                del GISAID[key]
                del clades[strains[key]]
                del strains[key]
    print("step2:%s" % len(clades))
##########################################################
if len(clades)!=0:
    for key in GISAID.copy():
        if len(clades)!=0:
            array = GISAID[key].split("\t")
            if int(array[8]) >= 29700 and array[22] != "" and float(array[22]) <= 0.01 and array[13] in clades:
                outfile.write("%s\n" % GISAID[key])
                del clades[array[13]]
                del GISAID[key]
        else:
            break
    print("step3:%s" % len(clades))
##########################################################
if len(clades)!=0:
    for key in GISAID.copy():
        if len(clades)!=0:
            array = GISAID[key].split("\t")
            if int(array[8]) >= 29700 and array[13] in clades:
                outfile.write("%s\n" % GISAID[key])
                del clades[array[13]]
                del GISAID[key]
        else:
            break
    print("step4:%s" % len(clades))
##########################################################
if len(clades)!=0:
    print("Not find %s" % len(clades))
    for key in clades:
        print("Not find %s"%key)
outfile.close()

end=time.time()
cmd='awk -F\"\\t\" \'{if($9!="Sequence length")print $5}\' %s.metadata.csv >%s.sequence_ID.txt'%(out,out)
subprocess.check_call(cmd,shell=True)
print("Total elapsed time:%s"%(end-start))