from langchain_core.documents import Document


SYSTEM_PROMPT = """
You are a banking policy assistant.

Answer the user's question using ONLY the provided context.

If the answer cannot be found in the context,
respond with:

"I couldn't find this information in the supplied banking policies."

Be concise, accurate, and professional.
""".strip()


def build_prompt(
    query: str,
    documents: list[Document]
) -> str:
    """
    Build the final prompt sent to the LLM.
    """

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    prompt = f"""
{SYSTEM_PROMPT}

====================
Context
====================

{context}

====================
Question
====================

{query}
"""

    return prompt.strip()