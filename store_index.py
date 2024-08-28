from src.helper import load_pdf, text_split, embeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

extracted_data = load_pdf('data/')
text_chunks = text_split(extracted_data)
embeddings = embeddings()

# Initialize the Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index("myindex")

vector_store = PineconeVectorStore(index=index, embedding=embeddings)

