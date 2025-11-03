
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import SimpleDirectoryReader
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.ingestion import IngestionPipeline
from llama_index.vector_stores.pinecone import PineconeVectorStore
from llama_index.core import VectorStoreIndex
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Load the lion.md file
lionMD = SimpleDirectoryReader(input_files=["lion/lion.md"]).load_data()

# Initialize connection to Pinecone
pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])

# Get or create index (text-embedding-3-small has 1536 dimensions)
index_name = "lion"

# Create your index (can skip this step if your index already exists)
try:
    pc.create_index(
        index_name,
        dimension=1536,  # text-embedding-3-small dimension
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
except Exception:
    # Index already exists, continue
    pass

# Initialize your index
pinecone_index = pc.Index(index_name)

# Initialize VectorStore
vector_store = PineconeVectorStore(pinecone_index=pinecone_index)

# Create embedding model
embed_model = OpenAIEmbedding(model="text-embedding-3-small")

# Create ingestion pipeline with transformations
pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(chunk_size=400, chunk_overlap=20),  # measure by tokens
        embed_model,
    ],
    vector_store=vector_store,
)

# Ingest directly into vector db
pipeline.run(documents=lionMD)

# Create your index from the vector store
index = VectorStoreIndex.from_vector_store(vector_store)


# Query the index and print the response
query_engine = index.as_query_engine()
response = query_engine.query("What are lions?")
print(response)

# Lions are large carnivorous mammals known for their distinctive manes, with males typically having fuller and darker manes compared to females.
#  They are social animals that live in groups called prides and are known for their hunting prowess.
#  Lions are facing threats such as habitat loss, conflicts with humans, and over-harvesting, leading to conservation concerns about their future survival.