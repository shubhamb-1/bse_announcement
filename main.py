from fastapi import FastAPI
from crud import create_dummy
from scrap import fetch_periodically
from scheduler import scheduler_function

app = FastAPI()

@app.get("/")
def home():
    # create_dummy()
    # add_to_cache(111)
    # result = in_chache(31421)
    # fetch_periodically()
    scheduler_function()
    return {"message":"success"}