<div align="center">

![RAG Bot Banner](images/img1.jpg)

# 🚀 GROQ RAG ChatBot

**Chat with your PDFs — Blazing Fast with Groq**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io/)
[![Groq](https://img.shields.io/badge/Groq-00FF9F?style=for-the-badge&logo=groq)](https://groq.com/)
[![Chroma](https://img.shields.io/badge/ChromaDB-FF6B6B?style=for-the-badge)](https://www.trychroma.com/)

</div>

---

### ✨ Live Demo

![App UI](images/img2.jpg)

![Chat Experience](images/img4.jpg)

![Features Highlight](images/img5.jpg)

---

## 📋 What It Does

This is a **Retrieval-Augmented Generation (RAG)** chatbot that lets you upload PDF documents and have intelligent conversations with them.

**Powered by**:

- **Groq** → Ultra-fast LLM inference
- **Hugging Face Embeddings**
- **ChromaDB** → Vector database
- **Streamlit** → Beautiful UI

---

## 🛠️ Architecture

![RAG Architecture](images/img3.jpg)

---

## 🚀 Features

- ✅ Upload one or multiple PDFs
- ✅ Smart chunking & embedding
- ✅ Fast responses powered by Groq
- ✅ Source citations with document references
- ✅ Chat history download
- ✅ Vector database inspector
- ✅ Clean, responsive dark UI

---

## 📂 Project Structure

```bash
rag-bot/
├── index.py                 # Main Streamlit app
├── requirements.txt         # Dependencies
├── .env.example             # Environment variables template
├── images/                  # README images
│
└── modules/
    ├── pdf_handler.py       # PDF upload & processing
    ├── vectorstore.py       # ChromaDB operations
    ├── llm.py               # Groq LLM + Retrieval chain
    ├── chat.py              # Chat logic & history
    └── chroma_inspector.py  # DB inspection tool
```

⚙️ Getting Started
1️⃣ Clone the Repository

git clone https://github.com/ojasss11/rag-bot.git
cd rag-bot

2️⃣ Create Virtual Environment
python -m venv venv

# Windows

venv\Scripts\activate

# macOS / Linux

source venv/bin/activate

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Setup Environment Variables
Copy .env.example to .env and add your keys:

GROQ_API_KEY=your_groq_api_key_here
HUGGINGFACEHUB_API_TOKEN=your_hf_token_here

5️⃣ Run the App

streamlit run index.py

🗝️ Important Notes

Never commit your .env file
To reset the vector database → delete the chroma_store folder
Works best with Groq's Llama3-70b or Mixtral models

## 👨‍💻 About the Author

**Ojas Bidkar**

🚀 Full-Stack Developer | **Generative AI Engineer** | Next.js & React Native Developer | 3D Web Developer

Building modern, scalable, and intelligent digital experiences across web, mobile, 3D platforms, and **Generative AI** applications.

**Skills & Expertise:**

- 💻 Full-Stack Development: Next.js, React, TypeScript, Node.js
- 🤖 Generative AI & RAG: LLM Applications, Groq, LangChain, Vector Databases
- 📱 App Development: React Native
- 🌐 3D Web Development: Three.js, React Three Fiber
- ⚡ Frontend Engineering: Responsive UI, Performance Optimization
- 🛠️ Backend & APIs: REST APIs, Database Integration

**Connect with me:**

- **GitHub**: [ojasss11](https://github.com/ojasss11)
- **LinkedIn**: [Ojas Bidkar](https://www.linkedin.com/in/ojas-bidkar-17ba8927b/)
