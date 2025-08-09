from dotenv import load_dotenv
import os
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
#model
model = ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key)

#prompt
prompt = ChatPromptTemplate.from_messages([
  ("system","You are a helpful translator. Keep punctuation and tone."),
  ("user","Translate the follwong into {language}:\n\n{text}")
])

#parser
parser = StrOutputParser()

#chain LCEL
chain = prompt | model | parser

#Streamlit UI
st.title("🌍 LCEL Language Translator (Groq)")
#Input text
text = st.text_area("Enter the text to translate",height=150)

#lang selection
language = st.text_input("Enter target language")

if st.button("Translate"):
  if not text.strip():
    st.warning("Please enter some text to translate.")
  elif not language.strip():
    st.warning("Please enter a target language.")
  else:
    with st.spinner("translating..."):
      result = chain.invoke({"language":language,"text":text})
    st.subheader("Translation")
    st.write(result)

