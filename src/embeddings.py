from langchain_huggingface import HuggingFaceEmbeddings

from src.config import LOCAL_EMBEDDING_MODEL

embedding_model = HuggingFaceEmbeddings(
    model_name=LOCAL_EMBEDDING_MODEL
)


def get_embedding_model() -> HuggingFaceEmbeddings:
    """
    Return the configured local embedding model.
    """

    return embedding_model