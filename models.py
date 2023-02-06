from database import  Base
from sqlalchemy import Column,Boolean,Integer,String,DateTime


class Announcement(Base):
    __tablename__ = "Announcement"
    
    id = Column(Integer,primary_key=True,index=True)
    unique_id = Column(String,nullable=False)
    company_name = Column(String,nullable=False)
    company_id = Column(Integer,nullable=False)
    announcement = Column(String,nullable=False)
    announcement_type = Column(String)
    announcement_link = Column(String,nullable=False)
    time = Column(DateTime,nullable=False)
