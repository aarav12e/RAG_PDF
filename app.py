from dotenv import load_dotenv

load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
### chroma, FAISS, InMemory

from langchain_community.vectorstores import InMemoryVectorStore

## document loading
loader = PyPDFLoader("./0002_Aarav_Kumar.pdf")
docs = loader.load()

print(len(docs))

## splitting
## embeggings and vector stors
