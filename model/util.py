import pandas as pd

def create_dataset(file):
    df = pd.read_csv(file,index_col=0)
    return df

def data_preprocess(df):
    df['zone_R'] = df['Zone Type'].apply(lambda x: 1 if x == 'R' else 0)
    df['zone_C'] = df['Zone Type'].apply(lambda x: 1 if x == 'C' else 0)
    df['zone_I'] = df['Zone Type'].apply(lambda x: 1 if x == 'I' else 0)
    return df


