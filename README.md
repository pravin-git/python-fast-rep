mkdir fastapi-server
cd fastapi-server
python -m venv venv
.\venv\Scripts\activate
uvicorn main:app --reload


http://127.0.0.1:8000/redoc
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/openapi.json


py -m notebook