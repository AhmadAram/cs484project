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
badPlaylistId = '4SVPwFqykhFf5fqiIIBc21'
goodPlaylistId = '4cAyKcVe0iUmFoorM3XpEL'

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

def bad_playlist_ids():
    tracks = Spotifyobj.user_playlist(username, badPlaylistId)['tracks']
    songs = tracks['items']
    # songs = [[x for x in tracks['items']] for y in tracks['next']]
    while tracks['next']:
        tracks = Spotifyobj.next(tracks)
        songs += [x for x in tracks['items']]
    ids = []
    for i in range(len(songs) - 500):
        ids.append(songs[i]['track']['id'])


def add_to_bad_playlist():
    badMusic = ["37i9dQZF1DWTcqUzwhNmKv","37i9dQZF1DX1lVhptIYRda",
                "37i9dQZF1DX0MuOvUqmxDz","37i9dQZF1DX8S0uQvJ4gaa",
                "37i9dQZF1DX0MuOvUqmxDz", "37i9dQZF1DWYiR2Uqcon0X"]
    for playlist in badMusic:
        sourcePlaylist = Spotifyobj.user_playlist(username, playlist)
        tracks = sourcePlaylist["tracks"]
        songs = tracks["items"]
        while tracks["next"]:
            tracks = Spotifyobj.next(tracks)
            for item in tracks["items"]:
                songs.append
        ids = []
        print(len(songs))
        print(songs[0]['track']['id'])
        for i in range(len(songs)):
            Spotifyobj.user_playlist_add_tracks(username,badPlaylistId,[songs[i]["track"]["id"]])

def add_to_good_playlist():
    goodMusic = {"37i9dQZF1DX4dyzvuaRJ0n","37i9dQZF1DX0BcQWzuB7ZO","37i9dQZF1DX8tZsk68tuDw",
                 "37i9dQZF1DX0hvSv9Rf41p","37i9dQZF1DXaXB8fQg7xif","37i9dQZF1DXcZDD7cfEKhW"}

    for playlist in goodMusic:
        sourcePlaylist = Spotifyobj.user_playlist(username, playlist)
        tracks = sourcePlaylist["tracks"]
        songs = tracks["items"]
        while tracks["next"]:
            tracks = Spotifyobj.next(tracks)
            for item in tracks["items"]:
                songs.append
        ids = []
        print(len(songs))
        print(songs[0]['track']['id'])
        for i in range(len(songs)):
            Spotifyobj.user_playlist_add_tracks(username,goodPlaylistId,[songs[i]["track"]["id"]])

##FUNCTION ABOVE ADDS BAD SONGS FUNCTION BELOW ADDS GOOD SONGS


def addGoodSongs():
    ######THIS PORTION WILL ADD GOOD PLAYLISTS TO THE GOODPLAYLIST playlist, and once this is done we compare them
    # mint playlist id : 37i9dQZF1DX4dyzvuaRJ0n
    # GoodPlaylist id is : 4cAyKcVe0iUmFoorM3XpEL
    # Bass Arcade ID : 37i9dQZF1DX0hvSv9Rf41p
    # Dance Rewind Playlist ID: 37i9dQZF1DX0BcQWzuB7ZO
    # Night Rider Playlist ID: 37i9dQZF1DX6GJXiuZRisr
    goodPlaylistIds = []
    goodPlaylistIds.append("37i9dQZF1DX4dyzvuaRJ0n")
    goodPlaylistIds.append("37i9dQZF1DX0hvSv9Rf41p")
    goodPlaylistIds.append("37i9dQZF1DX0BcQWzuB7ZO")
    goodPlaylistIds.append("37i9dQZF1DX6GJXiuZRisr")
    goodPlaylistIds.append("4cAyKcVe0iUmFoorM3XpEL")

    for x in range(len(goodPlaylistIds)):
        sourcePlaylist = Spotifyobj.user_playlist(username,goodPlaylistIds[x])
        tracks = sourcePlaylist["tracks"]
        songs = tracks["items"]

        while tracks['next']:
            tracks = Spotifyobj.next(tracks)
            for item in tracks["items"]:
                songs.append(item)
        ids = []

        print("Songs Added to Good Songs: {}".format(str(len(songs))))
        print(songs[0]['track']['id'])
        i = 0
        for i in range(len(songs)):
            Spotifyobj.user_playlist_add_tracks(username, "4cAyKcVe0iUmFoorM3XpEL", [songs[i]["track"]["id"]])


addGoodSongs()

#add_to_bad_playlist()
add_to_good_playlist()
