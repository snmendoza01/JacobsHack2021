import pandas as pd

dataName = 'spotify_data.csv'
rows = 21525


#Builds data frame
#Input values: 
    #Name of the file with data (csv file)
    #Number of rows to be extracted from file
#output values:
    #Data frame
def build_data_frame(file_name, rows_to_use):
    data = pd.read_csv(file_name, low_memory=False,
                   keep_default_na=False, nrows=rows_to_use)
    return data
    
    
def search_in_df(df, song):
    newdata = df.copy()
    newdata.query('song_name == song', inplace = True)
    return newdata

df = build_data_frame(dataName, rows)
newdf = search_in_df(df, "Pathology")
print(newdf)
    
    
    