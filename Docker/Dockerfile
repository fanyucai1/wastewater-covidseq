FROM covlineages/pangolin:latest
RUN mkdir -p /root/nextclade/ && mkdir -p /root/ref_fasta && mkdir -p /software /raw_data /script /outdir /reference/
COPY jvarkit.jar /software/
COPY NC_045512.2.fa /reference/
RUN conda update -n base -c defaults conda
RUN conda install -c bioconda nextclade trimmomatic ivar samtools bowtie2 kallisto bcftools minimap2 bbmap
RUN ln -s /opt/conda/bin/nextclade /root/nextclade/nextclade
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple seaborn matplotlib numpy pysam
RUN conda install -c conda-forge pyvcf
RUN nextclade dataset get --name='sars-cov-2' --output-dir='/root/nextclade/'
RUN conda create -n freyja-env
RUN conda config --add channels bioconda
RUN conda config --add channels conda-forge
RUN conda install freyja
RUN conda env export > freyja-env.yml
COPY trim_fastq.py /script/