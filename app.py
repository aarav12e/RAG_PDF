from dotenv import load_dotenv

load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
### chroma, FAISS, InMemory
from langchain_community.vectorstores import InMemoryVectorStore
import streamlit as st
from time import sleep

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
if "vector_db" not in st.session_state:
    st.session_state.vector_db = None

if "messages" not in st.session_state:
    st.session_state.messages = []


def document_process(path):
    ## document loading
    loader = PyPDFLoader(path)
    docs = loader.load()



## splitting
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = splitter.split_documents(docs)


## embeggings and vector stors

    embeddings = GoogleGenerativeAIEmbeddings(model ="gemini-embedding-2-preview")
    vector_db = InMemoryVectorStore.from_documents(documents=docs, embedding=embeddings)
    
    st.session_state.vector_db = vector_db
    st.session_state.document_uploaded = True


st.subheader("Document  Q&A ChatBot - Ask Anything")

if "document_uploaded" not in st.session_state:
    st.session_state.document_uploaded = False

### document upload 
if not st.session_state.document_uploaded:

    file = st.file_uploader(label="Select Your PDF File", type="pdf")
    if file:
    
        with open("uploaded_document.pdf", "wb") as f:
            f.write(file.getvalue())
        with st.spinner("Processing..."):
            document_process("./uploaded_document.pdf")

        st.markdown("Document Processed Successfully...")
        sleep(2)
        st.rerun()

## chat ui

if st.session_state.document_uploaded and st.session_state.vector_db:
    for oneMessage in st.session_state.messages:
        role = oneMessage["role"]
        content = oneMessage["content"]
        st.chat_message(role).markdown(content)
    query = st.chat_input("Ask Anything...")

    if query:
        st.session_state.messages.append({"role": "user", "content": query})
        st.chat_message("user").markdown(query)
        documents = st.session_state.vector_db.similarity_search(query, k=2)
        context = ""

        for doc in documents:
            context += doc.page_content + "\n\n"

        prompt = f"""You are a helpful assistant and you provide answers for user question based on the probided context. context: {context} and question is: {query} """
        result = llm.invoke(prompt)

        st.session_state.messages.append({"role": "ai", "content": result.content})
        st.chat_message("ai").markdown(result.content)