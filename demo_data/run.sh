docker run -v /staging3/fanyucai/waste_water/demo_data/:/mnt/data -it --rm hadrieng/insilicoseq iss generate --genomes /mnt/data/demo.fna -m miseq -z -o /mnt/data/reads --coverage_file /mnt/data/coverage.txt
mv reads_R1.fastq.gz test_S7_L001_R1_001.fastq.gz
mv reads_R2.fastq.gz test_S7_L001_R2_001.fastq.gz
#python3 ../script/main_process.py -p1 test_S7_L001_R1_001.fastq.gz -p2 test_S7_L001_R2_001.fastq.gz -r ../reference/ -s ../script/ -b ../reference/SARs-CoV-2_v5.3.2_400.primer.bed -m ../reference/2023-10-18.metadata.csv -a ../reference/adapter.fasta -i ../reference/2023-10-18.kallisto_idx -p test -f ../reference/2023-10-18.fna
