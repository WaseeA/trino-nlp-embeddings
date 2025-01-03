#!/usr/bin/env bash

set -euo pipefail
set -x

if [ -f release.properties ]; then
    VERSION=$(grep 'project.rel.ai.knorket\\:trino-nlp-embeddings=' release.properties | cut -d'=' -f2)
else
    VERSION=$(mvn help:evaluate -Dexpression=project.version -q -DforceStdout)
fi
TRINO_VERSION=$(mvn help:evaluate -Dexpression=dep.trino.version -q -DforceStdout)

echo "Using TRINO_VERSION: $TRINO_VERSION"
echo "Using VERSION: $VERSION"

TAG=waseedockerhub9/trino-nlp-embeddings:$VERSION

# FOR DEPLOYMENT
docker buildx build \
    --platform linux/amd64 \
    -t "$TAG" \
    --build-arg TRINO_VERSION="$TRINO_VERSION" \
    --build-arg VERSION="$VERSION" \
    --push \
    .

# FOR LOCAL TESTING
# docker buildx build \
#     -t "$TAG" \
#     --build-arg TRINO_VERSION="$TRINO_VERSION" \
#     --build-arg VERSION="$VERSION" \
#     --load \
#     .