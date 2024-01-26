import os
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
USER_TOKEN = os.getenv("MUSIXMATCH_USER_TOKEN")


class PyMusix:
    def __init__(self, q_name, q_artist=None, q_uri=None):
        self.__q_name = q_name
        self.__q_artist = q_artist
        self.__q_uri = q_uri

        # Initialize properties with None values
        self.track_name = None
        self.track_artist = None
        self.track_published = None
        self.track_duration = None
        self.album_name = None
        self.spotify_url = None
        self.spotify_uri = None
        self.spotify_image = None
        self.track_lyrics = None
        self.track_language = None
        self.is_nsfw = None
        self.is_instrumental = None
        self.lyrics_url = None
        self.snippet = None
        self.primary_genre = None
        self.secondary_genre = None

        # Automatically call these methods upon instance creation
        self.__search_track()
        self.__get_lyrics()

    def __get_spotify_token(self):
        # Use a meaningful name for the method
        endpoint = "https://accounts.spotify.com/api/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        payload = {
            "grant_type": "client_credentials",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        }
        response = requests.post(endpoint, headers=headers, params=payload)
        token = response.json()["access_token"]
        return token

    def __authorization_header(self, token: str):
        return {"Authorization": f"Bearer {token}"}

    def __search_track(self):
        endpoint = "https://api.spotify.com/v1"
        header = self.__authorization_header(self.__get_spotify_token())

        query_params = {"q": self.__q_name, "type": "track", "limit": 1}
        track_data = requests.get(
            f"{endpoint}/search", params=query_params, headers=header
        ).json()
        selected_track = track_data.get("tracks", {}).get("items", [])[0]

        if selected_track:
            self.track_name = selected_track["name"]
            self.track_artist = selected_track["album"]["artists"][0]["name"]
            self.album_name = selected_track["album"]["name"]
            self.track_published = selected_track["album"]["release_date"]
            self.track_duration = f"{selected_track['duration_ms'] // 60000:02d}:{(selected_track['duration_ms'] // 1000 % 60):02d}"
            self.spotify_url = selected_track["album"]["external_urls"].get("spotify")
            self.spotify_uri = selected_track.get("id")
            self.spotify_image = selected_track["album"]["images"][0].get("url")

    def __get_lyrics(self):
        base_url = "https://apic-desktop.musixmatch.com/ws/1.1/macro.subtitles.get?format=json&namespace=lyrics_synched&subtitle_format=mxm&app_id=web-desktop-app-v1.0&"

        params = {
            "q_track": self.__q_name,
            "q_artist": "" if not self.__q_artist else self.__q_artist,
            "track_spotify_id": self.spotify_uri if not self.__q_uri else self.__q_uri,
            "usertoken": USER_TOKEN,
        }
        response = requests.get(base_url, params=params).json()
        response = response["message"]["body"]["macro_calls"]

        track_lyrics = response["track.lyrics.get"]["message"]["body"]["lyrics"]
        track_snippet = response["track.snippet.get"]["message"]["body"]["snippet"]
        matcher_track = response["matcher.track.get"]["message"]["body"]["track"]

        self.is_nsfw = track_lyrics["explicit"] == 1
        self.is_instrumental = track_lyrics["instrumental"] == 1
        self.track_lyrics = track_lyrics["lyrics_body"]
        self.language = track_lyrics["lyrics_language"]
        self.lyrics_url = track_lyrics["backlink_url"].split("?")[0]
        self.snippet = track_snippet["snippet_body"]
        self.primary_genre = matcher_track["primary_genres"]["music_genre_list"][0][
            "music_genre"
        ]["music_genre_name"]
        self.secondary_genre = (
            None
            if len(matcher_track["secondary_genres"]["music_genre_list"]) == 0
            else matcher_track["secondary_genres"]["music_genre_list"][0][
                "music_genre"
            ]["music_genre_name"]
        )
