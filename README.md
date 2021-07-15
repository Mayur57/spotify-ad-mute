# Spotify Ad Mute
A simple script that blocks Spotify ads.

### Requirements
- macOS device -> Currently only available for macOS; Windows version will be up soon
- Python 3.8+ -> For the script runtime and interpretation
- osascript -> To execute Applescript commands and change volume of macOS
- spotipy -> Python interface for Spotify Web API
### Installation

1. Install `python3 3.10` from [here](https://www.python.org/)
2. Install `osascript` package using the command `pip3 install --user osascript`
3. Install `spotipy` package using the command `pip3 install --user spotipy`

### Run It
- Edit the script to include all your information (Spotify ID, Client ID, Client Secret) and save it.
- Type `cd <your-directory> && python3 mute-spotify.py` in your terminal.
- When prompted authorise the script in your browser and copy the auth URL opened to the terminal and hit enter.
- If `Process Initiated` shows up in terminal, the script is working in the background. Else, press `CMD+C` and re-run the script using second step.
