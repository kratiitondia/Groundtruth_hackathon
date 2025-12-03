# Customer Support Chatbot 

This is a production-ready starter for a Customer Support Chatbot using:
- FastAPI backend with RAG + OpenAI (embeddings + Chat)
- FAISS vectorstore (in-memory with optional persistence)
- Context enrichment & PII masking
- Simple frontend (HTML/CSS/JS)
- Docker + docker-compose

## Requirements
- Python 3.11+
- OpenAI API Key (set environment variable OPENAI_API_KEY)
- Docker (optional)

## Quickstart (local)
1. Copy `.env.example` -> `.env` and set `OPENAI_API_KEY`.
2. Create venv:
   ```
   python -m venv venv
   source venv/bin/activate
   pip install -r backend/requirements.txt
   ```
3. Seed demo data (optional):
   ```
   python -m backend.app.seed_data
   ```
4. Run backend:
   ```
   uvicorn backend.app.main:app --reload --port 8000
   ```
5. Open `frontend/index.html` in your browser.

## Quickstart (docker)
```
cp .env.example .env
docker-compose up --build
```

## Endpoints
- `POST /index` — index docs: body `[{id,title,text},...]`
- `POST /seed` — seed demo docs
- `POST /chat` — chat: body `{user_id,message,latitude,longitude}`

## Notes
- Keep your `OPENAI_API_KEY` private.
- FAISS is in-memory by default; use `datastore.save()` to persist.
- This starter focuses on secure prompt handling and strict RAG mode.
