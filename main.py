from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from scrap import fetch_periodically
from scheduler import scheduler_function
from database import get_db_session,create_table
import models
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def to_dict(announcement):
    result = dict()
    # result["id"] = announcement.id
    #result["company_name"] = announcement.id
    result["company_name"] = announcement.company_name
    result["announcement"] = announcement.announcement
    result["announcement_type"] = announcement.announcement_type
    result["announcement_link"] = announcement.announcement_link
    result["time"] = announcement.time.strftime("%m/%d/%Y  %H:%M:%S")
    return result


@app.get("/announcements")
def read_announcements(skip: int = 0, limit: int = 100):
    if limit > 100:
        limit = 100
    session = get_db_session()
    announcements = session.query(models.Announcement).offset(skip).limit(limit).all()
    session.close()
    announcements = [to_dict(announcement) for announcement in announcements]
    response = JSONResponse(content=announcements)
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:3000"
    return announcements

@app.get("/")
def home():
    create_table()
    scheduler_function()
    return {"message":"success"}