from database import  Base
from sqlalchemy import Column,Boolean,Integer,String,DateTime


class Announcement(Base):
    __tablename__ = "Announcement"
    
    id = Column(Integer,primary_key=True,index=True)
    company_name = Column(String,nullable=False)
    description = Column(String,nullable=False)
    announcement_link = Column(String,nullable=False)
    time = Column(DateTime,nullable=False)