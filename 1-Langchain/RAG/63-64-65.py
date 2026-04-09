import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st #  Run - streamlit run 63.py

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

## PROMPT TEMPLATE
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. please respond to questions asked by the user."),
        ("user", "Question: {question}"),
    ]
)

## Streamlit Framework
st.title("Langchain Demo With LLAMA3")
input_text = st.text_input("Enter your question here ? : ")

## Ollama Llama3 model
llm = Ollama(model="llama3")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))