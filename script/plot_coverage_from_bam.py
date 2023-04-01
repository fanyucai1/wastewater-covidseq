import pysam
import matplotlib.pyplot as plt
import numpy as np
import sys
import subprocess


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


