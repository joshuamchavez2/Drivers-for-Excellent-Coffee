import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import statistics

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_squared_error

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression, LassoLars, TweedieRegressor
from sklearn.preprocessing import PolynomialFeatures

import sklearn.preprocessing


############################## Cleaning ################################

def add_scaled_columns(train, validate, test, scaler, columns_to_scale):
    
    # new column names
    new_column_names = [c + '_scaled' for c in columns_to_scale]
    
    # Fit the scaler on the train
    scaler.fit(train[columns_to_scale])
    
    # transform train validate and test
    train = pd.concat([
        train,
        pd.DataFrame(scaler.transform(train[columns_to_scale]), columns=new_column_names, index=train.index),
    ], axis=1)
    
    validate = pd.concat([
        validate,
        pd.DataFrame(scaler.transform(validate[columns_to_scale]), columns=new_column_names, index=validate.index),
    ], axis=1)
    
    
    test = pd.concat([
        test,
        pd.DataFrame(scaler.transform(test[columns_to_scale]), columns=new_column_names, index=test.index),
    ], axis=1)
    
    return train, validate, test

################################## Data Dictionary #####################################

def get_data_dictionary(df):
    '''
    This function takes in a dataframe
    Fill in your values for d_list (description)
    concats your description with your feature, nonnull, and Dtype values
    '''
    
    d_list = ['index column',
        'Species of coffee bean (arabica or robusta)',
        'Owner of the farm',
        'Where the bean came from',
        'Name of the farm',
        'Lot number of the beans tested',
        'Mill where the beans were processed',
        'International Coffee Organization number',
        'Company name',
        'Altitude',
        'Region where bean came from',
        'Producer of the roasted bean',
        'Number of bags tested',
        'Bag weight tested',
        'Partner for the country',
        'When the beans were harvested (year)',
        'When the beans were graded',
        'Who owns the beans',
        'Variety of the beans',
        'character Method for processing',
        'Aroma grade',
        'Flavor grade',
        'Aftertaste grade',
        'Acidity grade',
        'Body grade',
        'Balance grade',
        'Uniformity grade',
        'Clean cup grade',
        'Sweetness grade',
        'Cupper Points',
        'Total rating/points (0 - 100 scale)',
        'Moisture Grade',
        'Category one defects (count)',
        'quakers',
        'Color of bean',
        'Category two defects (count)',
        'Expiration date of the beans',
        'Who certified it',
        'Certification body address',
        'Certification contact',
        'Unit of measurement',
        'Altitude low meters',
        'Altitude high meters',
        'Altitude mean meters',]

    data_dictionary = pd.DataFrame([{'Feature': col,
         'Datatype': f'{df[col].count()} non-null: {df[col].dtype}'} for col in df.columns])
    
    describe = pd.Series(d_list)
    df = pd.concat([data_dictionary, describe.rename("Description")], axis = 1)
    return df.set_index("Feature")

def get_target(df):  
    '''
    Takes in a data frame
    find out what index your target is set it to that number 
    '''  
    target_index = 8
    df = get_data_dictionary(df)
    df= df.reset_index()
    df = df.rename(index = {target_index: 'Target'})
    return df.iloc[61]