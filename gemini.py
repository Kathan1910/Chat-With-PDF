############################## Method 1 ########################## Q&A Working

# from dotenv import load_dotenv
# load_dotenv() ## loading all the environment variables

# import streamlit as st
# import os
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ## function to load Gemini Pro model and get repsonses
# model=genai.GenerativeModel("gemini-pro") 
# chat = model.start_chat(history=[])
# def get_gemini_response(question):
    
#     response=chat.send_message(question,stream=True)
#     return response

# ##initialize our streamlit app

# st.set_page_config(page_title="Q&A Demo")

# st.header("Gemini LLM Application")

# # Initialize session state for chat history if it doesn't exist
# if 'chat_history' not in st.session_state:
#     st.session_state['chat_history'] = []

# input=st.text_input("Input: ",key="input")
# submit=st.button("Ask the question")

# if submit and input:
#     response=get_gemini_response(input)
#     # Add user query and response to session state chat history
#     st.session_state['chat_history'].append(("You", input))
#     st.subheader("The Response is")
#     for chunk in response:
#         st.write(chunk.text)
#         st.session_state['chat_history'].append(("Bot", chunk.text))
# st.subheader("The Chat History is")
    
# for role, text in st.session_state['chat_history']:
#     st.write(f"{role}: {text}")
    

################################ Method 2 ########################### For Courses recommendation

# from dotenv import load_dotenv

# load_dotenv()  # take environment variables from .env.

# import streamlit as st
# import os
# import pathlib
# import textwrap

# import google.generativeai as genai

# from IPython.display import display
# from IPython.display import Markdown


# def to_markdown(text):
#   text = text.replace('•', '  *')
#   return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ## Function to load OpenAI model and get respones

# def get_gemini_response(question):
#     model = genai.GenerativeModel('gemini-pro')
#     response = model.generate_content(question)
#     return response.text

# ##initialize our streamlit app

# st.set_page_config(page_title="Q&A Demo")

# st.header("Gemini Application")

# input=st.text_input("Input: ",key="input")


# submit=st.button("Ask the question")

# ## If ask button is clicked

# if submit:
    
#     response=get_gemini_response(input)
#     st.subheader("The Response is")
#     st.write(response)

######################################### Method 3 ######################################## Q & A Bot

# Q&A Chatbot
#from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
def get_gemini_response(question):
    
    response =chat.send_message(question,stream=True)
    return response

##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Application")

input=st.text_input("Input: ",key="input")


submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    for chunk in response:
        print(st.write(chunk.text))
        print("_"*80)
    
    st.write(chat.history)