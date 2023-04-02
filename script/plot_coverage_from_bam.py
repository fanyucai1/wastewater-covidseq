import os
import pysam
import matplotlib.pyplot as plt
import numpy as np
import sys
import argparse
import time

parser=argparse.ArgumentParser("")
parser.add_argument("-b","--bam",help="bam file",required=True)
parser.add_argument("-o","--outdir",help="output directory",default=os.getcwd())
parser.add_argument("-p","--prefix",help="prefix of output",required=True)
parser.add_argument("--chr",help="chrome name")
args=parser.parse_args()



# 打开BAM文件
bamfile = pysam.AlignmentFile("/raw_data/SRR20696400.trimmed.bam", "rb")

# 获取参考序列长度
ref_len = bamfile.lengths[0]

# 初始化覆盖度列表
cov = [0] * ref_len

# 遍历BAM文件，累加每个位置的深度
for read in bamfile.fetch():
    for i in range(read.reference_start, read.reference_end):
        cov[i] += 1

# 绘制测序覆盖度图
plt.yscale("log")
plt.plot(cov)
plt.xlabel('Position')
plt.ylabel('Coverage')
plt.title('Coverage of your sample')
plt.savefig("/raw_data/test.pdf", dpi=300)


