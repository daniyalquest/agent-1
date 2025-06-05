from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from src.ai_agent import chat_response
import os

app = FastAPI()

# Serve static HTML/JS
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def get_chat_ui():
    with open("static/index.html", encoding="utf-8") as f:
        return f.read()

class Message(BaseModel):
    text: str

@app.post("/chat")
def chat(msg: Message):
    reply = chat_response(msg.text)
    return {"response": reply}
