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
#improvemtn, add 404 code chck of the main url, unit test, url arsing improve for params etc...

#main method
def __init__():
    
    url = "http://network.civilservicelive.com"
    url_temp = urlparse(url)
    mainnetloc = url_temp.netloc
    urlList = []
    
    getPage(url)
    get_hyperlinks(url, mainnetloc, urlList)
    getLocalUrl(urlList, mainnetloc)

    for address in urlList:
        print address


#save web-page in a file
def getPage(url):
    
    if url.endswith("/"):
        url = url[:-1]
        
    req = urllib2.Request(url)       
    response = urllib2.urlopen(req)

    f = file("myfile.html", "w")
    f.write(response.read())
    f.close()
 
#search all urls_href
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
  
            if finalmatch not in urlList:
                urlList.append(str(finalmatch))
                

def getLocalUrl(urlList, mainnetloc):
    for address in urlList[:]:
        tmpaddress = urlparse(address)
        if tmpaddress.netloc != mainnetloc:
            urlList.remove(address)
       
      
 
    #convert them from relative to absolute addresses
    
    #exclude the external match
    
    #print for each of them the match and the response 


if __name__ == "__main__":
    __init__()
        
    
