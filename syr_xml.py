from bs4 import BeautifulSoup
import urllib.request

#open the mrss feed url
req = urllib.request.urlopen("http://www.wsj.com/xml/rss/3_7085.xml")

#print(req.read())

xml = BeautifulSoup(req, 'xml')

for item in xml.findAll('link')[3:]:
    url = item.text
    print(url)
    news = urllib.request.urlopen(url)

    #news = urllib.request.urlopen(item.text)
    print(news.read())
    print(20*"#")

"""
url = item.text
print(url)
news = urllib.request.urlopen(url)
print(news.read())
print(20*"#")
"""


#req1 = urllib.request.urlopen("https://www.wsj.com/articles/north-and-south-korea-will-meet-against-backdrop-of-nuclear-threats-1515153657?mod=fox_australian")
#print(req1.read())