import urllib.request
import urllib.parse
"""
url = 'https://www.google.com/search'
values = {'q':'Python programming tutorials'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')

req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
resp_data = resp.read()

print(resp_data)
#405 Method not allowed
"""

"""
values = {'q':'Python programming tutorials'}

data = urllib.parse.urlencode(values)
url = 'https://www.google.com/search?q=' + data
#data = data.encode('utf-8')

req = urllib.request.Request(url)

resp = urllib.request.urlopen(req)
resp_data = resp.read()

print(resp_data)
#403 forbidden
"""
values = {'q': 'python programming tutorials'}

data = urllib.parse.urlencode(values)
#print(data)

url = 'https://www.google.com/search?' + data

headers = {}
headers['User-Agent'] = "Chrome/63"
#print(f"Headers: {headers} ")
req = urllib.request.Request(url,headers=headers)
res = urllib.request.urlopen(req)
res_data = res.read()
print(res_data)