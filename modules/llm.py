import os
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

# Load environment variables from .env file (like your GROQ_API_KEY)
load_dotenv()

# Create and return the LLM + retriever chain
def get_llm_chain(vectorstore):
    # Initialize the LLM using the Groq backend with your API key
    llm = ChatGroq(
        groq_api_key=os.environ.get("GROQ_API_KEY"),
        model_name="llama3-8b-8192"  # Specific model to use
    )
    # Convert the vector store into a retriever (fetch top 3 matches)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    # Wrap LLM + retriever into a single RetrievalQA chain
    return RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True  # Also return source docs for reference
    )
