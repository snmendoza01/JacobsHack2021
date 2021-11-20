from flask import Flask
from flask import render_template
from flask import request
from flask_cors import CORS, cross_origin
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials



app = Flask(__name__)
cors = CORS(app)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/search", methods=['POST'])
def search():
    cid = '4bb4bbafa39540db902e05b2e0d60b6a'
    secret = 'be8a2b6a8d554bacac4f8117db6e2ee4'
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    search = request.form['search']
    print("user searched for:"+ search)
    artist_name = []
    track_name = []
    popularity = []
    track_id = []
    for i in range(0,10000,50):
        track_results = sp.search(q='name:2018', type='track', limit=50,offset=i)
        print(track_results)
        # for i, t in enumerate(track_results['tracks']['items']):
        #     artist_name.append(t['artists'][0]['name'])
        #     track_name.append(t['name'])
        #     track_id.append(t['id'])
        #     popularity.append(t['popularity'])
    for x in track_name:
        print(x)
    return "got the gest request"

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
    