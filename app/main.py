"""
This is the main FastAPI application. Here is where the FastAPI app is executed.
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import logging
from app.routes import chat, favorites, recommend

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

logging.info("Starting FastAPI app...")
app = FastAPI(title="Cocktail Chatbot API")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

logging.info("Including routes...")
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(favorites.router, prefix="/favorites", tags=["Favorites"])
app.include_router(recommend.router, prefix="/recommend", tags=["Recommendations"])

@app.get("/")
def home():
    logging.info("Home route accessed.")
    return {"message": "Welcome to the Cocktail Chatbot API!"}

    