from langchain_chroma import Chroma
from langchain_core.documents import Document

from src.config import VECTOR_DB_DIRECTORY
from src.embeddings import get_embedding_model


def create_vector_store(chunks: list[Document]) -> Chroma:
    """
    Create and persist a Chroma vector database.
    """

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=get_embedding_model(),
        persist_directory=VECTOR_DB_DIRECTORY
    )

    return vector_store


def load_vector_store() -> Chroma:
    """
    Load an existing Chroma vector database.
    """

    vector_store = Chroma(
        persist_directory=VECTOR_DB_DIRECTORY,
        embedding_function=get_embedding_model()
    )

    return vector_store