import openai
openai.api_key = "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"


# response = openai.Embedding.create(
#     input="Your text string goes here",
#     model="text-embedding-ada-002"
# )
# embeddings = response['data'][0]['embedding']
# print(response)

# imports
import pandas as pd
import tiktoken

from openai.embeddings_utils import get_embedding

embedding_model = "text-embedding-ada-002"
embedding_encoding = "cl100k_base"  # this the encoding for text-embedding-ada-002
max_tokens = 8000  # the maximum for text-embedding-ada-002 is 8191