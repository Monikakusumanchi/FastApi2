from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base  = declarative_base()

class Book(Base):
   __tablename__ = 'book'
   book_id  = Column(Integer, primary_key=True, index=True)
   book_name = Column(String)
   book_author_id = Column(Integer)
   book_author_name = Column(String)
   time_created = Column(DateTime(timezone=True), server_default=func.now())
   time_updated = Column(DateTime(timezone=True), onupdate=func.now())
   author_id = Column(Integer, ForeignKey('author.id'))

   author = relationship('Author')


class Author(Base):
   __tablename__ = 'author'
   id = Column(Integer, primary_key=True)
   name = Column(String)
   age = Column(Integer)
   time_created = Column(DateTime(timezone=True), server_default=func.now())
   time_updated = Column(DateTime(timezone=True), onupdate=func.now())
