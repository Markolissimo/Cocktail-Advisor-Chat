"""
Test cases for the favourites module (add, remove, and retrieve favourites).
"""

from app.database import VectorDB
from rich.console import Console

console = Console()

def test_user_memory():
    console.rule("[bold cyan]Testing User Memory")

    db = VectorDB()
    db.store_user_preference("user1", ["Lime", "Mint"])

    favorites = db.get_user_preferences("user1")

    assert "Lime" in favorites
    assert "Mint" in favorites

    console.print("[green]✅ YEAP. User Memory passed![/green]")
