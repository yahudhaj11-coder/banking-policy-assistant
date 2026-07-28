from langchain_chroma import Chroma
from langchain_core.documents import Document


def retrieve_documents(
    query: str,
    vector_store: Chroma,
    k: int = 5
) -> list[Document]:
    """
    Retrieve the most relevant document chunks.
    """

    documents = vector_store.similarity_search(
        query=query,
        k=k
    )

    return documents