from fastapi import FastAPI

# Initialize the FastAPI application instance
app = FastAPI()

# Define a GET route at the root URL path
@app.get("/")
def read_root():
    return {"Hello": "World"}