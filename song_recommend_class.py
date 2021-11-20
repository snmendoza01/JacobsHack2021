import numpy as np
import pandas as pd
import requests
import sklearn

#The function Julian Made
def searchProperties(df, id):
    pass

#Class containig array of songs, along with method to compute the recommendation
class SongRecom():
    
    def __init__(self,data_frame):
        self.size = 0
        self.song_list = []
        self.df = data_frame
        
    #Appends the sound properties of the song to the song list 
    #Input value: array of the id of each songs
    #Return value: Void  
    def get_initial_data(self, id_arr):
        self.size = len(id_arr)
        for i in range(0,len(id_arr)):
            self.song_list.append(searchProperties(self.df, id_arr[i]))
        
        
    #Finds the recoomendation basing on the initial data
    def recommend(self):
        
        #take the average of each property and create a new dictionary
        avg_acoustic = 
        for i in range(0,len(self.song_list)):
            
            
        
        ###function using machine learning###
        return song
    
        
        

