"""
This module contains the RAG class which is used to represent the Retrieval Augmented Generator model (potentially LLM + RAG logic).
"""

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.schema import AIMessage, HumanMessage
from app.database import vector_db

embedder = OpenAIEmbeddings()
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)

def retrieve_cocktails(query: str, top_k: int=5) -> list:
    """Retrieve relevant cocktails for a given query.
    Args:
        query (stR): User query.
    Returns:
        list: List of relevant cocktails.
    """
    query_embedding = embedder.embed_query(query)
    similar_cocktails = vector_db.search_similar(query_embedding, top_k)
    return similar_cocktails

def generate_response(user_input: str, user_id: str) -> str:
    """Generate a response using RAG.
    Args:
        user_input (str): User input.
        user_id (str): User ID.
    REturns:
        str: Generated response
    """
    relevant_cocktails = retrieve_cocktails(user_input)
    user_favorites = vector_db.get_user_preferences(user_id)

    context = f"User favorites: {user_favorites}\n\nRelevant cocktails:\n"
    for cocktail in relevant_cocktails:
        context += f"- {cocktail[1]['name']} (Ingredients: {cocktail[1]['ingredients']})\n"

    messages = [
        HumanMessage(content=user_input),
        AIMessage(content=context)
    ]
    
    return llm(messages).content