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
import psycopg2
from transformers import BertTokenizer, BertModel
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine

# Define database connection parameters
DB_CONFIG = {
    "host": "some-postgres", # same name as your docker container running your postgres instance
    "port": "5432",
    "database": "postgres",
    "user": "postgres",
    "password": "password",
}

MODEL = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

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
            cursor.execute("SELECT * from pdf_embeddings;")
            rows = cursor.fetchall()
            return rows
    except Exception as e:
        print(f"Error fetching embeddings: {e}")
        return []

def find_most_similar_entry(to_find, embeddings_list):
    most_similar = None
    highest_similarity_so_far = -1

    for entry in embeddings_list:
        vector = entry[3]
        
        print(sentence_to_embeddings(MODEL, entry[1]))
        
        # similarity = 1 - cosine(embedding_to_find, vector)
        # if similarity > highest_similarity_so_far:
        #     highest_similarity_so_far = similarity
        #     most_similar = entry
    
    return most_similar

# Function to insert embeddings into the database
def insert_embedding_into_db(connection, id, vector, text, page_number):
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO pdf_embeddings (id, vector, text, page_number) VALUES (%s, %s, %s, %s)",
                (id, vector, text, page_number)
            )
        connection.commit()
    except Exception as e:
        print(f"Error inserting embeddings: {e}")

def insert_sample_data():
    connection = connect_db()
    if (connection):
        given_embeddings = fetch_embeddings_from_db(connection)
        print(given_embeddings)

        sample_data = [
            {"id": "1", "text": "Hello the weather is lovely today.", "page_number": 1},
            {"id": "2", "text": "Deep learning and neural networks is important.", "page_number": 2},
            {"id": "3", "text": "The healthcare system could use some work.", "page_number": 3},
        ]

        for data in sample_data:
            # Generate embeddings for each text
            embedding = model.encode(data["text"]).tolist()  # Convert to Python list
            insert_embedding_into_db(
                connection,
                data["id"],
                embedding,
                data["text"],
                data["page_number"],
            )
        connection.close()

if __name__ == "__main__":
    # The query is passed as the second argument
    if len(sys.argv) < 2:
        print("Usage: python script.py \"<query string>\"")
    else:
        query = sys.argv[1]
        embedding_to_find = sentence_to_embeddings(MODEL, query)
        connection = connect_db()
        if (connection):
            given_embeddings = fetch_embeddings_from_db(connection)
            print(given_embeddings)
            
