# dependencies install
FROM ubuntu:20.04 AS builder
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    unzip \
    openjdk-11-jdk \
    && apt-get clean

RUN mkdir -p /data/trino/src/py_scripts
COPY src/py_scripts/ /data/trino/src/py_scripts/
COPY --chmod=0755 src/py_scripts/requirements.txt /data/trino/src/py_scripts/
RUN pip3 install -r /data/trino/src/py_scripts/requirements.txt

# trino config
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
