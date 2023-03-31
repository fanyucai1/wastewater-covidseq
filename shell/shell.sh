docker run -v /staging3/fanyucai/waste_water/reference:/reference \
  -v /staging3/fanyucai/waste_water/script/:/script \
  -v /staging3/fanyucai/waste_water/test_data:/raw_data/ \
  -v /staging3/fanyucai/waste_water/outdir:/outdir/ \
  waste_water:latest python3 /script/trim_fastq.py -p1 /raw_data/SRR20696395_1.fastq.gz -p2 /raw_data/SRR20696395_2.fastq.gz \
  -a /reference/adapter.fasta \
  -i /reference/NC_045512.2 -b /reference/ARTICv4.bed -r /reference/NC_045512.2.fa \
  -g /reference/NC_045512.2.gff3 -o /outdir/

docker run -v /staging3/fanyucai/waste_water/reference:/reference \
  -v /staging3/fanyucai/waste_water/script/:/script \
  -v //staging3/fanyucai/waste_water/outdir2:/raw_data/ \
  waste_water:latest python3 /script/run_kallisto.py \
  -f /raw_data/2023-03-29.all_reads.fq -i /reference/GISAID_kallisto_index/sequences.kallisto_idx \
  -o /raw_data/ -p test


docker run -v /staging3/fanyucai/waste_water/Freyja-data/:/reference \
  -v /staging3/fanyucai/waste_water/Freyja_out:/outdir/ \
  -v /staging3/fanyucai/waste_water/outdir2:/raw_data/ \
  waste_water freyja variants /raw_data/2023-03-29.trimmed.bam \
  --variants /outdir/test.freyja.variants.tsv \
  --depths /outdir/test.freyja.depths.tsv \
  --ref /reference/NC_045512.2.fa

docker run -v /staging3/fanyucai/waste_water/Freyja-data/:/reference \
  -v /staging3/fanyucai/waste_water/Freyja_out:/outdir/ \
  -v /staging3/fanyucai/waste_water/outdir2:/raw_data/ \
  waste_water sh -c 'activate freyja-env && freyja demix /outdir/test.freyja.variants.tsv /outdir/test.freyja.depths.tsv --barcodes /reference/usher_barcodes.csv --meta /reference/curated_lineages.json --eps 0.0001 --output /outdir/test.demix --confirmedonly && freyja boot /outdir/test.freyja.variants.tsv /outdir/test.freyja.depths.tsv --boxplot pdf --nt 20 --nb 1000 --output_base /outdir/freyja_boot'

