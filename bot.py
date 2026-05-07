from fastapi import FastAPI
from pydantic import BaseModel
import os
from groq import Groq

app = FastAPI()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": req.message}
        ]
    )

    answer = completion.choices[0].message.content
    return {"answer": answer}
