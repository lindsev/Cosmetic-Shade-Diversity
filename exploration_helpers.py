# Data Inspection Module
import pandas as pd
import re
from unidecode import unidecode


''' This module improves the effeciency of Preliminary Data Exploration'''

def missing_values(df):
    '''
    Calculate and display the percentage and total missing values for each column in a DataFrame.

    Parameters:
    - df (pd.DataFrame): The input DataFrame.

    Returns:
    - tuple: A tuple containing the percentage and total missing values.
    '''
    missing = df.isna()
    average_missing = missing.mean().sort_values(ascending=False)
    total_missing = missing.sum().sort_values(ascending=False)

    percent_missing = average_missing[average_missing > 0] * 100
    total_missing = total_missing[total_missing > 0]
    print(f'---- Percentage of Missing Values (%) ----- \n{percent_missing}')
    print(f"---- Number of Missing Shade Values (%) ----- \n{total_missing}")
    return(percent_missing,total_missing)


def duplicate_rows(df):
    '''
   The duplicate_rows() function identifies and displays entirely duplicated rows in a DataFrame.

   Parameters:
   - df (pd.DataFrame): The input DataFrame.

   Returns:
   - pd.DataFrame
   '''
    duplicates = df.duplicated(keep=False)
    num_duplicates = duplicates.sum()

    print(f'No. of entirely duplicated rows: {num_duplicates}')

    # Return the DataFrame with entirely duplicated rows
    return df[duplicates] if num_duplicates > 0 else None

def remove_schar(df, column):
    def replace_schar(value):
        # Remove special characters and replace accented characters
        value = unidecode(value)
        return re.sub(r'[^a-zA-Z0-9]', '', value).lower()

    df[column] = df[column].apply(replace_schar)

