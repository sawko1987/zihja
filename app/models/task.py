from app.models.user import User
from sqlalchemy.orm import relationship
from sqlalchemy.sql.ddl import CreateTable
from app.backend.db import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class Task(Base):
    __tablename__ = 'tasks'
    id = Column (Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('Users.id'), nullable=True, index=True)
    slug = Column(String, unique=True,index=True)

    user = relationship('User', back_populates='tasks')


print(CreateTable(Task.__table__))