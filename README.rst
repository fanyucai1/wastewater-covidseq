#.  learn konwledge: *paper/*

#.  build docker image: *Docker/*

#.  analysis script:  *script/*

#.  prepare reference dataset: *reference/*

#.  download test data: *test_data/*

#.  test shell script: *shell/*

#.  usr guide

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
      waste_water:latest python3 /script/trim_fastq.py -p1 /raw_data/SRR20696400_1.fastq.gz -p2 /raw_data/SRR20696400_2.fastq.gz \
      -a /reference/adapter.fasta \
      -i /reference/NC_045512.2 -b /reference/ARTICv4.bed -r /reference/NC_045512.2.fa \
      -g /reference/NC_045512.2.gff3 -o /outdir/ -p SRR20696400

**step2:Run Freyja to recover relative lineage abundances(BAM aligned to the Hu-1 reference)**

    **python3 script/freyja.py**

