from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    # connect_agrs is only for SQlite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()


# Session = sessionmaker()
# engine = create_engine("sqlite:///your_db.sqlite")
# Session.configure(bind=engine)
# session = Session()

Base = declarative_base()

def create_table():
    Base.metadata.create_all(bind=engine)