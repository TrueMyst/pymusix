import re
import requests
from typing import Optional


class PyMusix:
    """
    A PyMusix class, lets you retrieve information about a song track.

    Attributes
    ----------
    name: str
        The track's name.

    artist: str
        The track's artist.

    published: str
        Published date of the track.

    duration: str
        Duration of the track.

    album_name: str
        Name of the track's album.

    spotify_url: str
        Spotify URL for the track.

    spotify_uri: str
        Spotify URI for the track.

    spotify_banner: str
        Cover image URL for the track.

    lyrics: str
        Lyrics of the track.

    lyrics_url: str
        URL for the track's lyrics.

    language: str
        Language of the track.

    is_explicit: bool
        Checks if the song is NSFW.

    is_instrumental: bool
        Checks if the track is instrumental.

    snippet: str
        A small snippet from the lyrics.

    primary_genre: str
        Primary genre of the track.

    secondary_genre: str
        Secondary genre of the track.
    """

    def __init__(self):
        # Set Token
        self.__SCLIENT_ID = None
        self.__SCLIENT_SECRET = None
        self.__MXM_USERTOKEN = None

        # Initialize properties with None values
        self.name = None
        self.artist = None
        self.published = None
        self.duration = None
        self.album_name = None
        self.spotify_url = None
        self.spotify_uri = None
        self.spotify_banner = None
        self.lyrics = None
        self.lyrics_url = None
        self.language = None
        self.is_explicit = None
        self.is_instrumental = None
        self.snippet = None
        self.primary_genre = None
        self.secondary_genre = None

    def set_secrets(self, SCLIENT_ID, SCLIENT_SECRET, MXM_USERTOKEN):
        """
        Set secrets for better search results.

        Parameters
        ----------
        SCLIENT_ID
            Spotify Client ID

        SCLIENT_SECRET
            Spotify Client Secret

        MXM_USERTOKEN
            Musixmatch User Token (Not API Token)
        """
        self.__SCLIENT_ID = SCLIENT_ID
        self.__SCLIENT_SECRET = SCLIENT_SECRET
        self.__MXM_USERTOKEN = MXM_USERTOKEN

    def __get_uri(self, url: str) -> str:
        """
        Returns the URI from a Spotify track link

        Parameters
        ----------
        url: str
            Spotify track URL

        Returns
        -------
        match: str
            Spotify track URI
        """
        pattern = re.compile(r"https://open\.spotify\.com/track/(\w+)")
        match = pattern.findall(url)[0] if pattern.findall(url) else ""

        return match

    def __get_spotify_token(self):
        """
        Authenticates with Spotify's Web API and returns a token

        Returns
        -------
        token: str
            Returns the app token that will be used for retrieving track information
        """
        endpoint = "https://accounts.spotify.com/api/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        payload = {
            "grant_type": "client_credentials",
            "client_id": self.__SCLIENT_ID,
            "client_secret": self.__SCLIENT_SECRET,
        }
        response = requests.post(endpoint, headers=headers, params=payload)
        token = response.json()["access_token"]
        return token

    def __authorization_header(self, token: str):
        """
        Returns the Authorization with the Bearer token
        """
        return {"Authorization": f"Bearer {token}"}

    def search_track(
        self, q_name: str, q_artist: Optional[str] = None, q_url: Optional[str] = None
    ):
        """
        Searches for the desired track

        Parameters
        ----------
        q_name: str
            The name of the song track

        q_artist: Optional[str]
            The artist of the song track

        q_url: Optional[str]
            The Spotify track link
        """
        spotify_endpoint = "https://api.spotify.com/v1/search"
        mxm_endpoint = "https://apic-desktop.musixmatch.com/ws/1.1/macro.subtitles.get?"

        spotify_header = self.__authorization_header(self.__get_spotify_token())
        spotify_params = {
            "q": f"{q_name} - {q_artist}" if q_artist != None else q_name,
            "type": "track",
            "limit": 1,
        }
        track_data = requests.get(
            f"{spotify_endpoint}", params=spotify_params, headers=spotify_header
        ).json()

        selected_track = track_data.get("tracks", {}).get("items", [])[0]

        if selected_track:
            self.name = selected_track["name"]
            self.artist = selected_track["album"]["artists"][0]["name"]
            self.album_name = selected_track["album"]["name"]
            self.published = selected_track["album"]["release_date"]
            self.duration = f"{selected_track['duration_ms'] // 60000:02d}:{(selected_track['duration_ms'] // 1000 % 60):02d}"
            self.spotify_url = selected_track["album"]["external_urls"].get("spotify")
            self.spotify_uri = selected_track.get("id")
            self.spotify_banner = selected_track["album"]["images"][0].get("url")

        q_uri = self.__get_uri(q_url) if q_url != None else ""

        mxm_params = {
            "format": "json",
            "namespace": "lyrics_synched",
            "app_id": "web-desktop-app-v1.0",
            "subtitle_format": "mxm",
            "q_track": self.name,
            "q_artist": self.artist,
            "track_spotify_id": q_uri if q_uri is not None else self.spotify_uri,
            "usertoken": self.__MXM_USERTOKEN,
        }

        mxm = requests.get(mxm_endpoint, params=mxm_params)
        mxm = mxm.json()["message"]["body"]["macro_calls"]

        track_lyrics = mxm["track.lyrics.get"]["message"]["body"]["lyrics"]
        track_snippet = mxm["track.snippet.get"]["message"]["body"]["snippet"]
        matcher_track = mxm["matcher.track.get"]["message"]["body"]["track"]

        self.is_explicit = track_lyrics["explicit"] == 1
        self.is_instrumental = track_lyrics["instrumental"] == 1
        self.lyrics = track_lyrics["lyrics_body"]
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
