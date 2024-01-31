import os
import pymusix
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("SCLIENT_ID")
CLIENT_SECRET = os.getenv("SCLIENT_SECRET")
USER_TOKEN = os.getenv("MXM_USER")

x = pymusix.PyMusix()
x.token(CLIENT_ID, CLIENT_SECRET, USER_TOKEN)

x.search_track(
    q_name="Romantic Homicide",
    q_artist="d4vd",
    q_url="https://open.spotify.com/track/1tuSpba0RXUMubHpAOWlMN?si=c0c46da27a824120",
)

print("Track name:", x.track_name)
print("Track artist:", x.track_artist)
print("Track published:", x.track_published)
print("Track duration:", x.track_duration)
print("Album name:", x.album_name)
print("Spotify url:", x.spotify_url)
print("Spotify uri:", x.spotify_uri)
print("Spotify image:", x.spotify_image)
print("Track lyrics:", x.track_lyrics)
print("Track language:", x.track_language)
print("Is Nsfw:", x.is_nsfw)
print("Is Instrumental:", x.is_instrumental)
print("Lyrics url:", x.lyrics_url)
print("Snippet:", x.snippet)
print("Primary genre:", x.primary_genre)
print("Secondary genre:", x.secondary_genre)
