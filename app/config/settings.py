from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

    ALLOWED_MODEL_NAMES = [
        "gemma2-9b-it",
        "llama-3.3-70b-versatile",
        "lamma-3.1-8b-instant",
        "llama-70b-8192",
        "llama-8b-8192",
        "whisper-large-v3",
        "whisper-large-v3-turbo"
        "distil-whisper-large-v3-en"
    ]

    API_URL = os.getenv("API_URL")

settings = Settings()