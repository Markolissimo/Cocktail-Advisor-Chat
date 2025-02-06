"""
This module contains the chat routes for the FastAPI app.
It includes the /chat route which is used to interact with the chatbot.
"""

from fastapi import APIRouter
from app.rag import generate_response

router = APIRouter()

@router.post("/")
def chat(input_text: str, user_id: str):
    response = generate_response(input_text, user_id)
    return {"response": response}
