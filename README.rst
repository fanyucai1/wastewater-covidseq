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

6.  The ViReflow pipeline enables user friendly large scale viral consensus genome reconstruction
::

    ViReflow:   https://github.com/niemasd/ViReflow
