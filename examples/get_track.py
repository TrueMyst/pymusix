import os
from pymusix import PyMusix
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("SCLIENT_ID")
CLIENT_SECRET = os.getenv("SCLIENT_SECRET")
USER_TOKEN = os.getenv("MXM_USER")

track = PyMusix()
track.set_secrets(CLIENT_ID, CLIENT_SECRET, USER_TOKEN)
track.search_track(
    q_name="Romantic Homicide",
    q_artist="d4vd",
    q_url="https://open.spotify.com/track/1tuSpba0RXUMubHpAOWlMN?si=c0c46da27a824120",
)

print("Track name:", track.track_name)
print("Track artist:", track.track_artist)
print("Track published:", track.track_published)
print("Track duration:", track.track_duration)
print("Album name:", track.album_name)
print("Spotify url:", track.spotify_url)
print("Spotify uri:", track.spotify_uri)
print("Spotify image:", track.spotify_image)
print("Track lyrics:", track.track_lyrics)
print("Track language:", track.track_language)
print("Is Nsfw:", track.is_explicit)
print("Is Instrumental:", track.is_instrumental)
print("Lyrics url:", track.lyrics_url)
print("Snippet:", track.snippet)
print("Primary genre:", track.primary_genre)
print("Secondary genre:", track.secondary_genre)
