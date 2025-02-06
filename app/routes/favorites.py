"""
This file contains the routes for the favorites blueprint.
It includes the /favorites route which is used to interact with the user's favorite cocktails.
"""

from fastapi import APIRouter
from app.database import vector_db

router = APIRouter()

@router.post("/add")
def add_favorite(user_id: str, ingredients: list[str]):
    vector_db.store_user_preference(user_id, ingredients)
    return {"message": "Preferences saved!"}

@router.get("/")
def get_favorites(user_id: str):
    favorites = vector_db.get_user_preferences(user_id)
    return {"favorites": favorites}
