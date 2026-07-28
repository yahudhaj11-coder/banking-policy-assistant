from src.prompts import build_prompt
from src.retriever import retrieve_documents
from src.vectordb import load_vector_store

vector_store = load_vector_store()

documents = retrieve_documents(
    query="What documents are required for KYC?",
    vector_store=vector_store
)

prompt = build_prompt(
    query="What documents are required for KYC?",
    documents=documents
)

print(prompt)