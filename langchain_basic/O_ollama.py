from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain_community.llms import Ollama                              (old/deprecated version)
from langchain_ollama import OllamaLLM

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

## environment variables call

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

## LANGSMITH tracking
os.environ["langchain_api_key"] =os.getenv("langchain_api_key")
os.environ["langchain_tracing_v2"] = "true"

## creating chatbot 

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Kindly provide response to the user queries."),
        ("user", "Question:{question}")
    ]
)

## streamlit framework

st.title("Langchain Demo With Gemini api")
input_text = st.text_input("Search the topic you want")

method = st.selectbox("Select Model", options= ["Gemini", "Ollama"])

## Gemini/Ollama LLM call

if method== "Gemini":
# llm = Ollama(model="llama3.2")                               (deprecated cmd)
    llm = ChatGoogleGenerativeAI(model = "gemini-1.5-flash")

elif method=="Ollama":
    llm = OllamaLLM(model = "llama3.2")
    
output_parser=StrOutputParser()

## chain
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))