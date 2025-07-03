from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from modules.pdf_handler import save_uploaded_files
import os
from dotenv import load_dotenv

# Load any environment variables from .env
load_dotenv()

# Local folder where Chroma will store the vector DB
PERSIST_DIR = "./chroma_store"

# Convert uploaded PDFs into a Chroma vector store
def load_vectorstore(uploaded_files):
    # Save uploaded PDF files to temp files and get their paths
    paths = save_uploaded_files(uploaded_files)

    docs = []
    # Load each PDF and extract its pages as documents
    for path in paths:
        loader = PyPDFLoader(path)
        docs.extend(loader.load())

    # Split large documents into smaller chunks for better embeddings
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts = splitter.split_documents(docs)

    # Use a small open-source sentence transformer for embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # If the Chroma DB folder already exists, add new docs to it
    if os.path.exists(PERSIST_DIR) and os.listdir(PERSIST_DIR):
        vectorstore = Chroma(persist_directory=PERSIST_DIR, embedding_function=embeddings)
        vectorstore.add_documents(texts)
        vectorstore.persist()
    else:
        # If it doesn’t exist yet, create it from scratch
        vectorstore = Chroma.from_documents(
            documents=texts,
            embedding=embeddings,
            persist_directory=PERSIST_DIR
        )
        vectorstore.persist()

    return vectorstore
