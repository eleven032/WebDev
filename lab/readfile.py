import pandas as pd
import os
import csv

path = 'C:/Users/Arthur/Desktop/WebDev/lab/data'
files = os.listdir(path)
rows = []
for file in files:
        df = pd.read_csv('data/'+file)
        start = file[9:-9]
        end = file[14:-4]
        for i in range(0, len(df)):
                if df.iloc[i][0] >= int(start) and df.iloc[i][0]<= int(end):
                        rows.append([str(df.iloc[i][0]), str(df.iloc[i][1])])
                        
with open('result.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(rows)
csvFile.close()