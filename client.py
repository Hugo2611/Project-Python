import requests
from server.api import search_artist, get_albums_by_artist, get_tracks_by_album, create_artist, list_all_artists, List, search_artists_by_name, get_albums_by_artist_id, get_tracks_by_album_id

base_url = "http://localhost:8000"
def list_all_albums():
    response = requests.get(f"{base_url}/albums/")
    return response.json()

def list_all_tracks():
    response = requests.get(f"{base_url}/tracks/")
    return response.json()

if __name__ == "__main__":
    while True:
        choice = input("Choose an option:\n1. Search artist by name\n2. Get albums by artist ID\n3. Get tracks by album ID\n4. Create Artist\n5. List all artists\n6. List all albums\n7. List all tracks\n8. Exit\n")
        
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
            artist_name = input("Enter artist name: ")
            result = create_artist(artist_name)
            print(result)
        elif choice == "5":
            result = list_all_artists()
            print(result)
        elif choice == "6":
            result = list_all_albums()
            print(result)  # Liste des albums
        elif choice == "7":
            result = list_all_tracks()
            print(result)  # Liste des musiques
        elif choice == "8":
            break
