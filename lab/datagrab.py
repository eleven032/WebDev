import pyperclip
from pyautogui import press, typewrite, hotkey
import webbrowser
import time
import os


def copy_val(js):
    pyperclip.copy(js)

def paste_val():
    hotkey('ctrl', 'v')

def wait(sec):
    time.sleep(sec)


keywords = ['disaster', 'hurricane']
timespan = 10
for keyword in keywords:
    # this part is for save location list
    orighin_url = 'https://www.newspapers.com/search/#query=' + keyword
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(orighin_url)
    wait(4)
    press('f12')
    wait(1)
    js = 'let target = document.getElementsByClassName("see-all");target[0].children[1].click();let rows = document.getElementsByTagName("table")[2].tBodies[0].children;let arr = [...rows];for(let i =0;i<arr.length;i++){arr[i].children[0].getElementsByTagName("a")[1].click();};document.getElementById("button_Update").click();let url = window.location.href;let list = url.substr(67).split(",");function down(list) {let tmp = document.createElement("a");tmp.href = "data:text/plain;charset=utf-8," + encodeURI(list);tmp.download = "location_list_'+keyword+'";tmp.click();};down(list);'
    copy_val(js)
    paste_val()
    wait(0.5)
    press('enter')
    wait(3)
    press('enter')
    wait(1)
    hotkey('ctrl', 'w')
    wait(4)
    
    file_path = "C:/Users/Arthur/Downloads/location_list_"+keyword+".txt";
    # save file
    text_file = open(file_path, "r")
     
    lines = text_file.readlines()
    location_list=lines[0].split(',')

    for location in location_list:
        # go through the location list
        for date in range(1751, 2031, timespan):
            url = 'https://www.newspapers.com/search/#query=' + keyword + '&dr_year=' + str(date) + '-' + str(date+timespan-1) + '&p_place=' + location
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url)
            wait(4)
            press('f12')
         
            wait(1)
            #js = 'var csv 
            # = "Year,Location,Data\\n";let keyword = document.getElementsByClassName("query-term query-keyword")[0].innerText;let filename = keyword.substr(0, 8);filename += ".csv";function down() {let tmp = document.createElement("a");tmp.href = "data:text/csv;charset=utf-8," + encodeURI(csv);tmp.download = filename;tmp.click();};let target = document.getElementsByClassName("see-all");target[0].children[1].click();let rows = document.getElementsByTagName("table")[2].tBodies[0].children;let arr = [...rows];arr[0].children[0].getElementsByTagName("a")[1].click();document.getElementById("button_Update").click();document.getElementById("timeline_refine_input").value = 1901 + "-" + 1950;document.getElementById("tl-gobtn").click();'
            js = 'let d1 = ' + str(date) + '; let d2 = ' + str(date+timespan-1) +'; let keyword = document.getElementsByClassName("query-term query-keyword")[0].innerText;let filename= keyword.substr(0,8) + "_' + str(location)+'_' + str(date) + '_' + str(date+timespan-1) + '";filename+=".csv"; let csv = "Year,Location,Data\\n"; if (document.getElementsByClassName("tl_bar").length == 0) { console.log("not exist data"); } else { let collection = document.getElementsByClassName("tl_bar"); let tmp = [...collection]; tmp.forEach(bar => { let pair = bar.title.split(": "); csv += pair[0]; csv += ","; csv += pair[1].replace(/[^0-9]/ig, ""); csv += "\\n"; });let ve = document.createElement("a");ve.href = "data:text/csv;charset=utf-8," + encodeURI(csv);ve.download = filename;ve.click(); };'
            copy_val(js)
            paste_val()
            wait(0.5)
            press('enter')
            wait(1)
            press('enter')
            # exit()
            wait(1)
            hotkey('ctrl', 'w')