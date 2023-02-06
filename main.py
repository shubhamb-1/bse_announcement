from fastapi import FastAPI
from scrap import fetch_periodically
from scheduler import scheduler_function
from database import create_table

app = FastAPI()

@app.get("/")
def home():
    # create_table()
    scheduler_function()
    return {"message":"success"}