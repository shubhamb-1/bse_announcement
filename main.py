from fastapi import FastAPI
from crud import create_dummy
app = FastAPI()


@app.get("/")
def home():
    create_dummy()
    return {"message":"Hello"}