"""
Test the RAG class.
"""

from app.rag import retrieve_cocktails, embedder
from app.database import vector_db
from rich.console import Console

console = Console()

console = Console()

def preload_cocktails():
    cocktails = [
        {"id": 1, "name": "Margarita", "ingredients": ["Tequila", "Lime", "Triple Sec"]},
        {"id": 2, "name": "Tequila Sunrise", "ingredients": ["Tequila", "Orange Juice", "Grenadine"]},
        {"id": 3, "name": "Paloma", "ingredients": ["Tequila", "Grapefruit Soda", "Lime"]},
    ]

    for cocktail in cocktails:
        embedding = embedder.embed_query(cocktail["name"])  # Generate embedding
        vector_db.add_cocktail(cocktail["id"], embedding, cocktail)

    console.print(f"[green]✅ Preloaded {len(cocktails)} cocktails into FAISS![/green]")

def test_rag_retrieval():
    console.rule("[bold cyan]Testing RAG Retrieval")

    preload_cocktails()

    query = "I like tequila-based cocktails"
    results = retrieve_cocktails(query, top_k=3)

    assert len(results) > 0, "No cocktails retrieved! FAISS may still be empty."
    console.print(f"[green]✅ OHHOO, Retrieved {len(results)} cocktails![/green]")
