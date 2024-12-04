from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
from google.cloud import vision
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

#initialize iur streamlit app

st.set_page_config(page_title="Q&A demo")
st.header("Gemini Llm Application")
input=st.text_input("Input: ",key="input")
submit=st.button("Ask The Question")


# Submit button
if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is:")
    st.write(response)
