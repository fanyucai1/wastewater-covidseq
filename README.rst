directory
+++++++++++++++++

#.  learn konwledge: *paper/*

#.  build docker image: *Docker/*

#.  analysis script:  *script/*

#.  prepare reference dataset: *reference/*

#.  download test data: *test_data/*

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

Previous versions of Freyja barcodes and metadata files: `Freyja-data <https://github.com/andersen-lab/Freyja-data>`_

associated barcodes: `usher_barcodes.csv <https://github.com/andersen-lab/Freyja-data/blob/main/>`_

the most recent metadata: `curated_lineages.json <https://github.com/andersen-lab/Freyja-data/blob/main/>`_

    **python3 script/freyja.py**


shell script ::

    docker run -v /path/to/reference/:/reference \
    -v /path/to/script/:/script \
    -v /path/to/outdir/freyja:/outdir/ \
    -v /path/to/outdir/pre_process/:/raw_data/ \
    waste_water:latest python3 /script/freyja.py -b /raw_data/SRR20696400.trimmed.bam \
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
    -f /raw_data/SRR20696400.resorted.fastq -i /reference/sequences.kallisto_idx \
    -o /outdir/ -p SRR20696400

