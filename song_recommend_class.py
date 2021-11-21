import numpy as np
import pandas as pd
import requests
# import optimizing_func
import requests
import json
import seaborn as sns
from tqdm import tqdm
import warnings
sns.set()
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

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


#Class containig array of songs, along with method to compute the recommendation
class SongRecom():
    
    def __init__(self,data_file):
        self.size = 0
        self.song_list = []
        self.df = pd.read_csv(data_file)
        
    #Appends the sound properties of the song to the song list 
    #Input value: array of the id of each songs
    #Return value: Void  
    def get_initial_data(self, id_arr):
        self.size = len(id_arr)
        for i in range(0,len(id_arr)):
            self.song_list.append(json.loads(getAudioFeatures(id_arr[i])))
            
        
        
    #Calculates average between all the properties
    #Input Values: None
    #Return Value: Dictionary    
    def calc_average(self):
        avg = self.song_list[0].copy()
        keys = list(self.song_list[0].keys())
        for i in range(0,len(keys)):
            if(type(self.song_list[0][keys[i]]) != str):
                avg[keys[i]] = 0
                for j in range(0,self.size):
                    avg[keys[i]] = avg[keys[i]]+self.song_list[j][keys[i]]
                avg[keys[i]] = float(avg[keys[i]]/self.size)
        return avg
    
    def normalize_data(self):
        #Normalizing all the numerical columns using MinMaxScalar
        newdf = self.df.copy()
        datatypes = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        normalization = self.df.select_dtypes(include=datatypes)
        for col in normalization.columns:
            MinMaxScaler(col)
        kmeans = KMeans(n_clusters=10)
        features = kmeans.fit_predict(normalization)
        newdf['features'] = features
        MinMaxScaler(newdf['features'])
        return normalization


    
    def recommend(self, amount=1):
        distance = []
        song = self.calc_average()
        rec = self.df[self.df['id'] != self.song_list[0]['id']]
        for elem in tqdm(rec.values):
            d = 0.
            for col in np.arange(len(rec.columns)):
                if not col in [1, 6, 12, 14, 18]:
                    print(np.absolute(float(song[col])))
                    d = d + np.absolute(float(song[col]) - float(elem[col]))
            distance.append(d)
        rec['distance'] = distance
        rec = rec.sort_values('distance')
        columns = ['artists', 'name']
        return rec[columns][:amount]   
    

arr = ['6ERvoKmAcsxZ4h1FVM69N8', '0rNLaGUleZ91DXMxmZNq5v']

my_obj = SongRecom('spotify_data.csv')
my_obj.get_initial_data(arr)
avg = my_obj.calc_average()
songs = my_obj.recommend()
print(songs)




        
        

