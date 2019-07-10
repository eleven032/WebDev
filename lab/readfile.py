import pandas as pd
import os
import csv

# path need to be the place you save the data files set
path = 'C:/Users/Arthur/Downloads'

files = os.listdir(path)
keyword = ''
# first line first elemnt is year tag
rows = [['Year']]


# assign 1701-2019 as row
for x in range(1701, 2020):
    rows.append([x])


# get into file dir
for file in files:
        # file path is based on your place
    
    df = pd.read_csv('data/'+file)


#     split file name by _
    tmp = file.split('_')
    keyword = tmp[0]
    location = tmp[1]
    start = tmp[2]
    end = tmp[3][:-4]

#     assign 0 to each year in the very begining
    if location not in rows[0]:
        rows[0].append(location)
        for x in rows[1:]:
            x.append(0)

    pos = int(len(rows[0])-1)

    # get each line data
    for i in range(0, len(df)):
        if int(df.iloc[i][0]) >= int(start) and int(df.iloc[i][0]) <= int(end):
                # update data
            index = int(318-(2019-int(df.iloc[i][0])))+1
            rows[index][pos] = int(df.iloc[i][1])


# save to result file
filename = 'result_'+keyword+'.csv'
f = open(filename, 'w+')
for row in rows:
    res = map(lambda a: str(a), row)
    placeholder = ''
    for ele in res:
        placeholder += (ele+',')
    placeholder = placeholder[0:-1]
    placeholder += '\n'
    f.write(placeholder)
f.close()



# path is the dir that where all download file saved 
filelist = [ f for f in os.listdir(path) ]
for f in filelist:
    if not os.path.isdir(os.path.join(path, f)):  
        os.remove(os.path.join(path, f))

