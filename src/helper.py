from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import LlamaCppEmbeddings


# Extract data from PDF
def load_pdf(data):
    loader = DirectoryLoader(data, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()

    return documents


# Create text chunks
def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=20)
    text_chunks = text_splitter.split_documents(extracted_data)

    return text_chunks


model_path = "C:\\Users\\User\\.cache\\huggingface\\hub\\models--second-state--All-MiniLM-L6-v2-Embedding-GGUF\\snapshots\\544f204f2eaa2d71361ffc74d6df7170285b286a\\all-MiniLM-L6-v2.F32.gguf"


# Loading the Embedding model
def embeddings():
    embeddings_model = LlamaCppEmbeddings(
        model_path=model_path,
        n_gpu_layers=10)

    return embeddings_model
