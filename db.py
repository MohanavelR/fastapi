from sqlalchemy import create_engine 
# create database engine

from sqlalchemy.orm import sessionmaker  ,declarative_base
# sessionmaker is database working session 
# declarative_base is basic class for orm model

from dotenv import load_dotenv
# you can access .env file variable 

import os
load_dotenv()

DATABASE_URL=os.getenv("DATABASE_URL")
engine=create_engine(DATABASE_URL)

SessionLocal=sessionmaker(bind=engine,autoflush=False)
Base=declarative_base()

# 

def get_db():
    db=SessionLocal() 
    try:
        yield db
    finally:
        db.close()



