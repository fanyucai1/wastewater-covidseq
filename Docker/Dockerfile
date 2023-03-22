FROM covlineages/pangolin:latest
RUN apk add build-base
RUN apk add --upgrade zlib-dev bzip2 bzip2-dev xz-dev
COPY bcftools-1.17.tar.bz2 /software/
RUN cd /software && tar xjvf bcftools-1.17.tar.bz2 && cd bcftools-1.17 && ./configure && make -j20 && make install
RUN mkdir -p /root/nextclade/ && mkdir -p /root/ref_fasta && mkdir -p /software /raw_data /script /outdir /reference/ /index/
COPY jvarkit.jar /software/
RUN conda update -n base -c defaults conda
RUN conda create -n ivar-env
RUN conda config --add channels bioconda
RUN conda install ivar=1.3
RUN conda env export >ivar-env.yml
RUN conda install -c bioconda nextclade trimmomatic samtools bowtie2 kallisto minimap2 bbmap mafft iqtree fastp
RUN conda install -c agbiome cdhit
RUN ln -s /opt/conda/bin/nextclade /root/nextclade/nextclade
RUN pip3 install seaborn matplotlib numpy pysam pandas
RUN mkdir -p /pangolin/
RUN conda install -c conda-forge pyvcf
RUN nextclade dataset get --name='sars-cov-2' --output-dir='/root/nextclade/'
RUN conda create -n freyja-env
RUN conda config --add channels conda-forge
RUN conda install -c bioconda freyja
RUN conda env export > freyja-env.yml