import pandas as pd
import numpy as np

def load_data(filepath):
    return pd.read_csv(filepath)

def clean_data(df):
    return df.dropna().drop_duplicates()
