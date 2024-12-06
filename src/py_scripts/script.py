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
from transformers import BertTokenizer, BertModel
from sentence_transformers import SentenceTransformer

def sentence_to_embeddings(query):
    # unpack the models
    model = SentenceTransformer("multi-qa-mpnet-base-cos-v1")
    query_embedding = model.encode("How big is London")
    print(query_embedding)
    
    # passage_embeddings = model.encode([
    #     "London is known for its financial district",
    #     "London has 9,787,426 inhabitants at the 2011 census",
    #     "The United Kingdom is the fourth largest exporter of goods in the world",
    # ])

    # similarity = model.similarity(query_embedding, passage_embeddings)
    # print(similarity)
    

if __name__ == "__main__":
    # The query is passed as the second argument
    if len(sys.argv) < 2:
        print("Usage: python script.py <arg1>")
    else:
        query = sys.argv[1]
        sentence_to_embeddings(query)
        

# models: https://huggingface.co/models?sort=downloads

# SELECT run_py('/data/trino/src/py_scripts/script.py') AS result;
# SELECT square(4);
# docker exec -it trino-nlp-embeddings bash
# docker cp src/py_scripts/requirements.txt trino-nlp-embeddings:/data/trino/src/py_scripts/requirements.txt
# docker cp src/py_scripts/script.py trino-nlp-embeddings:/data/trino/src/py_scripts/script.py