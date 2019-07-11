import pyperclip
from pyautogui import press, typewrite, hotkey
import webbrowser
import time
import os
import pandas as pd
import datetime
import csv


def copy_val(js):
    pyperclip.copy(js)


def paste_val():
    hotkey('ctrl', 'v')


def wait(sec):
    time.sleep(sec)


keywords = ['disaster', 'hurricane']
timespan = 40
for keyword in keywords:
    start_time = datetime.datetime.now()
    # this part is for save location list
    orighin_url = 'https://www.newspapers.com/search/#query=' + keyword
    webbrowser.get(
        "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(orighin_url)
    wait(4)
    press('f12')
    wait(1)
    js = 'let target = document.getElementsByClassName("see-all");target[0].children[1].click();let rows = document.getElementsByTagName("table")[2].tBodies[0].children;let arr = [...rows];for(let i =0;i<arr.length;i++){arr[i].children[0].getElementsByTagName("a")[1].click();};document.getElementById("button_Update").click();let url = window.location.href;let list = url.substr(67).split(",");function down(list) {let tmp = document.createElement("a");tmp.href = "data:text/plain;charset=utf-8," + encodeURI(list);tmp.download = "location_list_'+keyword+'";tmp.click();};down(list);'
    copy_val(js)
    paste_val()
    wait(0.5)
    press('enter')
    wait(2)
    press('enter')
    wait(0.5)
    hotkey('ctrl', 'w')
    wait(0.5)

    file_path = "C:/Users/Arthur/Downloads/location_list_"+keyword+".txt"
    # save file
    text_file = open(file_path, "r")

    lines = text_file.readlines()
    location_list = lines[0].split(',')

    for location in location_list:

        # go through the location list
        for date in range(1991, 2031, timespan):

            url = 'https://www.newspapers.com/search/#query=' + keyword + '&dr_year=' + \
                str(date) + '-' + str(date+timespan-1) + '&p_place=' + location
            webbrowser.get(
                "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url)
            wait(2)
            press('f12')

            wait(1)
            # js = 'var csv
            # = "Year,Location,Data\\n";let keyword = document.getElementsByClassName("query-term query-keyword")[0].innerText;let filename = keyword.substr(0, 8);filename += ".csv";function down() {let tmp = document.createElement("a");tmp.href = "data:text/csv;charset=utf-8," + encodeURI(csv);tmp.download = filename;tmp.click();};let target = document.getElementsByClassName("see-all");target[0].children[1].click();let rows = document.getElementsByTagName("table")[2].tBodies[0].children;let arr = [...rows];arr[0].children[0].getElementsByTagName("a")[1].click();document.getElementById("button_Update").click();document.getElementById("timeline_refine_input").value = 1901 + "-" + 1950;document.getElementById("tl-gobtn").click();'
            js = 'let d1 = ' + str(date) + '; let d2 = ' + str(date+timespan-1) + '; let keyword = document.getElementsByClassName("query-term query-keyword")[0].innerText;let filename= keyword.substr(0,8) + "_' + str(location)+'_' + str(date) + '_' + str(
                date+timespan-1) + '";filename+=".csv"; let csv = "Year,Location,Data\\n"; if (document.getElementsByClassName("tl_bar").length == 0) { console.log("not exist data"); } else { let collection = document.getElementsByClassName("tl_bar"); let tmp = [...collection]; tmp.forEach(bar => { let pair = bar.title.split(": "); csv += pair[0]; csv += ","; csv += pair[1].replace(/[^0-9]/ig, ""); csv += "\\n"; });let ve = document.createElement("a");ve.href = "data:text/csv;charset=utf-8," + encodeURI(csv);ve.download = filename;ve.click(); };'
            copy_val(js)
            paste_val()
            wait(0.5)
            press('enter')
            wait(1)
            press('enter')
            # exit()
            wait(1)
            hotkey('ctrl', 'w')

    end_time = datetime.datetime.now()
    print((end_time-start_time).seconds)

    dowload_path = 'C:/Users/Arthur/Downloads'

    files = os.listdir(dowload_path)
    keyword_read = ''
    # first line first elemnt is year tag
    rows = [['Year']]

    # assign 1701-2019 as row
    for x in range(1701, 2020):
        rows.append([x])
    # get into file dir
    for file in files:
        if(file != 'desktop.ini' and file != 'Install exe' and file[-4:] != '.txt'):
            # file path is based on your place

            pwd = dowload_path+'/'+file

            df = pd.read_csv(pwd)

        # split file name by _
            tmp = file.split('_')
            keyword_read = tmp[0]
            location_read = tmp[1]
            start = tmp[2]
            end = tmp[3][:-4]

    #     assign 0 to each year in the very begining
            if location_read not in rows[0]:
                rows[0].append(location_read)
                for x in rows[1:]:
                    x.append(0)

            pos = int(len(rows[0])-1)

            # get each line data
            for i in range(0, len(df)):
                if int(df.iloc[i][0]) >= int(start) and int(df.iloc[i][0]) <= int(end):
                    # update data
                    index = int(318-(2019-int(df.iloc[i][0])))+1
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
