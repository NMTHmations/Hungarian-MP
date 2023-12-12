import PyPDF2
import re

#Data structure to keep the data of MPs

class kepviselok:
    def __init__(self,csaladnev,keresztnevek):
        self.csaladnev = csaladnev
        self.keresztnevek = keresztnevek


#Imports all data from kepviselok.csv, and exports to list with Kepviselok data type
def import_from_CSV():
    file = open("kepviselok.csv","rt")
    li = []
    for i in file:
        nev = i.split(";")
        nev[1] = re.sub("\n","",nev[1])
        li.append(kepviselok(nev[0],nev[1]))
    file.close()
    return li

#Removes unnecessary accents from the string w/ RegEx

def regexer(name):
    new = str()
    length = len(name)
    for i in range(length):
        if name[i] == "Ó" or name[i] == "Ő" or name[i] == "Ö":
            new = new +"[O"+name[i]+"]"
            continue
        if name[i] == "Ű" or name[i] == "Ú" or name[i] == "Ü":
            new = new +"[U"+name[i]+"]"
            continue
        if name[i] == "Í":
            new = new +"[I"+name[i]+"]"
            continue
        if name[i] == "Á":
            new = new +"[A"+name[i]+"]"
            continue
        if name[i] == "É":
            new = new +"[E"+name[i]+"]"
            continue
        new = new + name[i]
    return new

# Sets the first page with the first occurance of the MP's name

def opening(pdfReader, csaladnev, keresztnev,num):
    start = 0
    csaladnev = csaladnev.upper()
    csaladnev = regexer(csaladnev)
    keresztnev = keresztnev.upper()
    keresztnev = regexer(keresztnev)
    for page in pdfReader.pages:
        text = page.extract_text()
        text = text.upper()
        res_csaladnev = re.findall(csaladnev,text)
        res_keresztnev = re.findall(keresztnev,text)
        start = start + 1
        if res_csaladnev != [] and res_keresztnev != []:
            break
    if start == num:        #if the start equals with the whole page length, it returns -1 - it decides it is in the document
        return -1
    return start


# Sets the ending of the part which is about the current MP's wealth statement

def ending(pdfReader,start,num):
    string = "Vagyon-, jövedelem- és gazdasági érdekeltségi nyilatkozat országgyűlési képviselő," # This is the always, fix part which is present in any part
    end = start
    pages = pdfReader.pages
    for i in range(start,num):
        text = pages[i].extract_text()
        res_search = re.findall(string,text)
        end = end + 1
        if res_search != [] and start < end: #if it found the fix string (the list is not empty), and the end is bigger, then stops the loop
            break
    end = end - 1
    return end

# Prints the pages in a separate file in a specified directory

def output(pdfReader,start,end,filename):
    output = PyPDF2.PdfWriter()
    for i in range(start - 1,end):
        output.add_page(pdfReader.pages[i])
    with open(filename,"wb") as outputStream:
        output.write(outputStream)