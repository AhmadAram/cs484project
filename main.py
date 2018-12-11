# import pyechonest
import spotipy
import spotipy.util as utility
import sys
import os
import webbrowser
import json
from json.decoder import JSONDecodeError
import pandas as pd
import matplotlib.pyplot as plt
import pickle

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as panda
from sklearn.neighbors import KNeighborsClassifier

# username = sys.argv[1]
from sklearn.tree import DecisionTreeClassifier

clientId = "ce7456ff192c41a28dd9b8bc55bb845c"
secret = "55bbc589f0d64cd0b711b309320c5f98"
scope = "user-library-read playlist-read-private playlist-modify-private playlist-read-collaborative playlist-modify-public"
redirectURI = 'http://google.com/'
username = 'ahmadaram34'
badPlaylistId = '50U9rtNbvgVVzj3ujj3W6E'
goodPlaylistId = '6UWatUup3LEpGIlQWyXz2N'

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
    badMusic = ["37i9dQZF1DX1lVhptIYRda","5YSpQCyxpQ84Jv9AedJMBQ"]
    for playlist in badMusic:
        sourcePlaylist = Spotifyobj.user_playlist(username, playlist)
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
            Spotifyobj.user_playlist_add_tracks(username, badPlaylistId, [songs[i]["track"]["id"]])


def add_to_good_playlist():
    goodMusic = {"37i9dQZEVXbLRQDuF5jeBp"}

    for playlist in goodMusic:
        sourcePlaylist = Spotifyobj.user_playlist(username, playlist)
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
            Spotifyobj.user_playlist_add_tracks(username, goodPlaylistId, [songs[i]["track"]["id"]])


def getGoodSongsIdFeatures():
    goodPlaylist = Spotifyobj.user_playlist(username, goodPlaylistId)

    good_trackList = goodPlaylist["tracks"]
    good_songList = good_trackList["items"]
    while good_trackList['next']:
        good_trackList = Spotifyobj.next(good_trackList)
        for item in good_trackList["items"]:
            good_songList.append(item)
    goodSongIDs = []
    for i in range(len(good_songList)):
    #for i in range(len(good_songList) - 500):
        goodSongIDs.append(good_songList[i]['track']['id'])
    print(goodSongIDs)

    features = []
    for i in range(0, len(goodSongIDs)):
        audiofeatures = Spotifyobj.audio_features(goodSongIDs[i:i + 50])
        for track in audiofeatures:
            features.append(track)
            features[-1]['target'] = 1
    print(features)
    return features

    #print(features)
def bad_playlist_idsFeatures():
    tracks = Spotifyobj.user_playlist(username, badPlaylistId)['tracks']
    songs = tracks['items']
    # songs = [[x for x in tracks['items']] for y in tracks['next']]
    while tracks['next']:
        tracks = Spotifyobj.next(tracks)
        songs += [x for x in tracks['items']]
    ids = []
    for i in range(len(songs)):#only need minus
    #for i in range(len(songs) - 500):
        ids.append(songs[i]['track']['id'])
    print(ids)

    features = []
    for i in range(0, len(ids)):
        audiofeatures = Spotifyobj.audio_features(ids[i:i + 50])
        for track in audiofeatures:
            features.append(track)
            features[-1]['target'] = 1
    print(features)
    #print(features)
    return features



def TrainTestClassification(goodSongFeatures,badSongFeatures):
    bad = panda.DataFrame(badSongFeatures)
    good = panda.DataFrame(goodSongFeatures)
    merge = [bad,good]
    trainingData = panda.concat(merge)
    #trainingData = panda.merge(bad,good)

    train,test = train_test_split(trainingData,test_size=0.20)
    features = ["danceability","loudness","valence","acousticness","key"]
    train1 = train[features]
    train2 = train["target"]
    test1 = test[features]
    test2 = test["target"]

    tree = DecisionTreeClassifier(min_samples_split=100)
    decisionTree = tree.fit(train1,train2)
    predict1 = tree.predict(test1)
    accy = accuracy_score(test2,predict1) *100
    print("Accuracy for Decision Tree:",round(accy,1),"%")

    knn = KNeighborsClassifier(3)
    knn.fit(train1,train2)
    knn_pred = tree.predict(test1)
    score = accuracy_score(test2,knn_pred)*100
    print("KNN IS ",round(score,1),"%")



print("ADDING SONGS TO BAD SONGS")
#add_to_bad_playlist()
print("ADDING TO GOOD SONGS")
#add_to_good_playlist()
print("GETTING GOOD SONGS")
goodSongFeatures = getGoodSongsIdFeatures()
print("GETTING BAD SONGS FEATURES")
badSongFeatures = bad_playlist_idsFeatures()
TrainTestClassification(goodSongFeatures,badSongFeatures)




if not os.path.exists('goodFeatures.dat'):
    pickle.dump(goodSongFeatures, open('goodFeatures.dat', 'wb+'))
else:
    goodFeatures = pickle.load(open('goodFeatures.dat', 'rb'))

if not os.path.exists('badFeatures.dat'):
    pickle.dump(badSongFeatures, open('badFeatures.dat', 'wb+'))
else:
    badFeatures = pickle.load(open('badFeatures.dat', 'rb'))

goodFrame = pd.DataFrame(goodSongFeatures)
badFrame = pd.DataFrame(badSongFeatures)

# print(goodFrame)
_,ax = plt.subplots()
ax.set_xlabel('valence')
ax.set_ylabel('features')
ax.set_title(r'Good Song Valence')
plt.hist(goodFrame['valence'])
_, bx = plt.subplots()
bx.set_xlabel('valence')
bx.set_ylabel('features')
bx.set_title(r'Bad Song Valence')
plt.hist(badFrame['valence'])
plt.show()
# goodFrame.plot(x=, y=goodFrame['valence'])
# badFrame.plot()
features = pd.merge(goodFrame, badFrame)
print(features)
