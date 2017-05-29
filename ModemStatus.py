import requests
from bs4 import BeautifulSoup


r = requests.get("http://192.168.100.1/cgi-bin/status_cgi")

#print(r.text)

soup = BeautifulSoup(r.content, 'html.parser')

#print(soup.prettify())

#list(soup.children)

#[type(item) for item in list(soup.children)]

html = list(soup.children)[2]

body = list(html.childern)[3]

wrapper = list(body.children)[1]

info = list(wrapper.children)[5]

p1 = list(info.children)[1]

downstreamtable = list(p1.children)[7]

downstreamtable = list(downstreamtable.children)[1]

ds1 = list(downstreamtable.children)[3]
ds2 = list(downstreamtable.children)[4]
ds3 = list(downstreamtable.children)[5]
ds4 = list(downstreamtable.children)[6]
ds5 = list(downstreamtable.children)[7]
ds6 = list(downstreamtable.children)[8]
ds7 = list(downstreamtable.children)[9]
ds8 = list(downstreamtable.children)[10]

upstreamtable = list(p1.children)[13]

statustabel = list(p1.children)[19]

interfaceparamstable = list(p1.children)[23]