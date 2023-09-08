import PyPDF2
import re
import os

class kepviselok:
    def __init__(self,csaladnev,keresztnevek):
        self.csaladnev = csaladnev
        self.keresztnevek = keresztnevek

def import_from_CSV():
    file = open("kepviselok.csv","rt")
    li = []
    for i in file:
        nev = i.split(";")
        nev[1] = re.sub("\n","",nev[1])
        li.append(kepviselok(nev[0],nev[1]))
    file.close()
    return li

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
    if start == num:
        return -1
    return start


def ending(pdfReader,start,num):
    string = "Vagyon-, jövedelem- és gazdasági érdekeltségi nyilatkozat országgyűlési képviselő,"
    end = start
    pages = pdfReader.pages
    for i in range(start,num):
        text = pages[i].extract_text()
        res_search = re.findall(string,text)
        end = end + 1
        if res_search != [] and start < end:
            break
    end = end - 1
    return end

def output(pdfReader,start,end,filename):
    output = PyPDF2.PdfWriter()
    for i in range(start - 1,end):
        output.add_page(pdfReader.pages[i])
    with open(filename,"wb") as outputStream:
        output.write(outputStream)

def main():
    file = open("Kepviselok_dec_20230712.pdf","rb")
    pdfReader = PyPDF2.PdfReader(file)
    path = "kepviselok"
    try:
        os.mkdir(path)
    except FileExistsError:
        print("FileExistsError: A könyvtár már létezik")
    li = import_from_CSV()
    os.chdir(path)
    length = len(li)
    num = len(pdfReader.pages)
    for i in range(length):
        vezeteknev = li[i].csaladnev
        keresztnev = li[i].keresztnevek
        nev = vezeteknev + " " + keresztnev
        filename = vezeteknev + "_" + keresztnev
        filename = re.sub("[óőö]","o",filename)
        filename = re.sub("é","e",filename)
        filename = re.sub("í","i",filename)
        filename = re.sub("[üűú]","u",filename)
        filename = re.sub("á","a",filename)
        filename = filename.lower()
        filename = filename.replace(" ","_")
        filename = filename + ".pdf"
        print("{}. képviselő neve: {} keresése:".format(i+1,nev))
        start = opening(pdfReader,vezeteknev,keresztnev,num)
        if start == -1:
            print("Nincs benne a PDF-ben")
        else:
            print("Megtaláltuk!")
            end = ending(pdfReader,start,num)
            output(pdfReader,start,end,filename)
    file.close()

if __name__ == "__main__":
    main()