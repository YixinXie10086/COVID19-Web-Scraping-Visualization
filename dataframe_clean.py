
from unidecode import unidecode
def numeric_col_clean(df):
    '''
    This function takes in a dataframe and it deletes all the space in every cell of the dataframe.
    Then, it deletes all the comma in every string.
    Finally, it converted those string to integers so that it can be processed later.The function will processed every column except column Continent and date.
    The function returns the cleaned dataframe.
    '''
    for i in range(df.shape[1]):
        try:
            df[df.columns[i]] =  df.iloc[:,i].apply(lambda x: (unidecode(x).replace(' ','')))
            df[df.columns[i]] = (df.iloc[:,i].apply(lambda x: (unidecode(x).replace(',','')))).astype(int)
        except:
            break
    return df
