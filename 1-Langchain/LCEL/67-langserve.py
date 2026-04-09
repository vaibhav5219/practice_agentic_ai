from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes
from dotenv import load_dotenv

load_dotenv("../../.env")

groq_api_key = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="llama-3.1-8b-instant", api_key=groq_api_key)

# 1. Create a prompt template
system_template = "Translate the following into {language} language."
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("human", "{text}"),
])

# 2. Create chain
parser=StrOutputParser()
chain = prompt_template | model | parser

# 3. App definition
app = FastAPI(title="Langchain Server", 
              description="A simple api server to demonstrate Langchain and Langserve integration", 
              version="1.0.0")

# 4. Add chain route
add_routes(
    app,
    chain,
    path="/chain"
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)