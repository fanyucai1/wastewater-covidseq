#.  software list ::

        pangolin
        nextclade
        fastp
        trimmomatic
        samtools
        bcftools
        ivar
        cdhit
        bowtie2
        kallisto
        minimap2
        bbmap
        mafft
        iqtree
        jvarkit
        freyja

#.  python3 module ::

        seaborn
        matplotlib
        numpy
        pysam
        pandas

#. build docker shell script ::

    docker rmi -f covlineages/pangolin:latest
    docker rmi -f waste_water:latest
    docker build -t waste_water ./
    docker push waste_water

