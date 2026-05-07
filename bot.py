from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()

GROQ_KEY = os.getenv("GROQ_API_KEY")

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={"Authorization": f"Bearer {GROQ_KEY}"},
        json={
            "model": "llama3-8b-8192",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": req.message}
            ]
        }
    )

    answer = response.json()["choices"][0]["message"]["content"]
    return {"answer": answer}
