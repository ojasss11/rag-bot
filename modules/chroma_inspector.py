import streamlit as st
from langchain.vectorstores import Chroma

# Simple sidebar tool to peek inside the Chroma vector store
def inspect_chroma(vectorstore):
    # Sidebar section header
    st.sidebar.markdown("🧪 **ChromaDB Inspector**")
    
    # Try to show how many documents are in the collection
    try:
        doc_count = vectorstore._collection.count()
        st.sidebar.success(f"🔎 {doc_count} documents stored in ChromaDB.")
    except Exception as e:
        st.sidebar.error("Could not fetch document count.")
        st.sidebar.code(str(e))

    # Add a text box for quick test queries against the vector DB
    query = st.sidebar.text_input("🔍 Test a query against ChromaDB")

    if query:
        try:
            # Run a similarity search and show the top 3 chunks
            results = vectorstore.similarity_search(query, k=3)
            st.sidebar.markdown("### Top Matching Chunks:")
            for i, doc in enumerate(results):
                st.sidebar.markdown(f"**Result {i+1}:**")
                # Show only the first 300 characters to keep it readable
                st.sidebar.markdown(doc.page_content[:300] + "...")
                st.sidebar.markdown("---")
        except Exception as e:
            st.sidebar.error("Error querying ChromaDB")
            st.sidebar.code(str(e))
