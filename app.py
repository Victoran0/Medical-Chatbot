from flask import Flask, render_template, jsonify, request
from src.helper import embeddings
from src.prompt import *
from pinecone import Pinecone, ServerlessSpec
from langchain.chains import RetrievalQA
from langchain_pinecone import PineconeVectorStore
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os
from langchain_community.llms import LlamaCpp


app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

embeddings = embeddings()

# Initialize the Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index("myindex")

vector_store = PineconeVectorStore(index=index, embedding=embeddings)

PROMPT = PromptTemplate(template=prompt_template,
                        input_variables=['context', 'question'])
chain_type_kwargs = {"prompt": PROMPT}

llm_path = "C:\\Users\\User\\.cache\\huggingface\\hub\\models--QuantFactory--Meta-Llama-3.1-8B-GGUF\\snapshots\\d0a93b5ad9c03e2e0f43b0814a36892638bfc856\\Meta-Llama-3.1-8B.Q4_1.gguf"

llm = LlamaCpp(
    model_path=llm_path,
    n_gpu_layers=33
)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',
    retriever=vector_store.as_retriever(
        search_type="similarity_score_threshold", search_kwargs={'k': 2, "score_threshold": 0.5}),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs
)


@app.route('/')
def index():
    return render_template('chat.html')


if __name__ == '__main__':
    app.run(debug=True)
