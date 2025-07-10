from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes
import uvicorn
import os
# from langchain_community.llms import ollama
from langchain_ollama import OllamaLLM
from dotenv import load_dotenv

from fastapi.openapi.utils import get_openapi


load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")



app = FastAPI(
    title  = 'Langchain Server',
    version = '1.0',
    description = 'A simple API server'
       
)


add_routes(
    app,
    ChatGoogleGenerativeAI(model = "gemini-1.5-flash"),
    path = "/chat_api",
    # include_schema=False
    
)

model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash")
## ollama llm model 
llm = OllamaLLM(model= "llama3.2")

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words.")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} for a 5 year old ")

from langchain_core.runnables import Runnable

chain1 = prompt1 | model
print("Chain1 type:", type(chain1))
print("Is chain1 a Runnable?", isinstance(chain1, Runnable))

chain2 = prompt2 | llm
print("Chain2 type:", type(chain2))
print("Is chain2 a Runnable?", isinstance(chain2, Runnable))

add_routes(
    app, 
    prompt1|model, 
    path = "/essay",
    # include_schema=False
    
)

add_routes(
    app, 
    prompt2|llm, 
    path = "/poem",
    # include_schema=False
)


if __name__ == "__main__":
    uvicorn.run(app, host = "localhost", port= 8101)
    
