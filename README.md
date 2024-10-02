Trino Plugin
============

[![Build Status](https://github.com/WaseeA/trino-nlp-embeddings/actions/workflows/release.yaml/badge.svg)](https://github.com/WaseeA/trino-nlp-embeddings/actions/workflows/release.yaml)

This is a [Trino](http://trino.io/) plugin that provides a connector.

# Quick Start

To run a Docker container with the connector, run the following:
Get your docker tag from https://hub.docker.com/repository/docker/waseedockerhub9/trino-nlp-embeddings/tags
```bash
docker run \
  -d \
  --name trino-nlp-embeddings \
  -p 8080:8080 \
  waseedockerhub9/trino-nlp-embeddings:0.22
```

Then use your favourite SQL client to connect to Trino running at http://localhost:8080

## Usage

Download one of the ZIP packages, unzip it and copy the `trino-nlp-embeddings-0.1` directory to the plugin directory on every node in your Trino cluster.
Create a `nlp_embeddings_connector.properties` file in your Trino catalog directory and set all the required properties.

```
connector.name=nlp_embeddings_connector
```

After reloading Trino, you should be able to connect to the `nlp_embeddings_connector` catalog.

## Build

Run all the unit tests:
```bash
mvn test
```

Creates a deployable zip file:
```bash
mvn clean package
```

Unzip the archive from the target directory to use the connector in your Trino cluster.
```bash
unzip target/*.zip -d ${PLUGIN_DIRECTORY}/
mv ${PLUGIN_DIRECTORY}/trino-nlp-embeddings-* ${PLUGIN_DIRECTORY}/trino-nlp-embeddings
```

## Debug

To test and debug the connector locally, run the `NLPQueryRunner` class located in tests:
```bash
mvn test-compile exec:java -Dexec.mainClass="ai.knorket.NLPQueryRunner" -Dexec.classpathScope=test
```

And then run the Trino CLI using `trino --server localhost:8080 --no-progress` and query it:
```
trino> show catalogs;
 Catalog
---------
 nlp_embeddings_connector
 system
(2 rows)

trino> show tables from nlp_embeddings_connector.default;
   Table
------------
 single_row
(1 row)

trino> select * from nlp_embeddings_connector.default.single_row;
 id |     type      |  name
----+---------------+---------
 x  | default-value | my-name
(1 row)
```
