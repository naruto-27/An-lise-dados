import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score

def basic_statistics(df):
    return df.describe()
