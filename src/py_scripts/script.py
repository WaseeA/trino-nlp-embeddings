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

def sentence_to_embeddings(query):
    # unpack the models
    print(query)

if __name__ == "__main__":
    # The query is passed as the second argument
    if len(sys.argv) < 2:
        print("Error: Query argument is missing")
    else:
        query = sys.argv[1]
        sentence_to_embeddings(query)
        

# models: https://huggingface.co/models?sort=downloads

# SELECT run_py('/data/trino/src/py_scripts/script.py') AS result;
# SELECT square(4);