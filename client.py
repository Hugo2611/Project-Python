# client.py
import requests

base_url = "http://localhost:8000"

def search_artists_by_name(name):
    response = requests.get(f"{base_url}/artists/?name={name}")
    return response.json()

def get_albums_by_artist_id(artist_id):
    response = requests.get(f"{base_url}/albums/?artist_id={artist_id}")
    return response.json()

def get_tracks_by_album_id(album_id):
    response = requests.get(f"{base_url}/tracks/?album_id={album_id}")
    return response.json()

if __name__ == "__main__":
    while True:
        choice = input("Choose an option:\n1. Search artist by name\n2. Get albums by artist ID\n3. Get tracks by album ID\n4. Exit\n")
        
        if choice == "1":
            artist_name = input("Enter artist name: ")
            result = search_artists_by_name(artist_name)
            print(result)
        elif choice == "2":
            artist_id = input("Enter artist ID: ")
            result = get_albums_by_artist_id(artist_id)
            print(result)
        elif choice == "3":
            album_id = input("Enter album ID: ")
            result = get_tracks_by_album_id(album_id)
            print(result)
        elif choice == "4":
            break
