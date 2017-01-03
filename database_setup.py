from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from datetime import datetime

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id=Column(Integer, primary_key=True)
    password=Column(String)
    email=Column(String)
    name=Column(String)
    dob=Column(Date)
