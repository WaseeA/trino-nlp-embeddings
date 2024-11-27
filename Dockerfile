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

# Install python
RUN apt-get update && apt-get install -y \
    python3 python3-pip build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install --upgrade pip

# install dependencies
RUN pip3 install -r /data/trino/src/py_scripts/requirements.txt

# debugging
RUN python3 -c "import torch; print('PyTorch version:', torch.__version__)"