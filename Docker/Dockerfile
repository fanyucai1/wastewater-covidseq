FROM covlineages/pangolin:latest
RUN apk add build-base
RUN apk add --upgrade zlib-dev bzip2 bzip2-dev xz-dev
COPY bcftools-1.17.tar.bz2 /software/
RUN cd /software && tar xjvf bcftools-1.17.tar.bz2 && cd bcftools-1.17 && ./configure && make -j20 && make install
RUN mkdir -p /root/nextclade/ && mkdir -p /root/ref_fasta && mkdir -p /software /raw_data /script /outdir /reference/ /index/
COPY jvarkit.jar /software/
RUN conda update -n base -c defaults conda
RUN conda install -c bioconda ivar=1.3 nextclade trimmomatic bowtie2 kallisto minimap2 bbmap mafft iqtree fastp
RUN conda install -c agbiome cdhit
RUN ln -s /opt/conda/bin/nextclade /root/nextclade/nextclade
RUN pip3 install seaborn matplotlib numpy pysam pandas
RUN mkdir -p /pangolin/
RUN conda install -c conda-forge pyvcf
RUN nextclade dataset get --name='sars-cov-2' --output-dir='/root/nextclade/'
RUN conda create -n freyja-env
RUN conda config --add channels conda-forge
RUN conda install conda-libmamba-solver
RUN conda install -c bioconda freyja=1.4.7
RUN conda env export > freyja-env.yml
COPY samtools-1.17.tar.bz2 /software/
RUN cd /software/ && tar xjvf samtools-1.17.tar.bz2 && cd samtools-1.17 &&  \
    ./configure --prefix=/software/samtools-v1.17 --without-curses && make -j20 && make install &&  \
    rm -rf samtools-1.17.tar.bz2 bcftools-1.17.tar.bz2 samtools-1.17
RUN conda install -c bioconda kraken2 krakentools bedtools
RUN apk add libxau
RUN conda install -c bioconda seqtk