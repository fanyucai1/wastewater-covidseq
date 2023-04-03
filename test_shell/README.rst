docker run -v /staging3/fanyucai/waste_water/script/:/script \
      -v /staging3/fanyucai/waste_water/outdir/pre_process/:/raw_data/ \
      waste_water:latest python3 /script/plot_coverage_from_bam.py

