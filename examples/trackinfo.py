# --------------------------------------
__import__("sys").path.append("../pymusix/")

# This snippet above is intended for addressing import issues and testing purposes.
# Please refrain from including it in your final script.
# --------------------------------------

import os
from dotenv import load_dotenv
from pymusix import PyMusix

load_dotenv()

CLIENT_ID = os.getenv("SCLIENT_ID")
CLIENT_SECRET = os.getenv("SCLIENT_SECRET")
USER_TOKEN = os.getenv("MXM_USER")

track = PyMusix()
track.set_secrets(CLIENT_ID, CLIENT_SECRET, USER_TOKEN)

print("\n-------------- 📑 Track Info --------------")

name = input("Type out the song name: ")
artist = input("And yeah, the artist: ")

track.search_track(
    q_name=name,
    q_artist=artist,
)

print("Track name:", track.name)
print("Track artist:", track.artist)
print("Track published:", track.published)
print("Track duration:", track.duration)
print("Album name:", track.album_name)
print("Spotify URL:", track.spotify_url)
print("Spotify URI:", track.spotify_uri)
print("Spotify image:", track.spotify_banner)
print("Track language:", track.language)
print("Is Nsfw:", track.is_explicit)
print("Is Instrumental:", track.is_instrumental)
print("Snippet:", track.snippet)
print("Primary genre:", track.primary_genre)
print("Secondary genre:", track.secondary_genre)
