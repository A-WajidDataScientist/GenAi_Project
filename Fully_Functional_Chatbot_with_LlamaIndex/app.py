import openai
import streamlit as st
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI
from llama_index.core.settings import Settings

# Set OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Sidebar for the app description
with st.sidebar:
    st.title("Chat with your data")
    st.markdown("""
                ## About
                This app is an LLM-powered chatbot built using:
                - [Streamlit](https://streamlit.io/)
                - [Llama Index](https://gpt-index.readthedocs.io/)
                - [OpenAI](https://platform.openai.com/docs/models)

                The app utilizes a powerful LLM model to chat with your data and provide insights.
                """)

def main(): 
    st.header("Chat with your data")
    
    # Read the documents
    reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
    docs = reader.load_data()
    
    # Set up the OpenAI LLM
    llm = OpenAI(model='gpt-3.5-turbo', temperature=0.5)
    
    # Create vector index without explicit settings
    index = VectorStoreIndex.from_documents(docs)
    
    # Take user input
    query = st.text_input("Ask me something related to your data")
    if query:
        chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)
        response = chat_engine.chat(query)
        st.write(response.response)

if __name__ == "__main__":
    main()