from pathlib import Path

from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader


POLICY_FOLDER = Path("data/policies")


def load_documents() -> list[Document]:
    """
    Load every PDF from the policies folder.
    """

    documents = []

    for pdf_file in POLICY_FOLDER.glob("*.pdf"):

        loader = PyPDFLoader(str(pdf_file))
        documents.extend(loader.load())

    return documents