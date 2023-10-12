directory
+++++++++++++++++

#.  learn konwledge: *paper/*

#.  build docker image: *Docker/*

#.  analysis script:  *script/*

#.  prepare reference dataset: *reference/*

#.  download test data: *test_data/*

bioinformatics
++++++++++++++++++++++++++++

    docker pull fanyucai1/waste_water:latest

build reference
++++++++++++++++++++++
`Kraken2 Refseq indexes <https://benlangmead.github.io/aws-indexes/k2>`_

`ARTIC bed <https://github.com/CFSAN-Biostatistics/C-WAP/tree/main/covidRefSequences>`_

`NC_045512.2 <https://www.ncbi.nlm.nih.gov/nuccore/NC_045512.2>`_ ::

    axel -n20 https://genome-idx.s3.amazonaws.com/kraken/k2_pluspfp_20230314.tar.gz
    tar xzvf k2_pluspfp_20230314.tar.gz
    bowtie2-build /reference/NC_045512.2.fa /reference/NC_045512.2
    samtools faidx /reference/NC_045512.2.fa

`Prepare GISAID and metadata <https://gisaid.org>`_

    **select GISAID sequence** ::

        python3 script/select_GISAID.py -m reference/GISAID_metadata.tsv -c reference/core.list -v reference/voc.txt -o reference/ -n 10

    **upload sequence id to GISAID to download fasta sequence**

    **select no redundant sequence and build kallisto index** ::

        python3 script/cd-hit-est.py -f reference/sequence.fna -c 0.995 -o reference/ -p test

`Freyja-data <https://github.com/andersen-lab/Freyja-data>`_

    **Downdload Previous versions of Freyja barcodes and metadata files**

    associated barcodes: `usher_barcodes.csv <https://github.com/andersen-lab/Freyja-data/blob/main/>`_

    the most recent metadata: `curated_lineages.json <https://github.com/andersen-lab/Freyja-data/blob/main/>`_

    **Only download two files, you can use** `DownGit <https://minhaskamal.github.io/DownGit/#/home>`_

usr guide
++++++++++++++++++

**step1:Preprocessing sequencing data**

    **python3 script/trim_fastq.py**

    #. quality control
    #. mapping reference
    #. trim primers、remove soft-clipped primers
    #. calculate depth
    #. restore fastq
    #. variantCalling
    #. consence sequence and determine the predominant lineage

shell script ::

    docker run -v /path/to/reference:/reference \
      -v /path/to/script/:/script \
      -v /path/to/test_data:/raw_data/ \
      -v /path/to/outdir/pre_process/:/outdir/ \
      waste_water:latest python3 /script/trim_fastq.py \
      -p1 /raw_data/SRR20696400_1.fastq.gz -p2 /raw_data/SRR20696400_2.fastq.gz \
      -a /reference/adapter.fasta \
      -i /reference/NC_045512.2 -b /reference/ARTICv4.bed -r /reference/NC_045512.2.fa \
      -g /reference/NC_045512.2.gff3 -o /outdir/ -p SRR20696400

**step2:Use Freyja to recover relative lineage abundances(BAM aligned to the Hu-1 reference)**

    **python3 script/freyja.py**

shell script ::

    docker run -v /path/to/reference/:/reference \
    -v /path/to/script/:/script \
    -v /path/to/outdir/freyja:/outdir/ \
    -v /path/to/outdir/pre_process/:/raw_data/ \
    waste_water:latest python3 /script/freyja.py -b /raw_data/SRR20696400.soft.clipped.sort.bam \
    -r /reference/NC_045512.2.fa \
    --barcode /reference/usher_barcodes.csv  \
    --meta /reference/curated_lineages.json \
    -o /outdir/ -p SRR20696400 --nb 100

**step3: Use kallisto to predict abundance per lineage**

    **python3 script/kallisto.py**

shell script ::

    docker run -v /path/to/reference:/reference \
    -v /path/to/script/:/script \
    -v /path/to/outdir/kallisto/:/outdir/ \
    -v /pat/to/outdir/pre_process:/raw_data/ \
    waste_water:latest python3 /script/kallisto.py \
    -p1 /raw_data/SRR20696400.R1.fq -p2 /raw_data/SRR20696400.R2.fq \
    -i /reference/sequences.kallisto_idx \
    -o /outdir/ -p SRR20696400 \
    --fna /reference/gisaid_hcov-19_2023_03_16_03.fasta \
    --meta /reference/2023-03-16.metadata.csv

    docker run -v /staging3/fanyucai/waste_water/reference:/reference \
    -v /staging3/fanyucai/waste_water/script:/script  \
    -v /staging3/fanyucai/waste_water/2023.10/test/:/outdir/ \
    -v /staging3/fanyucai/waste_water/2023.10/outdir/pre_process:/raw_data/
    waste_water:latest python3 /script/kallisto.py 	\
    -p1 /raw_data/4.R1.fq -p2 /raw_data/4.R2.fq     \
    -i /reference/2023-10-10.kallisto_idx     \
    -o /outdir/ -p 4 --fna /reference/2023-10-10.fna \
    --meta /reference/2023-10-10.metadata.csv

Other
+++++++++++++
1.Out of the 325, 183 (56.3%) samples had >50% sequence coverage of the whole genome (10x depth) and these were used for Freyja analysis.

`Yousif, M., Rachida, S., Taukobong, S. et al. SARS-CoV-2 genomic surveillance in wastewater as a model for monitoring evolution of endemic viruses. Nat Commun 14, 6325 (2023). <https://doi.org/10.1038/s41467-023-41369-5>`_

2.A maximum of 1 000 000 reads are kept to limit the computation time of variant calling processes(kallisto run slowly)

`Kayikcioglu T, Amirzadegan J, Rand H, et al. Performance of methods for SARS-CoV-2 variant detection and abundance estimation within mixed population samples[J]. PeerJ, 2023, 11: e14596. <https://peerj.com/articles/14596/>`_

3.Online services with SARS-CoV-2 genome resources and analytics

