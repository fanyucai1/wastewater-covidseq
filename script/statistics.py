import os
import json
import argparse

def run(json_file,depth_file,bam2fastq_file,outdir,prefix):
    out=outdir+"/"+prefix
    outfile = open("%s.tsv" % (out), "w")
    outfile.write("SampleID\tRaw_reads\tQ20_rate(%)\tQ30_rate(%)\tClean_reads\tReads aligned PF(%)\tGenomic coordinates 0X\tGenomic coordinates <10X\n")
    with open("%s" % (json_file), "r") as load_f:
        load_dict = json.load(load_f)
    outfile.write("%s\t%s\t%s\t%s\t"
                  % (prefix,load_dict['summary']['before_filtering']['total_reads'],
                     format(float(load_dict['summary']['before_filtering']['q20_rate'])*100,".2f"),
                     format(float(load_dict['summary']['before_filtering']['q30_rate']) * 100, ".2f")))
    outfile.write("%s\t"
                  % (load_dict['summary']['after_filtering']['total_reads']))
    raw_reads=int(load_dict['summary']['before_filtering']['total_reads'])

    infile=open(bam2fastq_file,"r")
    effect=[]
    for line in infile:
        line=line.strip()
        array=line.split(" ")
        effect.append(int(array[2]))
    outfile.write("%s(%s)\t"%(effect[1]-effect[0],format(float((effect[1]-effect[0])/raw_reads*100),".2f")))
    infile.close()
    infile=open(depth_file,"r")
    depth=[0,0]
    for line in infile:
        line=line.strip()
        array=line.split("\t")
        if int(array[2])==0:
            depth[0]+=1
        if int(array[2])<10:
            depth[1]+=1
    infile.close()
    outfile.write("%s\t%s"%(depth[0],depth[1]))
    outfile.close()



if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-j","--json",help="fastp json file",required=True)
    parser.add_argument("-d","--depth",help="depth file",required=True)
    parser.add_argument("-b2f","--bam2fastq",help="screen output file from:samtools fastq",required=True)
    parser.add_argument("-p","--prefix",help="prefix of output",required=True)
    parser.add_argument("-o","--outdir",help="output directory",default=os.getcwd())
    args=parser.parse_args()
    run(args.json,args.depth,args.bam2fastq,args.outdir,args.prefix)