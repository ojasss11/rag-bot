import warnings
import logging
import streamlit as st

# Local modules
from modules.chat import display_chat_history, handle_user_input, download_chat_history
from modules.pdf_handler import upload_pdfs
from modules.vectorstore import load_vectorstore
from modules.llm import get_llm_chain
from modules.chroma_inspector import inspect_chroma

# Ignore all Python warnings to keep the console clean
warnings.filterwarnings("ignore")
# Silence transformer model logs to avoid clutter in the output
logging.getLogger("transformers").setLevel(logging.ERROR)

# Configure Streamlit page settings
st.set_page_config(
    page_title="RagBot!",  # Sets the browser tab title
)

# Display the app title on the web page
st.title("Ragbot Task")

# Step 1: Allow user to upload PDF files and submit them
uploaded_files, submitted = upload_pdfs()

# Step 2: If the user submitted and uploaded files, create the vectorstore
if submitted and uploaded_files:
    with st.spinner(" Updating vector database..."):
        # Convert uploaded PDFs into a vector database for searching
        vectorstore = load_vectorstore(uploaded_files)
        # Store the vectorstore in Streamlit session state for reuse
        st.session_state.vectorstore = vectorstore

# Step 3: If vectorstore exists, show vectorstore details in the sidebar
if "vectorstore" in st.session_state:
    inspect_chroma(st.session_state.vectorstore)

# Step 4: Display previous chat messages on the main page
display_chat_history()

# Step 5: If vectorstore exists, process new user questions with the LLM
if "vectorstore" in st.session_state:
    handle_user_input(get_llm_chain(st.session_state.vectorstore))

# Step 6: Add option to download the chat history
download_chat_history()
