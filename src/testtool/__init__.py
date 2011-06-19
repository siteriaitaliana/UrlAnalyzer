import urllib2
from tempfile import *
import re
from urlparse import urlparse

"""
    print "Enter the URL: "
    url = raw_input("> ")
    usock = urllib2.urlopen(url)
    data = usock.read()
    usock.close() 
"""
#improvemts suggestions, add 404 code check of the main url, unit test, url arsing improve for params etc...

#main method
def __init__():
    
    url = "http://www.google.com"
    url_temp = urlparse(url)
    mainnetloc = url_temp.netloc
    urlList = []
    codeList = {}
    
    getPage(url)
    get_hyperlinks(url, mainnetloc, urlList)
    getLocalUrl(urlList, mainnetloc)
    getHttpStatusCode(urlList, codeList)

    for address,code in codeList.iteritems():
            print address + "\t" + code

def getPage(url):
    
    if url.endswith("/"):
        url = url[:-1]
        
    req = urllib2.Request(url)       
    response = urllib2.urlopen(req)

    f = file("myfile.html", "w")
    f.write(response.read())
    f.close()
 
def get_hyperlinks(url, mainnetloc, urlList): 
    
    f = file("myfile.html", "r")
    
    urlPat = re.compile(r'<a href=[\'"]?([^\'" >]+)')
                 
    for line in f.readlines():  
        for match in re.findall(urlPat, line):
            
            match = urlparse(match)
            
            #only parameters 
            if ((match.scheme == '' ) and (match.netloc == '') and (match.path == '')):
                finalmatch = "http://" + mainnetloc + "/" + match.params;
            
            #only path 
            elif ((match.scheme == '' ) and (match.netloc == '') and (match.params == '')):
                finalmatch = "http://" + mainnetloc + match.path;
                
            #only path and param
            elif ((match.scheme == '' ) and (match.netloc == '') and (match.params != '')):
                finalmatch = "http://" + mainnetloc + match.path + match.params;
            
            #mainhost missing    
            elif (match.netloc == ''):
                finalmatch = match.scheme + mainnetloc + match.path + match.params;
            
            #protocol missing    
            elif (match.scheme == '' ):
                finalmatch = "http://" + match.netloc + match.path + match.params;
            
            else:
                finalmatch =  match.geturl()
  
            if finalmatch not in urlList[:]:
                urlList.append(str(finalmatch))
                

def getLocalUrl(urlList, mainnetloc):
    for address in urlList[:]:
        tmpaddress = urlparse(address)
        if tmpaddress.netloc != mainnetloc:
            urlList.remove(address)

def getHttpStatusCode(urlList, codeList):
    for address in urlList[:]:
        req = urllib2.Request(address)       
        
        try:
            response = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            codeList[address]=str(e.code)             
        else:
            codeList[address]=str(response.code)


if __name__ == "__main__":
    __init__()
        
    
