

docker run -v /staging3/fanyucai/waste_water/reference:/reference \
  -v /staging3/fanyucai/waste_water/script/:/script \
  -v //staging3/fanyucai/waste_water/outdir2:/raw_data/ \
  waste_water:latest python3 /script/run_kallisto.py \
  -f /raw_data/2023-03-29.all_reads.fq -i /reference/GISAID_kallisto_index/sequences.kallisto_idx \
  -o /raw_data/ -p test
