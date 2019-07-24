import pyperclip
from pyautogui import press, typewrite, hotkey
import webbrowser
import time
import os
import pandas as pd
import datetime
import glob

SHORT_WAIT = 0.5
MED_WAIT = 1.0
MED2_WAIT = 2.0
LONG_WAIT = 4.0

PLATFORM = 'WINDOWS'  # 'MAC' # 'LINUX'

if PLATFORM == 'LINUX':
    BROWSER = 'google-chrome'
elif PLATFORM == 'WINDOWS':
    BROWSER = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
elif PLATFORM == 'MAC':
    BROWSER = 'chrome'
else:
    exit()


def copy_val(js):
    pyperclip.copy(js)


def paste_val():
    if PLATFORM == 'WINDOWS':
        hotkey('ctrl', 'v')
    elif PLATFORM == 'LINUX':
        hotkey('ctrl', 'v')
    elif PLATFORM == 'MAC':
        hotkey('command', 'v')
    else:
        exit()

    wait(SHORT_WAIT)


def hit_return():
    press('enter')
    wait(SHORT_WAIT)


def wait(sec):
    time.sleep(sec)


def display_console():
    if PLATFORM == 'WINDOWS':
        hotkey('ctrl', 'shift', 'j')
    elif PLATFORM == 'LINUX':
        hotkey('ctrl', 'shift', 'j')
    elif PLATFORM == 'MAC':
        hotkey('command', 'shift', 'j')
    else:
        exit()

    wait(MED2_WAIT)


def close_tab():
    if PLATFORM == 'WINDOWS':
        hotkey('ctrl', 'w')
    elif PLATFORM == 'LINUX':
        hotkey('ctrl', 'w')
    elif PLATFORM == 'MAC':
        hotkey('command', 'w')
    else:
        exit()

    wait(SHORT_WAIT)


#dowload_path = '/media/snehesh/DataDrive/MAIN DRIVE/Downloads'    
dowload_path = 'C:/Users/neosh/Downloads'


# keyword could read from outside
keywords = ['disaster', 'trump', 'hurricane', 'terrorist', 'facebook', 'snapchat'] #
# start and end year is based on special requirenment 
START_YEAR = 1850
END_YEAR = 2020
timespan = 40

for keyword in keywords:
    start_time = datetime.datetime.now()
    # this part is for save location list
    orighin_url = 'https://www.newspapers.com/search/#query=' + keyword
    webbrowser.get(BROWSER + ' %s').open(orighin_url)
    wait(LONG_WAIT)

    display_console()
    js = 'let target = document.getElementsByClassName("see-all");target[0].children[1].click();let rows = document.getElementsByTagName("table")[2].tBodies[0].children;let arr = [...rows];for(let i =0;i<arr.length;i++){arr[i].children[0].getElementsByTagName("a")[1].click();};document.getElementById("button_Update").click();let url = window.location.href;let list = url.substr(67).split(",");function down(list) {let tmp = document.createElement("a");tmp.href = "data:text/plain;charset=utf-8," + encodeURI(list);tmp.download = "location_list_'+keyword+'";tmp.click();};down(list);'
    copy_val(js)
    paste_val()
    hit_return()
    hit_return()
    close_tab()

    file_path = dowload_path + '/location_list_' + keyword + '.txt'
    # save file
    text_file = open(file_path, "r")

    lines = text_file.readlines()
    location_list = lines[0].split(',')
    counter = 0
    for location in location_list:
        # if(counter >5):
        #     break
        # counter+=1    
        # go through the location list
        for date in range(START_YEAR, END_YEAR, timespan):

            url = 'https://www.newspapers.com/search/#query=' + keyword + '&dr_year=' + \
                str(date) + '-' + str(date+timespan-1) + '&p_place=' + location
            webbrowser.get(BROWSER + ' %s').open(url)
            wait(MED_WAIT)

         
            display_console()
            js = 'let filename= "' +str(keyword) + '_' + str(location)+'_' + str(date) + '_' + str(date+timespan-1) + '";filename+=".csv"; let csv = "Year,Location,Data\\n"; if (document.getElementsByClassName("tl_bar").length == 0) { console.log("not exist data"); } else { let collection = document.getElementsByClassName("tl_bar"); let tmp = [...collection]; tmp.forEach(bar => { let pair = bar.title.split(": "); csv += pair[0]; csv += ","; csv += pair[1].replace(/[^0-9]/ig, ""); csv += "\\n"; });let ve = document.createElement("a");ve.href = "data:text/csv;charset=utf-8," + encodeURI(csv);ve.download = filename;ve.click(); };'
            copy_val(js)
            paste_val()
            hit_return()
            wait(1)
            hit_return()
            close_tab()

    end_time = datetime.datetime.now()
    print((end_time-start_time).seconds)

    # files = os.listdir(dowload_path)
    files = glob.glob(dowload_path + '/' + keyword + '_*.csv')

    keyword_read = ''
    # first line first elemnt is year tag
    rows = [['Year']]

    # assign 1701-2019 as row
    for x in range(START_YEAR, END_YEAR):
        rows.append([x])
    # get into file dir
    for file in files:
        if(file[-4:] != '.csv'):
            print('Error: ' + file)
            continue
    
        df = pd.read_csv(file)

        # split file name by _
        tmp = file.split('_')
        keyword_read = tmp[0]
        location_read = tmp[1]
        start = tmp[2]
        end = tmp[3][:-4]

        # assign 0 to each year in the very begining
        if location_read not in rows[0]:
            rows[0].append(location_read)
            for x in rows[1:]:
                x.append(0)

        pos = int(len(rows[0])-1)

        # get each line data
        for i in range(0, len(df)):
            if int(df.iloc[i][0]) >= int(start) and int(df.iloc[i][0]) <= int(end):
                # update data
                index = int( (END_YEAR-START_YEAR) - (END_YEAR-int(df.iloc[i][0])) )+1
                rows[index][pos] = int(df.iloc[i][1])

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
    filelist = [f for f in os.listdir(dowload_path)]
    for f in filelist:
        if not os.path.isdir(os.path.join(dowload_path, f)):
            if f[-4:] != '.txt':
                # print(os.path.join(dowload_path, f)[-4])
                os.remove(os.path.join(dowload_path, f))
                
    text_file.close()

filelist = [f for f in os.listdir(dowload_path)]
for f in filelist:
    if not os.path.isdir(os.path.join(dowload_path, f)):
        os.remove(os.path.join(dowload_path, f))
