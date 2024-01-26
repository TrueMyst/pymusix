## Overview

PyMusix is a Python package designed to retrieve information about a song, including details like the artist, album, release date, genres, and lyrics. The package utilizes the Spotify and Musixmatch APIs to gather this information.

## Installation

To install PyMusix from GitHub, follow these steps:

1.  Clone the GitHub repository to your local machine:
    
	```bash
	git clone https://github.com/your_username/pymusix.git
	cd pymusix 
	```

2. Install the required dependencies:
    
    ```bash
   pip install -r requirements.txt
    ```

3. Set up the environment variables by creating a `.env` file in the [project root](https://github.com/TrueMyst/pymusix/tree/main/pymusix). The file should contain the following:

	```bash
	SPOTIFY_CLIENT_ID=your_spotify_client_id
	SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
	MUSIXMATCH_USER_TOKEN=your_musixmatch_user_token
	```
Obtain the Spotify client ID and client secret from the [Spotify Developer Dashboard](https://developer.spotify.com/).
 For the Musixmatch user token, you can follow the guide [here](https://github.com/khanhas/genius-spicetify#musicxmatch).
    
You are now ready to use PyMusix!

## Usage

To use PyMusix, instantiate the `PyMusix` class with the desired song details. The class will fetch information from Spotify and Musixmatch APIs and provide various attributes with the song details.

Example:

```python
from pymusix import PyMusix

song_info = PyMusix(q_name="Song Name", q_artist="Artist Name")
print("Track Name:", song_info.track_name)
print("Artist:", song_info.track_artist)
print("Lyrics:", song_info.track_lyrics)
# ... and more
```

## Contributions

Contributions to PyMusix are welcomed! Feel free to fork the repository, make improvements, and submit pull requests. If you encounter any issues or have suggestions, please open an issue on GitHub.

Happy coding with PyMusix! 🎶
