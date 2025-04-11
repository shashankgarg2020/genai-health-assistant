from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from src.rag_pipeline import ask_question

app = FastAPI()
templates = Jinja2Templates(directory="src/templates")  # Make sure this folder exists

@app.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

class AskRequest(BaseModel):
    query: str

@app.post("/ask")
def ask(request: AskRequest):
    query = request.query
    answer, sources = ask_question(query)
    source_texts = [s.page_content[:200] for s in sources] if sources else []
    return {
        "question": query,
        "answer": answer,
        "sources": source_texts
    }
