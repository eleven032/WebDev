import pandas as pd


df = pd.read_csv('disaster_1811_1820.csv')

for i in range(0, len(df)):
    if df.iloc[i][0] >= 1811:
        print(df.iloc[i][1])