import modules.pdftools as pdftools
import modules.csvtools as csvtools
import PyPDF2
import os
import re


def main():
    # initalizing PDF and create CSV
    # creates kepviselok directory, where all MP's wealth statement is contained
    file = open("Kepviselok_dec_20230712.pdf","rb")
    pdfReader = PyPDF2.PdfReader(file)
    path = "kepviselok"
    try:
        os.mkdir(path)
    except FileExistsError:
        print("FileExistsError: A könyvtár már létezik")
    csvtools.create_csv()
    li = pdftools.import_from_CSV()
    os.chdir(path)
    length = len(li)
    num = len(pdfReader.pages)
    #Creates the file and misses all accents in the filename
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
        start = pdftools.opening(pdfReader,vezeteknev,keresztnev,num)
        if start == -1:
            print("Nincs benne a PDF-ben")
        else:
            print("Megtaláltuk!")
            end = pdftools.ending(pdfReader,start,num)
            pdftools.output(pdfReader,start,end,filename)
    file.close()

if __name__ == "__main__":
    main()