from dotenv import load_dotenv
import os

load_dotenv()

APP_TITLE = "Banking Policy Assistant"

MODEL_NAME = "gemini-2.5-flash"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")



GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY was not found. Please check your .env file."
    )