from flask import Flask
from flask import render_template
from flask import request
from flask_cors import CORS, cross_origin
import json
from requests.models import RequestEncodingMixin
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials



app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
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

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
    