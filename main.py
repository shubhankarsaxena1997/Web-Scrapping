# this project will fetch the top 100 songs of the date that you will enter in input from the website www.billboard.com and create a playlist in spotify


import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

billboard_url = "https://www.billboard.com/charts/hot-100/"
date = input("What year you would like to travel to in YYY-MM-DD format: ")
# 2000-08-12

CLIENT_ID = "99272196449c4396941bb9f4ab15ab40"
SECRET_ID = "115554a220594cb6a619e0b716193ed8"
redirect_uri = "http://www.example.com/"
scope = "playlist-modify-private"
username = "Python Test"


response = requests.get(f"{billboard_url}/{date}")
web_page_content = response.text
soup = BeautifulSoup(web_page_content, 'html.parser')
all_songs = soup.select(selector="li h3")

top_songs = []
for single_song in all_songs:
    title = (single_song.getText().replace("\t", "")).replace("\n", "")
    top_songs.append(title)

spotify = spotipy.oauth2.SpotifyOAuth(client_id=CLIENT_ID, client_secret=SECRET_ID, redirect_uri=redirect_uri,
                                      scope=scope)
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=SECRET_ID,
        show_dialog=True,
        cache_path="token.txt"
    )
)

current_user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in top_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")

    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        # pass
        print(f"{song} doesn't exist in Spotify. Skipped.")

create_playlist = sp.user_playlist_create(user=current_user_id, name=f"{date} Billboard 100", public=False)
playlist_id = create_playlist['id']

add_item_playlist = sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
