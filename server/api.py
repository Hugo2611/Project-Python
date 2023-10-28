# api.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import database, models

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route racine
@app.get("/")
def read_root():
    return {"message": "Welcome to the Chinook API"}

@app.get("/artists/")
def get_artists_by_name(name: str, db: Session = Depends(get_db)):
    artists = db.query(models.Artist).filter(models.Artist.name.contains(name)).all()
    return artists

@app.get("/albums/")
def get_albums_by_artist_id(artist_id: int, db: Session = Depends(get_db)):
    albums = db.query(models.Album).filter(models.Album.artist_id == artist_id).all()
    return albums

@app.get("/tracks/")
def get_tracks_by_album_id(album_id: int, db: Session = Depends(get_db)):
    tracks = db.query(models.Track).filter(models.Track.album_id == album_id).all()
    return tracks

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
