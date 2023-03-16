**File download link**
::
    bed and primer
    https://github.com/CFSAN-Biostatistics/C-WAP/tree/main/covidRefSequences
    fasta and gff
    https://www.ncbi.nlm.nih.gov/nuccore/NC_045512.2

**build reference index**
::
    bowtie2-build /reference/NC_045512.2.fa /reference/NC_045512.2
    samtools faidx /reference/NC_045512.2.fa