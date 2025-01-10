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

# USAGE: .\Scripts\python .\script.py "lovely weather I must say"

import sys
import psycopg2
import numpy as np
import json
from pprint import pprint
from transformers import BertTokenizer, BertModel
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine
from typing import List, Optional, Dict, Any

# Database connection config
DB_CONFIG = {
    "host": "localhost",
    "port": "5432",
    "database": "postgres",
    "user": "postgres",
    "password": "password",
}

# Preload the SentenceTransformer model
MODEL = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

def connect_db() -> Optional[psycopg2.extensions.connection]:
    """Establish a connection to the database."""
    try:
        connection = psycopg2.connect(**DB_CONFIG)
        return connection
    except Exception as e:
        print(f"Connection Failed: {e}")
        return None

def generate_embedding(model: SentenceTransformer, text: str) -> List[float]:
    """Generate sentence embeddings using the preloaded model."""
    return model.encode(query)

def fetch_all_embeddings(connection: psycopg2.extensions.connection) -> List[tuple]:
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * from pdf_embeddings;")
            rows = cursor.fetchall()
            return rows
    except Exception as e:
        print(f"Error fetching embeddings: {e}")
        return []

def insert_embedding_into_db(connection: psycopg2.extensions.connection, entry_id: str, vector: List[float], text: str, page_number: int) -> None:
    """Insert a single embedding into the database."""
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO pdf_embeddings (id, vector, text, page_number) VALUES (%s, %s, %s, %s)",
                (entry_id, vector, text, page_number)
            )
        connection.commit()
    except Exception as e:
        print(f"Error inserting embeddings: {e}")

def find_most_similar_entry(query_embedding: List[float], embeddings: List[tuple]) -> Optional[Dict[str, Any]]:
    """Find the most similar entry in the database to the given query embedding."""
    most_similar = None
    highest_similarity_so_far = -1

    for entry in given_embeddings:
        entry_id, vector, text, page_number = entry
        vector_list = json.loads(vector)
        similarity = 1 - cosine(query_embedding, vector_list)
        
        if similarity > highest_similarity_so_far:
            highest_similarity_so_far = similarity
            most_similar = {
                "id": entry_id,
                "text": text,
                "page_number": page_number,
                "similarity": similarity,
            }
    
    return most_similar

def insert_sample_data() -> None:
    """Insert sample embeddings into the database for testing."""
    connection = connect_to_db()
    if connection:
        sample_data = [
            {"id": "1", "text": "Hello the weather is lovely today.", "page_number": 1},
            {"id": "2", "text": "Deep learning and neural networks is important.", "page_number": 2},
            {"id": "3", "text": "The healthcare system could use some work.", "page_number": 3},
        ]
        # Generate embeddings for each text
        for data in sample_data:
            embedding = MODEL.encode(data["text"]).tolist()  # Convert to Python list
            insert_embedding_into_db(
                connection,
                data["id"],
                embedding,
                data["text"],
                data["page_number"],
            )
        connection.close()
    return None

if __name__ == "__main__":
    # The query is passed as the second argument
    if len(sys.argv) < 2:
        print("Usage: python script.py \"<query string>\"")
    else:
        query = sys.argv[1]
        embedding_to_find = generate_embedding(MODEL, query)
        connection = connect_db()
        if (connection):
            given_embeddings = fetch_all_embeddings(connection)
            print(find_most_similar_entry(embedding_to_find, given_embeddings))
            