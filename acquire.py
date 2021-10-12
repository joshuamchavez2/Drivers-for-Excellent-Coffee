import pandas as pd

def acquire():
    '''
    This function reads in titanic data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    df = pd.read_csv('arabica_data_cleaned.csv')
    return df

def get_data_dictionary(df):
    
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
'character	Method for processing',
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
    df = get_data_dictionary(df)
    df= df.reset_index()
    df = df.rename(index = {61: 'Target'})
    return df.iloc[61]