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
    g = open('myurl','w')
    

    
    #search all url
def get_hyperlinks(url, source): 
    
    if url.endswith("/"):
        url = url[:-1]
    
     urlPat = re.compile(r'<a [^<>]*?href=("|\')([^<>"\']*?)("|\')')
    
     result = re.findall(urlPat, source)
    
     urlList = []
    
     for item in result:
         link = item[1]     
         if link.startswith("http://") and link.startswith(url):
             if link not in urlList:
                 urlList.append(link)
         elif link.startswith("/"):
             link = url + link
             if link not in urlList:
                 urlList.append(link)
         else:
             link = url + "/" + link
             if link not in urlList:
                 urlList.append(link)
     
     return urlList
    
    print "Enter the URL: "
    url = raw_input("> ")
    usock = urllib2.urlopen(url)
    data = usock.read()
    usock.close()
    print get_hyperlinks(url, data)
    
    #convert them from relative to absolute addresses
    
    #exclude the external link
    
    #print for each of them the link and the response
      
   
    
 

        
    
