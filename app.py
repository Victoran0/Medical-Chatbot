from flask import Flask, render_template, jsonify, request
from src.helper import embeddings
from src.prompt import *
from pinecone import Pinecone, ServerlessSpec
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
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
                        input_variables=['context', 'input'])

llm_path = "C:\\Users\\User\\.cache\\huggingface\\hub\\models--QuantFactory--Meta-Llama-3.1-8B-GGUF\\snapshots\\d0a93b5ad9c03e2e0f43b0814a36892638bfc856\\Meta-Llama-3.1-8B.Q4_1.gguf"

llm = LlamaCpp(
    model_path=llm_path,
    n_gpu_layers=25
)

combine_docs_chain = create_stuff_documents_chain(llm, PROMPT)

retriever = vector_store.as_retriever(
    search_type="similarity_score_threshold", search_kwargs={'k': 2, "score_threshold": 0.5})

rag_chain = create_retrieval_chain(retriever, combine_docs_chain)


@app.route('/')
def index():
    return render_template('chat.html')


@app.route('/get', methods=['GET', 'POST'])
def chat():
    msg = request.form['msg']
    input = msg
    print(input)
    result = rag_chain.invoke({'input': input})
    print(f"Response: {result['answer']}")
    return str(result['answer'])


if __name__ == '__main__':
    app.run(debug=True)
