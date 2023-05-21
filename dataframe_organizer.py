def dataframe_organizer(df):
    '''
    This function takes in dataframe and match each column of the dataframe with corresponding column names.
    Then, it drops irrelevant columns and set the column 'Country Name' as the index column.
    Finally, return the processed dataframe.
    '''
    df = df.iloc[:222,:16]
    col_names = ['index','Country Name','Total Cases','New Cases','Total Deaths','New Deaths','Total Recovered','unknown','Active Cases','Serious Critical','Tot cases/1M pop','Deaths/1M pop','Total Tests','Tests/1M pop','Population','Continent']
    df.columns = col_names
    df = df.drop(columns=['index', 'unknown'])
    df = df.set_index(['Country Name'])
    return df
