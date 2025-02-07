from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.rag import generate_response

router = APIRouter()

class ChatRequest(BaseModel):
    input_text: str
    user_id: str

@router.post("/")
def chat(request: ChatRequest):
    response = generate_response(request.input_text, request.user_id)
    return {"response": response}