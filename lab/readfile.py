import pandas as pd
import os
import csv

path = 'C:/Users/Arthur/Desktop/WebDev/lab/data'
files = os.listdir(path)
rows = [['Year']]
for x in range(1701, 2020):
        rows.append([str(x)])

for file in files:
        df = pd.read_csv('data/'+file)
        tmp = file.split('_')
        location = tmp[1]
        start = tmp[2]
        end = tmp[3]
        for i in range(0, len(df)):
                if df.iloc[i][0] >= int(start) and df.iloc[i][0]<= int(end):
                        rows[0].append(location)

print(rows)




                        






#                         rows.append([df.iloc[i][0], df.iloc[i][1]])
# final_rows = [rows[0]]
# for i in range(1, len(rows)):
#         while(not rows[i][0] == final_rows[-1][0]+1):
#                 final_rows.append([final_rows[-1][0]+1, 0])                
#         final_rows.append(rows[i])

        

# f= open('result.csv','w+')
# for row in final_rows:
#         f.write(str(row[0]) + "," + str(row[1]) + '\n')
# f.close()