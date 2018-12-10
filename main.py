# import pyechonest
import spotipy
import spotipy.util as utility
import sys
import os
import webbrowser
import json
from json.decoder import JSONDecodeError

# username = sys.argv[1]
clientId = "ce7456ff192c41a28dd9b8bc55bb845c"
secret = "55bbc589f0d64cd0b711b309320c5f98"
scope = "user-library-read playlist-read-private playlist-modify-private playlist-read-collaborative playlist-modify-public"
redirectURI = 'http://google.com/'
username = 'ahmadaram34'

# this gets the authentiaction token for us to access the account through spotify
try:
    token = utility.prompt_for_user_token(username=username, scope=scope, client_id=clientId, client_secret=secret,
                                          redirect_uri=redirectURI)
except:
    token = utility.prompt_for_user_token(username)

# craeting spotify object

Spotifyobj = spotipy.Spotify(auth=token)

user = Spotifyobj.current_user()
print(user)
# print(json.dump(user, sort_keys=True, indent=4))


# going to add some bad music that i dont like into a playlist we made called BadMusic
sourcePlaylist = Spotifyobj.user_playlist(username, "37i9dQZF1DWTcqUzwhNmKv")
tracks = sourcePlaylist["tracks"]
songs = tracks["items"]

while tracks['next']:
    tracks = Spotifyobj.next(tracks)
    for item in tracks["items"]:
        songs.append(item)
ids = []

print(len(songs))
print(songs[0]['track']['id'])
i = 0
for i in range(len(songs)):
    Spotifyobj.user_playlist_add_tracks(username, "4SVPwFqykhFf5fqiIIBc21", [songs[i]["track"]["id"]])
