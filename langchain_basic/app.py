# environment variables
# langchain_api_key  = "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"
# GOOGLE_API_KEY = "AIzaSyBzGHUo_yeZ4babsuo3K6sE4Z7aq-qJju0"
# langchain_project = "Chatbot using Langchain1"

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


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

## Gemini LLM call

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
output_parser=StrOutputParser()

## chain
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))