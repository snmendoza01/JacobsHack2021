#We are going to use the spotify library to build a music 
#reccomendation engine which will generate a playlist of
#related songs to the entered input song(s)

#importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm
import warnings
sns.set()
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

#Reading all the data from the .csv file
data = pd.read_csv("C:\VS Workspaces\Python\Start\spotify.csv")
# data.head()
# data.info()

#Dropping the columns with irrelevant characteristics
# df = data.drop(columns=['id', 'name', 'artists', 'release_date', 'year'])
# df.corr()
# df.head()
# df.info()

#Normalizing all the numerical columns using MinMaxScalar
datatypes = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
normalization = data.select_dtypes(include=datatypes)
for col in normalization.columns:
    MinMaxScaler(col)

#Using K means clustering algorithm to minimize within-cluster variences
kmeans = KMeans(n_clusters=10)
features = kmeans.fit_predict(normalization)
data['features'] = features
MinMaxScaler(data['features'])

#Class for computing the recommendations
class Spotify_Recommendation():
    def __init__(self, dataset):
        self.dataset = dataset
    def recommend(self, songs, amount=1):
        distance = []
        song = self.dataset[(self.dataset.name.str.lower() == songs.lower())].head(1).values[0]
        rec = self.dataset[self.dataset.name.str.lower() != songs.lower()]
        for songs in tqdm(rec.values):
            d = 0
            for col in np.arange(len(rec.columns)):
                if not col in [1, 6, 12, 14, 18]:
                    d = d + np.absolute(float(song[col]) - float(songs[col]))
            distance.append(d)
        rec['distance'] = distance
        rec = rec.sort_values('distance')
        columns = ['artists', 'name']
        return rec[columns][:amount]

recommendations = Spotify_Recommendation(data)
new = recommendations.recommend("Fireflies", 10)
print(new)

