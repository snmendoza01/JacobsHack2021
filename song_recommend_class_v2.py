import numpy as np
import pandas as pd
import requests
import requests
import json
import seaborn as sns
from tqdm import tqdm
import torch
sns.set()
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

#Function to obtain audio features from spotify API
#Input value: ID of a song
#Output Value: Json file 
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
    #Initialization function
    #Input: Dataframe to be used and external weights
    def __init__(self,data_file, weights):
        self.size = 0
        self.song_list = []
        self.df = pd.read_csv(data_file)
        self.weights = weights
        
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
        avg = self.song_list[0].copy() #copy function to prevent deep copy
        keys = list(self.song_list[0].keys())
        for i in range(0,len(keys)):
            if(type(self.song_list[0][keys[i]]) != str):
                avg[keys[i]] = 0
                for j in range(0,self.size):
                    avg[keys[i]] = avg[keys[i]]+self.song_list[j][keys[i]]
                avg[keys[i]] = float(avg[keys[i]]/self.size)
        return avg
    
    
    #Normalizing all the numerical columns using MinMaxScalar
    #Return Value: Dataframe
    def normalize_data(self):
        newdf = self.df.copy()
        datatypes = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        normalization = self.df.select_dtypes(include=datatypes)
        for col in normalization.columns:
            MinMaxScaler(col)
        return newdf


    #Uses distance function to find songs with minimal
    #distance under the current metric
    #Input Value: Amount of songs to be calculated
    #Return Value: Array of lists (songs)
    def recommend(self, amount = 1 ):
        
        newdf = self.df #self.normalize_data()
        
        #creates distance array ('distance' between rec and song)
        distance = []
        
        #Song to be used as initial data (dtype = dictionary)
        song = self.calc_average()
        
        #array of dictionaries: all songs except input songs
        rec =  newdf[newdf['id'] != self.song_list[0]['id']] #can be generalized to all songs
       
        #key elements for the song dictionaries
        keys = list(self.df.keys())
        
        #calculating 'distance' between any two songs
        for elem in tqdm(rec.values):
            d = 0.
            for col in np.arange(len(rec.columns)):
                if not col in [1,5, 6,11, 12,13, 14, 18,19 ]:
                    d = d + self.weights[col]*np.absolute(
                        float(song[keys[col]]) - float(elem[col]))
            distance.append(d)
        rec['distance'] = distance
        
        #orders songs by smallest distance
        rec = rec.sort_values('distance')
        columns = ['artists', 'name','id']
        
        #choose amount of songs with the lowest distance
        return rec[columns][:amount]
    
    
    
    #Algorithm to update weight values after receiving feedback from user
    def learning(self, song):
        ##connect with frontend feedback slidebar##
        
        keys = list(self.df.keys())
        learning_rate = 1e-6
        grading = 90 #grading inputed by user
        loss =  1/(grading+10) #computing loss 

        # Backprop to compute gradients of weights with respect to loss
        grad_y= 2.0 * loss
        grad_weights = np.zeros((len(self.weights)))
        for i in range(0,len(self.weights)):
            if not i in [1,5, 6,11, 12,13, 14, 18,19 ]:
                print(song)
                grad_weights[i]= grad_weights[i]*song[keys[i]]
            
            # Update weights using gradient descent
            self.weights[i] -= learning_rate*grad_weights[i]
            

        
############################################################################
#TEST#
arr = ['4g5LUzHFRr4Zlok8KzERmI']

my_obj = SongRecom('spotify.csv',[1]*20)
my_obj.get_initial_data(arr)
avg = my_obj.calc_average()
songs = my_obj.recommend(amount=1)
x = str(songs['id']).split(" ", 1)
print(x)
songs_full = json.loads(getAudioFeatures(x[1]))
my_obj.learning(song= songs_full)
print(my_obj.weights)
print(songs)




        
        

