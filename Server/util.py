import pickle
import json
import numpy as np

import warnings
warnings.filterwarnings("ignore")


__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    
    # Finding the location index in the dataset
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    
    # Forming the input
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    # Return the predicted output
    return round(__model.predict([x])[0],2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("./Server./artifacts/columns.json", "r") as f:

        # Loading the columns
        __data_columns = json.load(f)['data_columns']

        # Extracting locations 
        __locations = __data_columns[3:]  


    # Loading model
    global __model
    if __model is None:
        with open('./Server./artifacts/banglore_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

# No executable code for the program on its own to execute
if __name__ == '__main__':
    pass