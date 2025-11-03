# parsing done with docling
# chunking done with llamaindex import json


from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import SimpleDirectoryReader
from llama_index.embeddings.openai import OpenAIEmbedding


# Load the lion.md file
lionMD= SimpleDirectoryReader(input_files=["lion.md"]).load_data()

# measure by tokens
splitter = SentenceSplitter(
    chunk_size=400,
    chunk_overlap=20,
)
nodes = splitter.get_nodes_from_documents(lionMD)

# embedding 
embed_model = OpenAIEmbedding(model="text-embedding-3-small")
