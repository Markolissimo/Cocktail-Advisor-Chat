"""
This file contains the routes for the recommendation system.
It includes the /recommend route which is used to interact with the recommendation system.
"""

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def recommend():
    return {"message": "Recommendation endpoint working!"}