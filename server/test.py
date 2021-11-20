import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
cid = '4bb4bbafa39540db902e05b2e0d60b6a'
secret = 'be8a2b6a8d554bacac4f8117db6e2ee4'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist_name = []
track_name = []
popularity = []
track_id = []

file = open("output.txt", 'w')

track_results = sp.search(q='mercury:retrograde', type='track', limit=10)
for i, t in enumerate(track_results['tracks']['items']):
    artist_name.append(t['artists'][0]['name'])
    track_name.append(t['name'])
    track_id.append(t['id'])
    popularity.append(t['popularity'])


file.write(json.dumps(track_results))

for i in range(0,10):
    if(track_name[i] == "All I Want for Christmas Is You"):
        file.write("Fuck you\n")
    else:
        file.write(json.dumps(artist_name[i]))
        file.write(json.dumps(track_name[i]))
        file.write(json.dumps(popularity[i]))
        file.write(json.dumps(track_id[i]))
        file.write("\n")


# for i in range(0,10000,50):
#     track_results = sp.search(q='year:2018', type='track', limit=50,offset=i)
#     