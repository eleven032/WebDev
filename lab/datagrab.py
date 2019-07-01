import pyperclip
from pyautogui import press, typewrite, hotkey
import webbrowser
import time

# pyperclip.copy('let collection=document.getElementsByClassName("tl_bar");let keyword = document.getElementsByClassName("query-term query-keyword")[0].innerText;let filename= keyword.substr(0,8);filename+=".csv";var arr = [...collection];var csv = "Year,Data\\n";arr.forEach(bar => {csv += bar.title.substr(0, 9);csv += ",";csv += bar.title.substr(11).replace(/[^0-9]/ig,"");csv += "\\n";});let tmp = document.createElement("a");tmp.href = "data:text/csv;charset=utf-8," + encodeURI(csv);tmp.download = filename;document.body.appendChild(tmp);tmp.click();')

# # pyperclip.copy('let collection=document.getElementsByClassName("tl_bar");let keyword = document.getElementsByClassName("query-term query-keyword")[0].innerText;let filename= keyword.substr(0,8);filename+=".csv";var arr = [...collection];var csv = "Year,Data\\n";arr.forEach(bar => {csv += bar.title.substr(0, 9);csv += ",";csv += bar.title.substr(11).replace(/[^0-9]/ig,"");csv += "\\n";}); var saved = document.createElement("input");saved.type = "text";saved.value=csv;document.body.appendChild(saved);saved.select();document.execCommand("copy");')

# browser = webbrowser.get('firefox').open_new_tab('https://www.newspapers.com/search/#query=hurricane')



def copy_val(js):
    pyperclip.copy(js)

def paste_val():
    hotkey('ctrl', 'v')

def wait(sec):
    time.sleep(sec)



# start
#browser = webbrowser.get('firefox').open_new_tab('https://www.newspapers.com/search/#query=hurricane')
#webbrowser.get("C:/Users/Arthur/AppData/Local/Mozilla Firefox/firefox.exe %s").open("https://www.newspapers.com/search/#query=hurricane")
keywords = ['disaster', 'hurricane']
location_list = ['PA', 'NY', 'FL']
timespan = 10
for keyword in keywords:
    for location in location_list:
        for date in range(1751, 2031, timespan):
            url = 'https://www.newspapers.com/search/#query=' + keyword + '&dr_year=' + str(date) + '-' + str(date+timespan-1) + '&p_place=' + location
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url)
            wait(4)
            press('f12')
            #hotkey('fn', 'shift', 'k')
            wait(1)
            #js = 'var csv = "Year,Location,Data\\n";let keyword = document.getElementsByClassName("query-term query-keyword")[0].innerText;let filename = keyword.substr(0, 8);filename += ".csv";function down() {let tmp = document.createElement("a");tmp.href = "data:text/csv;charset=utf-8," + encodeURI(csv);tmp.download = filename;tmp.click();};let target = document.getElementsByClassName("see-all");target[0].children[1].click();let rows = document.getElementsByTagName("table")[2].tBodies[0].children;let arr = [...rows];arr[0].children[0].getElementsByTagName("a")[1].click();document.getElementById("button_Update").click();document.getElementById("timeline_refine_input").value = 1901 + "-" + 1950;document.getElementById("tl-gobtn").click();'
            js = 'let d1 = ' + str(date) + '; let d2 = ' + str(date+timespan-1) +'; let keyword = document.getElementsByClassName("query-term query-keyword")[0].innerText;let filename= keyword.substr(0,8) + "_' + str(date) + '_' + str(date+timespan-1) + '";filename+=".csv"; let csv = "Year,Data\\n"; if (document.getElementsByClassName("tl_bar").length == 0) { console.log("not exist data"); } else { let collection = document.getElementsByClassName("tl_bar"); let tmp = [...collection]; tmp.forEach(bar => { let pair = bar.title.split(": "); csv += pair[0]; csv += ","; csv += pair[1].replace(/[^0-9]/ig, ""); csv += "\\n"; });let ve = document.createElement("a");ve.href = "data:text/csv;charset=utf-8," + encodeURI(csv);ve.download = filename;ve.click(); };'
            copy_val(js)
            paste_val()
            wait(0.5)
            press('enter')
            wait(1)
            press('enter')
            # exit()
            wait(1)
            hotkey('ctrl', 'w')
    




# let target = document.getElementsByClassName("see-all");
# target[0].children[1].click();
# let rows = document.getElementsByTagName("table")[2].tBodies[0].children;
# let arr = [...rows];

# for(let i =0;i<arr.length;i++){
#     arr[i].children[0].getElementsByTagName("a")[1].click();
# };
# document.getElementById("button_Update").click();

# let url = window.location.href;

# let list = url.substr(67).split(",");

# function down(list) {
#     let tmp = document.createElement("a");
#     tmp.href = "data:text/plain;charset=utf-8," + encodeURI(list);
#     tmp.download = "location_list";
#     tmp.click();
# };

# down(list);
# wait(3)
# js = 'document.getElementsByClassName("tl_bar").length'
# copy_val(js)
# paste_val()
# wait(0.5)
# press('enter')