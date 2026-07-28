import google.generativeai as genai

from src.config import GEMINI_API_KEY, MODEL_NAME

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(MODEL_NAME)


def generate_response(prompt: str) -> str:
    """
    Send a prompt to Gemini and return the generated text.
    """

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as ex:
        raise RuntimeError(
            f"Failed to generate Gemini response: {ex}"
        ) from ex