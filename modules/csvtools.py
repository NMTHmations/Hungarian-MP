import requests
from bs4 import BeautifulSoup
import re

# Changes and slices the MPs name: -DR. misses the dot and it slices the next part which is 
#                                   separated by space.
#                                   If the surname is ending to -né then it slices the next part which is 
#                                   separated by space.

def name_change(x):
    
    name = str()
    
    if re.findall("[.]",x) != []:
        search = re.search("[.]",x)
        start = search.start()
        begin = start + 2
        length = len(x)
        position = begin
        name = x[0:start + 1] + " "
        for i in range(begin,length):
            if x[i] == ' ':
                name = name + x[position:i] + ";"
                position = i + 1
        name = name + x[position:]
        return name
    
    if re.findall("né",x) != []:
        search = re.search("né",x)
        start = search.start()
        begin = start + 3
        length = len(x)
        position = begin
        name = x[0:start + 2] + " "
        for i in range(begin,length):
            if x[i] == ' ':
                name = name + x[position:i] + ";"
                position = i + 1
        name = name + x[position:]
        return name
    
    name = x.replace(" ",";",1)
    return name

# Writing to CSV

def CSV_convert(x,file):
    name = name_change(x)
    file.write("{}\n".format(name))

# Parsing the initalized HTML file and find the names in the columns.

def name_extract(URL,file):
    soup = BeautifulSoup(URL.content,"html.parser")
    tag = 0
    names = soup.find_all("td")
    for i in names:
        name = i.find('a')
        if name != None:
            try:
                x = name['title']
                y = name.text
                if re.findall("[Pp]árt",x) == [] and re.findall("[Ss]zövetség", x) == [] and re.findall("[Kk]oalíció",x) == [] and re.findall("[vV]álasztókerület",x) == [] and re.findall("[Mm]ozgalom",x) == [] and re.findall("[Mm]agyarországért",x) == [] and re.findall("[Oo]rszággyűlés",x) == []:
                    CSV_convert(y,file)
                    tag += 1
            except KeyError:
                print("CSVTools: Exception KeyError: Adatlekérés nem sikerült, de hagyd figyelmen kívül ezt az üzenetet!")
        if tag > 200:
            break

#Creates CSV file from the URL and returns the file name (or relative path in that case)

def create_csv():
    path = "kepviselok.csv"
    file = open(path,"wt")
    URL = requests.get("https://hu.wikipedia.org/wiki/2022–2026_közötti_magyar_országgyűlési_képviselők_listája")
    name_extract(URL,file)
    file.close()
    return path