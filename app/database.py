"""
This file contains the vector database connection (FAISS), database models and possible configurations.
"""

import faiss
import numpy as np

class VectorDB:
    def __init__(self, embedding_size: int=1536):
        self.index = faiss.IndexFlatL2(embedding_size)
        self.data = []
        self.user_memory = {}

    def add_cocktail(self, cocktail_id: int, embedding: np.ndarray, metadata: dict) -> None:
        """Add a cocktail embedding with metadata.
        Args:
            cocktail_id (int): Cocktail ID.
            embedding (np.ndarray): Cocktail embedding.
            metadata (dict): Cocktail metadata.
        Returns:
            None
        """
        print(f"Adding Cocktail: {metadata['name']} | Embedding Dimension: {len(embedding)}")
    
        self.index.add(np.array([embedding], dtype=np.float32))
        self.data.append((cocktail_id, metadata))

        print(f"FAISS now contains {self.index.ntotal} embeddings.")

    def search_similar(self, query_embedding: np.ndarray, top_k: int=5) -> list:
        """Find top-k similar cocktails.
        Args:
            query_embedding (np.ndarray): Query embedding.
            top_k (int): Number of similar cocktails to return.
        Returns:
            list: List of similar cocktails.
        """
        
        if self.index.ntotal == 0:
            print("FAISS Index is empty! Returning an empty list.")
            return []
    
        print(f"Searching FAISS Index with {self.index.ntotal} stored embeddings...")
        
        distances, indices = self.index.search(np.array([query_embedding], dtype=np.float32), top_k)

        valid_results = []
        for idx in indices[0]:
            if idx == -1:
                print("FAISS returned -1 (no valid match found). Skipping.")
                continue  # Skip invalid indices
            if 0 <= idx < len(self.data):
                valid_results.append(self.data[idx])
            else:
                print(f"Invalid FAISS index: {idx}. Skipping.")

        return valid_results
    
    def store_user_preference(self, user_id: str, ingredients: list) -> None:
        """Store user's favorite ingredients.
        Args:
            user_id (str): User ID.
            ingredients (list): List of ingredient names.
        """
        self.user_memory[user_id] = ingredients

    def get_user_preferences(self, user_id: str) -> list:
        """Get user's favorite ingredients.
        Args:
            user_id (str): User ID.
        Returns:
            list: List of ingredient names.
        """
        return self.user_memory.get(user_id, [])

vector_db = VectorDB()