import pandas as pd
import numpy as np


def clean(df):
    '''
    Takes in a pandas dataframe
    Designed to clean the 'arabica_data_cleaned.csv' file
    Dropped columns that didn't offer any value.
    Dropped any row that was missing a value from - Altitude, Region, Quakers, Harvest.Year, Variety
    Used the median value to fill in missing values from - Color, Processing.Method
    Convert Data Types
    Miscellaneous fixes
    Renamed columns
    returns a pandas dataframe
    '''
    
    # Dropped Columns
    col_remove = ['Unnamed: 0', 'Owner', 'Farm.Name', 'Company', 'Expiration','Lot.Number', 'Mill', 'Producer', 'Certification.Address', 'Certification.Contact', 'ICO.Number','Certification.Body','In.Country.Partner', 'Owner.1', ]
    df = df.drop(columns=col_remove)
    
    # Dropped any row that was missing a value from - Altitude, Region, Quakers, Harvest.Year, Variety
    df = df[~df['Altitude'].isnull()]
    df = df[~df['Region'].isnull()]
    df = df[~df['Quakers'].isnull()]
    df = df[~df['Harvest.Year'].isnull()]
    df = df[~df['Variety'].isnull()]
    
    # Used the median value to fill in missing values for - Color, Processing.Method
    df['Color'] = np.where(df['Color'] == 'None', 'Green', df.Color)
    df['Color'] = np.where(df['Color'].isnull(), 'Green', df.Color)
    df['Color'] = np.where(df['Color'] == 'Bluish-Green', 'Blue-Green', df.Color)
    df['Processing.Method'] = np.where(df['Processing.Method'].isnull(), 'Washed / Wet', df['Processing.Method'])

    # Convert Data Type of Bag.Weight and change from lbs to Kilograms
    df[['bag_weight', 'bag_weight_unit']]= df['Bag.Weight'].str.split(expand=True)
    df.bag_weight = df.bag_weight.astype(float)
    df.bag_weight = np.where(df.bag_weight_unit == 'lbs', round(df.bag_weight * 2.20462), df.bag_weight)
    df = df.drop(columns=['bag_weight_unit', 'Bag.Weight'])
    
    # Convert Data Type for Grading.Date and split by day,month, year 
    df['Grading.Date'] = pd.to_datetime(df['Grading.Date'])
    df['grading_month'] = df['Grading.Date'].dt.month
    df['grading_year'] = df['Grading.Date'].dt.year
    df['grading_day'] = df['Grading.Date'].dt.day

    # Miscellaneous fixes
    
    # Dropped this value of Harvest.Year because it equalled 'Mayo a Julio'
    df = df.drop(list(df[df['Harvest.Year']=='Mayo a Julio'].index))
    
    # Anywhere where given two years as a range for Harvest.Year I filled with grading year instead
    df['Harvest.Year'] = np.where(df['Harvest.Year'].str.contains('/'), df.grading_year, df['Harvest.Year'])
    df['Harvest.Year'] = np.where(df['Harvest.Year'].str.contains('-'), df.grading_year, df['Harvest.Year'])
    
    # Data Input Errors, used google to compare regions altitude to confirm correct altitude
    df.at[543,'altitude_mean_meters']=1100
    df.at[896, 'altitude_mean_meters']=1901.64
    df.at[1040, 'altitude_mean_meters']=1100
    df.at[1144, 'altitude_mean_meters']=1901.64
    df.at[41, 'altitude_mean_meters']=1150
    df.at[42, 'altitude_mean_meters']=1150
    
    # Removing older verisons or now un-needed columns
    more_col_remove = ['Species', 'Altitude', 'unit_of_measurement', 'altitude_low_meters', 'altitude_high_meters']
    df = df.drop(columns=more_col_remove)
    
    # Renamed Columns
    df = df.rename(columns={'Country.of.Origin':'country', 'Region':'region', 'Number.of.Bags':'number_of_bags', 'Harvest.Year':'harvest_year', 
                   'Grading.Date':'grading_date', 'Variety':'variety', 'Processing.Method':'processing_method', 'Aroma':'aroma',
                   'Flavor':'flavor', 'Aftertaste':'aftertaste', 'Acidity':'acidity', 'Body':'body', 'Balance':'balance',
                   'Uniformity':'uniformity', 'Clean.Cup':'clean_cup', 'Sweetness':'sweetness', 'Cupper.Points':'cupper_points',
                   'Total.Cup.Points':'total_cup_points', 'Moisture':'moisture', 'Category.One.Defects':'category_one_defects', 
                   'Quakers':'quakers', 'Color':'color', 'Category.Two.Defects': 'category_two_defects'})
    
    # Created Target Feature, Looking for total_cup_points greater than 85
    df['excellent_rating'] = np.where(df.total_cup_points > 85, 1, 0)
    
    return df