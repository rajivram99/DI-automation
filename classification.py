from typing import Container
import urllib.request 
from requests.exceptions import HTTPError
import googlesearch
import datetime
from datetime import datetime
from bs4 import BeautifulSoup 
from bs4 import BeautifulSoup as soup
from urllib.request import Request,urlopen 
import PIL.ImageTk
import PIL.Image
import pandas as pd
import os
import ctypes  # An included library with Python install
# Changing the CWD 
os.chdir(os.path.dirname(os.path.abspath(__file__))) 

#tkinter


import tkinter
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkcalendar import DateEntry
import tkinter as tk
root = tk.Tk()
name_var=tk.StringVar()
fromDate_var=tk.StringVar()
toDate_var=tk.StringVar()
num_var = tk.StringVar()
geoL = tk.StringVar()

#validation tkinter - isdigit
def callback(input): 
    if input.isdigit() and int(input) <= 19:
        print(input)
        return True
                          
    elif input == "":
        print(input)
        return True
  
    else:
        print(input)
        return False

#validation tkinter - ischar
def callback1(input): 
    if input.isalpha():
        print(input)
        return True
                          
    elif input == "":
        print(input)
        return True
  
    else:
        print(input)
        return False

#clear or edit
def clear_text():
   nameEntry.delete(0, END)
   numEntry.delete(0, END)
   geoLocation.current(0)

#X button overrriding
def overrideX():
    # check if saving
    # if not:
    root.destroy()

#submit function

def submit():
    global nametk
    global fromDatetk
    global numtk 
    global toDatetk 
    global geotk  
    nametk=name_var.get()
    fromDatetk=fromDate_var.get()
    toDatetk=toDate_var.get()
    numtk = num_var.get()
    geotk = geoL.get()
    print("The company name is : " + nametk)
    print("The from date : " + fromDatetk)
    print("The to date : " + toDatetk)
    print("The links number is : " + numtk)
    print("Geolocation is : " + geotk)
    exit_button =tk.Button(root, text="Start scraping", command=root.destroy).grid(row=9,column=1)
     
root.title("D&I Automation Bot")
root.geometry("900x700")


#Logo Display1 -TMIlogo
#open image
logo1=PIL.Image.open("logo/TMI_Logo.png")
#resize
resized = logo1.resize((250,150),PIL.Image.ANTIALIAS)
new_pic = PIL.ImageTk.PhotoImage(resized)
logo_label = tk.Label(root,image = new_pic)
logo_label.grid(row=0,column=0)

#Logo Display2-TCSlogo
#open image
logo2=PIL.Image.open("logo/TCS_Logo.jpg")
#resize
resized2 = logo2.resize((250,130),PIL.Image.ANTIALIAS)
new_pic2 = PIL.ImageTk.PhotoImage(resized2)
logo_label2 = tk.Label(root,image = new_pic2)
logo_label2.grid(row=0,column=1)

introlabel1 = tk.Label(root,text="DI Automation Bot automatically scales the company's diversity and inclusion parameters \n in a score range of 0 - 5 and also plots the results in bar graphs and dot graph for actionable insights",font="Arial 13 bold underline").grid(row=1,columnspan=2,padx=30, pady=30)


reg1 = root.register(callback1)
nameLabel = tk.Label(root,text="Enter the Company Name",font="Arial 13 bold").grid(row=2)
nameEntry = tk.Entry(root,textvariable=name_var,font="Arial 13 bold",validate="key",validatecommand=(reg1,'%P'))
nameEntry.grid(row=2,column=1,padx=10, pady=10)

fDateEntry = tk.Label(root,text="Enter the From Date",font="Arial 13 bold").grid(row=3)
cal = DateEntry(root,textvariable=fromDate_var,date_pattern='d/m/y',width=12, year=2019, month=1, day=1, 
background='darkblue', foreground='white', borderwidth=2 ,font="Arial 13 bold")
cal.grid(row=3,column=1,padx=10, pady=10)

tDateEntry = tk.Label(root,text="Enter the To Date",font="Arial 13 bold").grid(row=4)
cal = DateEntry(root, textvariable=toDate_var,date_pattern='d/m/y',width=12, year=2020, month=1, day=1, 
background='darkblue', foreground='white', borderwidth=2 ,font="Arial 13 bold")
cal.grid(row=4,column=1,padx=10, pady=10)

reg2 = root.register(callback)
numLabel = tk.Label(root,text="Enter the number of websites to scrape*",font="Arial 13 bold").grid(row=5)
numEntry = tk.Entry(root,textvariable=num_var,font="Arial 13 bold",validate="key",validatecommand=(reg2,'%P'))
numEntry.grid(row=5,column=1,padx=10, pady=10)
clearButton = Button(root,text="Clear All ", command=clear_text, font=('Helvetica bold',10)).grid(row=7,column=1)
submitButton = tk.Button(root,text="Proceed",command=submit).grid(row=8,column=1)

ttk.Label(root,text="Enter Geographical Location",font="Arial 13 bold").grid(row=6,column=0,padx=10, pady=10)
  
l1 = tk.Label(root,text="* Enter the scrape count greater than 5 and less than 20 for robust working of the tool",font="Arial 9").grid(row=10)
l2 = tk.Label(root,text="  Scrape count >20 results in Google_Search_Module error stating *too many requests* ",font="Arial 9").grid(row=11)
geoLocation = ttk.Combobox(root, width = 27, 
                            textvariable = geoL,font="Arial 13 bold")
  
# Adding combobox drop down list
geoLocation['values'] = ('Global', 
                          'North America',
                          'India',
                          'Japan',
                          'UK and Ireland',
                          'Europe',
                          'Latan America', 
                          'Australia and NewZealand', 
                          'Asia Pacific', 
                          'Middle East and Africa')
  
geoLocation.grid(column = 1, row = 6)
  
# Shows february as a default value
geoLocation.current(0) 

 


root.mainloop()
def current_path(): 
    print("Current working directory\n") 
    print(os.getcwd()) 
    print() 

#helper function for get_tbs google search
def get_tbs(from_date, to_date):
    from_date = datetime.strptime(from_date, '%d/%m/%Y')
    from_date = from_date.strftime("%m/%d/%Y")
    to_date = datetime.strptime(to_date, '%d/%m/%Y')
    to_date = to_date.strftime("%m/%d/%Y")
    return 'cdr:1,cd_min:%(from_date)s,cd_max:%(to_date)s' % vars()

def isWordPresentInBusinessWire(sentence, word):
 
    # To convert the word in uppercase
    word = word.upper()
 
    # To convert the complete
    # sentence in uppercase
    sentence = sentence.upper()
 
    # splitting the sentence to list
    lis = sentence.split()
    # checking if word is present
    if(lis.count(word) > 0):
        return True
    else:
        return False

#Try catch block to catch the HTTPS 404 forbidden 
def httpsException(websitelink):
    try:
        response = urllib.request.urlopen(websitelink)
    except urllib.error.HTTPError as exception:
        return False
    else:
        return True

def requestUsingBrowserVersion(link,fileLocation):
    try:
        url= link
        req=Request(url,headers={'User-Agent' : 'Google Chrome/89.0.4389.90 (Official Build) (64-bit)'})
        webpage =urlopen(req).read()
        pageSoup = soup(webpage,"html.parser")
        print(type(pageSoup))
        f = open(fileLocation, "w", encoding="utf8") 
        for data in pageSoup.find_all("p"): 
            sum = data.get_text() 
            print("\n")
            f.writelines(sum) 
    except urllib.error.HTTPError as exception:
        return False
    else:
        return True

def requestUsingBrowserVersion2(link,fileLocation):
    try:
        url= link
        req=Request(url,headers={'User-Agent' : 'Google Chrome/89.0.4389.90 (Official Build) (64-bit)'})
        webpage =urlopen(req).read()
        pageSoup = soup(webpage,"html.parser")
        print(type(pageSoup))
        f = open(fileLocation, "a", encoding="utf8") 
        for data in pageSoup.find_all("p"): 
            sum = data.get_text() 
            print("\n")
            f.writelines(sum) 
    except urllib.error.HTTPError as exception:
        return False
    else:
        return True

#closing or Erasing Files except the test_clean file 
def closeAllFiles():
    for i in range(0,len(foundationScrapeFiles)):
        open(foundationScrapeFiles[i], "w").close()
    open("foundationScrapeFiles/resultSummary.txt", "w").close()
    open("foundationScrapeFiles/test1.txt", "w").close()
    open("foundationScrapeFiles/test_clean.txt", "w").close()
    open("foundationScrapeFiles/result20.txt", "w").close()
    open("foundationScrapeFiles/test_cleanFinal.txt", "w").close()

    if(geotk == "Global"):
        open("geoLocation/GeoLocation.txt", "w").close()


# Changing the CWD 
os.chdir(os.path.dirname(os.path.abspath(__file__))) 
# Printing CWD after 
current_path() 

foundationScrapeFiles=["foundationScrapeFiles/result.txt","foundationScrapeFiles/result1.txt","foundationScrapeFiles/result2.txt","foundationScrapeFiles/result3.txt","foundationScrapeFiles/result4.txt","foundationScrapeFiles/result5.txt","foundationScrapeFiles/result6.txt","foundationScrapeFiles/result7.txt","foundationScrapeFiles/result8.txt","foundationScrapeFiles/result9.txt","foundationScrapeFiles/result10.txt","foundationScrapeFiles/result11.txt","foundationScrapeFiles/result12.txt","foundationScrapeFiles/result13.txt","foundationScrapeFiles/result14.txt","foundationScrapeFiles/result15.txt","foundationScrapeFiles/result16.txt","foundationScrapeFiles/result17.txt","foundationScrapeFiles/result18.txt","foundationScrapeFiles/result19.txt",]

#google search for scraping weblinks
try:
    from googlesearch import search
except:
    print("no module found")
fromDate = fromDatetk
toDate =toDatetk
print(fromDate)
print(" TO \n")
print(toDate)
query = nametk
print(nametk)
print("\n")
numCount = int(numtk)
if(numCount >=18):
    numCount = 18
print(numCount)
print("\n")
result =query +" diversity and inclusion " 
resultBusinessWire = "www.businesswire.com " +query+" diversity and inclusion "
filterdate =get_tbs(fromDate, toDate)
print("Google searching..")
gsearch=[]
for j in search(result, tld="co.in",tbs= filterdate,num=20,start=0, stop=20, pause=2.0): 
    gsearch.append(j)

print("scraped in gsearch new mode")
print(gsearch)


print("fetching data from Businesswire.com")
businesswire=[]
for j in search(resultBusinessWire,num=1,start=0, stop=1, pause=2.0):
    businesswire.append(j)
print("business wire new google search")
print(businesswire[0])

businesswirelink = businesswire[0]
businesswirelinkLower = businesswirelink.lower()
queryLower = query.lower()
if(queryLower in businesswirelinkLower):
    try:
        requestUsingBrowserVersion(businesswire[0], "foundationScrapeFiles/result19.txt")
    except:
        print("Exception while handling businesswire.com website")
else:
    print("no appropriate business wire links")

#remove duplicates
res = []
[res.append(x) for x in gsearch if x not in res]
print(res)
print("\n")

#remove unrelated sites
clean = [x for x in res if '.pdf' not in x and 'youtube' not in x]
cleangsearch =[]
[cleangsearch.append(x) for x in clean if x not in cleangsearch] 
print("\n")

#scarping with the exception handlings
scrapecount=0
print("\n")
print("working on scraping.. \n") 


if(numCount > len(cleangsearch)):
    numCount = len(cleangsearch)

for i in range(0,numCount):
    if(httpsException(cleangsearch[i]) == True):
        scrapecount+=1
        urllib.request.urlretrieve(cleangsearch[i],foundationScrapeFiles[i])
        print("scraping on progress..") 
    else:
        try:
            requestUsingBrowserVersion2(cleangsearch[i], "foundationScrapeFiles/result20.txt")
            scrapecount+=1
        except:
            print("404 forbidden or Exception")
    


scrapecount_str= str(scrapecount)
print("scraped "+ scrapecount_str +" websites successfully")     


# Reading data from files
data = ""
temp = ""
for i in range(0,len(foundationScrapeFiles)-2):
    try:
        with open(foundationScrapeFiles[i],'r',encoding="utf8") as fp: 
            temp = fp.read() 
            data += "\n"
            data += temp
            temp=""
    except:
        print("Exception occured")

#resultSummary.txt has all textfile's html code
with open ('foundationScrapeFiles/resultSummary.txt', 'w',encoding="utf8") as fp: 
    fp.write(data) 
print("cleaning files 1/2...\n")


#read all code from textfile and parse 
file = open("foundationScrapeFiles/resultSummary.txt", "r" , encoding="utf8") 
contents = file.read() 
soup = BeautifulSoup(contents, 'html.parser') 
soup2 =BeautifulSoup(contents, 'html.parser') 

#read files from resul19 (Businesswire.com text file)
with open("foundationScrapeFiles/result19.txt","r",encoding="utf8") as g:
    cont = g.read()
print(cont)
r2 = cont.strip('][').split('\n') 
r2 = list(filter(None, r2))
cleanBW = [x for x in r2 if 'Read more' not in x and 'visit us' not in x and 'phone' not in x and 'website' not in x and 'address' not in x 
and 'call' not in x and '.com' not in x and 'www' not in x and 'next page' not in x and 'read more' not in x and 'related content' not in x and 'suggested' not in x and '2025' not in x and '?' not in x and 'number' not in x
and 'contact' not in x and 'learn more' not in x and 'visit' not in x and 'https' not in x and 'http' not in x and 'news' not in x 
and '<<< End >>>' not in x and '<<< Start >>>' not in x and 'join' not in x and 'agree' not in x and 'yahoo' not in x and 'News' not in x and 'reporter' not in x and 'CNBC' not in x and 'copyright' not in x and 'Copyright' not in x and 'COPYRIGHT' not in x
and 'Telegram' not in x and 'telegram' not in x and 'Photo' not in x ] 
print(cleanBW)
print("cleaning BusinessWire files \n")

#read files from result20.txt (File read from new scrape exception model)
stra = open("foundationScrapeFiles/result20.txt", "r" , encoding="utf8")
cont = stra.read().replace(".", "\n")
stra.close()
r3 = cont.strip('][').split('\n') 
r3 = list(filter(None, r3))
cleanResult20txt = [x for x in r3 if 'Read more' not in x and 'visit us' not in x and 'phone' not in x and 'website' not in x and 'address' not in x 
and 'call' not in x and '.com' not in x and 'www' not in x and 'next page' not in x and 'read more' not in x and 'related content' not in x and 'suggested' not in x and '2025' not in x and '?' not in x and 'number' not in x
and 'contact' not in x and 'learn more' not in x and 'visit' not in x and 'https' not in x and 'http' not in x and 'news' not in x 
and '<<< End >>>' not in x and '<<< Start >>>' not in x and 'join' not in x and 'agree' not in x and 'yahoo' not in x and 'News' not in x and 'reporter' not in x and 'CNBC' not in x and 'copyright' not in x and 'Copyright' not in x and 'COPYRIGHT' not in x
and 'Telegram' not in x and 'telegram' not in x and 'Photo' not in x ] 
print(cleanResult20txt)
print("cleaning BusinessWire files \n")



#write businesswire.com files to test_clean
with open("foundationScrapeFiles/test1.txt","w",encoding="utf8") as f:
    for item in cleanBW:
        f.write("%s\n" % item)

with open("foundationScrapeFiles/test1.txt","a",encoding="utf8") as f:
    for item in cleanResult20txt:
        if '\n' in item:
            f.write(".")
        f.write("%s. \n" % item)

# traverse paragraphs from soup   
f = open("foundationScrapeFiles/test1.txt", "a", encoding="utf8") 
for data in soup.find_all("p"): 
    sum = data.get_text() 
    f.writelines(sum) 

f = open("foundationScrapeFiles/test1.txt", "r", encoding="utf8")
from nltk.tokenize import sent_tokenize
cont = f.read()
token_text =  sent_tokenize(cont)
print("Sentences Tokenised Successfully!!")

f = open("foundationScrapeFiles/test1.txt", "a", encoding="utf8") 
for s in token_text:
    if '.' in s :
        f.write("\n")
    f.writelines(s)

with open("foundationScrapeFiles/test1.txt","r",encoding="utf8") as ff:
    contents2 = ff.read()
print(contents2)
result2 = contents2.strip('][').split('\n') 
result2 = list(filter(None, result2))
cleanres = [x for x in result2 if 'Read more' not in x and 'visit us' not in x and 'phone' not in x and 'website' not in x and 'address' not in x 
and 'call' not in x and '.com' not in x and 'www' not in x and 'next page' not in x and 'read more' not in x and '2022' not in x and '2023' not in x and 
'2024' not in x and '2025' not in x and 'related content' not in x and 'suggested' not in x and '2025' not in x and '?' not in x and 'number' not in x
and 'contact' not in x and 'learn more' not in x and 'visit' not in x and 'https' not in x and 'http' not in x and 'news' not in x 
and '<<< End >>>' not in x and '<<< Start >>>' not in x and 'join' not in x and 'agree' not in x and 'yahoo' not in x and 'News' not in x and '2014' not in x 
and '2015' not in x and '2016' not in x and 'reporter' not in x and 'CNBC' not in x and 'copyright' not in x and 'Copyright' not in x and 'COPYRIGHT' not in x
and 'Telegram' not in x  and 'Photo' not in x ] 


print("cleaning files 2/2..\n")


res = []
[res.append(x) for x in cleanres if x not in res]

#list to file
with open("foundationScrapeFiles/test_clean.txt","w",encoding="utf8") as f:
    for item in res:
        f.write("%s\n" % item)

#remove dups and produce clean file
import hashlib

#1
output_file_path = "foundationScrapeFiles/test_cleanFinal.txt"
input_file_path = "foundationScrapeFiles/test_clean.txt"

#2
completed_lines_hash = set()

#3
output_file = open(output_file_path, "w",encoding='utf8')

#4
for line in open(input_file_path, "r",encoding='utf8'):
	#5
	hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
	#6
	if hashValue not in completed_lines_hash:
		output_file.write(line)
		completed_lines_hash.add(hashValue)
#7
output_file.close()

print("\n")
print("Refer text TestcleanFinal.txt file for results \n")
f.close()

#geoGraphical analysis

with open("geoLocationEdit\INDIA.txt","r",encoding='utf8') as gl1:
    gl1contents = gl1.read()
INDIA = gl1contents.strip('][').split('\n') 
print(INDIA)

with open("geoLocationEdit\JAPAN.txt","r",encoding='utf8') as gl2:
    gl2contents = gl2.read()
JAPAN = gl2contents.strip('][').split('\n') 
print(JAPAN)

with open("geoLocationEdit\APAC.txt","r",encoding='utf8') as gl3:
    gl3contents = gl3.read()
APAC = gl3contents.strip('][').split('\n') 
print(APAC)

with open("geoLocationEdit\AUSNZ.txt","r",encoding='utf8') as gl4:
    gl4contents = gl4.read()
AUSNZ = gl4contents.strip('][').split('\n') 
print(AUSNZ)

with open("geoLocationEdit\EUROPE.txt","r",encoding='utf8') as gl5:
    gl5contents = gl5.read()
EUROPE = gl5contents.strip('][').split('\n') 
print(EUROPE)

with open("geoLocationEdit\LATINAMERICA.txt","r",encoding='utf8') as gl6:
    gl6contents = gl6.read()
LATINAMERICA = gl6contents.strip('][').split('\n') 
print(LATINAMERICA)

with open("geoLocationEdit\MIDEASTAFRICA.txt","r",encoding='utf8') as gl7:
    gl7contents = gl7.read()
MIDEASTAFRICA = gl7contents.strip('][').split('\n') 
print(MIDEASTAFRICA)

with open(r"geoLocationEdit\NA.txt","r",encoding='utf8') as gl8:
    gl8contents = gl8.read()
NA = gl8contents.strip('][').split('\n') 
print(NA)

with open(r"geoLocationEdit\UKI.txt","r",encoding='utf8') as gl9:
    gl9contents = gl9.read()
UKI = gl9contents.strip('][').split('\n') 
print(UKI)
		
with open("foundationScrapeFiles/test_cleanFinal.txt","r",encoding='utf8') as gl:
    glcontents = gl.read()
glcontentsList = glcontents.strip('][').split('\n') 

for i in range(len(APAC)):
    APAC[i] = APAC[i].lower()
for i in range(len(MIDEASTAFRICA)):
    MIDEASTAFRICA[i] = MIDEASTAFRICA[i].lower()

f = open("geoLocation/GeoLocation.txt","w",encoding='utf8')

NA1=[]
UKI1=[]
EUROPE1=[]
LA1=[]
AUSNZ1=[]
APAC1=[]
MIDEASTAFRICA1=[]
INDIA1=[]
JAPAN1=[]

if (geotk == "North America"):
    for item in glcontentsList:
        tempstring = item
        for item1 in NA:
                if(item1.lower() in item.lower()):
                    NA1.append(tempstring)
if (geotk == "India"):
    for item in glcontentsList:
        tempstring = item
        for item1 in INDIA:
                if(item1.lower() in item.lower()):
                    INDIA1.append(tempstring)   
if (geotk == "Japan"):
    for item in glcontentsList:
        tempstring = item
        for item1 in JAPAN:
                if(item1.lower() in item.lower()):
                    JAPAN1.append(tempstring)                                     
if (geotk == "UK and Ireland"):
    for item in glcontentsList:
        tempstring = item
        for item1 in UKI:
                if(item1.lower() in tempstring.lower()):
                    UKI1.append(tempstring)  
if (geotk == "Europe"):
    for item in glcontentsList:
        tempstring = item
        for item1 in EUROPE:
                if(item1.lower() in tempstring.lower()):
                    EUROPE1.append(tempstring)                             
if (geotk == "Latan America"):
    for item in glcontentsList:
        tempstring = item
        for item1 in LATINAMERICA:
                if(item1.lower() in tempstring.lower()):
                    LA1.append(tempstring)
if (geotk == "Australia and NewZealand"):
    for item in glcontentsList:
        tempstring = item
        for item1 in AUSNZ:
                if(item1.lower() in tempstring.lower()):
                    AUSNZ1.append(tempstring)
if (geotk == "Asia Pacific"):
    for item in glcontentsList:
        tempstring = item
        for item1 in APAC:
                if(item1.lower() in tempstring.lower()):
                    APAC1.append(tempstring) 
if (geotk == "Middle East and Africa"):
    for item in glcontentsList:
        tempstring = item
        for item1 in MIDEASTAFRICA:
                if(item1.lower() in tempstring.lower()):
                    MIDEASTAFRICA1.append(tempstring) 

cleanNA = []
[cleanNA.append(x) for x in NA1 if x not in cleanNA]
cleanINDIA = []
[cleanINDIA.append(x) for x in INDIA1 if x not in cleanINDIA]
cleanJAPAN = []
[cleanJAPAN.append(x) for x in JAPAN1 if x not in cleanJAPAN]
cleanUK = []
[cleanUK.append(x) for x in UKI1 if x not in cleanUK]
cleanLA = []
[cleanLA.append(x) for x in LA1 if x not in cleanLA]
cleanEU = []
[cleanEU.append(x) for x in EUROPE1 if x not in cleanEU]
cleanAZ = []
[cleanAZ.append(x) for x in AUSNZ1 if x not in cleanAZ]
cleanAPAC = []
[cleanAPAC.append(x) for x in APAC1 if x not in cleanAPAC]
cleanMEA = []
[cleanMEA.append(x) for x in MIDEASTAFRICA1 if x not in cleanMEA]

if(geotk == "North America" ):
    for i in cleanNA:
        f.write("%s\n" % i)
if(geotk == "UK and Ireland" ):
    for i in cleanUK:
        f.write("%s\n" % i)       
if(geotk == "Europe" ):
    for i in cleanEU:
        f.write("%s\n" % i)
if(geotk == "Latan America" ):
    for i in cleanLA:
        f.write("%s\n" % i)
if(geotk == "Australia and NewZealand" ):
    for i in cleanAZ:
        f.write("%s\n" % i)
if(geotk == "Asia Pacific" ):
    for i in cleanAPAC:
        f.write("%s\n" % i)
if(geotk == "Middle East and Africa"):
    for i in cleanMEA:
        f.write("%s\n" % i)   
if(geotk == "India"):
    for i in cleanINDIA:
        f.write("%s\n" % i) 
if(geotk == "Japan"):
    for i in cleanJAPAN:
        f.write("%s\n" % i) 



#scraping successfull message
ctypes.windll.user32.MessageBoxW(0, "Scraping process successfull", "D&I automation BOT", 1)

#classification Tkinter popup

from tkinter import *
import tkinter as tk
root = tk.Tk()

root.title("Diversity and Inclusion BOT Step-2")
root.geometry("300x300")
closeButton = Button(root, text="Run the NLP", command=root.destroy,height=1 ,width=15,bg="white").place(relx=0.5, rely=0.5,anchor=CENTER)

root.mainloop()




#classification.py


import gensim
import os
# Changing the CWD 
os.chdir(os.path.dirname(os.path.abspath(__file__))) 
import sys
#read from excel file and store in list
import pandas as pd

#NLP using NLTK
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer()
stopwords =['i', 'me', 'my', 'myself', 'we', 'our', 
'ours', 'ourselves', 'you', "you're", "you've", "you'll", 
"you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 
'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 
'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 
'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 
'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 
'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 
'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 
'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 
'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 
'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 
'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 
'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 
'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', 
"should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 
'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', 
"hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', 
"mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 
'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

#function for class list to string 
def listToString(s):  
    str1 = ""    
    for ele in s:  
        str1 += ele   

    return str1  

#marks assignment based on average of list
def Average(nums):
    total = 0
    count = 0
    for x in nums:
       if x > 0:
           total += x
           count += 1

    if(count == 0):
        return 0
    return float(total) / count

def doc2vecRefined(n):
    if(n>=80):
        return 5
    elif(n>=60 and n<80):
        return 4
    elif(n>=40 and n<60):
        return 3
    elif(n>=20 and n<40):
        return 2
    elif(n>=1 and n<20):
        return 1
    else:
        return 0


mylist=[]
from nltk.tokenize import sent_tokenize
#read data from scraped textfile
f = open("foundationScrapeFiles/test_cleanFinal.txt", "r", encoding="utf8")
cont = f.read()
token_text =  sent_tokenize(cont)
print("sentence tokenize success")
for s in token_text:
    mylist.append(s)
print(mylist)
lengthList =len(mylist)

#chapter 1


division=[]
#raw docs for file equaltiy predictions
#thesaurus files for equality predictions
file =  open("thesaurus-files/thesaurus-mission-vision.txt","r",encoding="utf8")
contents=file.read()
vision = contents.strip('][').split('\n') 
print("Number of documents:",len(vision))
print(vision)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in vision]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list1 = []

#loop for sentences
for i in range(lengthList):
    print("\n")
    temppass = listToString(mylist[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])

    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list1.append(0)
        print("No Big matches found")
    else:
        result = (sum/count)
        print("the result in percentage..")
        print(round(result*100))
        result_list1.append(round(result*100))
        sims[query_doc_tf_idf]
        if(round(result*100)>30):
            division.append(temppass)
            print(temppass)
print("the resultant list of chapter 1.........")    
print(result_list1)


#chapter 1.2
diVisionLength= len(division)

#raw docs for file equaltiy predictions
#thesaurus files for equality predictions
file =  open("corpus/foundationVision.txt","r",encoding="utf8")
contents=file.read()
visionCorpus = contents.strip('][').split('\n') 
print("Number of documents:",len(visionCorpus))
print(visionCorpus)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in visionCorpus]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list11 = []
doc2vecsum=0
#loop for sentences
for i in range(diVisionLength):
    print("\n")
    temppass = listToString(division[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    maxi1=[]
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])
        maxi1.append(query_doc_tf_idf[i][1])

    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list11.append(0)
        print("No Big matches found")
    else:
        result = (max(maxi1))
        print("the result in percentage..")
        print(round(result*100))
        result_list11.append(round(result*100))
        doc2vecsum+=round(result*100)
        sims[query_doc_tf_idf]
print("the resultant list of chapter 1.1.........")    
print(division)
print(result_list11)
if(len(division) == 0):
    doc2vecVision = 10
else:
    doc2vecVision = doc2vecsum/diVisionLength




#chapter 2.1

distrategy=[]
#raw docs for file equaltiy predictions
#thesaurus files
file2 =  open("thesaurus-files/thesaurus-strategy-targets.txt","r",encoding="utf8")
contents2=file2.read()
strategy = contents2.strip('][').split('\n') 
print("Number of documents:",len(strategy))


#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in strategy]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list2 = []

#loop for sentences
for i in range(lengthList):
    print("\n")
    temppass = listToString(mylist[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])

    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list2.append(0)
        print("No Big matches found")
    else:
        result = (sum/count)
        print("the result in percentage..")
        print(round(result*100))
        result_list2.append(round(result*100))
        sims[query_doc_tf_idf]
        if(round(result*100)>30):
            distrategy.append(temppass)
            print(temppass)
print("the resultant list is chapter 2.1........")
print(distrategy)
print(result_list2)



#chapter 2.2
diStrategyLength= len(distrategy)


#raw docs for file equaltiy predictions
#thesaurus files for equality predictions
file2 =  open("corpus/foundationStrategy.txt","r",encoding="utf8")
contents=file2.read()
strategyCorpus = contents.strip('][').split('\n') 
print("Number of documents:",len(strategyCorpus))
print(strategyCorpus)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in strategyCorpus]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list21 = []
doc2vecsum=0
#loop for sentences
for i in range(diStrategyLength):
    print("\n")
    temppass = listToString(distrategy[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    maxi2=[]
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])
        maxi2.append(query_doc_tf_idf[i][1])

    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list21.append(0)
        print("No Big matches found")
    else:
        result = (max(maxi2))
        print("the result in percentage..")
        print(round(result*100))
        result_list21.append(round(result*100))
        doc2vecsum+=round(result*100)
        sims[query_doc_tf_idf]
print("the resultant list of chapter 2.2.........")    
print(distrategy)
print(result_list21)
if(len(distrategy) == 0):
    doc2vecStrategy = 10
else:
    doc2vecStrategy = doc2vecsum/diStrategyLength




#chapter 3.1

dileadership=[]
#raw docs for file equaltiy predictions
file3 =  open("thesaurus-files/thesaurus-leadership.txt","r",encoding="utf8")
contents3=file3.read()
leadership = contents3.strip('][').split('\n') 
print("Number of documents:",len(leadership))


#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in leadership]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list3 = []

#loop for sentences
for i in range(lengthList):
    print("\n")
    temppass = listToString(mylist[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])

    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list3.append(0)
        print("No Big matches found")
    else:
        result = (sum/count)
        print("the result in percentage..")
        print(round(result*100))
        result_list3.append(round(result*100))
        sims[query_doc_tf_idf]
        if(round(result*100)>30):
            dileadership.append(temppass)
            print(temppass)
print("the resultant list of chapter 3.1........")
print(dileadership)
print(result_list3)


#chapter 3.2
diLeadershipLength= len(dileadership)


#raw docs for file equaltiy predictions
file3 =  open("corpus/foundationLeadership.txt","r",encoding="utf8")
contents=file3.read()
leadershipCorpus = contents.strip('][').split('\n') 
print("Number of documents:",len(leadershipCorpus))
print(leadershipCorpus)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in leadershipCorpus]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list31 = []
doc2vecsum=0
#loop for sentences
for i in range(diLeadershipLength):
    print("\n")
    temppass = listToString(dileadership[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    maxi3=[]
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])
        maxi3.append(query_doc_tf_idf[i][1])
    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list31.append(0)
        print("No Big matches found")
    else:
        result = (max(maxi3))
        print("the result in percentage..")
        print(round(result*100))
        result_list31.append(round(result*100))
        doc2vecsum+=round(result*100)
        sims[query_doc_tf_idf]
print("the resultant list of chapter 3.2.........")    
print(dileadership)
print(result_list31)
if(len(dileadership) == 0):
    doc2vecLeadership = 10
else:
    doc2vecLeadership = doc2vecsum/diLeadershipLength



#chapter 4.1

diinfrastructure=[]
#raw docs for file equaltiy predictions
file4 =  open("thesaurus-files/thesaurus-infrastructure.txt","r",encoding="utf8")
contents4=file4.read()
infrastructure = contents4.strip('][').split('\n') 
print("Number of documents:",len(infrastructure))


#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in infrastructure]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list4 = []

#loop for sentences
for i in range(lengthList):
    print("\n")
    temppass = listToString(mylist[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])

    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list4.append(0)
        print("No Big matches found")
    else:
        result = (sum/count)
        print("the result in percentage..")
        print(round(result*100))
        result_list4.append(round(result*100))
        sims[query_doc_tf_idf]
        if(round(result*100)>30):
            diinfrastructure.append(temppass)
            print(temppass)
print("the resultant list of chapter 4.1.........")
print(result_list4)


#chapter 4.2
diInfrastructureLength= len(diinfrastructure)


#raw docs for file equaltiy predictions
file4 =  open("corpus/foundationInfrastructure.txt","r",encoding="utf8")
contents=file4.read()
infrastructureCorpus = contents.strip('][').split('\n') 
print("Number of documents:",len(infrastructureCorpus))
print(infrastructureCorpus)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in infrastructureCorpus]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list41 = []
doc2vecsum=0
#loop for sentences
for i in range(diInfrastructureLength):
    print("\n")
    temppass = listToString(diinfrastructure[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    maxi=[]
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])
        maxi.append(query_doc_tf_idf[i][1])
    
    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list41.append(0)
        print("No Big matches found")
    else:
        result = (max(maxi))
        print("the result in percentage..")
        print(round(result*100))
        result_list41.append(round(result*100))
        doc2vecsum+=round(result*100)
        sims[query_doc_tf_idf]
print("the resultant list of chapter 4.2.........")    
print(diinfrastructure)
print(result_list41)
if(len(diinfrastructure) == 0):
    doc2vecInfrastructure = 10
else:
    doc2vecInfrastructure = doc2vecsum / diInfrastructureLength


#Initiatives
#--------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------

#chapter 2.1.1

diawareness=[]
#raw docs for file equaltiy predictions
#thesaurus files for equality predictions
Ifile1 =  open("thesaurus-files/thesaurus-awareness.txt","r",encoding="utf8")
contents=Ifile1.read()
awareness = contents.strip('][').split('\n') 
print("Number of documents:",len(awareness))
print(awareness)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in awareness]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_init1 = []

#loop for sentences
for i in range(lengthList):
    print("\n")
    temppass = listToString(mylist[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])

    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_init1.append(0)
        print("No Big matches found")
    else:
        result = (sum/count)
        print("the result in percentage..")
        print(round(result*100))
        result_list_init1.append(round(result*100))
        sims[query_doc_tf_idf]
        if(round(result*100)>30):
            diawareness.append(temppass)
            print(temppass)
print("the resultant list of chapter 2.1.1.........")    
print(diawareness)

#chapter 2.1.2
diawarenessLength= len(diawareness)


#raw docs for file equaltiy predictions
Ifile2 =  open("corpus/initiativesAwareness.txt","r",encoding="utf8")
contents=Ifile2.read()
awarenessCorpus = contents.strip('][').split('\n') 
print("Number of documents:",len(awarenessCorpus))
print(awarenessCorpus)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in awarenessCorpus]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_init11 = []
doc2vecsum=0
#loop for sentences
for i in range(diawarenessLength):
    print("\n")
    temppass = listToString(diawareness[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    maxi=[]
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])
        maxi.append(query_doc_tf_idf[i][1])
    
    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_init11.append(0)
        print("No Big matches found")
    else:
        result = (max(maxi))
        print("the result in percentage..")
        print(round(result*100))
        result_list_init11.append(round(result*100))
        doc2vecsum+=round(result*100)
        sims[query_doc_tf_idf]
print("the resultant list of chapter 2.1.2.........")    
print(diawareness)
print(result_list_init11)
if(len(diawareness) == 0):
    doc2vecawareness = 10
else:
    doc2vecawareness = doc2vecsum / diawarenessLength




#chapter 2.2.1

disteering=[]
#raw docs for file equaltiy predictions
#thesaurus files for equality predictions
Ifile3 =  open("thesaurus-files/thesaurus-steeringCommittees.txt","r",encoding="utf8")
contents=Ifile3.read()
steering = contents.strip('][').split('\n') 
print("Number of documents:",len(steering))
print(steering)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in steering]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_init2 = []

#loop for sentences
for i in range(lengthList):
    print("\n")
    temppass = listToString(mylist[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])

    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_init2.append(0)
        print("No Big matches found")
    else:
        result = (sum/count)
        print("the result in percentage..")
        print(round(result*100))
        result_list_init2.append(round(result*100))
        sims[query_doc_tf_idf]
        if(round(result*100)>30):
            disteering.append(temppass)
            print(temppass)
print("the resultant list of chapter 2.2.1.........")    
print(disteering)

#chapter 2.2.2
disteeringLength= len(disteering)


#raw docs for file equaltiy predictions
Ifile4 =  open("corpus/initiativesSteeringCommittee.txt","r",encoding="utf8")
contents=Ifile4.read()
steeringCorpus = contents.strip('][').split('\n') 
print("Number of documents:",len(steeringCorpus))
print(steeringCorpus)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in steeringCorpus]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_init21 = []
doc2vecsum=0
#loop for sentences
for i in range(disteeringLength):
    print("\n")
    temppass = listToString(disteering[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    maxi=[]
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])
        maxi.append(query_doc_tf_idf[i][1])
    
    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_init21.append(0)
        print("No Big matches found")
    else:
        result = (max(maxi))
        print("the result in percentage..")
        print(round(result*100))
        result_list_init21.append(round(result*100))
        doc2vecsum+=round(result*100)
        sims[query_doc_tf_idf]
print("the resultant list of chapter 2.2.2........")    
print(disteering)
print(result_list_init21)
if(len(disteering) == 0):
    doc2vecsteering = 10
else:
    doc2vecsteering = doc2vecsum / disteeringLength





#chapter 2.3.1

digenderparity=[]
#raw docs for file equaltiy predictions
#thesaurus files for equality predictions
Ifile5 =  open("thesaurus-files/thesaurus-genderparity.txt","r",encoding="utf8")
contents=Ifile5.read()
genderparity = contents.strip('][').split('\n') 
print("Number of documents:",len(genderparity))
print(genderparity)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in genderparity]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_init3 = []

#loop for sentences
for i in range(lengthList):
    print("\n")
    temppass = listToString(mylist[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])

    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_init3.append(0)
        print("No Big matches found")
    else:
        result = (sum/count)
        print("the result in percentage..")
        print(round(result*100))
        result_list_init3.append(round(result*100))
        sims[query_doc_tf_idf]
        if(round(result*100)>30):
            digenderparity.append(temppass)
            print(temppass)
print("the resultant list of chapter 2.3.1.........")    
print(digenderparity)

#chapter 2.3.2
digenderparityLength= len(digenderparity)


#raw docs for file equaltiy predictions
Ifile6 =  open("corpus/initiativesGenderAndPayParity.txt","r",encoding="utf8")
contents=Ifile6.read()
genderparityCorpus = contents.strip('][').split('\n') 
print("Number of documents:",len(genderparityCorpus))
print(genderparityCorpus)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in genderparityCorpus]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_init31 = []
doc2vecsum=0
#loop for sentences
for i in range(digenderparityLength):
    print("\n")
    temppass = listToString(digenderparity[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    maxi=[]
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])
        maxi.append(query_doc_tf_idf[i][1])
    
    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_init31.append(0)
        print("No Big matches found")
    else:
        result = (max(maxi))
        print("the result in percentage..")
        print(round(result*100))
        result_list_init31.append(round(result*100))
        doc2vecsum+=round(result*100)
        sims[query_doc_tf_idf]
print("the resultant list of chapter 2.3.2........")    
print(digenderparity)
print(result_list_init31)
if(len(digenderparity) == 0):
    doc2vecgenderparity = 10
else:
    doc2vecgenderparity = doc2vecsum / digenderparityLength






#chapter 2.4.1

didemographicalHiring=[]
#raw docs for file equaltiy predictions
#thesaurus files for equality predictions
Ifile7 =  open("thesaurus-files/thesaurus-demographicalhiring.txt","r",encoding="utf8")
contents=Ifile7.read()
demographicalhiring = contents.strip('][').split('\n') 
print("Number of documents:",len(demographicalhiring))
print(demographicalhiring)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in demographicalhiring]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_init4 = []

#loop for sentences
for i in range(lengthList):
    print("\n")
    temppass = listToString(mylist[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])

    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_init4.append(0)
        print("No Big matches found")
    else:
        result = (sum/count)
        print("the result in percentage..")
        print(round(result*100))
        result_list_init4.append(round(result*100))
        sims[query_doc_tf_idf]
        if(round(result*100)>30):
            didemographicalHiring.append(temppass)
            print(temppass)
print("the resultant list of chapter 2.4.1.........")    
print(didemographicalHiring)

#chapter 2.4.2
didemographicalHiringLength= len(didemographicalHiring)


#raw docs for file equaltiy predictions
Ifile8 =  open("corpus/initiativesDemographicalHiring.txt","r",encoding="utf8")
contents=Ifile8.read()
demographicalHiringCorpus = contents.strip('][').split('\n') 
print("Number of documents:",len(demographicalHiringCorpus))
print(demographicalHiringCorpus)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in demographicalHiringCorpus]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_init41 = []
doc2vecsum=0
#loop for sentences
for i in range(didemographicalHiringLength):
    print("\n")
    temppass = listToString(didemographicalHiring[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    maxi=[]
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])
        maxi.append(query_doc_tf_idf[i][1])
    
    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_init41.append(0)
        print("No Big matches found")
    else:
        result = (max(maxi))
        print("the result in percentage..")
        print(round(result*100))
        result_list_init41.append(round(result*100))
        doc2vecsum+=round(result*100)
        sims[query_doc_tf_idf]
print("the resultant list of chapter 2.4.2........")    
print(didemographicalHiring)
print(result_list_init41)
print(didemographicalHiring)
if(len(didemographicalHiring) == 0):
    doc2vecdemographicalHiring = 10
else:
    doc2vecdemographicalHiring = doc2vecsum / didemographicalHiringLength




#chapter 2.5.1

dimentorsponsor=[]
#raw docs for file equaltiy predictions
#thesaurus files for equality predictions
Ifile9 =  open("thesaurus-files/thesaurus-mentoring.txt","r",encoding="utf8")
contents=Ifile9.read()
mentorsponsor = contents.strip('][').split('\n') 
print("Number of documents:",len(mentorsponsor))
print(mentorsponsor)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in mentorsponsor]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_init5 = []

#loop for sentences
for i in range(lengthList):
    print("\n")
    temppass = listToString(mylist[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])

    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_init5.append(0)
        print("No Big matches found")
    else:
        result = (sum/count)
        print("the result in percentage..")
        print(round(result*100))
        result_list_init5.append(round(result*100))
        sims[query_doc_tf_idf]
        if(round(result*100)>30):
            dimentorsponsor.append(temppass)
            print(temppass)
print("the resultant list of chapter 2.5.1.........")    
print(dimentorsponsor)

#chapter 2.5.2
dimentorsponsorLength= len(dimentorsponsor)


#raw docs for file equaltiy predictions
Ifile10 =  open("corpus/initiativesDemographicalHiring.txt","r",encoding="utf8")
contents=Ifile10.read()
mentorsponsorCorpus = contents.strip('][').split('\n') 
print("Number of documents:",len(mentorsponsorCorpus))
print(mentorsponsorCorpus)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in mentorsponsorCorpus]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_init51 = []
doc2vecsum=0
#loop for sentences
for i in range(dimentorsponsorLength):
    print("\n")
    temppass = listToString(dimentorsponsor[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    maxi=[]
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])
        maxi.append(query_doc_tf_idf[i][1])
    
    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_init51.append(0)
        print("No Big matches found")
    else:
        result = (max(maxi))
        print("the result in percentage..")
        print(round(result*100))
        result_list_init51.append(round(result*100))
        doc2vecsum+=round(result*100)
        sims[query_doc_tf_idf]
print("the resultant list of chapter 2.5.2........")    
print(dimentorsponsor)
print(result_list_init51)
if(len(dimentorsponsor) == 0):
    doc2vecmentorsponsor = 10
else:
    doc2vecmentorsponsor = doc2vecsum / dimentorsponsorLength



#chapter 2.6.1


ditechnologies=[]
#raw docs for file equaltiy predictions
#thesaurus files for equality predictions
Ifile11 =  open("thesaurus-files/thesaurus-technologies.txt","r",encoding="utf8")
contents=Ifile11.read()
technologies = contents.strip('][').split('\n') 
print("Number of documents:",len(technologies))
print(technologies)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in technologies]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_init6 = []
maxi=0
doc2vecsum=0
count=0
#loop for sentences
for i in range(lengthList):
    print("\n")
    temppass = listToString(mylist[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    sum=0
    temp=0
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        doc2vecsum+=temp
        count+=1
        print (query_doc_tf_idf[i][1])

    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_init6.append(0)
        print("No Big matches found")
    else:
        result = (sum/count)
        print("the result in percentage..")
        print(round(result*100))
        result_list_init6.append(round(result*100))
        sims[query_doc_tf_idf]
        if(round(result*100)>30):
            ditechnologies.append(temppass)
            print(temppass)
print("the resultant list of chapter 2.6.1.........")    
print(ditechnologies)
if(count == 0):
    doc2vectechnologies = 45
else:
    doc2vectechnologies = (doc2vecsum/count)*100



#chapter 2.7.1

diservices=[]
#raw docs for file equaltiy predictions
#thesaurus files for equality predictions
Ifile12 =  open("thesaurus-files/thesaurus-services.txt","r",encoding="utf8")
contents=Ifile12.read()
services = contents.strip('][').split('\n') 
print("Number of documents:",len(services))
print(services)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in services]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_init7 = []

#loop for sentences
for i in range(lengthList):
    print("\n")
    temppass = listToString(mylist[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])

    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_init7.append(0)
        print("No Big matches found")
    else:
        result = (sum/count)
        print("the result in percentage..")
        print(round(result*100))
        result_list_init7.append(round(result*100))
        sims[query_doc_tf_idf]
        if(round(result*100)>30):
            diservices.append(temppass)
            print(temppass)
print("the resultant list of chapter 2.7.1.........")    
print(diservices)

#chapter 2.5.2
diservicesLength= len(diservices)


#raw docs for file equaltiy predictions
Ifile13 =  open("corpus/initiativesServices.txt","r",encoding="utf8")
contents=Ifile13.read()
servicesCorpus = contents.strip('][').split('\n') 
print("Number of documents:",len(servicesCorpus))
print(servicesCorpus)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in servicesCorpus]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_init71 = []
doc2vecsum=0
#loop for sentences
for i in range(diservicesLength):
    print("\n")
    temppass = listToString(diservices[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    maxi=[]
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])
        maxi.append(query_doc_tf_idf[i][1])
    
    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_init71.append(0)
        print("No Big matches found")
    else:
        result = (max(maxi))
        print("the result in percentage..")
        print(round(result*100))
        result_list_init71.append(round(result*100))
        doc2vecsum+=round(result*100)
        sims[query_doc_tf_idf]
print("the resultant list of chapter 2.7.2........")    
print(diservices)
print(len(diservices))
print(result_list_init71)
if(len(diservices) == 0):
    doc2vecservices = 10
else:
    doc2vecservices = doc2vecsum / diservicesLength




#Bridging
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------


#chapter 3.1.1

dicommunication=[]
#raw docs for file equaltiy predictions
file30 =  open("thesaurus-files/thesaurus-communication.txt","r",encoding="utf8")
contents4=file30.read()
communication = contents4.strip('][').split('\n') 
print("Number of documents:",len(communication))


#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in communication]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_brid1 = []

#loop for sentences
for i in range(lengthList):
    print("\n")
    temppass = listToString(mylist[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])

    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_brid1.append(0)
        print("No Big matches found")
    else:
        result = (sum/count)
        print("the result in percentage..")
        print(round(result*100))
        result_list_brid1.append(round(result*100))
        sims[query_doc_tf_idf]
        if(round(result*100)>30):
            dicommunication.append(temppass)
            print(temppass)
print("the resultant list of chapter 4.1.........")
print(result_list_brid1)


#chapter 3.1.2
dicommunicationLength= len(dicommunication)


#raw docs for file equaltiy predictions
file31 =  open("corpus/bridgingCommunication.txt","r",encoding="utf8")
contents=file31.read()
communicationCorpus = contents.strip('][').split('\n') 
print("Number of documents:",len(communicationCorpus))
print(communicationCorpus)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in communicationCorpus]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_brid11 = []
doc2vecsum=0
#loop for sentences
for i in range(dicommunicationLength):
    print("\n")
    temppass = listToString(dicommunication[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    maxi=[]
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])
        maxi.append(query_doc_tf_idf[i][1])
    
    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_brid11.append(0)
        print("No Big matches found")
    else:
        result = (max(maxi))
        print("the result in percentage..")
        print(round(result*100))
        result_list_brid11.append(round(result*100))
        doc2vecsum+=round(result*100)
        sims[query_doc_tf_idf]
print("the resultant list of chapter 4.2.........")    
print(len(dicommunication))
print(dicommunication)
print(result_list_brid11)
if(len(dicommunication) == 0):
    doc2veccommunication = 10
else:
    doc2veccommunication = doc2vecsum / dicommunicationLength



#chapter 3.2.1

dipolicy=[]

#raw docs for file equaltiy predictions
file32 =  open("thesaurus-files/thesaurus-policy.txt","r",encoding="utf8")
contents4=file32.read()
policy = contents4.strip('][').split('\n') 
print("Number of documents:",len(policy))


#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in policy]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_brid21 = []

doc2vecsum=0
#loop for sentences
for i in range(lengthList):
    print("\n")
    temppass = listToString(mylist[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    maxi=[]
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])
        maxi.append(query_doc_tf_idf[i][1])

    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        print("No Big matches found")
    else:
        result = (max(maxi))
        print("the result in percentage..")
        print(round(result*100))
        sims[query_doc_tf_idf]
        if(round(result*100)>30):
            result_list_brid21.append(round(result*100))
            doc2vecsum+=round(result*100)
            sims[query_doc_tf_idf]
            dipolicy.append(temppass)

print("the resultant list of chapter 3.2.1........")    
print(len(dipolicy))
print(dipolicy)
dipolicyLength=len(dipolicy)
print(result_list_brid21)
if(len(dipolicy) == 0):
    doc2vecpolicy = 10
else:
    doc2vecpolicy = doc2vecsum / dipolicyLength



#chapter 3.3.1

ditraining=[]
#raw docs for file equaltiy predictions
file34 =  open("thesaurus-files/thesaurus-training.txt","r",encoding="utf8")
contents4=file34.read()
training = contents4.strip('][').split('\n') 
print("Number of documents:",len(training))


#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in training]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_brid3 = []

#loop for sentences
for i in range(lengthList):
    print("\n")
    temppass = listToString(mylist[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])

    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_brid3.append(0)
        print("No Big matches found")
    else:
        result = (sum/count)
        print("the result in percentage..")
        print(round(result*100))
        result_list_brid3.append(round(result*100))
        sims[query_doc_tf_idf]
        if(round(result*100)>30):
            ditraining.append(temppass)
            print(temppass)
print("the resultant list of chapter 4.1.........")
print(result_list_brid3)


#chapter 3.3.2
ditrainingLength= len(ditraining)


#raw docs for file equaltiy predictions
file35 =  open("corpus/bridgingTrainings.txt","r",encoding="utf8")
contents=file35.read()
trainingCorpus = contents.strip('][').split('\n') 
print("Number of documents:",len(trainingCorpus))
print(trainingCorpus)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in trainingCorpus]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_brid31 = []
doc2vecsum=0
#loop for sentences
for i in range(ditrainingLength):
    print("\n")
    temppass = listToString(ditraining[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    maxi=[]
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])
        maxi.append(query_doc_tf_idf[i][1])
    
    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_brid31.append(0)
        print("No Big matches found")
    else:
        result = (max(maxi))
        print("the result in percentage..")
        print(round(result*100))
        result_list_brid31.append(round(result*100))
        doc2vecsum+=round(result*100)
        sims[query_doc_tf_idf]
print("the resultant list of chapter 4.2.........")    
print(len(ditraining))
print(ditraining)
print(result_list_brid31)
if(len(ditraining) == 0):
    doc2vectraining = 10
else:
    doc2vectraining = doc2vecsum / ditrainingLength



#chapter 3.4.1

dicollaboration=[]
#raw docs for file equaltiy predictions
file36 =  open("thesaurus-files/thesaurus-collaboration.txt","r",encoding="utf8")
contents4=file36.read()
collaboration = contents4.strip('][').split('\n') 
print("Number of documents:",len(collaboration))


#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in collaboration]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_brid4 = []

#loop for sentences
for i in range(lengthList):
    print("\n")
    temppass = listToString(mylist[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])

    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_brid4.append(0)
        print("No Big matches found")
    else:
        result = (sum/count)
        print("the result in percentage..")
        print(round(result*100))
        result_list_brid4.append(round(result*100))
        sims[query_doc_tf_idf]
        if(round(result*100)>30):
            dicollaboration.append(temppass)
            print(temppass)
print("the resultant list of chapter 4.1.........")
print(result_list_brid4)


#chapter 3.4.2
dicollaborationLength= len(dicollaboration)


#raw docs for file equaltiy predictions
file37 =  open("corpus/bridgingCollaboration.txt","r",encoding="utf8")
contents=file37.read()
collaborationCorpus = contents.strip('][').split('\n') 
print("Number of documents:",len(collaborationCorpus))
print(collaborationCorpus)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in collaborationCorpus]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_brid41 = []
doc2vecsum=0
#loop for sentences
for i in range(dicollaborationLength):
    print("\n")
    temppass = listToString(dicollaboration[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    maxi=[]
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])
        maxi.append(query_doc_tf_idf[i][1])
    
    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_brid41.append(0)
        print("No Big matches found")
    else:
        result = (max(maxi))
        print("the result in percentage..")
        print(round(result*100))
        result_list_brid41.append(round(result*100))
        doc2vecsum+=round(result*100)
        sims[query_doc_tf_idf]
print("the resultant list of chapter 4.2.........")    
print(len(dicollaboration))
print(dicollaboration)
print(result_list_brid41)
if(len(dicollaboration) == 0):
    doc2veccollaboration = 10
else:
    doc2veccollaboration = doc2vecsum / dicollaborationLength



#chapter 3.5.1

direports=[]
#raw docs for file equaltiy predictions
file38 =  open("thesaurus-files/thesaurus-reports.txt","r",encoding="utf8")
contents4=file38.read()
reports = contents4.strip('][').split('\n') 
print("Number of documents:",len(reports))


#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in reports]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_brid5 = []

#loop for sentences
for i in range(lengthList):
    print("\n")
    temppass = listToString(mylist[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])

    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_brid5.append(0)
        print("No Big matches found")
    else:
        result = (sum/count)
        print("the result in percentage..")
        print(round(result*100))
        result_list_brid5.append(round(result*100))
        sims[query_doc_tf_idf]
        if(round(result*100)>30):
            direports.append(temppass)
            print(temppass)
print("the resultant list of chapter 3.5.1........")
print(result_list_brid5)


#chapter 3.5.2
direportsLength= len(direports)


#raw docs for file equaltiy predictions
file39 =  open("corpus/bridgingReports.txt","r",encoding="utf8")
contents=file39.read()
reportsCorpus = contents.strip('][').split('\n') 
print("Number of documents:",len(reportsCorpus))
print(reportsCorpus)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in reportsCorpus]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_brid51 = []
doc2vecsum=0
#loop for sentences
for i in range(direportsLength):
    print("\n")
    temppass = listToString(direports[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    maxi=[]
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])
        maxi.append(query_doc_tf_idf[i][1])
    
    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_brid51.append(0)
        print("No Big matches found")
    else:
        result = (max(maxi))
        print("the result in percentage..")
        print(round(result*100))
        result_list_brid51.append(round(result*100))
        doc2vecsum+=round(result*100)
        sims[query_doc_tf_idf]
print("the resultant list of chapter 4.2.........")    
print(len(direports))
print(direports)
print(result_list_brid51)
if(len(direports) == 0):
    doc2vecreports = 10
else:
    doc2vecreports = doc2vecsum / direportsLength



#chapter 3.6.1

dicsr=[]
#raw docs for file equaltiy predictions
file40 =  open("thesaurus-files/thesaurus-csr.txt","r",encoding="utf8")
contents4=file40.read()
csr = contents4.strip('][').split('\n') 
print("Number of documents:",len(csr))


#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in csr]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_brid6 = []

#loop for sentences
for i in range(lengthList):
    print("\n")
    temppass = listToString(mylist[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])

    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_brid6.append(0)
        print("No Big matches found")
    else:
        result = (sum/count)
        print("the result in percentage..")
        print(round(result*100))
        result_list_brid6.append(round(result*100))
        sims[query_doc_tf_idf]
        if(round(result*100)>30):
            dicsr.append(temppass)
            print(temppass)
print("the resultant list of chapter 3.5.1........")
print(result_list_brid6)


#chapter 3.6.2
dicsrLength= len(dicsr)


#raw docs for file equaltiy predictions
file41 =  open("corpus/bridgingReports.txt","r",encoding="utf8")
contents=file41.read()
csrCorpus = contents.strip('][').split('\n') 
print("Number of documents:",len(csrCorpus))
print(csrCorpus)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in csrCorpus]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_brid61 = []
doc2vecsum=0
#loop for sentences
for i in range(dicsrLength):
    print("\n")
    temppass = listToString(dicsr[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    maxi=[]
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])
        maxi.append(query_doc_tf_idf[i][1])
    
    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_brid61.append(0)
        print("No Big matches found")
    else:
        result = (max(maxi))
        print("the result in percentage..")
        print(round(result*100))
        result_list_brid61.append(round(result*100))
        doc2vecsum+=round(result*100)
        sims[query_doc_tf_idf]
print("the resultant list of chapter 4.2.........")    
print(len(dicsr))
print(dicsr)
print(result_list_brid61)
if(len(dicsr) == 0):
    doc2veccsr = 10
else:
    doc2veccsr = doc2vecsum / dicsrLength




#chapter 3.7.1

disurvey=[]
#raw docs for file equaltiy predictions
file42 =  open("thesaurus-files/thesaurus-survey.txt","r",encoding="utf8")
contents4=file42.read()
survey = contents4.strip('][').split('\n') 
print("Number of documents:",len(survey))


#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in survey]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_brid7 = []

#loop for sentences
for i in range(lengthList):
    print("\n")
    temppass = listToString(mylist[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])

    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_brid7.append(0)
        print("No Big matches found")
    else:
        result = (sum/count)
        print("the result in percentage..")
        print(round(result*100))
        result_list_brid7.append(round(result*100))
        sims[query_doc_tf_idf]
        if(round(result*100)>30):
            disurvey.append(temppass)
            print(temppass)
print("the resultant list of chapter 3.7.1........")
print(result_list_brid7)


#chapter 3.7.2
disurveyLength= len(disurvey)


#raw docs for file equaltiy predictions
file43 =  open("corpus/bridgingReports.txt","r",encoding="utf8")
contents=file43.read()
surveyCorpus = contents.strip('][').split('\n') 
print("Number of documents:",len(surveyCorpus))
print(surveyCorpus)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in surveyCorpus]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_brid71 = []
doc2vecsum=0
#loop for sentences
for i in range(disurveyLength):
    print("\n")
    temppass = listToString(disurvey[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    maxi=[]
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])
        maxi.append(query_doc_tf_idf[i][1])
    
    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_brid71.append(0)
        print("No Big matches found")
    else:
        result = (max(maxi))
        print("the result in percentage..")
        print(round(result*100))
        result_list_brid71.append(round(result*100))
        doc2vecsum+=round(result*100)
        sims[query_doc_tf_idf]
print("the resultant list of chapter 3.7.2........")    
print(len(disurvey))
print(disurvey)
print(result_list_brid71)
if(len(disurvey) == 0):
    doc2vecsurvey = 10
else:
    doc2vecsurvey = doc2vecsum / disurveyLength



#---------------------------------OUTCOMES-------------------------------------------#
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------#

#chapter 4.1.1


dithoughtLeadership=[]
#raw docs for file equaltiy predictions
#thesaurus files for equality predictions
Ifile50 =  open("thesaurus-files/thesaurus-thoughtLeadership.txt","r",encoding="utf8")
contents=Ifile50.read()
thoughtleadership = contents.strip('][').split('\n') 
print("Number of documents:",len(thoughtleadership))
print(thoughtleadership)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in thoughtleadership]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_outc1 = []

#loop for sentences
for i in range(lengthList):
    print("\n")
    temppass = listToString(mylist[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])

    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_outc1.append(0)
        print("No Big matches found")
    else:
        result = (sum/count)
        print("the result in percentage..")
        print(round(result*100))
        result_list_outc1.append(round(result*100))
        sims[query_doc_tf_idf]
        if(round(result*100)>30):
            dithoughtLeadership.append(temppass)
            print(temppass)
print("the resultant list of chapter 2.5.1.........")    
print(dithoughtLeadership)

#chapter 4.1.2
dithoughtLeadershipLength= len(dithoughtLeadership)


#raw docs for file equaltiy predictions
Ifile51 =  open("corpus/outcomesThoughtLeadership.txt","r",encoding="utf8")
contents=Ifile51.read()
thoughtleadershipcorpus = contents.strip('][').split('\n') 
print("Number of documents:",len(thoughtleadershipcorpus))
print(thoughtleadershipcorpus)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in thoughtleadershipcorpus]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_outc11 = []
doc2vecsum=0
#loop for sentences
for i in range(dithoughtLeadershipLength):
    print("\n")
    temppass = listToString(dithoughtLeadership[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    maxi=[]
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])
        maxi.append(query_doc_tf_idf[i][1])
    
    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_outc11.append(0)
        print("No Big matches found")
    else:
        result = (max(maxi))
        print("the result in percentage..")
        print(round(result*100))
        result_list_outc11.append(round(result*100))
        doc2vecsum+=round(result*100)
        sims[query_doc_tf_idf]
print("the resultant list of chapter 2.5.2........")    
print(dithoughtLeadership)
print(result_list_outc11)
if(len(dithoughtLeadership) == 0):
    doc2vecthoughtLeadership = 10
else:
    doc2vecthoughtLeadership = doc2vecsum / dithoughtLeadershipLength

print(dithoughtLeadership)
print(result_list_outc11)
print(doc2vecthoughtLeadership)



#chapter 4.2.1

diawards=[]
#raw docs for file equaltiy predictions
#thesaurus files for equality predictions
Ifile52 =  open("thesaurus-files/thesaurus-awards.txt","r",encoding="utf8")
contents=Ifile52.read()
awards = contents.strip('][').split('\n') 
print("Number of documents:",len(awards))
print(awards)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in awards]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_outc2 = []

#loop for sentences
for i in range(lengthList):
    print("\n")
    temppass = listToString(mylist[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])

    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_outc2.append(0)
        print("No Big matches found")
    else:
        result = (sum/count)
        print("the result in percentage..")
        print(round(result*100))
        result_list_outc2.append(round(result*100))
        sims[query_doc_tf_idf]
        if(round(result*100)>30):
            diawards.append(temppass)
            print(temppass)
print("the resultant list of chapter 2.5.1.........")    
print(diawards)

#chapter 4.2.2
diawardsLength= len(diawards)


#raw docs for file equaltiy predictions
Ifile52 =  open("corpus/outcomesAwards.txt","r",encoding="utf8")
contents=Ifile52.read()
awardscorpus = contents.strip('][').split('\n') 
print("Number of documents:",len(awardscorpus))
print(awardscorpus)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in awardscorpus]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_outc21 = []
doc2vecsum=0
#loop for sentences
for i in range(diawardsLength):
    print("\n")
    temppass = listToString(diawards[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    maxi=[]
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])
        maxi.append(query_doc_tf_idf[i][1])
    
    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_outc21.append(0)
        print("No Big matches found")
    else:
        result = (max(maxi))
        print("the result in percentage..")
        print(round(result*100))
        result_list_outc21.append(round(result*100))
        doc2vecsum+=round(result*100)
        sims[query_doc_tf_idf]
print("the resultant list of chapter 4.2.2........")    
if(len(diawards) == 0):
    doc2vecawards = 10
else:
    doc2vecawards = doc2vecsum / diawardsLength

print(diawards)
print(result_list_outc21)
print(doc2vecawards)



#chapter 4.3.1
disocialmedia = []
result_list_outc3 = []
doc2vecsum=0
count=0
for i in range(0,len(mylist)):
    tempstring = mylist[i]
    tempstringLower = tempstring.lower()
    tempstringSplit = tempstringLower.split()
    if("like" not in tempstringSplit and "subscribe" not in tempstringSplit and "followus" not in tempstringSplit and "follow us" not in tempstringSplit and "follow" not in tempstringSplit and "contact" not in tempstringSplit and "support" not in tempstringSplit and "read more" not in tempstringSplit and "readmore" not in tempstringSplit and "follows" not in tempstringSplit and "likes" not in tempstringSplit and "subscribers" not in tempstringSplit and "contact" not in tempstringSplit and  "contact:" not in tempstringSplit and  "click" not in tempstringSplit and "phone:" not in tempstringSplit and "sign in" not in tempstringSplit and "all rights reserved." not in tempstringSplit):
        print(tempstringSplit)
        if("social media traction" in tempstringLower or "linkedin" in tempstringLower or "facebook" in tempstringLower or "instagram" in tempstringLower or "twitter" in tempstringLower or "tweet" in tempstringLower or "media traction" in tempstringLower or "social media" in tempstringLower or "hashtag" in tempstringLower or "tweets" in tempstringLower or "tweetstorm" in tempstringLower or "hashtags" in tempstringLower):
            print(tempstringLower)
            disocialmedia.append(tempstring)
            result_list_outc3.append(int(4))
            doc2vecsum+=4
            count+=1
if(count > 0):
    doc2vecsocialmedia = doc2vecsum / count
else:
    doc2vecsocialmedia = 10
print(disocialmedia)
print(result_list_outc3)
print(doc2vecsocialmedia)


#chapter 4.4.1

diinterviews=[]
#raw docs for file equaltiy predictions
#thesaurus files for equality predictions
Ifile56 =  open("thesaurus-files/thesaurus-interviews.txt","r",encoding="utf8")
contents=Ifile56.read()
interviews = contents.strip('][').split('\n') 
print("Number of documents:",len(interviews))
print(interviews)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in interviews]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_outc4 = []

#loop for sentences
for i in range(lengthList):
    print("\n")
    temppass = listToString(mylist[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])

    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_outc4.append(0)
        print("No Big matches found")
    else:
        result = (sum/count)
        print("the result in percentage..")
        print(round(result*100))
        result_list_outc4.append(round(result*100))
        sims[query_doc_tf_idf]
        if(round(result*100)>30):
            diinterviews.append(temppass)
            print(temppass)
print("the resultant list of chapter 4.4.1.........")    
print(diinterviews)

#chapter 4.4.2
diinterviewsLength= len(diinterviews)


#raw docs for file equaltiy predictions
Ifile57 =  open("corpus/outcomesInterviews.txt","r",encoding="utf8")
contents=Ifile57.read()
interviewscorpus = contents.strip('][').split('\n') 
print("Number of documents:",len(interviewscorpus))
print(interviewscorpus)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in interviewscorpus]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_outc41 = []
doc2vecsum=0
#loop for sentences
for i in range(diinterviewsLength):
    print("\n")
    temppass = listToString(diinterviews[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    maxi=[]
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])
        maxi.append(query_doc_tf_idf[i][1])
    
    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_outc41.append(0)
        print("No Big matches found")
    else:
        result = (max(maxi))
        print("the result in percentage..")
        print(round(result*100))
        result_list_outc41.append(round(result*100))
        doc2vecsum+=round(result*100)
        sims[query_doc_tf_idf]
print("the resultant list of chapter 4.4.2........")    
if(len(diinterviews) == 0):
    doc2vecinterviews = 10
else:
    doc2vecinterviews = doc2vecsum / diinterviewsLength

print(diinterviews)
print(result_list_outc41)
print(doc2vecinterviews)

#chapter 4.5.1

diimpact=[]
#raw docs for file equaltiy predictions
#thesaurus files for equality predictions
Ifile58 =  open("thesaurus-files/thesaurus-impact.txt","r",encoding="utf8")
contents=Ifile58.read()
impact = contents.strip('][').split('\n') 
print("Number of documents:",len(impact))
print(impact)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in impact]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_outc5 = []

#loop for sentences
for i in range(lengthList):
    print("\n")
    temppass = listToString(mylist[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])

    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_outc5.append(0)
        print("No Big matches found")
    else:
        result = (sum/count)
        print("the result in percentage..")
        print(round(result*100))
        result_list_outc5.append(round(result*100))
        sims[query_doc_tf_idf]
        if(round(result*100)>30):
            diimpact.append(temppass)
            print(temppass)
print("the resultant list of chapter 4.5.1.........")    
print(diimpact)

#chapter 4.5.2
diimpactLength= len(diimpact)


#raw docs for file equaltiy predictions
Ifile59 =  open("corpus/outcomesImpact.txt","r",encoding="utf8")
contents=Ifile59.read()
impactcorpus = contents.strip('][').split('\n') 
print("Number of documents:",len(impactcorpus))
print(impactcorpus)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in impactcorpus]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_outc51 = []
doc2vecsum=0
#loop for sentences
for i in range(diimpactLength):
    print("\n")
    temppass = listToString(diimpact[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    maxi=[]
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])
        maxi.append(query_doc_tf_idf[i][1])
    
    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_outc51.append(0)
        print("No Big matches found")
    else:
        result = (max(maxi))
        print("the result in percentage..")
        print(round(result*100))
        result_list_outc51.append(round(result*100))
        doc2vecsum+=round(result*100)
        sims[query_doc_tf_idf]
print("the resultant list of chapter 4.5.2........")    
if(len(diimpact) == 0):
    doc2vecimpact = 10
else:
    doc2vecimpact = doc2vecsum / diimpactLength

print(diimpact)
print(result_list_outc51)
print(doc2vecimpact)


#chapter 4.6.1

diinnovation=[]
#raw docs for file equaltiy predictions
#thesaurus files for equality predictions
Ifile60 =  open("thesaurus-files/thesaurus-innovation.txt","r",encoding="utf8")
contents=Ifile60.read()
innovations = contents.strip('][').split('\n') 
print("Number of documents:",len(innovations))
print(innovations)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in innovations]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_outc6 = []

#loop for sentences
for i in range(lengthList):
    print("\n")
    temppass = listToString(mylist[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])

    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_outc6.append(0)
        print("No Big matches found")
    else:
        result = (sum/count)
        print("the result in percentage..")
        print(round(result*100))
        result_list_outc6.append(round(result*100))
        sims[query_doc_tf_idf]
        if(round(result*100)>30):
            diinnovation.append(temppass)
            print(temppass)
print("the resultant list of chapter 4.4.1.........")    
print(diinnovation)

#chapter 4.4.2
diinnovationLength= len(diinnovation)


#raw docs for file equaltiy predictions
Ifile61 =  open("corpus/outcomesInnovation.txt","r",encoding="utf8")
contents=Ifile61.read()
innovationcorpus = contents.strip('][').split('\n') 
print("Number of documents:",len(innovationcorpus))
print(innovationcorpus)

#NLP using NLTK
gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stopwords] 
            for text in innovationcorpus]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)


tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)
s = 0
for i in corpus:
    s += len(i)
print(s)

sims = gensim.similarities.Similarity('foundationScrapeFiles/workdir',tf_idf[corpus],
                                      num_features=len(dictionary))
print(sims)
result_list_outc61 = []
doc2vecsum=0
#loop for sentences
for i in range(diinnovationLength):
    print("\n")
    temppass = listToString(diinnovation[i]) #class list to string convertion

    query_doc_unrefined = [w.lower() for w in word_tokenize(temppass) if w not in stopwords]
    query_doc = [lemmatizer.lemmatize(w) for w in query_doc_unrefined]
    print(query_doc)
    query_doc_bow = dictionary.doc2bow(query_doc)
    print(query_doc_bow)
    query_doc_tf_idf = tf_idf[query_doc_bow]
    print(query_doc_tf_idf)
    count=0
    sum=0
    temp=0
    maxi=[]
    for i in range(len(query_doc_tf_idf)):
        temp = query_doc_tf_idf[i][1]
        sum=sum+temp
        count+=1
        print (query_doc_tf_idf[i][1])
        maxi.append(query_doc_tf_idf[i][1])
    
    #calculation and marks predictions 
    print("the sum is..")
    print(sum)
    print("the count is") 
    print(count)
    if(count == 0):
        result_list_outc61.append(0)
        print("No Big matches found")
    else:
        result = (max(maxi))
        print("the result in percentage..")
        print(round(result*100))
        result_list_outc61.append(round(result*100))
        doc2vecsum+=round(result*100)
        sims[query_doc_tf_idf]
print("the resultant list of chapter 4.4.2........")    
if(len(diinnovation) == 0):
    doc2vecinnovation = 10
else:
    doc2vecinnovation = doc2vecsum / diinnovationLength

print(diinnovation)
print(result_list_outc61)
print(doc2vecinnovation)


#chapter 4.7.1
dicontroversies = []
result_list_outc7 = []
doc2vecsum=0
count=0
for i in range(0,len(mylist)):
    tempstring = mylist[i]
    tempstringLower = tempstring.lower()
    tempstringSplit = tempstringLower.split()
    if "alleged" in tempstringSplit or "complaint" in tempstringSplit or "filed" in tempstringSplit or "lawsuit" in tempstringSplit or "alleging" in tempstringSplit or "complaints" in tempstringSplit or "lawsuits" in tempstringSplit or "alleging" in tempstringSplit or "files" in tempstringSplit or "law suit" in tempstringSplit or "accused" in tempstringSplit or "arrested" in tempstringSplit or "arrests" in tempstringSplit or "jailed" in tempstringSplit:
        dicontroversies.append(tempstring)
        result_list_outc7.append(int(2))
        doc2vecsum+=2
        count+=1
if(count > 0):
    doc2veccontroversies = doc2vecsum / count
else:
    doc2veccontroversies = 70
print(dicontroversies)
print(result_list_outc7)
print(doc2veccontroversies)


#result print 
print("the resultant of the foundation of D&I aspects")
print('\n')
print('D & I Vision \n')
print(division)
print('\n')
print('D & I strategies \n')
print(distrategy)
print('\n')
print('D & I leadership \n')
print(dileadership)
print('\n')
print('D & I Infrastructure \n')
print(diinfrastructure)
print('\n')
print("the resultant of the Initiatives of D&I aspects")
print('\n')
print('D & I awareness and sensitisation \n')
print(diawareness)
print('\n')
print('D & I steering commmittees \n')
print(disteering)
print('\n')
print('D & I gender and pay parity \n')
print(digenderparity)
print('\n')
print('D & I Demographical targeted hiring \n')
print(didemographicalHiring)
print('\n')
print('D & I Mentoring and sponsors \n')
print(dimentorsponsor)
print('\n')
print('D & I Technolgies \n')
print(ditechnologies)
print('\n')
print('D & I Organisation provided services \n')
print(diservices)
print('\n')
print('D & I Communication, Campaigns and Events \n')
print(dicommunication)
print('\n')
print('D & I Government Policies \n')
print(dipolicy)
print('\n')
print('D & I trainings \n')
print(ditraining)
print('\n')
print('D & I Collaborations \n')
print(dicollaboration)
print('\n')
print('D & I Assessing the progress of D&I programs and improvements, and reporting \n')
print(direports)
print('\n')
print('D & I CSR activities \n')
print(dicsr)
print('\n')
print('D & I Surveys \n')
print(disurvey)
print('\n')
print('D & I Thought Leadership \n')
print(dithoughtLeadership)
print('\n')
print('D & I Awards and accolades \n')
print(diawards)
print('\n')
print('D & I Social media traction \n')
print(disocialmedia)
print('\n')
print('D & I excerpts interviews and testimonals \n')
print(diinterviews)
print('\n')
print('D & I successrate and impacts \n')
print(diimpact)
print('\n')
print('D & I Innovations and creativity \n')
print(diinnovation)
print('\n')
print('D & I Controversies \n')
print(dicontroversies)
print('\n')


#doc2vec calculations
resultdoc2vecVision = doc2vecRefined(doc2vecVision)
resultdoc2vecInfrastructure = doc2vecRefined(doc2vecInfrastructure)
resultdoc2vecStrategy = doc2vecRefined(doc2vecStrategy)
resultdoc2vecLeadership= doc2vecRefined(doc2vecLeadership)

resultdoc2vecawareness = doc2vecRefined(doc2vecawareness)
resultdoc2vecsteering = doc2vecRefined(doc2vecsteering)
resultdoc2vecgenderparity = doc2vecRefined(doc2vecgenderparity)
resultdoc2vecdemographicalHiring = doc2vecRefined(doc2vecdemographicalHiring)
resultdoc2vecmentorsponsor = doc2vecRefined(doc2vecmentorsponsor)
resultdoc2vectechnologies = doc2vecRefined(doc2vectechnologies)
resultdoc2vecservices = doc2vecRefined(doc2vecservices)

resultdoc2veccommunication = doc2vecRefined(doc2veccommunication)
resultdoc2vecpolicy = doc2vecRefined(doc2vecpolicy)
resultdoc2vectrainings = doc2vecRefined(doc2vectraining)
resultdoc2veccollaboration = doc2vecRefined(doc2veccollaboration)
resultdoc2vecreports = doc2vecRefined(doc2vecreports)
resultdoc2veccsr = doc2vecRefined(doc2veccsr)
resultdoc2vecsurveys = doc2vecRefined(doc2vecsurvey)

resultdoc2vecthoughtleadership = doc2vecRefined(doc2vecthoughtLeadership)
resultdoc2vecawards = doc2vecRefined(doc2vecawards)
resultdoc2vecsocialmedia = doc2vecRefined(doc2vecsocialmedia)
resultdoc2vecinterviews = doc2vecRefined(doc2vecinterviews)
resultdoc2vecimpact = doc2vecRefined(doc2vecimpact)
resultdoc2vecinnovation = doc2vecRefined(doc2vecinnovation)
resultdoc2veccontroversies = doc2vecRefined(doc2veccontroversies)


#marks calculations
avgOfVision_str=str(resultdoc2vecVision)
avgOfVision_str="result of vision = " + avgOfVision_str
avgOfStrategy_str=str(resultdoc2vecStrategy)
avgOfStrategy_str="result of Strategy & targets = " + avgOfStrategy_str
avgOfLeadership_str=str(resultdoc2vecLeadership)
avgOfLeadership_str="result of Leadership & Accountable = " + avgOfLeadership_str
avgOfInfrastructure_str=str(resultdoc2vecInfrastructure)
avgOfInfrastructure_str="result of Infrastructure = " + avgOfInfrastructure_str
avgofFoundation = (resultdoc2vecVision + resultdoc2vecInfrastructure + resultdoc2vecStrategy + resultdoc2vecLeadership)/4
avgofFoundation_str=str(avgofFoundation)
avgofFoundation_str="result of Foundation = "+ avgofFoundation_str


avgOfawareness_str=str(resultdoc2vecawareness)
avgOfawareness_str="result of awareness = " + avgOfawareness_str
avgOfSteering_str=str(resultdoc2vecsteering)
avgOfSteering_str="result of steering committee = " + avgOfSteering_str
avgOfgenderparity_str=str(resultdoc2vecgenderparity)
avgOfgenderparity_str="result of Gender Pay parity = " + avgOfgenderparity_str
avgOfdemographicalHiring_str=str(resultdoc2vecdemographicalHiring)
avgOfdemographicalHiring_str="result of demographical hiring = " + avgOfdemographicalHiring_str
avgOfmentorsponsor_str=str(resultdoc2vecmentorsponsor)
avgOfmentorsponsor_str="result of Mentorship and sponsorship = " + avgOfmentorsponsor_str
avgOftechnologies_str=str(resultdoc2vectechnologies)
avgOftechnologies_str="result of technolgies= " + avgOftechnologies_str
avgOfservices_str=str(resultdoc2vecservices)
avgOfservices_str="result of services by company = " + avgOfservices_str
avgofInitiatives = (resultdoc2vecawareness + resultdoc2vecsteering + resultdoc2vecgenderparity + resultdoc2vecdemographicalHiring + resultdoc2vecmentorsponsor + resultdoc2vectechnologies + resultdoc2vecservices ) / 7
avgofInitiatives_str=str(avgofInitiatives)
avgofInitiatives_str="result of Initiatives = "+ avgofInitiatives_str



avgOfcommunication_str=str(resultdoc2veccommunication)
avgOfcommunication_str="result of communication = " + avgOfcommunication_str
avgOfpolicy_str=str(resultdoc2vecpolicy)
avgOfpolicy_str="result of policies = " + avgOfpolicy_str
avgOftrainings_str=str(resultdoc2vectrainings)
avgOftrainings_str="result of Trainings = " + avgOftrainings_str
avgOfcollaboration_str=str(resultdoc2veccollaboration)
avgOfcollaboration_str="result of collaboration = " + avgOfcollaboration_str
avgOfreports_str=str(resultdoc2vecreports)
avgOfreports_str="result of programs,improvements,reporting = " + avgOfreports_str
avgOfcsr_str=str(resultdoc2veccsr)
avgOfcsr_str="result of CSR = " + avgOfcsr_str
avgOfsurveys_str=str(resultdoc2vecsurveys)
avgOfsurveys_str="result of surveys = " + avgOfsurveys_str
avgofBridging = (resultdoc2veccommunication + resultdoc2vecpolicy + resultdoc2vectrainings + resultdoc2veccollaboration + resultdoc2vecreports + resultdoc2veccsr + resultdoc2vecsurveys ) / 7
avgofBridging_str=str(avgofBridging)
avgofBridging_str="result of Bridging = "+ avgofBridging_str


avgOfthoughtleadership_str=str(resultdoc2vecthoughtleadership)
avgOfthoughtleadership_str="result of Thought Leadership = " + avgOfthoughtleadership_str
avgOfawards_str=str(resultdoc2vecawards)
avgOfawards_str="result of awards = " + avgOfawards_str
avgOfsocialmedia_str=str(resultdoc2vecsocialmedia)
avgOfsocialmedia_str="result of social media traction = " + avgOfsocialmedia_str
avgOfinterviews_str=str(resultdoc2vecinterviews)
avgOfinterviews_str="result of interviews = " + avgOfinterviews_str
avgOfimpact_str=str(resultdoc2vecimpact)
avgOfimpact_str="result of DI impacts = " +avgOfimpact_str
avgOfinnovation_str=str(resultdoc2vecinnovation)
avgOfinnovation_str="result of Innovation&Creativity = " + avgOfinnovation_str
avgOfcontroversies_str=str(resultdoc2veccontroversies)
avgOfcontroversies_str="result of Controversies = " + avgOfcontroversies_str
avgofOutcomes = (resultdoc2vecthoughtleadership +resultdoc2vecawards + resultdoc2vecsocialmedia + resultdoc2vecinterviews + resultdoc2vecimpact + resultdoc2vecinnovation + resultdoc2veccontroversies ) / 7
avgofOutcomes_str=str(avgofOutcomes)
avgofOutcomes_str="result of Outcomes = "+ avgofOutcomes_str



#Row calculations
lenOfVisionList = len(division)
lenOfStrategyList =len(distrategy)
lenOfLeadershipList = len(dileadership)
lenOfInfrastrucutureList = len(diinfrastructure)
maxOfLists = max(lenOfInfrastrucutureList,lenOfLeadershipList,lenOfStrategyList,lenOfVisionList)

lenOfAwarenessList = len(diawareness)
lenOfSteeringList = len(disteering)
lenOfDemographicalHiringList =len(didemographicalHiring)
lenOfMentorSponsorList = len(dimentorsponsor)
lenOfTechnologiesList = len(ditechnologies)
lenOfGenderParityList = len(digenderparity)
lenOfServiesList =len(diservices)
maxOfLists1 = max(lenOfAwarenessList,lenOfSteeringList,lenOfDemographicalHiringList,lenOfMentorSponsorList,lenOfTechnologiesList,lenOfGenderParityList,lenOfServiesList)

maxOfLists2 = max(len(dicommunication),len(dipolicy),len(ditraining),len(dicollaboration),len(direports),len(dicsr),len(disurvey))

maxOfLists3 = max(len(dithoughtLeadership),len(diawards),len(disocialmedia),len(diinterviews),len(diimpact),len(diinnovation),len(dicontroversies))


#Pandas to make a dataframe and export to xlsx file
listNumbers = list(range(1,maxOfLists))
dict_excelsheet1 = {}
de = pd.DataFrame(dict_excelsheet1, columns = ['listNum','D&I Vision','D&I Strategies','D&I Leadership','D&I Infrastructure','h1','h2','h3'])
de["listNum"]=pd.Series(listNumbers)
de["D&I Vision"]=pd.Series(division)
de["D&I Strategies"]=pd.Series(distrategy)
de["D&I Leadership"]=pd.Series(dileadership)
de["D&I Infrastructure"]=pd.Series(diinfrastructure)

listNumbers2=["Results"]
dict_excelsheet2 = {}
de1 = pd.DataFrame(dict_excelsheet2, columns = ['listNum','D&I Vision','D&I Strategies','D&I Leadership','D&I Infrastructure','h1','h2','h3'])
de1["listNum"]=pd.Series(listNumbers2)
de1["D&I Vision"] = pd.Series(avgOfVision_str)
de1["D&I Strategies"] = pd.Series(avgOfStrategy_str)
de1["D&I Leadership"] = pd.Series(avgOfLeadership_str)
de1["D&I Infrastructure"] = pd.Series(avgOfInfrastructure_str)

listNumbers3=["Final Results"]
dict_excelsheet3 = {}
de2 = pd.DataFrame(dict_excelsheet3, columns = ['listNum','D&I Vision','D&I Strategies','D&I Leadership','D&I Infrastructure','h1','h2','h3'])
de2["listNum"]=pd.Series(listNumbers3)
de2["D&I Vision"] = pd.Series(avgofFoundation_str)

topicinitiatives=["D&I Initiatives"]
topicawareness=["D&I Awareness and Awareness and Sensitisation"]
topicsteering = ["D&I Steering committees"]
topicdemotarget = ["D&I Demographically targeted hiring and promotion"]
topicmentorsponsor =["D&I Mentoring and Sponsorship for career progression"]
topictechnologies = ["Technologies to scale D&I initiatives"]
topicservices = ["D&I Organization-provided services"]
topicgenderpayparity=["D&I Gender and Pay Parity"]


dict_excelsheet4 = {}
de3 = pd.DataFrame(dict_excelsheet4, columns = ['listNum','D&I Vision','D&I Strategies','D&I Leadership','D&I Infrastructure','h1','h2','h3'])
de3["listNum"]=pd.Series(topicinitiatives)
de3["D&I Vision"]=pd.Series(topicawareness)
de3["D&I Strategies"]=pd.Series(topicsteering)
de3["D&I Leadership"]=pd.Series(topicgenderpayparity)
de3["D&I Infrastructure"]=pd.Series(topicdemotarget)
de3["h1"]=pd.Series(topicmentorsponsor)
de3["h2"]=pd.Series(topictechnologies)
de3["h3"]=pd.Series(topicservices)

listNumbers11 = list(range(1,maxOfLists1))
dict_excelsheet5 = {}
de4 = pd.DataFrame(dict_excelsheet5, columns = ['listNum','D&I Vision','D&I Strategies','D&I Leadership','D&I Infrastructure','h1','h2','h3'])
de4["listNum"]=pd.Series(listNumbers11)
de4["D&I Vision"]=pd.Series(diawareness)
de4["D&I Strategies"]=pd.Series(disteering)
de4["D&I Leadership"]=pd.Series(digenderparity)
de4["D&I Infrastructure"]=pd.Series(didemographicalHiring)
de4["h1"]=pd.Series(dimentorsponsor)
de4["h2"]=pd.Series(ditechnologies)
de4["h3"]=pd.Series(diservices)

listNumbers21=["Results"]
dict_excelsheet6 = {}
de5 = pd.DataFrame(dict_excelsheet6, columns = ['listNum','D&I Vision','D&I Strategies','D&I Leadership','D&I Infrastructure','h1','h2','h3'])
de5["listNum"]=pd.Series(listNumbers21)
de5["D&I Vision"]=pd.Series(avgOfawareness_str)
de5["D&I Strategies"]=pd.Series(avgOfSteering_str)
de5["D&I Leadership"]=pd.Series(avgOfgenderparity_str)
de5["D&I Infrastructure"]=pd.Series(avgOfdemographicalHiring_str)
de5["h1"]=pd.Series(avgOfmentorsponsor_str)
de5["h2"]=pd.Series(avgOftechnologies_str)
de5["h3"]=pd.Series(avgOfservices_str)

listNumbers31=["Final Results"]
dict_excelsheet7 = {}
de6 = pd.DataFrame(dict_excelsheet7, columns = ['listNum','D&I Vision','D&I Strategies','D&I Leadership','D&I Infrastructure','h1','h2','h3'])
de6["listNum"]=pd.Series(listNumbers31)
de6["D&I Vision"] = pd.Series(avgofInitiatives_str)


topicbridging=["D&I Bridging"]
topiccommunication=["D&I Communication, Campaigns and Events"]
topicpolicy=["D&I Government Policies"]
topictraining = ["D&I trainings"]
topiccollaboration = ["D&I Collaborations"]
topicreports =["D&I programs,improvements,and reporting"]
topiccsr = ["CSR activities"]
topicsurvey = ["D&I Surveys"]



dict_excelsheet8 = {}
de7 = pd.DataFrame(dict_excelsheet8, columns = ['listNum','D&I Vision','D&I Strategies','D&I Leadership','D&I Infrastructure','h1','h2','h3'])
de7["listNum"]=pd.Series(topicbridging)
de7["D&I Vision"]=pd.Series(topiccommunication)
de7["D&I Strategies"]=pd.Series(topicpolicy)
de7["D&I Leadership"]=pd.Series(topictraining)
de7["D&I Infrastructure"]=pd.Series(topiccollaboration)
de7["h1"]=pd.Series(topicreports)
de7["h2"]=pd.Series(topiccsr)
de7["h3"]=pd.Series(topicsurvey)

listNumbers111 = list(range(1,maxOfLists2))
dict_excelsheet9 = {}
de8 = pd.DataFrame(dict_excelsheet9, columns = ['listNum','D&I Vision','D&I Strategies','D&I Leadership','D&I Infrastructure','h1','h2','h3'])
de8["listNum"]=pd.Series(listNumbers111)
de8["D&I Vision"]=pd.Series(dicommunication)
de8["D&I Strategies"]=pd.Series(dipolicy)
de8["D&I Leadership"]=pd.Series(ditraining)
de8["D&I Infrastructure"]=pd.Series(dicollaboration)
de8["h1"]=pd.Series(direports)
de8["h2"]=pd.Series(dicsr)
de8["h3"]=pd.Series(disurvey)

listNumbers222=["Results"]
dict_excelsheet10 = {}
de9 = pd.DataFrame(dict_excelsheet10, columns = ['listNum','D&I Vision','D&I Strategies','D&I Leadership','D&I Infrastructure','h1','h2','h3'])
de9["listNum"]=pd.Series(listNumbers222)
de9["D&I Vision"]=pd.Series(avgOfcommunication_str)
de9["D&I Strategies"]=pd.Series(avgOfpolicy_str)
de9["D&I Leadership"]=pd.Series(avgOftrainings_str)
de9["D&I Infrastructure"]=pd.Series(avgOfcollaboration_str)
de9["h1"]=pd.Series(avgOfreports_str)
de9["h2"]=pd.Series(avgOfcsr_str)
de9["h3"]=pd.Series(avgOfsurveys_str)

listNumbers333=["Final Results"]
dict_excelsheet11 = {}
de10 = pd.DataFrame(dict_excelsheet11, columns = ['listNum','D&I Vision','D&I Strategies','D&I Leadership','D&I Infrastructure','h1','h2','h3'])
de10["listNum"]=pd.Series(listNumbers333)
de10["D&I Vision"] = pd.Series(avgofBridging_str)



topictleadership=["D&I Thought Leadership"]
topicawards=["D&I Awards & Accolades"]
topicsocialmedia=["D&I Social Media Traction"]
topicinterviews = ["D&I Excerpts, Interviews and Testimonials"]
topicimpact = ["D&I Impacts"]
topicinnovation =["D&I Innovation, Creativity and Ability"]
topiccontroversies = ["D&I Controversies"]
topicoutcomes = ["D&I Outcomes"]



dict_excelsheet12 = {}
de11 = pd.DataFrame(dict_excelsheet12, columns = ['listNum','D&I Vision','D&I Strategies','D&I Leadership','D&I Infrastructure','h1','h2','h3'])
de11["listNum"]=pd.Series(topicoutcomes)
de11["D&I Vision"]=pd.Series(topictleadership)
de11["D&I Strategies"]=pd.Series(topicawards)
de11["D&I Leadership"]=pd.Series(topicsocialmedia)
de11["D&I Infrastructure"]=pd.Series(topicinterviews)
de11["h1"]=pd.Series(topicimpact)
de11["h2"]=pd.Series(topicinnovation)
de11["h3"]=pd.Series(topiccontroversies)

listNumbersa = list(range(1,maxOfLists3))
dict_excelsheet13 = {}
de12 = pd.DataFrame(dict_excelsheet13, columns = ['listNum','D&I Vision','D&I Strategies','D&I Leadership','D&I Infrastructure','h1','h2','h3'])
de12["listNum"]=pd.Series(listNumbersa)
de12["D&I Vision"]=pd.Series(dithoughtLeadership)
de12["D&I Strategies"]=pd.Series(diawards)
de12["D&I Leadership"]=pd.Series(disocialmedia)
de12["D&I Infrastructure"]=pd.Series(diinterviews)
de12["h1"]=pd.Series(diimpact)
de12["h2"]=pd.Series(diinnovation)
de12["h3"]=pd.Series(dicontroversies)

listNumbersb=["Results"]
dict_excelsheet14 = {}
de13 = pd.DataFrame(dict_excelsheet14, columns = ['listNum','D&I Vision','D&I Strategies','D&I Leadership','D&I Infrastructure','h1','h2','h3'])
de13["listNum"]=pd.Series(listNumbersb)
de13["D&I Vision"]=pd.Series(avgOfthoughtleadership_str)
de13["D&I Strategies"]=pd.Series(avgOfawards_str)
de13["D&I Leadership"]=pd.Series(avgOfsocialmedia_str)
de13["D&I Infrastructure"]=pd.Series(avgOfinterviews_str)
de13["h1"]=pd.Series(avgOfimpact_str)
de13["h2"]=pd.Series(avgOfinnovation_str)
de13["h3"]=pd.Series(avgOfcontroversies_str)

listNumbersc=["Final Results"]
dict_excelsheet14 = {}
de14 = pd.DataFrame(dict_excelsheet14, columns = ['listNum','D&I Vision','D&I Strategies','D&I Leadership','D&I Infrastructure','h1','h2','h3'])
de14["listNum"]=pd.Series(listNumbersc)
de14["D&I Vision"] = pd.Series(avgofOutcomes_str)


frames = [de, de1,de2,de3,de4,de5,de6,de7,de8,de9,de10,de11,de12,de13,de14]
frames_result=pd.concat(frames)
print(frames_result)


frames_result.to_excel (r'result/result.xlsx', index = False, header=True )

#result summary excel sheet

topicVision=["D&I Vision and mission"]
topicStrategyandtargets=["D&I Strategy and targets"]
topicInfrastructure = ["D&I Infrastructure"]
topicLeadership = ["D&I Leadership"]
topicFoundation=["D&I Foundation"]

dict_excelsheet15 = {}
de15 = pd.DataFrame(dict_excelsheet15, columns = ['A','B','C','D','E','F','G','H'])
de15["A"]=pd.Series(topicFoundation)
de15["B"]=pd.Series(topicVision)
de15["C"]=pd.Series(topicStrategyandtargets)
de15["D"]=pd.Series(topicInfrastructure)
de15["E"]=pd.Series(topicLeadership)

lnResult=["Result"]
lnResultSummary=["Final Result"," "]
dict_excelsheet16 = {}
de16 = pd.DataFrame(dict_excelsheet16, columns = ['A','B','C','D','E','F','G','H'])
de16["A"]=pd.Series(lnResult)
de16["B"] = pd.Series(avgOfVision_str)
de16["C"] = pd.Series(avgOfStrategy_str)
de16["D"] = pd.Series(avgOfInfrastructure_str)
de16["E"] = pd.Series(avgOfLeadership_str)

dict_excelsheet17 = {}
de17 = pd.DataFrame(dict_excelsheet17, columns = ['A','B','C','D','E','F','G','H'])
de17["A"]=pd.Series(lnResultSummary)
de17["B"] = pd.Series(avgofFoundation_str)


dict_excelsheet18 = {}
de18 = pd.DataFrame(dict_excelsheet18, columns = ['A','B','C','D','E','F','G','H'])
de18["A"]=pd.Series(topicinitiatives)
de18["B"]=pd.Series(topicawareness)
de18["C"]=pd.Series(topicsteering)
de18["D"]=pd.Series(topicdemotarget)
de18["E"]=pd.Series(topicmentorsponsor)
de18["F"]=pd.Series(topictechnologies)
de18["G"]=pd.Series(topicservices)
de18["H"]=pd.Series(topicgenderpayparity)

dict_excelsheet19 = {}
de19 = pd.DataFrame(dict_excelsheet19, columns = ['A','B','C','D','E','F','G','H'])
de19["A"]=pd.Series(lnResult)
de19["B"] = pd.Series(avgOfawareness_str)
de19["C"] = pd.Series(avgOfSteering_str)
de19["D"] = pd.Series(avgOfdemographicalHiring_str)
de19["E"] = pd.Series(avgOfmentorsponsor_str)
de19["F"]=pd.Series(avgOftechnologies_str)
de19["G"]=pd.Series(avgOfservices_str)
de19["H"]=pd.Series(avgOfgenderparity_str)

dict_excelsheet20 = {}
de20 = pd.DataFrame(dict_excelsheet20, columns = ['A','B','C','D','E','F','G','H'])
de20["A"]=pd.Series(lnResultSummary)
de20["B"] = pd.Series(avgofInitiatives_str)



dict_excelsheet21 = {}
de21 = pd.DataFrame(dict_excelsheet21, columns = ['A','B','C','D','E','F','G','H'])
de21["A"]=pd.Series(topicbridging)
de21["B"]=pd.Series(topiccommunication)
de21["C"]=pd.Series(topicpolicy)
de21["D"]=pd.Series(topictraining)
de21["E"]=pd.Series(topiccollaboration)
de21["F"]=pd.Series(topicreports)
de21["G"]=pd.Series(topiccsr)
de21["H"]=pd.Series(topicsurvey)

dict_excelsheet22 = {}
de22 = pd.DataFrame(dict_excelsheet22, columns = ['A','B','C','D','E','F','G','H'])
de22["A"]=pd.Series(lnResult)
de22["B"] = pd.Series(avgOfcommunication_str)
de22["C"] = pd.Series(avgOfpolicy_str)
de22["D"] = pd.Series(avgOftrainings_str)
de22["E"] = pd.Series(avgOfcollaboration_str)
de22["F"]=pd.Series(avgOfreports_str)
de22["G"]=pd.Series(avgOfcsr_str)
de22["H"]=pd.Series(avgOfsurveys_str)

dict_excelsheet23 = {}
de23 = pd.DataFrame(dict_excelsheet23, columns = ['A','B','C','D','E','F','G','H'])
de23["A"]=pd.Series(lnResultSummary)
de23["B"] = pd.Series(avgofBridging_str)


dict_excelsheet24 = {}
de24 = pd.DataFrame(dict_excelsheet24, columns = ['A','B','C','D','E','F','G','H'])
de24["A"]=pd.Series(topicoutcomes)
de24["B"]=pd.Series(topictleadership)
de24["C"]=pd.Series(topicawards)
de24["D"]=pd.Series(topicsocialmedia)
de24["E"]=pd.Series(topicinterviews)
de24["F"]=pd.Series(topicimpact)
de24["G"]=pd.Series(topicinnovation)
de24["H"]=pd.Series(topiccontroversies)

dict_excelsheet25 = {}
de25 = pd.DataFrame(dict_excelsheet25, columns = ['A','B','C','D','E','F','G','H'])
de25["A"]=pd.Series(lnResult)
de25["B"] = pd.Series(avgOfthoughtleadership_str)
de25["C"] = pd.Series(avgOfawards_str)
de25["D"] = pd.Series(avgOfsocialmedia_str)
de25["E"] = pd.Series(avgOfinterviews_str)
de25["F"]=pd.Series(avgOfimpact_str)
de25["G"]=pd.Series(avgOfinnovation_str)
de25["H"]=pd.Series(avgOfcontroversies_str)

dict_excelsheet26 = {}
de26 = pd.DataFrame(dict_excelsheet26, columns = ['A','B','C','D','E','F','G','H'])
de26["A"]=pd.Series(lnResultSummary)
de26["B"] = pd.Series(avgofOutcomes_str)


#final result
finalResult = ["Final D&I score"]
fscore = (avgofFoundation + avgofBridging + avgofInitiatives + avgofOutcomes)/4
finalscore_str = str(fscore)
finalscore_str = "Score = "+finalscore_str

dict_excelsheet27 = {}
de27 = pd.DataFrame(dict_excelsheet27, columns = ['A','B','C','D','E','F','G','H'])
de27["A"] = pd.Series(finalResult)
de27["B"] = pd.Series(finalscore_str)

frames1 = [de15, de16,de17,de18,de19,de20,de21,de22,de23,de24,de25,de26,de27]
frames1_result=pd.concat(frames1)
print(frames1_result)

frames1_result.to_excel (r'result/resultsummary.xlsx', index = False, header=True )

ctypes.windll.user32.MessageBoxW(0, "Refer Results and Geolocation folders! STARTED PLOTTING MICRO AND MACRO ASSESMENT GRAPHS", "D&I automation BOT", 1)

closeAllFiles()

print("Refer Results in result/result.xlsx file \n")
print("Refer Result summary in result/resultsummary.xlsx file \n")
print("Refer geoLocation/GeoLocation.txt file for Geolocation results \n")


#barGraph plot -bar graph-1
from re import A
import matplotlib.pyplot as plt
  
# x-coordinates of left sides of bars 
left = [1, 2, 3, 4]
  
# heights of bars
height = [resultdoc2vecVision, resultdoc2vecInfrastructure,resultdoc2vecStrategy,resultdoc2vecLeadership]
  
# labels for bars
tick_label = ['VISION', 'INFRASTRUCTURE', 'STRATEGY', 'LEADERSHIP']

plt.figure(figsize=(15,15))

# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 0.8, color = ['blue'])
  
# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('DI FOUNDATION '+query.upper())
  
# function to show the plot

plt.savefig('result/microLevelGraph/DI-foundation.png',dpi=300)

plt.close()

#bargraph-2
# x-coordinates of left sides of bars 

left = [1,2,3,4,5,6,7]
  
# heights of bars
height = [resultdoc2vecawareness, resultdoc2vecsteering,resultdoc2vecgenderparity,resultdoc2vecdemographicalHiring,resultdoc2vecmentorsponsor,resultdoc2vectechnologies,resultdoc2vecservices]
  
# labels for bars
tick_label = ['AWARENESS', 'STEERINGCOMMITTEE', 'GENDERPARITY', 'HIRING','MENTORSPONSOR','TECHNOLOGIES','SERVICES']

plt.figure(figsize=(15,15))
  
# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 0.8, color = ['blue'])
  
# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('DI INITIATIVES '+query.upper())
  
# function to show the plot

plt.savefig('result/microLevelGraph/DI-initiatives.png',dpi=300)

plt.close()


#bargraph-3
# x-coordinates of left sides of bars 
left = [1,2,3,4,5,6,7]
  
# heights of bars
height = [resultdoc2veccommunication, resultdoc2vecpolicy,resultdoc2vectrainings,resultdoc2veccollaboration,resultdoc2vecreports,resultdoc2veccsr,resultdoc2vecsurveys]
  
# labels for bars
tick_label = ['COMMUNICATION', 'POLICIES', 'TRAININGS', 'COLLABORATION','REPORTS','CSR ACTIVITY','SURVEYS']

plt.figure(figsize=(15,15))
  
# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 0.8, color = ['blue'])
  
# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('DI BRIDGING '+query.upper())
  
# function to show the plot

plt.savefig('result/microLevelGraph/DI-bridging.png',dpi=300)

plt.close()



#bargraph-4
# x-coordinates of left sides of bars 
left = [1,2,3,4,5,6,7]
  
# heights of bars
height = [resultdoc2vecthoughtleadership, resultdoc2vecawards ,resultdoc2vecsocialmedia,resultdoc2vecinterviews,resultdoc2vecimpact,resultdoc2vecinnovation,resultdoc2veccontroversies]
  
# labels for bars
tick_label = ['THOUGHT-LEADERSHIP', 'AWARDS', 'SOCIAL-MEDIA TRACTION', 'INTERVIEWS','IMPACTS','INNOVATIONS','CONTROVERSIES']

plt.figure(figsize=(15,15))
  
# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 0.8, color = ['blue'])
  
# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('DI OUTCOMES '+query.upper())
  
# function to show the plot

plt.savefig('result/microLevelGraph/DI-outcomes.png',dpi=300)

plt.close()


import matplotlib.pyplot as plt

r1 = resultdoc2vecVision + resultdoc2vecInfrastructure + resultdoc2vecStrategy + resultdoc2vecLeadership

r2 = resultdoc2vecawareness + resultdoc2vecsteering + resultdoc2vecgenderparity + resultdoc2vecdemographicalHiring + resultdoc2vecmentorsponsor + resultdoc2vectechnologies + resultdoc2vecservices 

r3 = resultdoc2veccommunication + resultdoc2vecpolicy + resultdoc2vectrainings + resultdoc2veccollaboration + resultdoc2vecreports + resultdoc2veccsr + resultdoc2vecsurveys

r4 = resultdoc2vecthoughtleadership +resultdoc2vecawards + resultdoc2vecsocialmedia + resultdoc2vecinterviews + resultdoc2vecimpact + resultdoc2vecinnovation + resultdoc2veccontroversies 

r1r2r3=r1+r2+r3


x_coordinates = [r1r2r3]
y_coordinates = [r4]

# naming the x-axis
plt.xlabel('FIB')
# naming the y-axis
plt.ylabel('OUTCOMES')
# plot title
companyNameInGraph = ""
companyNameInGraph = "DI FIB " +query
plt.title(companyNameInGraph.upper())
plt.scatter(x_coordinates, y_coordinates)
plt.savefig('result/macroLevelGraph/DI-FIBvsOutcomes.png',dpi=300)
plt.close()
plt.close('all')

ctypes.windll.user32.MessageBoxW(0, "GRAPHS PLOTTED SUCCESSFULLY (refer results/graphs/png)", "D&I automation BOT", 1)



#ref https://www.oreilly.com/content/how-do-i-compare-document-similarity-using-python/ - gensim
#ref https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/ - class list to str conversion
#ref https://www.machinelearningplus.com/nlp/lemmatization-examples-python/ - lemma implementation
#ref https://www.geeksforgeeks.org/python-ways-to-create-a-dictionary-of-lists/ - pandas list to dictionary