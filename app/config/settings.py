from dotenv import load_dotenv
import os

load_dotenv()

os.environ["LANGCHAIN_ENDPOINT"] = "https://eu.api.smith.langchain.com"

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    
    LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2", "true")
    LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
    LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT", "multi-ai-agent")
    LANGCHAIN_ENDPOINT = "https://eu.api.smith.langchain.com"
    
    ALLOWED_MODEL_NAMES = [
        "gemma2-9b-it",
        "llama-3.3-70b-versatile",
        "llama-3.1-8b-instant",
        "llama-70b-8192",
    ]
    
    API_URL = os.getenv("API_URL")

settings = Settings()

os.environ["LANGCHAIN_TRACING_V2"] = settings.LANGCHAIN_TRACING_V2
os.environ["LANGCHAIN_API_KEY"] = settings.LANGCHAIN_API_KEY or ""
os.environ["LANGCHAIN_PROJECT"] = settings.LANGCHAIN_PROJECT