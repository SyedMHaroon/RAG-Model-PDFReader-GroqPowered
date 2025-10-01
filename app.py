from dotenv import load_dotenv
import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_groq import ChatGroq


def main():
    load_dotenv()
    st.set_page_config(page_title="Ask your PDF")
    st.header("Ask your PDF🙋🏻‍♂️")

    #uploading the pdf
    pdf = st.file_uploader("Upload your PDF",type="pdf")
    
    #extracting text from pdf
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text +=page.extract_text()

        #splitting into chunks
        text_splitter = CharacterTextSplitter(
            separator="\n", 
            chunk_size = 1000,
            chunk_overlap = 200,
            length_function = len

        )
        chunks = text_splitter.split_text(text)
        
        #Create Embeddings
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        knowledgeBase = FAISS.from_texts(chunks, embeddings)
        
        userQuestions = st.text_input("Ask a question about your PDF")
        if userQuestions:
            docs = knowledgeBase.similarity_search(userQuestions)
            llm = ChatGroq(
                    model="llama-3.1-8b-instant",      # <- required
                    groq_api_key = os.environ.get("GROQ_API_KEY")
                )
            chain = load_qa_chain(llm, chain_type="stuff")
            response = chain.run(input_documents=docs, question=userQuestions)
            

            st.write(response)



if __name__ == '__main__':
    main()