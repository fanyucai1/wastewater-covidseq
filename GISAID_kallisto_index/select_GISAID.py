# Email:yucai.fan@illumina.com
# 2023.03.15-2023.03.16
# version:1.0
# 基本原则：
    #   手动核心序列98条
    #   china 每个分类不超过默认值(Sequence length >29400+有准确分类+N含量小于5%)
    #   voc每个分类不超过默认值(Sequence length >29700+有准确分类+N含量小于1%+来自不同国家)
    #   其它分类默认1条(Sequence length >29700+有准确分类+N含量小于1%)
# 后续处理
    # 可以将程序输出的sequence id 上传到GISAID网站获得fasta序列，请实时条件参数，默认上传的序列数目不超过1万条
    # 如果输出超过1万条，可以从GISAID下载所有序列，然后另行写脚本筛选
import os
import re
import argparse
import subprocess
import time

parser=argparse.ArgumentParser("Select meta data from GISAID.\n")
parser.add_argument("-m","--meta",help="meta file download GISAID.")
parser.add_argument("-c","--core",help="manually curated sequences ID",required=True)
parser.add_argument("-v","--voc",help="voc",required=True)
parser.add_argument("-n","--num",help="limit number sequence per pangolin id,default=10",default=10)
parser.add_argument("-o","--outdir",help="output directory",default=os.getcwd(),required=True)
args=parser.parse_args()

args.outdir=os.path.abspath(args.outdir)
if not os.path.exists(args.outdir):
    os.makedirs(args.outdir)
out=args.outdir+"/"+time.strftime("%Y-%m-%d")
seq_id=[]
pangolin={}
#########################################get curated sequences id
infile=open(args.core,"r")
for line in infile:
    line=line.strip()
    if not line.startswith("#"):
        seq_id.append(line)
infile.close()
#########################################get voc list
voc_id=[]
infile=open(args.voc,"r")
for line in infile:
    line=line.strip()
    if not line.startswith("#"):
        voc_id.append(line)
infile.close()
#########################################
index={}
infile=open(args.meta,"r")
outfile1=open("%s.metadata.csv"%out,"w")
for line in infile:
    line=line.strip()
    array=line.split("\t")
    if array[4] in seq_id or array[8]=="Sequence length":
        if array[4] in seq_id:
            seq_id.remove(array[4])
        outfile1.write("%s\n" % (line))  # direct output first line + curated sequences id
    else:
        # 输出高质量的高质量的来自中国区的GISAID条目
        # all sub-china
        # Sequence length >29400
        # Pango lineage!="Unassigned"
        # N-Content <0.05
        if re.search('China', line) and int(array[8]) >= 29400 and array[13] != "" and array[22] != "" and array[13] != "Unassigned" and float(array[22]) <= 0.05:
            if not array[13] in pangolin:
                pangolin[array[13]] = 1
                outfile1.write("%s\n" % (line))
            elif pangolin[array[13]] <= args.num:
                pangolin[array[13]] += 1
                outfile1.write("%s\n" % (line))
        # 输出更高质量的高质量的来自中国区的GISAID条目
        # Sequence length >=29700
        # Pango lineage!="Unassigned"
        # N-Content <0.01
        if not re.search('China',line) and int(array[8]) >= 29700 and array[13]!="" and array[22]!="" and array[13] !="Unassigned" and float(array[22]) <= 0.01:
            location=array[6]
            if not array[13] in index:
                index[array[13]]=[]
                index[array[13]].append(location)
                outfile1.write("%s\n" % (line))#other(output=1)
                pangolin[array[13]] = 1
            else:
                if location not in index[array[13]] and array[13] in voc_id and len(index[array[13]]) <= args.num:#voc list(output different country default:<=10)
                    index[array[13]].append(location)
                    outfile1.write("%s\n" % (line))
infile.close()
outfile1.close()
for key in voc_id:
    if not key in pangolin:
        print("Warning:This classify not find %s"%key)
if not len(seq_id)==0:
    for key in seq_id:
        print("Warning:This classify not find %s"%key)
print("Done")
cmd='awk -F\"\\t\" \'{if($9!="Sequence length")print $5}\' %s.metadata.csv >%s.sequence_ID.txt'%(out,out)
subprocess.check_call(cmd,shell=True)