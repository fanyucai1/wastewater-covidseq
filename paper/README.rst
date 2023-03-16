1.   N的含量要小于1% 长度低于29K的肯定不行的，如果没有明确病人信息的序列也可以去掉
::
    2020-Noisy genome data and faulty clade statistics undermine conclusions on SARS-CoV-2 evolution and strain typing in the Brazilian epidemy: A Technical Note

2.   We found that detection of all low-frequency variants at an abundance of 10, 5, 3, and 1%, requires at least a sequencing coverage of 250, 500, 1500, and 10,000×, respectively
::
    2021-Strategy and Performance Evaluation of Low-Frequency Variant Calling for SARS-CoV-2 Using Targeted Deep Illumina Sequencing

3.  We removed from all analyses the genomic posi- tions recommended to be masked from SARS-CoV-2 alignments by https://virological.org/t/masking -strategies-for-sars-cov-2-alignments/480.
::
    2021-Genome Sequencing of Sewage Detects Regionally Prevalent SARS-CoV-2 Variants

4.  read coverage >90%
::
    2021-High-throughput sequencing of SARS-CoV-2 in wastewater provides insights into circulating variants

5.  全球数据筛选This global dataset contained 2,552 subsampled sequences (full length with Ns <5%) to include 1 unique genome per country or state per week.
::

6.  序列长度可以选择29400bp以上的，对于单个样本测序，测序深度低于10的碱基数目小于3000，拼接的平均coverage大于25，比对到武汉参考基因大于65%，N小于10%，这篇文章提供了人工修订的参考基因序列
::
    2022-Benchmark datasets for SARS-CoV-2 surveillance bioinformatics

7.  提供了几个参考基因组序列名字
::
    Evaluation of variant calling algorithms for wastewater-based epidemiology using mixed populations of SARS-CoV-2 variants in synthetic and wastewater samples

8.  Lineage/clade analysis of SARS- CoV-2 wastewater samples with >80 % genome coverage was performed using Pangolin and NextClade tools, v1.13.1,
::
    2022-Temporal dynamics of SARS-CoV-2 genome and detection of variants of concern in wastewater influent from two metropolitan areas in Arkansas

9.  过滤参考
::
    Sequence length >29400
    Pango lineage!="Unassigned" $14!="Unassigned"
    Is high coverage?="TRUE"
    Is complete? ="TRUE"
    N-Content <0.01 ###### $23 <=0.05

10.  abc
::
    variant of concern (VOC)
    variant of interest (VOI)
    Variants Being Monitored (VBM)
    https://www.cdc.gov/coronavirus/2019-ncov/variants/variant-classifications.html
