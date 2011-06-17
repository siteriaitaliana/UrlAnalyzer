import urllib2
from tempfile import *


def getPage():
    url = "http://network.civilservicelive.com"
    req = urllib2.Request(url)       
    response = urllib2.urlopen(req)
    return  response.read()

if __name__ == "__main__":
    namesPage = getPage()
    

    f = file("myfile.html", "w+")
    f.write(namesPage)
    f.close()
    
    f = open('myfile.html','r')
    print f.read()
    f.close()
    
 

        
    
