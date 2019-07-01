import pandas as pd
import os
import csv

path = 'C:/Users/Arthur/Desktop/WebDev/lab/data'
files = os.listdir(path)
rows = [['Year']]

for x in range(1701, 2020):
    rows.append([x])


for file in files:
    df = pd.read_csv('data/'+file)
    tmp = file.split('_')
    location = tmp[1]
    start = tmp[2]
    end = tmp[3][:-4]
    if location not in rows[0]:
        rows[0].append(location)
        for x in rows[1:]:
            x.append(0)

    pos = int(len(rows[0])-1)
# file line
    for i in range(0, len(df)):
        if int(df.iloc[i][0]) >= int(start) and int(df.iloc[i][0]) <= int(end):
            index = int(318-(2019-int(df.iloc[i][0])))+1
            rows[index][pos] = int(df.iloc[i][1])


#                     position = int(2019-df.iloc[i][0]-1)
#                     print(position)
#                     rows[position][index-1] = df.iloc[i][1];

#                 #                         rows.append([df.iloc[i][0], df.iloc[i][1]])
#                 # final_rows = [rows[0]]
#                 # for i in range(1, len(rows)):
#                 #         while(not rows[i][0] == final_rows[-1][0]+1):
#                 #                 final_rows.append([final_rows[-1][0]+1, 0])
#                 #         final_rows.append(rows[i])


f = open('result.csv', 'w+')
for row in rows:
    res = map(lambda a: str(a), row)
    placeholder = ''
    for ele in res:
            placeholder+=(ele+',')
#     f.write(str(row[0]) + "," + str(row[1]) + '\n')
    placeholder = placeholder[0:-1]
    placeholder+='\n'
    f.write(placeholder)
f.close()
# print(rows)
