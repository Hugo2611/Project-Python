from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Artist(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, index=True, unique=True)

    # Définissez la relation avec les albums
    albums = relationship("Album", back_populates="artist")

class Album(Base):
    __tablename__ = "albums"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String, index=True)
    artist_id = Column(Integer, ForeignKey("artists.id"))

    # Définissez la relation avec les pistes
    tracks = relationship("Track", back_populates="album")
    artist = relationship("Artist", back_populates="albums")

class Track(Base):
    __tablename__ = "tracks"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String, index=True)
    album_id = Column(Integer, ForeignKey("albums.id"))

    album = relationship("Album", back_populates="tracks")

# Modèle Pydantic pour la création d'artiste
from pydantic import BaseModel

class ArtistCreate(BaseModel):
    name: str

# Modèle Pydantic pour la création d'album
class AlbumCreate(BaseModel):
    title: str
    artist_id: int

# Modèle Pydantic pour la création de piste
class TrackCreate(BaseModel):
    title: str
    album_id: int
