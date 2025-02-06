"""
This module contains the tests for the main API used in the application.
"""

import pytest
from httpx import AsyncClient
from app.main import app
from rich.console import Console

console = Console()

@pytest.mark.asyncio
async def test_chat_api():
    """Test chat endpoint. It should return a response with a status code of 200 which will indicate that the API is working correctly.
    Args:
        app (FastAPI): FastAPI instance.
    Returns:
        None
    """
    console.rule("[bold cyan]Testing Chat API")
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/chat/", json={"input_text": "What is in a Mojito?", "user_id": "user1"})
    
    assert response.status_code == 200
    console.print("[green]✅ Chat API passed![/green]")

@pytest.mark.asyncio
async def test_favorites_api():
    """Test adding and retrieving favorites. It should return a response with a status code of 200 which will indicate that the API is working correctly.
    Args:
        app (FastAPI): FastAPI instance.
    Returns:
        None
    """
    console.rule("[bold cyan]Testing Favorites API")
    async with AsyncClient(app=app, base_url="http://test") as client:
        add_response = await client.post("/favorites/add", json={"user_id": "user1", "ingredients": ["Mint", "Lime"]})
        get_response = await client.get("/favorites/", params={"user_id": "user1"})
    
    assert add_response.status_code == 200
    assert get_response.status_code == 200
    assert "Mint" in get_response.json()["favorites"]
    
    console.print("[green]✅ All good. Favorites API passed![/green]")
