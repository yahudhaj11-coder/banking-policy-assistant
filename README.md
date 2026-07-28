# 🏦 Banking Policy Assistant (RAG)

An AI-powered Banking Policy Assistant built using **Retrieval-Augmented Generation (RAG)**.

This application answers banking policy questions by retrieving relevant information from banking policy documents instead of relying solely on the Large Language Model's pretrained knowledge.

The project was built as a learning exercise to understand the complete RAG architecture, including document ingestion, chunking, embeddings, vector databases, semantic retrieval, prompt engineering, and LLM integration.

---

# Features

- PDF document ingestion
- Recursive document chunking
- Local Hugging Face embeddings
- Chroma Vector Database
- Semantic similarity search
- Retrieval-Augmented Generation (RAG)
- Prompt engineering
- Google Gemini integration
- Streamlit web interface

---

# Architecture

```
                        Banking Policy PDFs
                                │
                                ▼
                        PyPDFLoader
                                │
                                ▼
                  RecursiveCharacterTextSplitter
                                │
                                ▼
          Hugging Face Embedding Model (Local)
          sentence-transformers/all-MiniLM-L6-v2
                                │
                                ▼
                     Chroma Vector Database
                                │
                                ▼
                     Semantic Document Retrieval
                                │
                                ▼
                         Prompt Builder
                                │
                                ▼
                         Google Gemini LLM
                                │
                                ▼
                           Final Response
```

---

# Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | User Interface |
| LangChain | RAG Framework |
| ChromaDB | Vector Database |
| Sentence Transformers | Local Embeddings |
| Google Gemini | Large Language Model |
| PyPDFLoader | PDF Processing |
| python-dotenv | Environment Variables |

---

# Project Structure

```
banking-policy-assistant/

│
├── app.py
│
├── data/
│   └── policies/
│
├── src/
│   ├── __init__.py
│   ├── chunking.py
│   ├── config.py
│   ├── embeddings.py
│   ├── gemini_client.py
│   ├── loaders.py
│   ├── prompts.py
│   ├── retriever.py
│   └── vectordb.py
│
├── tests/
│
├── vectordb/
│
├── .env
├── requirements.txt
└── README.md
```

---

# How It Works

### 1. Document Ingestion

Banking policy PDF documents are loaded using LangChain's `PyPDFLoader`.

---

### 2. Chunking

Large documents are divided into overlapping chunks using `RecursiveCharacterTextSplitter`.

This improves retrieval accuracy while preserving context.

---

### 3. Embedding Generation

Each chunk is converted into a dense semantic vector using the local Hugging Face model:

```
sentence-transformers/all-MiniLM-L6-v2
```

This eliminates external embedding API costs and rate limits.

---

### 4. Vector Storage

Embeddings are stored inside a persistent Chroma Vector Database.

Each vector is stored together with:

- Original document text
- Metadata
- Source document
- Page information

---

### 5. Semantic Retrieval

When a user submits a question:

- The question is converted into an embedding.
- Chroma searches for the most semantically similar document chunks.
- The top matching chunks are returned.

---

### 6. Prompt Augmentation

The retrieved document chunks are combined with the user's question into a structured prompt.

The prompt instructs Gemini to answer only using the retrieved context.

---

### 7. Response Generation

Google Gemini generates the final response using the supplied banking policy context.

This significantly reduces hallucinations compared to a standard chatbot.

---

# RAG Workflow

```
User Question
      │
      ▼
Generate Query Embedding
      │
      ▼
Semantic Search
      │
      ▼
Retrieve Top-K Chunks
      │
      ▼
Build Prompt
      │
      ▼
Google Gemini
      │
      ▼
Final Answer
```

---

# Installation

Clone the repository.

```bash
git clone <repository-url>
```

Navigate to the project.

```bash
cd banking-policy-assistant
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate the virtual environment.

Windows

```bash
.venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

```
GEMINI_API_KEY=your_api_key_here
```

---

# Running the Application

```bash
streamlit run app.py
```

---

# Key Concepts Demonstrated

- Retrieval-Augmented Generation (RAG)
- Prompt Engineering
- Semantic Search
- Dense Vector Embeddings
- Vector Databases
- Chunking Strategies
- Context Injection
- Hallucination Reduction
- Modular Software Architecture
- Dependency Injection Principles
- Separation of Responsibilities

---

# Future Enhancements

- Conversation memory
- Source citations
- Hybrid search (keyword + semantic)
- Multi-document collections
- Local LLM integration using Ollama
- Docker deployment
- Authentication and authorization
- Cloud deployment (Azure / AWS)

---

# Learning Objectives

This project was developed to gain practical experience with:

- End-to-end RAG architecture
- LangChain fundamentals
- Local embedding models
- Vector databases
- Semantic retrieval
- Prompt engineering
- Enterprise-style modular application design

---

# License

This project is intended for educational and learning purposes.
