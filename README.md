mkdir fastapi-server
cd fastapi-server
python -m venv venv
.\venv\Scripts\activate
uvicorn main:app --reload