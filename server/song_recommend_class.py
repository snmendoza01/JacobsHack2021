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

#Class containig array of songs, along with method to compute the recommendation
class SongRecom():
    
    def __init__(data_file, choosenSongsWithAudioFeatures):
        self.size = 0
        self.song_list = choosenSongsWithAudioFeatures
        self.df = pd.read_csv(data_file)
        
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
    





        
        

