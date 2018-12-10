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

print("Songs Added: " + str(len(songs)))
print(songs[0]['track']['id'])
# add_to_bad_playlist("4SVPwFqykhFf5fqiIIBc21", songs)

# i = 0
# for i in range(len(songs)):
#     Spotifyobj.user_playlist_add_tracks(username,"4SVPwFqykhFf5fqiIIBc21",[songs[i]["track"]["id"]])
    #playlist in this for loop is for the BadMusic Playlist

#adding country music to the BagMusicPlaylist
sourcePlaylist = Spotifyobj.user_playlist(username,"37i9dQZF1DX1lVhptIYRda")
tracks = sourcePlaylist["tracks"]
songs = tracks["items"]

while tracks['next']:
    tracks = Spotifyobj.next(tracks)
    for item in tracks["items"]:
        songs.append(item)
ids = []

print("Songs Added: " + str(len(songs)))
print(songs[0]['track']['id'])
# add_to_bad_playlist("4SVPwFqykhFf5fqiIIBc21", songs)

# i = 0
# for i in range(len(songs)):
#     Spotifyobj.user_playlist_add_tracks(username,"4SVPwFqykhFf5fqiIIBc21",[songs[i]["track"]["id"]])

#adding a bunch of playlists to the BadMusic playlist this is one is called Country Christmas

sourcePlaylist = Spotifyobj.user_playlist(username,"37i9dQZF1DX0MuOvUqmxDz")
tracks = sourcePlaylist["tracks"]
songs = tracks["items"]

while tracks['next']:
    tracks = Spotifyobj.next(tracks)
    for item in tracks["items"]:
        songs.append(item)
ids = []

print("Songs Added: " + str(len(songs)))
print(songs[0]['track']['id'])
# add_to_bad_playlist("4SVPwFqykhFf5fqiIIBc21", songs)

# i = 0
# for i in range(len(songs)):
#     Spotifyobj.user_playlist_add_tracks(username,"4SVPwFqykhFf5fqiIIBc21",[songs[i]["track"]["id"]])

#adding songs to BadMusic playlist this playlist
#playlist: 37i9dQZF1DX8S0uQvJ4gaa

sourcePlaylist = Spotifyobj.user_playlist(username,"37i9dQZF1DX8S0uQvJ4gaa")
tracks = sourcePlaylist["tracks"]
songs = tracks["items"]

while tracks['next']:
    tracks = Spotifyobj.next(tracks)
    for item in tracks["items"]:
        songs.append(item)
ids = []

print("Songs Added: " + str(len(songs)))
print(songs[0]['track']['id'])
# add_to_bad_playlist("4SVPwFqykhFf5fqiIIBc21", songs)

# i = 0
# for i in range(len(songs)):
#     Spotifyobj.user_playlist_add_tracks(username,"4SVPwFqykhFf5fqiIIBc21",[songs[i]["track"]["id"]])

#adding more music to the badMusic playlist
#playlist id: 37i9dQZF1DX0MuOvUqmxDz

sourcePlaylist = Spotifyobj.user_playlist(username,"37i9dQZF1DX0MuOvUqmxDz")
tracks = sourcePlaylist["tracks"]
songs = tracks["items"]

while tracks['next']:
    tracks = Spotifyobj.next(tracks)
    for item in tracks["items"]:
        songs.append(item)
ids = []

print("Songs Added: " + str(len(songs)))
print(songs[0]['track']['id'])
# add_to_bad_playlist("4SVPwFqykhFf5fqiIIBc21", songs)

# i = 0
# for i in range(len(songs)):
#     Spotifyobj.user_playlist_add_tracks(username,"4SVPwFqykhFf5fqiIIBc21",[songs[i]["track"]["id"]])

#adding songs to BadMusic playlist this playlist
#playlist: 37i9dQZF1DWYiR2Uqcon0X

sourcePlaylist = Spotifyobj.user_playlist(username,"37i9dQZF1DWYiR2Uqcon0X")
tracks = sourcePlaylist["tracks"]
songs = tracks["items"]

while tracks['next']:
    tracks = Spotifyobj.next(tracks)
    for item in tracks["items"]:
        songs.append(item)
ids = []

print("Songs Added: {}".format(str(len(songs))))
print(songs[0]['track']['id'])
# add_to_bad_playlist("4SVPwFqykhFf5fqiIIBc21", songs)

# i = 0
# for i in range(len(songs)):
#     Spotifyobj.user_playlist_add_tracks(username, "4SVPwFqykhFf5fqiIIBc21", [songs[i]["track"]["id"]])

def add_to_bad_playlist(playlistId, songs):
    for i in range(len(songs)):
        Spotifyobj.user_playlist_add_tracks(username, playlistId, [songs[i]["track"]["id"]])
