# --------------------------------------
# This snippet below is intended for addressing import issues and testing purposes.
# Please refrain from including it in your final script.
__import__("sys").path.append("../pymusix/")
# --------------------------------------

import os
from dotenv import load_dotenv
from pymusix import PyMusix

load_dotenv()

CLIENT_ID = os.getenv("SCLIENT_ID")
CLIENT_SECRET = os.getenv("SCLIENT_SECRET")
USER_TOKEN = os.getenv("MXM_USER")

song = PyMusix()
song.set_secrets(CLIENT_ID, CLIENT_SECRET, USER_TOKEN)

print("\n---------------- ✨ Lyrics ----------------")
name = input("Type out the song name: ")
artist = input("And yeah, the artist: ")

song.search_track(
    q_name=name,
    q_artist=artist,
)

print(song.lyrics)
