from bs4 import BeautifulSoup
import time
import urllib3
from mysqldbconnect import sqldbconnect


url='http://www.wsj.com/xml/rss/3_7085.xml'
#opent the rss feed url
http = urllib3.PoolManager()
req=http.request('GET',url)
data=req.data
#print(data)

xml=BeautifulSoup(req.data,'xml')

c, conn = sqldbconnect()

for item in xml.findAll('link')[3:]:
    text= item.text

#    c.execute("INSERT INTO rssfeed (time,link) VALUES (%s,%s)",(time.time(),text))
#    conn.commit()
    queryresults=c.execute("select * from rssfeed where link = (%s)",text)
    rows=c.fetchall()
    print(rows)
conn.close()
