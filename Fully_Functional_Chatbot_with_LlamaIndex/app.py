import streamlit as st


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
    
    


if __name__ == "_main_":
    main()