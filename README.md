📚 GROQ RAG ChatBot — Chat With Your PDFs
This project is a Retrieval-Augmented Generation (RAG) chatbot that lets you upload PDF files and chat with their contents.
It uses GROQ LLM, Hugging Face embeddings, and a Chroma vector database under the hood — all wrapped in a simple Streamlit app.

🚀 What It Does
✅ Upload one or more PDFs
✅ Break documents into chunks and store them as embeddings in ChromaDB
✅ Ask questions — answers are pulled from your PDFs using GROQ’s LLM
✅ Inspect what’s stored in the vector DB
✅ Download your chat history

📂 Project Structure

groq_rag_chatbot/
│
├── index.py # Main Streamlit app
├── requirements.txt # Project dependencies
├── .env.example # Example environment variables
│
├── modules/ # Modular app logic
│ ├── pdf_handler.py # Handles PDF uploads and saving
│ ├── vectorstore.py # Loads/splits/embeds PDFs into Chroma
│ ├── llm.py # Sets up GROQ LLM + RetrievalQA chain
│ ├── chat.py # Chat input/output and chat history
│ ├── chroma_inspector.py # Sidebar tool to inspect vector DB

⚙️ Getting Started
Follow these steps to get your local chatbot running.

1️⃣ Clone the Repository

2️⃣ Create a Virtual Environment
python -m venv venv

Activate the environment:

On Windows:
venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

3️⃣ Install Python Dependencies
pip install -r requirements.txt

4️⃣ Set Up Your Environment Variables
Create a .env file in the project root (you can copy .env.example):

GROQ_API_KEY="YOUR_GROQ_API_KEY"
HUGGINGFACEHUB_API_TOKEN="YOUR_HUGGINGFACEHUB_API_TOKEN"
OPENAI_API_KEY="YOUR_OPENAI_API_KEY"

▶️ Run the ChatBot
Launch the Streamlit app:

streamlit run index.py

🗝️ Notes
Keep your .env secrets private — don’t commit them to Git!

If you want to reset the DB, just delete the ./chroma_store folder.
