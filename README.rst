1.  **Wastewater Surveillance for SARS-CoV-2 Variants**
::

    https://www.fda.gov/food/whole-genome-sequencing-wgs-program/wastewater-surveillance-sars-cov-2-variants

2.  **C-VIEW: COVID-19 VIral Epidemiology Workflow**
::

    C-WAP:  https://github.com/CFSAN-Biostatistics/C-WAP

    * Designating a reference and NGS data in fastq format
    * Alignment of reads to the reference via Bowtie2
    * Taxonomy check via kraken2
    * Processing of alignment results via samtools
    * Detection of variant positions with ivar
    * Determine composition of variants via kallisto, linear regression, kraken2/bracken and freyja
    * Generate an html and pdf formatted summary of results

    Karthikeyan S, Levy J I, De Hoff P, et al. Wastewater sequencing reveals early cryptic SARS-CoV-2 variant transmission[J]. Nature, 2022, 609(7925): 101-108.

3.  **Estimation of relative abundance**
::

    Freyja:
            https://github.com/andersen-lab/Freyja
            https://github.com/andersen-lab/Freyja-data

4.  **COJAC - CoOccurrence adJusted Analysis and Calling**
::

    cojac:  https://github.com/cbg-ethz/cojac/

    Jahn K, Dreifuss D, Topolsky I, et al. Early detection and surveillance of SARS-CoV-2 genomic variants in wastewater using COJAC[J]. Nature Microbiology, 2022, 7(8): 1151-1160.

5.  **VLQ: Viral Lineage Quantification**
::

    VLQ:    https://github.com/baymlab/wastewater_analysis

    Baaijens J A, Zulli A, Ott I M, et al. Lineage abundance estimation for SARS-CoV-2 in wastewater using transcriptome quantification techniques[J]. Genome biology, 2022, 23(1): 236.

6.  **SD-COVID-Sequencing**
::

    SD-COVID-Sequencing: https://github.com/niemasd/SD-COVID-Sequencing/
    ViReflow:   https://github.com/niemasd/ViReflow

    Moshiri N, Fisch K M, Birmingham A, et al. The ViReflow pipeline enables user friendly large scale viral consensus genome reconstruction[J]. Scientific reports, 2022, 12(1): 5077.

7.  **Freyja vs kallisto**
::

    Kayikcioglu T, Amirzadegan J, Rand H, et al. Performance of methods for SARS-CoV-2 variant detection and abundance estimation within mixed population samples[J]. PeerJ, 2023, 11: e14596.

8.  **waste_water metagenomics**
::

    Wyler E, Lauber C, Manukyan A, et al. Comprehensive profiling of wastewater viromes by genomic sequencing[J]. bioRxiv, 2022: 2022.12. 16.520800.

9.  **Review paper**
::

    Tamáš M, Potocarova A, Konecna B, et al. Wastewater Sequencing—An Innovative Method for Variant Monitoring of SARS-CoV-2 in Populations[J]. International Journal of Environmental Research and Public Health, 2022, 19(15): 9749.

10. **SARS-CoV-2 (Va)riant (Qu)antification in s(E)wage, designed for (Ro)bustness**
::

    VaQuERo v2: https://github.com/fabou-uobaf/VaQuERo

    Amman F, Markt R, Endler L, et al. Viral variant-resolved wastewater surveillance of SARS-CoV-2 at national scale[J]. Nature Biotechnology, 2022, 40(12): 1814-1822.

11. **Compared the performance of six variant callers (VarScan, iVar, GATK, FreeBayes, LoFreq and BCFtools)**
::

    Bassano I, Ramachandran V K, Khalifa M S, et al. Evaluation of variant calling algorithms for wastewater-based epidemiology using mixed populations of SARS-CoV-2 variants in synthetic and wastewater samples[J]. medRxiv, 2022: 2022.06. 06.22275866.

12. **Lineagespot is a framework written in R, and aims to identify SARS-CoV-2 related mutations based on a single (or a list) of variant(s) file(s)**
::
    lineagespot:
    https://github.com/BiodataAnalysisGroup/lineagespot
    https://github.com/BiodataAnalysisGroup/lineagespot/blob/master/inst/scripts/raw-data-analysis.md

    Pechlivanis N, Tsagiopoulou M, Maniou M C, et al. Detecting SARS-CoV-2 lineages and mutational load in municipal wastewater and a use-case in the metropolitan area of Thessaloniki, Greece[J]. Scientific reports, 2022, 12(1): 2659.