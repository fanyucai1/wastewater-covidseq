1.  Wastewater Surveillance for SARS-CoV-2 Variants
::

    https://www.fda.gov/food/whole-genome-sequencing-wgs-program/wastewater-surveillance-sars-cov-2-variants

2.  C-VIEW: COVID-19 VIral Epidemiology Workflow
::

    C-WAP:  https://github.com/CFSAN-Biostatistics/C-WAP

    * Designating a reference and NGS data in fastq format
    * Alignment of reads to the reference via Bowtie2
    * Taxonomy check via kraken2
    * Processing of alignment results via samtools
    * Detection of variant positions with ivar
    * Determine composition of variants via kallisto, linear regression, kraken2/bracken and freyja
    * Generate an html and pdf formatted summary of results

3.  Estimation of relative abundance
::

    Freyja: https://github.com/andersen-lab/Freyja

4.  COJAC - CoOccurrence adJusted Analysis and Calling
::

    cojac:  https://github.com/cbg-ethz/cojac/

5.  VLQ: Viral Lineage Quantification
::

    VLQ:    https://github.com/baymlab/wastewater_analysis

    Baaijens J A, Zulli A, Ott I M, et al. Lineage abundance estimation for SARS-CoV-2 in wastewater using transcriptome quantification techniques[J]. Genome biology, 2022, 23(1): 236.



7. Nextclade https://docs.nextstrain.org/projects/nextclade/en/stable/index.html

进化分析Nextstain+auspice(进化树可视化)

* auspice https://docs.nextstrain.org/projects/auspice/en/stable/introduction/how-to-run.html

* Nextstain的GISAID筛选（"Augur pipeline”）

    https://docs.nextstrain.org/projects/ncov/en/latest/guides/data-prep/gisaid-full.html
    https://docs.nextstrain.org/projects/ncov/en/latest/guides/data-prep/gisaid-search.html


a.数据质控、去adapter

b.比对bowtie2

c.ivar去引物并生成一致性序列 https://andersen-lab.github.io/ivar/html/manualpage.html

d.丰度评估（仅新冠）

Download software:
https://github.com/lindenb/jvarkit

