import streamlit as st
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
import os

# Function to process PDF and answer queries using OpenAI
def process_pdf_and_answer_query_openai(pdf_file, query):
    # Read the PDF
    pdfreader = PdfReader(pdf_file)

    # Extract text from PDF
    raw_text = ''
    for page in pdfreader.pages:
        content = page.extract_text()
        if content:
            raw_text += content

    # Split the text
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=800,
        chunk_overlap=200,
        length_function=len,
    )
    texts = text_splitter.split_text(raw_text)

    # Load embeddings and document search
    embeddings = OpenAIEmbeddings()
    document_search = FAISS.from_texts(texts, embeddings)

    # Load QA chain
    chain = load_qa_chain(OpenAI(), chain_type="stuff")

    # Perform document search and run the chain
    docs = document_search.similarity_search(query)
    response = chain.run(input_documents=docs, question=query)
    return response

def main():
    st.title("PDF Chat Application with OpenAI")

    # File uploader
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    # Chat interface
    user_query = st.text_input("Enter your query")
    if st.button("Ask"):
        if uploaded_file is not None and user_query:
            # Process the PDF and get the response
            response = process_pdf_and_answer_query_openai(uploaded_file, user_query)

            # Display the response
            st.write(response)
        else:
            st.warning("Please upload a PDF file and enter a query.")

if __name__ == "__main__":
    os.environ["OPENAI_API_KEY"] = "Enter Your API Key Here"  
