import streamlit as st
import requests
import os
import dotenv
from dotenv import load_dotenv

load_dotenv()

os.environ["langchain_api_key"] =os.getenv("langchain_api_key")
os.environ["langchain_tracing_v2"] = "true"

def get_genai_response(input_text):
    response = requests.post("http://localhost:8101/essay/invoke",
                             json={'input':{'topic': input_text}})
    return response.json()['output']['content']
    
def get_ollama_response(input_text):
    response = requests.post("http://localhost:8101/poem/invoke",
                             json={'input':{'topic': input_text1}})
    return response.json()['output']
    
## streamlit framework 

st.title('Langchain Demo With GeminiGenAI and LLAMA3.2 API chains')
input_text = st.text_input("Write an essay on ")
input_text1 = st.text_input("Write a poem on ")

if input_text:
    st.write(get_genai_response(input_text))
    
if input_text1:
    st.write(get_ollama_response(input_text))


