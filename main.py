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
# print(json.dump(user, sort_keys=True, indent=4))


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
        i=0
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
        i=0
        for i in range(len(songs)):
            Spotifyobj.user_playlist_add_tracks(username,goodPlaylistId,[songs[i]["track"]["id"]])
def getGoodSongsIdFeatures():
    goodPlaylist = Spotifyobj.user_playlist(username,goodPlaylistId)

    good_trackList = goodPlaylist["tracks"]
    good_songList = good_trackList["items"]
    while good_trackList['next']:
        good_trackList = Spotifyobj.next(good_trackList)
        for item in good_trackList["items"]:
            good_songList.append(item)
    goodSongIDs = []
    for i in range(len(good_songList)-500):
        goodSongIDs.append(good_songList[i]['track']['id'])
    print(goodSongIDs)

    goodsongFeatures = []
    for i in range(0,len(goodSongIDs)):

#add_to_bad_playlist()
#add_to_good_playlist()
getGoodSongsIdFeatures()



