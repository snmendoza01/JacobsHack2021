import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns


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


df = pd.DataFrame(norm_features)
x = df.join(song_name)
df = pd.pivot_table(x, x[[0,1,2,3,4,5]],["Song-Names"])#for indexing song_name to our df
def current_music(value):
    print("Top 5 recommendations for given music are:")
    print(df)
    value = df.loc[value]
    print(value)
    similarities = df.dot(value)
    print(format(similarities.nlargest()))

current_music("Hello")