"""
Test the database module.
"""

import numpy as np
from app.database import VectorDB
from rich.console import Console

console = Console()

def test_vector_db():
    console.rule("[bold cyan]Testing Vector Database")
    
    db = VectorDB(embedding_size=3)
    test_embedding = np.array([0.1, 0.2, 0.3], dtype=np.float32)
    test_metadata = {"name": "Test Cocktail", "ingredients": ["Rum", "Sugar"]}
    
    db.add_cocktail(cocktail_id=1, embedding=test_embedding, metadata=test_metadata)
    results = db.search_similar(test_embedding, top_k=1)
    
    assert len(results) > 0
    assert results[0][1]["name"] == "Test Cocktail"
    
    console.print("[green]✅ GOTCHA. Vector Database passed![/green]")
