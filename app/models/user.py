from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.ddl import CreateTable
from app.backend.db import Base




class User(Base):
    __tablename__ = 'Users'
    id = Column (Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True,index=True)

    task=relationship('Task', back_populates='task' )

print(CreateTable(User.__table__))



