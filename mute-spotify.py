import spotipy
import spotipy.util as util
import osascript
import time

username = "<SPOTIFY-USERNAME>"
clientID = "<CLIENT-ID>"
clientSecret = "<CLIENT-TOKEN>"
spotifyRedirection = "https://mayurbhoi.com/"
appScope = "user-read-currently-playing user-modify-playback-state"


def createSpotifyObj(username, appScope, clientID, clientSecret, spotifyRedirection):
    token = util.prompt_for_user_token(username, appScope, clientID, clientSecret, spotifyRedirection)
    return spotipy.Spotify(auth=token)

def mute(shouldMute):
    volumeLevel = osascript.osascript("output volume of(get volume settings)")
    if shouldMute:
        osascript.osascript("set volume output volume 0")
        print("Ad encountered. Spotify muted.")

    else:
        osascript.osascript(f"set volume output volume {volumeLevel}")
        print("Not an ad. Songs will play!")

def main():

    sobj = createSpotifyObj(username, appScope, clientID, clientSecret, spotifyRedirection)
    try:
        track = sobj.current_user_playing_track()
    except:
        print("Token error")
        sobj = createSpotifyObj(username, appScope, clientID, clientSecret, spotifyRedirection)
        track = sobj.current_user_playing_track()


    try: 
        if track['currently_playing_type'] == 'ad':
            mute(True)
        else:
            mute(False)
    except:
        print("OS interface error")


if __name__ == "__main__":
    sobj = createSpotifyObj(username, appScope, clientID, clientSecret, spotifyRedirection)

    print("Process initiated")
    print("Process running in background")

    while(True):
        main()
        time.sleep(0.5)

