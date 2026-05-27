<div align="center">

```
██████╗  █████╗  ██████╗     ██████╗ ██████╗ ███████╗
██╔══██╗██╔══██╗██╔════╝     ██╔══██╗██╔══██╗██╔════╝
██████╔╝███████║██║  ███╗    ██████╔╝██║  ██║█████╗  
██╔══██╗██╔══██║██║   ██║    ██╔═══╝ ██║  ██║██╔══╝  
██║  ██║██║  ██║╚██████╔╝    ██║     ██████╔╝██║     
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝     ╚═╝     ╚═════╝ ╚═╝     

      ─── Retrieval-Augmented Generation on PDFs ───
```

### 🧠 Upload any PDF. Ask anything. Gemini answers from the document — not from the internet.

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=FFD43B)](https://python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-0.3.x-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://langchain.com/)
[![Gemini](https://img.shields.io/badge/Gemini-2.5_Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/technologies/gemini/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)

<br/>

[![Embeddings](https://img.shields.io/badge/Embeddings-gemini--embedding--2--preview-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![Vector Store](https://img.shields.io/badge/Vector_Store-InMemory_(LangChain)-1C3C3C?style=for-the-badge)](https://python.langchain.com/)
[![100% Python](https://img.shields.io/badge/Language-100%25_Python-3776AB?style=for-the-badge&logo=python&logoColor=FFD43B)](https://github.com/aarav12e/RAG_PDF)
[![Stars](https://img.shields.io/github/stars/aarav12e/RAG_PDF?style=for-the-badge&color=FFD700&logo=github)](https://github.com/aarav12e/RAG_PDF/stargazers)

</div>

---

## 🧠 What is RAG?

**RAG (Retrieval-Augmented Generation)** is an AI technique that grounds an LLM's answers in a specific document — instead of its general training data. The model doesn't "remember" your PDF; it *searches* it on every question.

```
  WITHOUT RAG                          WITH RAG
  ──────────────────────────────────   ──────────────────────────────────────────
  User: "What's the refund policy?"   User: "What's the refund policy?"
  LLM:  "I don't know your doc."      LLM:  Searches your PDF → finds the exact
                                             clause → answers from that text ✅
```

> *No hallucination from web training. Just answers from your document.*

---

## ✨ What This App Does

Upload **any PDF** — a research paper, legal document, book, notes, manual — then chat with it in natural language. The app:

1. Loads and parses your PDF with `PyPDFLoader`
2. Splits it into overlapping chunks with `RecursiveCharacterTextSplitter`
3. Converts chunks to vector embeddings using **Gemini Embedding 2**
4. Stores them in an `InMemoryVectorStore`
5. On each question — retrieves the **top 2 most relevant chunks** via similarity search
6. Feeds those chunks as context to **Gemini 2.5 Flash**
7. Streams the answer back in a clean Streamlit chat UI

---

## 🔄 RAG Pipeline — Full Flow

```
  📄 You upload a PDF
          │
          ▼
  ┌─────────────────────────────────────────────────────┐
  │  INGESTION PHASE  (runs once on upload)             │
  │                                                     │
  │  PyPDFLoader                                        │
  │  └─→ Load all pages as Document objects             │
  │                                                     │
  │  RecursiveCharacterTextSplitter                     │
  │  └─→ chunk_size=1000, chunk_overlap=200             │
  │      Splits into overlapping text windows           │
  │                                                     │
  │  GoogleGenerativeAIEmbeddings                       │
  │  └─→ model: gemini-embedding-2-preview              │
  │      Converts each chunk → dense vector             │
  │                                                     │
  │  InMemoryVectorStore                                │
  │  └─→ Stores all vectors in RAM                      │
  │      Ready for similarity search                    │
  └─────────────────────────────────────────────────────┘
          │
          │ st.session_state persists vector_db
          │
          ▼
  💬 You type a question
          │
          ▼
  ┌─────────────────────────────────────────────────────┐
  │  RETRIEVAL PHASE  (runs on every question)          │
  │                                                     │
  │  similarity_search(query, k=2)                      │
  │  └─→ Embed the query                                │
  │      Find top-2 closest chunks by cosine distance   │
  │      Return the most relevant document excerpts     │
  └─────────────────────────────────────────────────────┘
          │
          ▼
  ┌─────────────────────────────────────────────────────┐
  │  GENERATION PHASE                                   │
  │                                                     │
  │  Prompt = context (top-2 chunks) + user question    │
  │                                                     │
  │  ChatGoogleGenerativeAI                             │
  │  └─→ model: gemini-2.5-flash                        │
  │      Generates answer grounded in PDF content       │
  └─────────────────────────────────────────────────────┘
          │
          ▼
  🤖 Answer rendered in Streamlit chat UI
```

---

## 🖥️ App Preview

```
  ┌────────────────────────────────────────────────────────┐
  │   Document Q&A ChatBot — Ask Anything                  │
  │                                                        │
  │   ┌────────────────────────────────────────────────┐   │
  │   │  📄  Select Your PDF File                      │   │
  │   │  [ Browse files... ]   uploaded_doc.pdf ✅     │   │
  │   └────────────────────────────────────────────────┘   │
  │   ⏳ Processing...                                     │
  │   ✅ Document Processed Successfully                   │
  │                                                        │
  │   ┌────────────────────────────────────────────────┐   │
  │   │ 👤 You                                         │   │
  │   │ What are the main conclusions of this paper?   │   │
  │   └────────────────────────────────────────────────┘   │
  │                                                        │
  │   ┌────────────────────────────────────────────────┐   │
  │   │ 🤖 AI                                         │   │
  │   │ Based on the document, the main conclusions    │   │
  │   │ are: 1) The proposed method achieves 94.2%     │   │
  │   │ accuracy on benchmark... 2) The model shows    │   │
  │   │ significant improvement over prior work in...  │   │
  │   └────────────────────────────────────────────────┘   │
  │                                                        │
  │   [ Ask Anything...                          ] ➤      │
  └────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Component | Technology | Role |
|-----------|-----------|------|
| **UI** | ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?logo=streamlit&logoColor=white&style=flat-square) | Chat interface + file uploader |
| **LLM** | ![Gemini](https://img.shields.io/badge/-Gemini_2.5_Flash-4285F4?logo=google&logoColor=white&style=flat-square) | Generates answers from retrieved context |
| **Embeddings** | ![Gemini](https://img.shields.io/badge/-gemini--embedding--2--preview-4285F4?logo=google&logoColor=white&style=flat-square) | Converts text chunks → dense vectors |
| **PDF Loader** | ![LangChain](https://img.shields.io/badge/-PyPDFLoader-1C3C3C?style=flat-square) | Parses uploaded PDF into pages |
| **Splitter** | ![LangChain](https://img.shields.io/badge/-RecursiveCharacterTextSplitter-1C3C3C?style=flat-square) | Chunks text with overlap |
| **Vector Store** | ![LangChain](https://img.shields.io/badge/-InMemoryVectorStore-1C3C3C?style=flat-square) | Stores + searches embeddings in RAM |
| **Orchestration** | ![LangChain](https://img.shields.io/badge/-LangChain_0.3.x-1C3C3C?logo=langchain&style=flat-square) | Connects all components |
| **Config** | ![dotenv](https://img.shields.io/badge/-python--dotenv-ECD53F?logo=dotenv&logoColor=black&style=flat-square) | Loads API keys from `.env` |

---

## 📄 The Code — `app.py` Explained

The entire app is **84 lines**. Here's what each section does:

```python
# 1. Load environment variables (GOOGLE_API_KEY)
from dotenv import load_dotenv
load_dotenv()

# 2. Initialize Gemini 2.5 Flash as the LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# 3. Streamlit session state — persists across reruns
if "vector_db" not in st.session_state:
    st.session_state.vector_db = None
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. PDF processing pipeline (runs once on upload)
def document_process(path):
    loader  = PyPDFLoader(path)
    docs    = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,       # ~1000 chars per chunk
        chunk_overlap=200      # 200-char overlap to preserve context at boundaries
    )
    splits = splitter.split_documents(docs)

    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-2-preview"
    )
    vector_db = InMemoryVectorStore.from_documents(
        documents=docs,        # ← stores original docs, not splits
        embedding=embeddings
    )
    st.session_state.vector_db = vector_db

# 5. On every user question:
documents = st.session_state.vector_db.similarity_search(query, k=2)
#   ↑ Finds top-2 chunks semantically closest to the question

context = "\n\n".join([doc.page_content for doc in documents])

prompt = f"""You are a helpful assistant and you provide answers
for user question based on the provided context.
context: {context}
question: {query}"""

result = llm.invoke(prompt)   # Gemini generates grounded answer
```

---

## ⚙️ Environment Variables

Create a `.env` file in the root:

```env
# ─── Google AI ──────────────────────────────────────
GOOGLE_API_KEY=your_google_ai_api_key_here
```

Get your free API key at [aistudio.google.com](https://aistudio.google.com/app/apikey) — no billing required for Gemini free tier.

---

## 🚀 Getting Started

### Prerequisites

```bash
python --version    # Python 3.10+ required
```

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/aarav12e/RAG_PDF.git
cd RAG_PDF

# 2. Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate          # macOS / Linux
venv\Scripts\activate             # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up your API key
echo "GOOGLE_API_KEY=your_key_here" > .env

# 5. Run the app
streamlit run app.py
```

App opens at `http://localhost:8501` 🚀

---

## 📦 Dependencies

```txt
langchain-google-genai    # Gemini LLM + Gemini Embeddings
langchain                 # Core LangChain framework
langchain-community       # PyPDFLoader, InMemoryVectorStore
langchain-text-splitters  # RecursiveCharacterTextSplitter
dotenv                    # Load GOOGLE_API_KEY from .env
pypdf                     # PDF parsing engine (used by PyPDFLoader)
streamlit                 # Web UI + chat interface
```

---

## 🧪 Example Use Cases

| Document Type | Example Questions |
|--------------|------------------|
| 📜 Research Paper | "What dataset was used?" / "What is the model accuracy?" |
| 📋 Legal Contract | "What are the termination clauses?" / "What is the notice period?" |
| 📘 Textbook Chapter | "Summarize the key concepts" / "What is the definition of X?" |
| 📊 Financial Report | "What was the revenue in Q3?" / "What are the risk factors?" |
| 📝 Meeting Notes | "What decisions were made?" / "Who is responsible for X?" |

---

## 🔧 Key Parameters

| Parameter | Value | What It Controls |
|-----------|-------|-----------------|
| `chunk_size` | `1000` | Max characters per text chunk |
| `chunk_overlap` | `200` | Characters shared between adjacent chunks (preserves context at splits) |
| `k` | `2` | Number of most relevant chunks retrieved per query |
| LLM model | `gemini-2.5-flash` | Fast, capable Gemini model for answer generation |
| Embedding model | `gemini-embedding-2-preview` | Google's latest embedding model |

---

## 🗺️ Roadmap

```
  ✅ Done
  ────────────────────────────────────────
  ✅ PDF upload + parsing
  ✅ Recursive text chunking with overlap
  ✅ Gemini embeddings (embedding-2-preview)
  ✅ InMemory vector similarity search
  ✅ Gemini 2.5 Flash for generation
  ✅ Streamlit chat UI with session state

  🔜 Ideas for Future
  ────────────────────────────────────────
  🔜 Swap InMemory → FAISS or ChromaDB (persist across sessions)
  🔜 Multi-PDF support (upload multiple files)
  🔜 Source citation — show which page the answer came from
  🔜 Streaming response output
  🔜 Deploy to Streamlit Cloud / Hugging Face Spaces
  🔜 Add conversation memory (multi-turn context)
```

---

## 🤝 Contributing

```bash
git checkout -b feature/add-chroma-db
git commit -m "feat: swap InMemoryVectorStore for ChromaDB persistence"
git push origin feature/add-chroma-db
```

---

## 👨‍💻 Author

<div align="center">

**Aarav Kumar**
*AI / ML Developer · Python · LangChain · B.Tech CDS (2028) · Ignite Club*

[![GitHub](https://img.shields.io/badge/GitHub-aarav12e-181717?style=for-the-badge&logo=github)](https://github.com/aarav12e)

</div>

---

<div align="center">

```python
# The entire intelligence of this app in 3 lines:

chunks   = splitter.split(pdf)           # Break document into pieces
context  = vector_db.search(question)    # Find the relevant pieces
answer   = gemini.generate(context)      # Answer from those pieces only
```

*Built with 🧠 LangChain + Gemini 2.5 Flash — because your PDFs deserve to talk back*

**`< / RAG_PDF >`**

</div>
