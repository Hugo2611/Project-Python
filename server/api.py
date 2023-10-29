from fastapi import FastAPI, HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from . import models, database

app = FastAPI()

# Function to get a database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create an artist
@app.post("/artists/", response_model=models.Artist)
def create_artist(artist: models.ArtistCreate, db: Session = Depends(get_db)):
    db_artist = models.Artist(**artist.dict())
    db.add(db_artist)
    db.commit()
    db.refresh(db_artist)
    return db_artist

# Get a list of all artists
@app.get("/artists/", response_model=list[models.Artist])
def list_all_artists(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    artists = db.query(models.Artist).offset(skip).limit(limit).all()
    return artists

# Create an album
@app.post("/albums/", response_model=models.Album)
def create_album(album: models.AlbumCreate, db: Session = Depends(get_db)):
    db_album = models.Album(**album.dict())
    db.add(db_album)
    db.commit()
    db.refresh(db_album)
    return db_album

# Get a list of all albums
@app.get("/albums/", response_model=list[models.Album])
def list_all_albums(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    albums = db.query(models.Album).offset(skip).limit(limit).all()
    return albums

# Create a track
@app.post("/tracks/", response_model=models.Track)
def create_track(track: models.TrackCreate, db: Session = Depends(get_db)):
    db_track = models.Track(**track.dict())
    db.add(db_track)
    db.commit()
    db.refresh(db_track)
    return db_track

# Get a list of all tracks
@app.get("/tracks/", response_model=list[models.Track])
def list_all_tracks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tracks = db.query(models.Track).offset(skip).limit(limit).all()
    return tracks

# Search for an artist by name
@app.get("/artists/search/")
def search_artist(name: str, db: Session = Depends(get_db)):
    artists = db.query(models.Artist).filter(models.Artist.name.ilike(f"%{name}%")).all()
    return artists
