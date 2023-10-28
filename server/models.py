# models.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Artist(Base):
    __tablename__ = "artists"
    
    artist_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class Album(Base):
    __tablename__ = "albums"
    
    album_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    artist_id = Column(Integer, index=True)

class Track(Base):
    __tablename__ = "tracks"
    
    track_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    album_id = Column(Integer, index=True)
