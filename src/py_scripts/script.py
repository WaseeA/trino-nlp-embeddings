#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import sys
import torch
import psycopg2
import numpy as np
from transformers import BertTokenizer, BertModel
from sentence_transformers import SentenceTransformer

# Define database connection parameters
DB_CONFIG = {
    "host": "13.50.106.58",
    "database": "test",
    "user": "test",
    "password": "test",
}

def sentence_to_embeddings(model, query):
    return model.encode(query)

def connect_db():
    connection = None
    cursor = None

    try:
        connection = psycopg2.connect(**DB_CONFIG)
        return connection
    except Exception as e:
        print(f"Connection Failed: {e}")
        return None

def fetch_embeddings_from_db(connection):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, embedding FROM embeddings;")
            rows = cursor.fetchall()
            return [(row[0], np.array(row[1])) for row in rows]
    except Exception as e:
        print(f"Error fetching embeddings: {e}")
        return []
    
if __name__ == "__main__":
    # The query is passed as the second argument
    if len(sys.argv) < 2:
        print("Usage: python script.py \"<query string>\"")
    else:
        model = SentenceTransformer("multi-qa-mpnet-base-cos-v1")
        query = sys.argv[1]
        embeddings = sentence_to_embeddings(model, query)
        connection = connect_db()
        if (connection):
            connection.close()

        

# models: https://huggingface.co/models?sort=downloads

# SELECT run_py('/data/trino/src/py_scripts/script.py') AS result;
# SELECT square(4);
# docker exec -it trino-nlp-embeddings bash
# docker cp src/py_scripts/requirements.txt trino-nlp-embeddings:/data/trino/src/py_scripts/requirements.txt
# docker cp src/py_scripts/script.py trino-nlp-embeddings:/data/trino/src/py_scripts/script.py
# .\Scripts\python .\script.py