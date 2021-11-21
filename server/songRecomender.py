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


#Class containig array of songs, along with method to compute the recommendation
class SongRecom():
    
    def __init__(self,data_file, choosenSongsWithAudioFeatures):
        self.song_list = choosenSongsWithAudioFeatures
        self.size = len(choosenSongsWithAudioFeatures)
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
        for i in range(0, self.size):
            self.song_list[i] = json.loads(self.song_list[i])
        avg = self.song_list[0].copy()
        for key in avg:
            avg[key] = 0
        print(avg)
        numberOfKeys = len(self.song_list[0])
        print(numberOfKeys)
        for key in self.song_list[0]:
            print("THe key is " + key)
            print(type(self.song_list[0][key]))
            if(type(self.song_list[0][key]) == str):
                avg[key] = 0
            else:
                for j in self.song_list:
                    avg[key] = avg[key]+j[key]
                print(avg[key])
                avg[key] = float(avg[key]/self.size)
        print(avg)
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