from dotenv import load_dotenv
import os

load_dotenv()

APP_TITLE = "Banking Policy Assistant"

MODEL_NAME = "gemini-2.5-flash"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

LOCAL_EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

EMBEDDING_MODEL = "gemini-embedding-2"

VECTOR_DB_DIRECTORY = "vectordb"

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY was not found. Please check your .env file."
    )