docker run -v /staging3/fanyucai/waste_water/script/:/script \
      -v /staging3/fanyucai/waste_water/outdir/pre_process/:/raw_data/ \
      waste_water:latest python3 /script/plot_coverage_from_bam.py

docker run -v /staging3/fanyucai/waste_water/script/:/script \
    -v /staging3/fanyucai/waste_water/reference:/reference \
      -v /staging3/fanyucai/waste_water/outdir/kallisto/:/raw_data/ \
      waste_water:latest python3 /script/kallisto.py \
-f /raw_data/SRR20696400.resorted.fastq -i /reference/sequences.kallisto_idx \
-o /outdir/ -p SRR20696400 -f /reference/gisaid_hcov-19_2023_03_16_03.fasta -m /reference/2023-03-16.metadata.csv

