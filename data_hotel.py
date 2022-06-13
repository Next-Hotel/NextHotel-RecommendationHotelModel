import pandas as pd 

def load_data(data):
	df = pd.read_csv(data)
	return df 

def get_list_hotel():
    df = load_data("https://storage.googleapis.com/data-hotel/list-hotel/Data%20API.csv")
    results_json = df.to_json(orient ='table')
    return(results_json)