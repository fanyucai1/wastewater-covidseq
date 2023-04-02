**shell command** ::

    fastq-dump --split-3 --gzip SRR20696401
    fastq-dump --split-3 --gzip SRR20696400

**reference paper** ::

    Kayikcioglu T, Amirzadegan J, Rand H, et al. Performance of methods for SARS-CoV-2 variant detection and abundance estimation within mixed population samples[J]. PeerJ, 2023, 11: e14596.

**project info** ::

    # Amplicon_panel          NCBI_bioproject_accession
        ARTICv4                 PRJNA765612
        QIAseq DIRECT           PRJNA757447
        NEB VSS v1a             PRJNA767800, PRJNA757447


docker run -v /staging3/fanyucai/waste_water/script/:/script \
      -v /staging3/fanyucai/waste_water/outdir/pre_process/:/raw_data/ \
      waste_water:latest python3 /script/plot_coverage_from_bam.py

docker run -v /staging3/fanyucai/waste_water/script/:/script \
    -v /staging3/fanyucai/waste_water/reference:/reference \
      -v /staging3/fanyucai/waste_water/outdir/kallisto/:/raw_data/ \
      waste_water:latest python3 /script/output_abundances.py -o /raw_data/predictions.tsv \
        --metadata /reference/2023-03-16.metadata.csv /raw_data/abundance.tsv