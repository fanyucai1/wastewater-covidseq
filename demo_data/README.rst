1.下载docker软件 ::

    docker pull hadrieng/insilicoseq:latest

2.获得高质量的参考数据 ::

    wget http://hgdownload.soe.ucsc.edu/goldenPath/wuhCor1/UShER_SARS-CoV-2/public-latest.metadata.tsv.gz

    awk '{if($9==$11)print}' public-latest.metadata.tsv|grep "BA.1.1"|grep 2023 |head
        EPI_ISL_16586702
    awk '{if($9==$11)print}' public-latest.metadata.tsv|grep "BA.5.1"|grep 2023 |head
         EPI_ISL_17542743
    awk '{if($9==$11)print}' public-latest.metadata.tsv|grep "BA.5.2.48"|grep 2023 |head
         EPI_ISL_16722022
    awk '{if($9==$11)print}' public-latest.metadata.tsv|grep "BF.7.14"|grep 2023 |head
         EPI_ISL_16722021
    awk '{if($9==$11)print}' public-latest.metadata.tsv|grep "B.1.617.2"|grep 2023 |head
         EPI_ISL_6245845

3. download fasta sequence from GISAID https://gisaid.org/

4. prepare coverage.txt ::

    BA.1.1 2100
    BA.5.1 600
    BA.5.2.48 450
    BF.7.14 300
    B.1.617.2 150

5. 模拟数据 注意fasta文件序列名称不能太长建议，上面的就好模拟失败 ::

    docker run -v /staging/explify_china/test_data/:/mnt/data -it --rm hadrieng/insilicoseq iss generate --genomes /mnt/data/demo.fna -m NovaSeq -z -o /mnt/data/reads --coverage_file /mnt/data/coverage.txt
    mv reads_R1.fastq.gz test_S7_L001_R1_001.fastq.gz
    mv reads_R2.fastq.gz test_S7_L001_R2_001.fastq.gz
