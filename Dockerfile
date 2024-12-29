ARG TRINO_VERSION=436
FROM nineinchnick/trino-core:$TRINO_VERSION

ARG VERSION

# Add the trino configuration files
ADD target/trino-nlp-embeddings-$VERSION/ /usr/lib/trino/plugin/nlp_embeddings_connector/
ADD catalog/nlp_embeddings_connector.properties /etc/trino/catalog/nlp_embeddings_connector.properties
RUN mkdir -p /usr/lib/trino/etc/
ADD catalog/config.properties /usr/lib/trino/etc/config.properties

# Create the directory for Python scripts inside the container
RUN mkdir -p /data/trino/src/py_scripts
COPY --chmod=0755 src/py_scripts/script.py /data/trino/src/py_scripts/
COPY --chmod=0755 src/py_scripts/requirements.txt /data/trino/src/py_scripts/

# install dependencies
# postgresql
RUN curl -o /tmp/postgresql.tar.gz https://ftp.postgresql.org/pub/source/v15.3/postgresql-15.3.tar.gz && \
    tar -xzf /tmp/postgresql.tar.gz -C /tmp && \
    cd /tmp/postgresql-15.3 && \
    ./configure && make && make install && \
    rm -rf /tmp/postgresql*

# pip
RUN curl -sSL https://bootstrap.pypa.io/get-pip.py | python3
ENV PATH="/home/trino/.local/bin:${PATH}"
RUN pip install -r /data/trino/src/py_scripts/requirements.txt

# debugging
RUN python3 -c "import torch; print('PyTorch version:', torch.__version__)"