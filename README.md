# Cocktail-Advisor-Chat
Develop a Python-based chat application that integrates with a large language model (LLM) to create a Retrieval-Augmented Generation (RAG) system using a vector database. The final application should have a simple interface to demonstrate its functionality.

# STILL IN PROCESS OF CREATION, but if you want to try it out note this:

1. Prerequisites
Ensure you have the following installed on your system:
* Python 3.9+
* pip (Python package manager)
* Git
* Virtual Environment (venv)

2. Clone the Repository
Clone the project from GitHub:
git clone https://github.com/your-repo/cocktail-chatbot.git
cd cocktail-chatbot

3. Create & Activate a Virtual Environment
Windows (PowerShell):
python -m venv .venv
.venv\Scripts\Activate

Mac/Linux:
python -m venv .venv
source .venv/bin/activate

4. Install Dependencies
pip install -r requirements.txt

5. Set Up Environment Variables
Create a .env file in the root directory and add your OpenAI API key:
OPENAI_API_KEY=your-api-key-here

6. Start the FastAPI Server
uvicorn app.main:app --reload
The API will be available at: http://localhost:8000/
The Chat UI will be available at: http://localhost:8000/static/index.html

# API Endpoints

Chat with the AI
curl -X POST "http://localhost:8000/chat/" \
     -H "Content-Type: application/json" \
     -d '{"input_text": "What are my favorite ingredients?", "user_id": "user1"}'

Store User Preferences
curl -X POST "http://localhost:8000/favorites/add" \
     -H "Content-Type: application/json" \
     -d '{"user_id": "user1", "ingredients": ["Rum", "Lemon", "Sugar"]}'

Retrieve User Preferences
curl -X GET "http://localhost:8000/favorites/?user_id=user1"

# Troubleshooting

1. Chat UI is Not Loading?
* Make sure you're accessing http://localhost:8000/static/index.html.
* Ensure app/main.py contains:
app.mount("/static", StaticFiles(directory="app/static"), name="static")

2. API Not Working?
* Run uvicorn app.main:app --reload and check logs for errors.
* Ensure .env contains the correct OpenAI API key.

3. User Preferences Not Saving?
* Run curl commands to check if favorites/add and favorites/ endpoints are storing data correctly.

# Project Structure
📂 cocktail-chatbot/
├── 📂 app/
│   ├── main.py        # FastAPI main app
│   ├── database.py    # FAISS Vector DB
│   ├── rag.py         # Retrieval-Augmented Generation logic
│   ├── routes/        # API endpoints
│   ├── static/        # Frontend HTML UI
├── 📂 data/          # Application data
├── 📂 tests/          # Unit tests
├── requirements.txt   # Python dependencies
├── README.md          # Project documentation

# Contributing
Want to improve the chatbot? Feel free to fork this repo and submit pull requests! Thanks:)

# Credits
Developed by Berezovskyi Mark as part of a cocktail recommendation chatbot using FastAPI, FAISS, OpenAI, and Langchain.

# License
MIT License

