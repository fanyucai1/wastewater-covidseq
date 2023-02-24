1.  https://www.fda.gov/food/whole-genome-sequencing-wgs-program/wastewater-surveillance-sars-cov-2-variants

2.  生信分析

**CFSAN Wastewater Analysis Pipeline(美国FDA)**

All variant data was process with C-WAP(**https://github.com/CFSAN-Biostatistics/C-WAP**) which inludes the estimation of relative abundance of SARS-CoV-2 sublineages via the bioinformatics package Freyja(**https://github.com/andersen-lab/Freyja**) By default, Freyja now only includes lineages that are present on pangolin.（**https://github.com/cov-lineages/pangolin**）

* Designating a reference and NGS data in fastq format
* Alignment of reads to the reference via Bowtie2
* Taxonomy check via kraken2
* Processing of alignment results via samtools
* Detection of variant positions with ivar
* Determine composition of variants via kallisto, linear regression, kraken2/bracken and freyja
* Generate an html and pdf formatted summary of results

Karthikeyan S, Levy J I, De Hoff P, et al. Wastewater sequencing reveals early cryptic SARS-CoV-2 variant transmission[J]. Nature, 2022, 609(7925): 101-108.


3.  illumina推荐的生信分析流程 筛选GISAID数据筛选

    https://github.com/baymlab/wastewater_analysis
    https://github.com/baymlab/wastewater_analysis/tree/main/manuscript

Baaijens J A, Zulli A, Ott I M, et al. Lineage abundance estimation for SARS-CoV-2 in wastewater using transcriptome quantification techniques[J]. Genome biology, 2022, 23(1): 236.

4. https://github.com/fabou-uobaf/VaQuERo

5. https://github.com/cbg-ethz/cojac/





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

