import streamlit as st
import tempfile

# Show a sidebar uploader for PDF files and a submit button
def upload_pdfs():
    with st.sidebar:
        st.header("📁 Upload PDFs")
        # Allow users to select one or more PDF files
        uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)
        # Button to confirm upload and start processing
        submit = st.button(" Submit to DB")
    return uploaded_files, submit

# Save the uploaded PDF files to temporary files on disk
def save_uploaded_files(uploaded_files):
    file_paths = []
    for file in uploaded_files:
        # Create a temp file with a .pdf extension
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            # Write the uploaded file’s content to the temp file
            tmp.write(file.read())
            # Save the temp file path for later use
            file_paths.append(tmp.name)
    return file_paths
