import streamlit as st

# Show all previous messages in the chat area
def display_chat_history():
    # If this is the first run, make sure there's a place to store messages
    if "messages" not in st.session_state:
        st.session_state.messages = []
    # Loop through each saved message and display it in the right style
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).markdown(msg["content"])

# Take user input, send it to the LLM chain, and show the reply
def handle_user_input(chain):
    # Show an input box for the user to type a prompt
    user_input = st.chat_input("Pass your prompt here")
    if not user_input:
        return  # If they didn’t type anything, stop here

    # Display the user's message immediately
    st.chat_message("user").markdown(user_input)
    # Save the user message to the session so it shows up next time too
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        # Send the prompt to the LLM chain and get the answer
        result = chain({"query": user_input})
        response = result["result"]
        # Show the assistant’s reply
        st.chat_message("assistant").markdown(response)
        # Save the assistant’s reply to the chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    except Exception as e:
        # If anything goes wrong, show an error message on the page
        st.error(f"Error: {str(e)}")

# Let the user download the whole conversation as a text file
def download_chat_history():
    if st.session_state.get("messages"):
        # Format messages nicely with USER/ASSISTANT labels
        content = "\n\n".join([f"{m['role'].upper()}: {m['content']}" for m in st.session_state.messages])
        # Show a download button to save the chat to a .txt file
        st.download_button("💾 Download Chat History", content, file_name="chat_history.txt", mime="text/plain")
