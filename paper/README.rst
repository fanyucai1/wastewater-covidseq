1. **Wastewater Surveillance for SARS-CoV-2 Variants** ::

        https://www.fda.gov/food/whole-genome-sequencing-wgs-program/wastewater-surveillance-sars-cov-2-variants

2. **C-VIEW: COVID-19 VIral Epidemiology Workflow** ::

        C-WAP:  https://github.com/CFSAN-Biostatistics/C-WAP

        * Designating a reference and NGS data in fastq format
        * Alignment of reads to the reference via Bowtie2
        * Taxonomy check via kraken2
        * Processing of alignment results via samtools
        * Detection of variant positions with ivar
        * Determine composition of variants via kallisto, linear regression, kraken2/bracken and freyja
        * Generate an html and pdf formatted summary of results

        Karthikeyan S, Levy J I, De Hoff P, et al. Wastewater sequencing reveals early cryptic SARS-CoV-2 variant transmission[J]. Nature, 2022, 609(7925): 101-108.

3. **Estimation of relative abundance** ::

        Freyja:
                https://github.com/andersen-lab/Freyja
                https://github.com/andersen-lab/Freyja-data

4. **COJAC - CoOccurrence adJusted Analysis and Calling** ::

        cojac:  https://github.com/cbg-ethz/cojac/

        Jahn K, Dreifuss D, Topolsky I, et al. Early detection and surveillance of SARS-CoV-2 genomic variants in wastewater using COJAC[J]. Nature Microbiology, 2022, 7(8): 1151-1160.

5. **VLQ: Viral Lineage Quantification** ::

        VLQ:    https://github.com/baymlab/wastewater_analysis

        Baaijens J A, Zulli A, Ott I M, et al. Lineage abundance estimation for SARS-CoV-2 in wastewater using transcriptome quantification techniques[J]. Genome biology, 2022, 23(1): 236.

6. **SD-COVID-Sequencing** ::

        SD-COVID-Sequencing: https://github.com/niemasd/SD-COVID-Sequencing/
        ViReflow:   https://github.com/niemasd/ViReflow

        Moshiri N, Fisch K M, Birmingham A, et al. The ViReflow pipeline enables user friendly large scale viral consensus genome reconstruction[J]. Scientific reports, 2022, 12(1): 5077.

7. **Freyja vs kallisto** ::

        Kayikcioglu T, Amirzadegan J, Rand H, et al. Performance of methods for SARS-CoV-2 variant detection and abundance estimation within mixed population samples[J]. PeerJ, 2023, 11: e14596.

8. **waste_water metagenomics** ::

        Wyler E, Lauber C, Manukyan A, et al. Comprehensive profiling of wastewater viromes by genomic sequencing[J]. bioRxiv, 2022: 2022.12. 16.520800.

9. **Review paper** ::

        Tamáš M, Potocarova A, Konecna B, et al. Wastewater Sequencing—An Innovative Method for Variant Monitoring of SARS-CoV-2 in Populations[J]. International Journal of Environmental Research and Public Health, 2022, 19(15): 9749.

10. **SARS-CoV-2 (Va)riant (Qu)antification in s(E)wage, designed for (Ro)bustness** ::

        VaQuERo v2: https://github.com/fabou-uobaf/VaQuERo
        Amman F, Markt R, Endler L, et al. Viral variant-resolved wastewater surveillance of SARS-CoV-2 at national scale[J]. Nature Biotechnology, 2022, 40(12): 1814-1822.

11. **Compared the performance of six variant callers (VarScan, iVar, GATK, FreeBayes, LoFreq and BCFtools)** ::

        Bassano I, Ramachandran V K, Khalifa M S, et al. Evaluation of variant calling algorithms for wastewater-based epidemiology using mixed populations of SARS-CoV-2 variants in synthetic and wastewater samples[J]. medRxiv, 2022: 2022.06. 06.22275866.

12. **Lineagespot is a framework written in R, and aims to identify SARS-CoV-2 related mutations based on a single (or a list) of variant(s) file(s)** ::

        lineagespot:
        https://github.com/BiodataAnalysisGroup/lineagespot
        https://github.com/BiodataAnalysisGroup/lineagespot/blob/master/inst/scripts/raw-data-analysis.md
        Pechlivanis N, Tsagiopoulou M, Maniou M C, et al. Detecting SARS-CoV-2 lineages and mutational load in municipal wastewater and a use-case in the metropolitan area of Thessaloniki, Greece[J]. Scientific reports, 2022, 12(1): 2659.

13. **Quality control** ::

        QC Metrics                                              Cutoff
        number of nucleotides with depth <10 (for Illumina)     <3000
        assembly total length                                   >29400
        ambiguous Ns                                            <10%
        assembly mean coverage                                  >25

        Xiaoli L, Hagey J V, Park D J, et al. Benchmark datasets for SARS-CoV-2 surveillance bioinformatics[J]. PeerJ, 2022, 10: e13821.

14. **read coverage >90%** ::

        Fontenele R S, Kraberger S, Hadfield J, et al. High-throughput sequencing of SARS-CoV-2 in wastewater provides insights into circulating variants[J]. Water Research, 2021, 205: 117710.

15. **sequence depth** ::

        We found that detection of all low-frequency variants at an abundance of 10, 5, 3, and 1%, requires at least a sequencing coverage of 250, 500, 1500, and 10,000×, respectively

        Van Poelvoorde L A E, Delcourt T, Coucke W, et al. Strategy and performance evaluation of low-frequency variant calling for SARS-CoV-2 using targeted deep Illumina sequencing[J]. Frontiers in Microbiology, 2021: 3073.

16. **Select reference from GISAID** ::

        N的含量要小于1% 长度低于29K的肯定不行的，如果没有明确病人信息的序列也可以去掉

        [1] Briones M R S, Antoneli F, Ferreira R C, et al. Noisy genome data and faulty clade statistics undermine conclusions on sars-cov-2 evolution and strain typing in the Brazilian epidemy: a technical note[J]. 2020.

        This global dataset contained 2,552 subsampled sequences (full length with Ns <5%) to include 1 unique genome per country or state per week.

        [2] Izquierdo-Lara R, Elsinga G, Heijnen L, et al. Monitoring SARS-CoV-2 circulation and diversity through community wastewater sequencing, the Netherlands and Belgium[J]. Emerging infectious diseases, 2021, 27(5): 1405.

        GISAID considers genomes with length greater than 29,000 nucleotides as complete and assigns the high coverage label when there is less than 1% of undefined bases, less than 0.05% unique amino acid mutations and without insertion or deletion unless verified by the submitter.

        [3] Yu C Y, Wong S Y, Liew N W C, et al. Whole genome sequencing analysis of SARS-CoV-2 from Malaysia: From alpha to Omicron[J]. Frontiers in Medicine, 2022, 9.

        any sequence of length less than 29,000 nucleotides; any sequences with ambiguous nucleotides in excess of 0.5% of the genome; any sequences with greater than 1% divergence from the longest sampled sequence (Wuhan-Hu- 1); and any sequence with stop codons.

        [4]  Maclean O A ,  Lytras S ,  Weaver S , et al. Natural selection in the evolution of SARS-CoV-2 in bats created a generalist virus and highly capable human pathogen[J]. PLoS Biology, 2021, 19(3):e3001115.

17. **Consence seuqence coverage** ::

        Lineage/clade analysis of SARS-CoV-2 wastewater samples with >80 % genome coverage was performed using Pangolin and NextClade tools

        Silva C S, Tryndyak V P, Camacho L, et al. Temporal dynamics of SARS-CoV-2 genome and detection of variants of concern in wastewater influent from two metropolitan areas in Arkansas[J]. Science of The Total Environment, 2022, 849: 157546.

18. **genomic positions recommended to be masked from SARS-CoV-2 alignments** ::

        genomic positions recommended to be masked from SARS-CoV-2 alignments https://virological.org/t/masking
        Crits-Christoph A, Kantor R S, Olm M R, et al. Genome sequencing of sewage detects regionally prevalent SARS-CoV-2 variants[J]. MBio, 2021, 12(1): e02703-20.

19. **variant of concern (VOC)/variant of interest (VOI)/Variants Being Monitored (VBM)** ::

        https://www.ecdc.europa.eu/en/covid-19/variants-concern
        https://www.cdc.gov/coronavirus/2019-ncov/variants/variant-classifications.html

20. **CoVariants** ::

        CoVariants https://covariants.org/

21. **COVID CG(COVID-19 CoV Genetics)** ::

        COVID CG(COVID-19 CoV Genetics) https://covidcg.org
        Chen A T ,  Altschuler K ,  Zhan S H , et al. COVID-19 CG enables SARS-CoV-2 mutation and lineage tracking by locations and dates of interest[J]. eLife Sciences, 2021, 10.

22. **PiGx SARS-CoV-2 Wastewater Sequencing Pipeline** ::

        PiGx SARS-CoV-2 Wastewater Sequencing Pipeline https://github.com/BIMSBbioinfo/pigx_sars-cov-2

23. **National Wastewater Surveillance System (NWSS)** ::

        National Wastewater Surveillance System (NWSS) https://www.cdc.gov/nwss/wastewater-surveillance/index.html

24. **Santiago-Rodriguez T M. The Detection of SARS-CoV-2 in the Environment: Lessons from Wastewater[J]. Water, 2022, 14(4): 599.** ::

        Unlike untargeted high-throughput sequencing, targeted or amplicon-based approaches only require < 1 million reads to gain insights into the SARS-CoV-2 prevalence and variant genomic information.
        The potential caveat of amplicon-based approaches for SARS-CoV-2 detection is that the genomic ends may not be covered; thus, 100% genome coverage may not be reached.
        However, genome recovery can usually be attained at around > 99.0%, which may be sufficient for phylogenetic relatedness analyses

25. **Variants located outside of the region targeted by the amplicon panel were filtered out (reference genome positions 1–54 and 29,836–29,903)** ::

        Gohl D M, Garbe J, Grady P, et al. A rapid, cost-effective tailed amplicon method for sequencing SARS-CoV-2[J]. BMC genomics, 2020, 21(1): 1-10.
