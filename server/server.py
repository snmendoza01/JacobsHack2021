from flask import Flask
from flask import render_template
from flask import request
from flask_cors import CORS, cross_origin
import json
from requests.models import RequestEncodingMixin
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import numpy as np
import pandas as pd
import requests
# import optimizing_func
import seaborn as sns
from tqdm import tqdm
import warnings
sns.set()
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from songRecomender import SongRecom
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

#The function Julian Made
def getAudioFeatures(songID):
    cid = '4bb4bbafa39540db902e05b2e0d60b6a'
    secret = 'be8a2b6a8d554bacac4f8117db6e2ee4'

    authUrl = 'https://accounts.spotify.com/api/token'
    baseUrl = 'https://api.spotify.com/v1/'

    authResponse = requests.post(authUrl, {
        'grant_type' : 'client_credentials',
        'client_id' : cid,
        'client_secret' : secret
    })

    # print(authResponse)

    authResponseData = authResponse.json()

    accessToken = authResponseData['access_token']

    # print(accessToken)

    headers = {'Authorization': 'Bearer {token}'.format(token=accessToken)}

    response = requests.get(baseUrl + 'audio-features/' + songID, headers=headers)

    # print(response)

    response = response.json()

    # print(json.dumps(response))
    return json.dumps(response)

def getNameOfSong(songID):
    cid = '4bb4bbafa39540db902e05b2e0d60b6a'
    secret = 'be8a2b6a8d554bacac4f8117db6e2ee4'

    authUrl = 'https://accounts.spotify.com/api/token'
    baseUrl = 'https://api.spotify.com/v1/'

    authResponse = requests.post(authUrl, {
        'grant_type' : 'client_credentials',
        'client_id' : cid,
        'client_secret' : secret
    })

    # print(authResponse)

    authResponseData = authResponse.json()

    accessToken = authResponseData['access_token']

    # print(accessToken)

    headers = {'Authorization': 'Bearer {token}'.format(token=accessToken)}

    response = requests.get(baseUrl + 'tracks/' + songID, headers=headers)

    # print(response)

    response = response.json()

    # print(json.dumps(response))
    return response["name"]  


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
@cross_origin()
def hello_world():
    return render_template('index.html')

@app.route("/search", methods=['POST'])
@cross_origin()
def search():
    search = request.json
    print (search)
    cid = '4bb4bbafa39540db902e05b2e0d60b6a'
    secret = 'be8a2b6a8d554bacac4f8117db6e2ee4'
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    artist_name = []
    track_name = []
    popularity = []
    track_id = []

    file = open("output.txt", 'w')

    track_results = sp.search(q=search["search"], type='track', limit=5)
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])

    file.write(json.dumps(track_results))

    songs = []

    for i in range(0,5):
        song = {
            "artist" : artist_name[i],
            "track_name" :  track_name[i],
            "track_id" : track_id[i],
            "popularity" : popularity[i]
        }
        songs.append(song)

    return json.dumps(songs)

@app.route("/predictSongs", methods=['POST'])
@cross_origin()
def predictSong():
    print("here")
    print(type(request.json))
    print(request.json)
    choosenSongs = request.json["data"]
    print("here")
    nameOfSong = getNameOfSong(choosenSongs[0])
    print("The name of the song is:" + nameOfSong)
    spoti = pd.read_csv("spotify.csv", encoding='utf-8', quotechar='"')
    print(spoti.head(3))
    print(spoti.shape)
    print(type(spoti))

    song_name = spoti["song_name"]
    print(song_name.head(3))


    print(song_name.shape)
    print(song_name.isnull().values.any())
    print(song_name)

    song_name = song_name.values.reshape(-1,1)
    print("song_name reshape")
    song_name.shape
    print("song_name shape")

    from sklearn.impute import SimpleImputer
    imr = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
    imr = imr.fit(song_name)
    imputed_data = imr.transform(song_name)
    song_name = pd.DataFrame(imputed_data)
    song_name = song_name.rename(columns={0:"Song-Names"})
    song_name.head(3)

    print(song_name.head(3))



    core = spoti[["genre","mode","duration_ms"]]
    # print(core.dtypes)
    # print(core.head())

    core.dtypes


    core["genre"].value_counts()

    core = core.replace({"genre":{"Underground Rap":0, "Dark Trap":1, "Hiphop":2, "trance":3, "trap":4, "techhouse":5, "dnb":6, "psytrance": 7, "techno":8, "hardstyle":9, "RnB":10, "Trap Metal":11, "Rap":12, "Emo":13, "Pop":14}})

    from sklearn.decomposition import NMF
    nmf = NMF(n_components = 6) #creates NMF model
    nmf_features = nmf.fit_transform(core) #Learn a NMF model for the data X and returns the transformed data.

    print(nmf)

    from sklearn.preprocessing import normalize
    norm_features = normalize(nmf_features)
    current_music = norm_features[23,:]
    similarities = norm_features.dot(current_music)

    closestSong = ""
    df = pd.DataFrame(norm_features)
    x = df.join(song_name)
    df = pd.pivot_table(x, x[[0,1,2,3,4,5]],["Song-Names"])#for indexing song_name to our df
    def current_music(value):
        print("Top 5 recommendations for given music are:")
        print(df)
        value = df.loc[value]
        print(value)
        similarities = df.dot(value)
        print("xxxxxxxxxx")
        print(similarities.idxmax())
        closestSong = format(similarities.idxmax())
        return closestSong

    a = current_music(nameOfSong)

    print(closestSong)
    print(type(closestSong))
    print(closestSong)



    return a











    
    # choosenSongsWithAudioFeatures = []
    # for x in choosenSongs:
    #     print(x)
    #     choosenSongsWithAudioFeatures.append(getAudioFeatures(x))
    #     print(getAudioFeatures(x))
    # recommender = SongRecom("spotify.csv", choosenSongsWithAudioFeatures)
    # recommender.recommend()
    # return 'twat%S'

   

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
    