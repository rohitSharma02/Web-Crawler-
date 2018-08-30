import webbrowser
import urllib.request
from urllib.request import urlopen
import bs4
import threading
glnks=[]
ylnks=[]
blnks=[]

v=input('Enter your query:').strip().split()
ag="+".join(v)
def google():
    print('searching on google...')
    pageurl='http://google.com/search?q='+ag
    reqt=urllib.request.Request(pageurl,None,headers={ 'User-Agent':'Mozilla/5.0'})
    
    res=urlopen(reqt)
    html_byte=res.read()
    html_str=html_byte.decode('utf-8')
    soup=bs4.BeautifulSoup(html_str)
    linkElemnts=soup.select('.r a')
    numOfLinks=len(linkElemnts)
    print('Number of links from google: '+str(numOfLinks))

    for k in range(numOfLinks):
        if (linkElemnts[k].get('href')[7:])[0:4]=='http':
            t=(linkElemnts[k].get('href')[7:]).split('&sa')
            glnks.append(t[0])
        

def yahoo():
    print('searching on yahoo search...')
    pageurl='https://in.search.yahoo.com/search?p='+ag
    reqt=urllib.request.Request(pageurl,None,headers={ 'User-Agent':'Chrome/51.0.2704.79'})
    
    res=urlopen(reqt)
    html_byte=res.read()
    html_str=html_byte.decode('utf-8')
    soup=bs4.BeautifulSoup(html_str)
    linkElemnts=soup.select('.title a')
    numOfLinks=len(linkElemnts)
    print('Number of links from yahoo: '+str(numOfLinks))
    ads='r.bat.bing.'
    infoads='kb/search/SLN'
    for k in range(numOfLinks):
        check=(linkElemnts[k].get('href')).find(ads)
        check2=(linkElemnts[k].get('href')).find(infoads)
        if check==-1 and check2==-1:
            ylnks.append(linkElemnts[k].get('href'))

def bing():
    print('searching on bing...')
    pageurl='https://www.bing.com/search?q='+ag
    reqt=urllib.request.Request(pageurl,None,headers={ 'User-Agent':'Chrome/51.0.2704.79'})
    res=urlopen(reqt)
    html_byte=res.read()
    html_str=html_byte.decode('utf-8')
    soup=bs4.BeautifulSoup(html_str)
    linkElemnts=soup.select('.b_algo a')
    numOfLinks=len(linkElemnts)
    print('Number of links from bing: '+str(numOfLinks))
    for k in range(numOfLinks):
        if linkElemnts[k].get('href')[0:4]=='http':
            blnks.append(linkElemnts[k].get('href'))
        

t1=threading.Thread(target=google)
t2=threading.Thread(target=yahoo)
t3=threading.Thread(target=bing)
t1.start()
t2.start()
t3.start()
threads=[]
threads.append(t1)
threads.append(t2)
threads.append(t3)

for t in threads:
    t.join()
    
topresult=[]
tm=min(len(glnks),min(len(ylnks),len(blnks)))

for k in range(tm):
    if glnks[k] not in topresult:
        topresult.append(glnks[k])
    if ylnks[k] not in topresult:
        topresult.append(ylnks[k])
    if blnks[k] not in topresult:
        topresult.append(blnks[k])
        
total=len(topresult)
print("\nTotal result size:"+str(total))
i=0
print("The results are:")
for j in topresult:
    print(str(i)+' '+j)
    i=i+1
    
choice=str(input('do you want to open a link(y or n):'))

if choice=='y' or choice=='Y':
    ln=int(input('Enter the link number:'))
    if ln>=0 and ln<len(topresult):
        webbrowser.open(topresult[ln])
    else:
        print('Index out of range')
        

