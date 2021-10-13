
import pandas as pd




def acquire():
    '''
    This function reads in arabica_data_cleaned.csv.  It must be downloaded from
    https://www.kaggle.com/volpatto/coffee-quality-database-from-cqi/download
    the link will download a folder named archive
    Grab the csv file named arabica_data_cleaned.csv from within the archive folder
    and place it in your cloned repository working directory. 
    '''

    df = pd.read_csv('arabica_data_cleaned.csv')

    return df