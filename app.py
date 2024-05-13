import os   
import streamlit as st
import pickle   
import google.generativeai as genai    
 
from streamlit_extras.add_vertical_space import add_vertical_space 
from PyPDF2 import PdfReader      
from langchain.text_splitter import RecursiveCharacterTextSplitter    
from langchain.embeddings.openai import OpenAIEmbeddings  
from langchain.vectorstores import FAISS        
  
with st.title('💖 LLM Chat BOt By RVC'):     
    st.markdown('''  
    ## About   
    THe app is an LLM-powered chatbot built using 
    ''')  
  
    

    add_vertical_space(5)   
    st.write("Made by RVC from 💝")  
   

def main():
    st.header("ChatBot PDF by Rohan 💬🤖")  
    pdf=st.file_uploader('Upload Your PDF',type='pdf')
    if pdf is not None:  
        pdf_reader=PdfReader(pdf)  
        st.write(pdf.name)
        # st.write(pdf_reader) 
        text=''
        for page in pdf_reader.pages:
            text+=page.extract_text()
        
        text_splitter=RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=200,
            length_function=len
        )

        chunks=text_splitter.split_text(text=text)

        # embeddings=OpenAIEmbeddings()
        # VectorStore=FAISS.fron_texts(chunks,embeddings=embeddings)
        # store_name=pdf.name[:-4]
        # if os.path.exists(f'{store_name}.pkl'):
        #     with open(f'{store_name}.pkl','rb') as f:
        #         pickle.load(f)
            
        # else:
        #     with open(f'{store_name}.pkl','wb') as f:
        #         pickle.dump(f

        genai.configure(api_key=st.secrets['api_key'])


        model = genai.GenerativeModel('gemini-pro')
        chat=model.start_chat(history=[])


            # print('AI-: ',response.text)
        st.write("Ask questions related to your PDF file-:")
        query=st.text_input("")
        # st.write(query)
        
        if query!='':
            response = chat.send_message(f'{query} Answer in one or few lines from this given text below \n {text}')
            st.write(response.text)
        elif query=='':
            st.write("Please write something in input box")
        # st.write(text)



if __name__=='__main__':
    main()

# # import os
# # cwd = os.getcwd()
# # print(cwd)
