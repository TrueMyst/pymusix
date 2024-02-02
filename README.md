<h3 align = "center">
	<img width="750" height="250" src="https://i.imgur.com/jyqlTug.png"><br>
</h3>

<p align="center">🌿 PyMusix, a tool that lets you retrieve information about a song, including details like the <b>artist, album, release date, genres, lyrics</b> and more. Uses Spotify and Musixmatch APIs to gather this information.
</p>

<p align="center">
	<img alt="Maintained" src="https://img.shields.io/badge/Maintained%3F-Yes-%23d7dead?style=for-the-badge&logo=undertale&logoColor=%23d7dead&labelColor=%237d8a27">
	<a href="https://www.pepy.tech/projects/pymusix"><img alt="Pepy Total Downlods" src="https://img.shields.io/pepy/dt/pymusix?style=for-the-badge&logo=9gag&logoColor=%23d7dead&labelColor=%237d8a27&color=%23d7dead"></a>
	<a href="https://pypi.org/project/pymusix/"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/pymusix?style=for-the-badge&logo=python&logoColor=%23d7dead&labelColor=%237d8a27&color=%23d7dead"></a>
	<img alt="GitHub License" src="https://img.shields.io/github/license/TrueMyst/pymusix?style=for-the-badge&logo=gitbook&logoColor=%23d7dead&labelColor=%237d8a27&color=%23d7dead">
</p>

## 📦 Installation

Install the Stable Version of **pymusix** from PyPi:

```bash
# Linux/macOS
python3 -m pip install -U pymusix
```

```bash
# Windows
py -3 -m pip install -U pymusix
```

**OR** Install the Working Version of **pymusix** from Github:

1.  Clone the GitHub repository:

    ```bash
    git clone https://github.com/TrueMyst/pymusix.git
    cd pymusix
    ```

2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

After installing it anyway, set up the environment variables by creating a `.env` file in your root directory. The file should contain the following:

```bash
SPOTIFY_CLIENT_ID = "spotify-client-id"
SPOTIFY_CLIENT_SECRET = "spotify-client-secret"
MUSIXMATCH_USERTOKEN = "musixmatch-usertoken"
```

You can get the Spotify Client ID and Client Secret from the [Spotify Developer Dashboard](https://developer.spotify.com/).
For Musixmatch User Token, you can follow this guide [here](https://github.com/khanhas/genius-spicetify#musicxmatch).

You are now ready to use PyMusix!

## 🤌 How to use?

A basic usage is shown below, for more information, please check out the [examples](https://github.com/TrueMyst/pymusix/examples/) given here.

```python
import os
from dotenv import load_dotenv
from pymusix import PyMusix

load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
USER_TOKEN = os.getenv("MUSIXMATCH_USERTOKEN")

song = PyMusix()

song.set_secrets(CLIENT_ID, CLIENT_SECRET, USER_TOKEN)
song.search_track(q_name = "Pluto Projector", q_artist = "Rex Orange County")

print("Track Name:", song.name)
print("Lyrics:", song.lyrics)
print("Primary Genre:", song.primary_genre)
# ... and more
```

## 🤗 Contributing

Contributions to **pymusix** are welcomed. Feel free to submit your suggestions via pull requests. Your contributions are invaluable in enhancing this tool for everyone.

## 📋 License

🌿 **pymusix** is licensed under the MIT license, which you can find in the LICENSE file.

<br>

<p align="center">
Made with 💜<br>
<b>elysianmyst, 2024</b>
</p>
