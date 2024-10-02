ARG TRINO_VERSION
FROM nineinchnick/trino-core:$TRINO_VERSION

ARG VERSION

ADD target/trino-nlp-embeddings-$VERSION/ /usr/lib/trino/plugin/nlp_embeddings_connector/
ADD catalog/nlp_embeddings_connector.properties /etc/trino/catalog/nlp_embeddings_connector.properties
RUN mkdir -p /usr/lib/trino/etc/
ADD catalog/config.properties /usr/lib/trino/etc/config.properties
