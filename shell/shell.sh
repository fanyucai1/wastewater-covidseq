docker run -v /staging3/fanyucai/waste_water/reference:/reference \
  -v /staging3/fanyucai/waste_water/script/:/script \
  -v /staging3/fanyucai/waste_water/test_data:/raw_data/ \
  -v /staging3/fanyucai/waste_water/outdir:/outdir/ \
  waste_water:latest python3 /script/trim_fastq.py -p1 /raw_data/SRR20696395_1.fastq.gz -p2 /raw_data/SRR20696395_2.fastq.gz \
  -a /reference/adapter.fasta \
  -i /reference/NC_045512.2 -b /reference/ARTICv4.bed -r /reference/NC_045512.2.fa \
  -g /reference/NC_045512.2.gff3 -o /outdir/
