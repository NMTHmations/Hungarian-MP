import PyPDF2
import modules.pdftools as pdftools
import modules.csvtools as csvtools
import re

#search for the typed name or characters in the list

def search_name(li,text):
    result = []
    for i in range(0,len(li)):
        string = li[i].csaladnev + " " + li[i].keresztnevek
        if text.lower() in string.lower():
            result.append(li[i])
    return result

# shows all result of the search

def show_all_result(result):
    print("A kereses eredmenye")
    for i in range(0,len(result)):
        print("{}. {} {}".format(i+1,result[i].csaladnev,result[i].keresztnevek))

# saves the wealth statement of the selected MP to a selected PDF file

def save_file(pdfReader,result):
    if len(result) == 1: # if there's a single result
        filename = ""
        while True:
            filename = input("Miként mentsünk el a fájlt? ") # save file as
            if ".pdf" in filename:
                break
            print("A kiterjesztésnek .pdf formátumúnak kell lennie!")
        num = len(pdfReader.pages)
        start = pdftools.opening(pdfReader,result[0].csaladnev,result[0].keresztnevek,num)
        end = pdftools.ending(pdfReader,start,num)
        pdftools.output(pdfReader,start,end,filename)
        exit(0)
    else: #if there's a multiple result
        while True:
            i = input("Adja meg a sorszámot a mentéshez!") #choose index number
            for m in i:
                if m.isdigit() == False:
                    print("Számot adjon meg!")
                    continue
            if len(result) < int(i)-1:
                print("A szám túl nagy!")
            else:
                break
        filename = ""
        while True:
            filename = input("Miként mentsünk el a fájlt? ") #save file as
            if ".pdf" in filename.lower():
                break
            print("A kiterjesztésnek .pdf formátumúnak kell lennie!")
        num = len(pdfReader.pages)
        start = pdftools.opening(pdfReader,result[int(i)-1].csaladnev,result[int(i)-1].keresztnevek,num)
        end = pdftools.ending(pdfReader,start,num)
        pdftools.output(pdfReader,start,end,filename)
        exit(0)

def main():
    #create CSV
    csvtools.create_csv()
    #open the CSV
    try:
        file = open("kepviselok.csv","rt")
    except FileNotFoundError:
        print("A fajl nem letezik! Generalja a kepviselok neveit a names_to_csv.py-val!")
        exit(-1)
    
    #read MP's name or a character(s)
    text = input("Adjon meg egy kepviselo nevet! ")
    # list all MPs from the CSV
    li = pdftools.import_from_CSV()
    # list all result
    result = search_name(li,text)
    # show all result
    show_all_result(result)
    
    #open the wealth statement
    try:
        pdf = open("Kepviselok_dec_20230712.pdf","rb")
        pdfReader = PyPDF2.PdfReader(pdf)
    except FileNotFoundError:
        print ("Kepviselok_dec_20230712.pdf nem letezik!")
        exit(-1)
    
    #save file and result
    save_file(pdfReader,result)
    file.close()
    pdf.close()

if __name__ == "__main__":
    main()