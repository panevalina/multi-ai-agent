# Multi AI Agent

A full-stack AI agent application that allows users to interact with multiple LLM models via a Streamlit frontend and a FastAPI backend. Supports optional web search via Tavily and is containerized with Docker, analyzed with SonarQube, and built/deployed via a Jenkins CI/CD pipeline.

---

## Tech Stack

- **Frontend:** Streamlit
- **Backend:** FastAPI
- **AI/LLM:** LangChain, LangGraph, Groq
- **Web Search:** Tavily
- **Containerization:** Docker
- **CI/CD:** Jenkins
- **Code Quality:** SonarQube
- **Observability:** LangSmith

---

## Project Structure

```
multi-ai-agent/
├── app/
│   ├── backend/
│   │   └── api.py            
│   ├── common/
│   │   ├── logger.py           
│   │   └── custom_exception.py
│   ├── config/
│   │   └── settings.py         
│   ├── core/
│   │   └── ai_agent.py        
│   ├── frontend/
│   │   └── ui.py               
│   └── main.py                
├── Dockerfile
├── .dockerignore
├── .gitignore
├── Jenkinsfile
├── pyproject.toml
└── requirements.txt
```

---

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/panevalina/multi-ai-agent.git
cd multi-ai-agent
```

### 2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -e .
```

### 4. Configure environment variables

Create a `.env` file in the root directory:
```
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
HOST=your_host
API_URL=your_backend_url
```

### 5. Run the application
```bash
python app/main.py
```

- Frontend: `http://localhost:8501`
- Backend: `http://localhost:8000`

---

## Running with Docker

### Build the image
```bash
docker build -t multi-ai-agent .
```

### Run the container
```bash
docker run -p 8000:8000 -p 8501:8501 --env-file .env multi-ai-agent
```

---

## Supported Models

- `gemma2-9b-it`
- `llama-3.3-70b-versatile`
- `llama-3.1-8b-instant`
- `llama-70b-8192`
---

## API

### `POST /chat`

**Request body:**
```json
{
  "model_name": "llama-3.3-70b-versatile",
  "system_prompt": "You are a medical assistant. Only answer questions related to health and medicine.",
  "messages": ["What are the best stocks to invest in right now?"],
  "allow_search": true
}
```

**Response:**
```json
{
  "response": "As a medical assistant, I can only speak to healthcare-related investments. Some notable medical and pharmaceutical stocks include Johnson & Johnson, Pfizer, and UnitedHealth Group. However, please consult a financial advisor before making any investment decisions."
}
```

**Error responses:**
- `400` — Invalid model name
- `500` — Failed to get AI response

---

## CI/CD Pipeline (Jenkins)

The `Jenkinsfile` defines the following stages:

1. **Clone** — pulls the latest code from GitHub
2. **SonarQube Analysis** — scans code for bugs and vulnerabilities

> AWS ECR and Fargate deployment stages to be added.

---

## Environment Variables

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | API key from [Groq](https://console.groq.com) |
| `TAVILY_API_KEY` | API key from [Tavily](https://tavily.com) |
| `HOST` | Backend host (default: `127.0.0.1`) |
| `API_URL` | Full backend URL (default: `http://127.0.0.1:8000/`) |
| `LANGCHAIN_API_KEY` | API key from [LangSmith](https://smith.langchain.com) |
| `LANGCHAIN_PROJECT` | LangSmith project name (default: `multi-ai-agent`) |
---

## Author

**Lina Paneva**