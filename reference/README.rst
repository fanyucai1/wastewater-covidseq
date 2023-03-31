#. **File download link** ::

    bed and primer
    https://github.com/CFSAN-Biostatistics/C-WAP/tree/main/covidRefSequences
    fasta and gff
    https://www.ncbi.nlm.nih.gov/nuccore/NC_045512.2

#. **build reference index** ::

    bowtie2-build /reference/NC_045512.2.fa /reference/NC_045512.2
    samtools faidx /reference/NC_045512.2.fa

#. `Freyja-data: https://github.com/andersen-lab/Freyja-data <https://github.com/andersen-lab/Freyja-data>`_

    Only download Previous versions of Freyja barcodes and metadata files.

    You can use DownGit: https://minhaskamal.github.io/DownGit/#/home

    `metadata: https://github.com/andersen-lab/Freyja-data/blob/main/curated_lineages.json <https://github.com/andersen-lab/Freyja-data/blob/main/curated_lineages.json>`_

    `barcode file: https://github.com/andersen-lab/Freyja-data/blob/main/usher_barcodes.csv  <https://github.com/andersen-lab/Freyja-data/blob/main/usher_barcodes.csv>`_

#.  **select GISAID sequence and build kallisto index**

        python3 script/select_GISAID.py -m GISAID_metadata.tsv -c core.list -v voc.txt -o ./ -n 10

        upload sequence id to GISAID to download fasta sequence

        python3 script/cd-hit-est.py -f sequence.fna -c 0.995 -o ./ -p test

        kallisto index -i sequences.kallisto_idx test.fna