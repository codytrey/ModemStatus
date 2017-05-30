import requests
from bs4 import BeautifulSoup


r = requests.get("http://192.168.100.1/cgi-bin/status_cgi")


soup = BeautifulSoup(r.content, 'html.parser')


html = list(soup.children)[2]

body = list(html.children)[3]

wrapper = list(body.children)[1]

info = list(wrapper.children)[5]

p1 = list(info.children)[1]

downstreamtable = list(p1.children)[7]
downstreamtable = list(downstreamtable.children)[1]

ds1 = list(downstreamtable.children)[3]
ds1pwr = str(list(ds1.children)[3])
ds1pwr = ds1pwr[4:-10]
ds1snr = str(list(ds1.children)[4])
ds1snr = ds1snr[4:-8]

ds2 = list(downstreamtable.children)[4]
ds2pwr = str(list(ds2.children)[3])
ds2pwr = ds2pwr[4:-10]
ds2snr = str(list(ds2.children)[4])
ds2snr = ds2snr[4:-8]

ds3 = list(downstreamtable.children)[5]
ds3pwr = str(list(ds3.children)[3])
ds3pwr = ds3pwr[4:-10]
ds3snr = str(list(ds3.children)[4])
ds3snr = ds3snr[4:-8]

ds4 = list(downstreamtable.children)[6]
ds4pwr = str(list(ds4.children)[3])
ds4pwr = ds4pwr[4:-10]
ds4snr = str(list(ds4.children)[4])
ds4snr = ds4snr[4:-8]

ds5 = list(downstreamtable.children)[7]
ds5pwr = str(list(ds5.children)[3])
ds5pwr = ds5pwr[4:-10]
ds5snr = str(list(ds5.children)[4])
ds5snr = ds5snr[4:-8]

ds6 = list(downstreamtable.children)[8]
ds6pwr = str(list(ds6.children)[3])
ds6pwr = ds6pwr[4:-10]
ds6snr = str(list(ds6.children)[4])
ds6snr = ds6snr[4:-8]

ds7 = list(downstreamtable.children)[9]
ds7pwr = str(list(ds7.children)[3])
ds7pwr = ds7pwr[4:-10]
ds7snr = str(list(ds7.children)[4])
ds7snr = ds7snr[4:-8]

ds8 = list(downstreamtable.children)[10]
ds8pwr = str(list(ds8.children)[3])
ds8pwr = ds8pwr[4:-10]
ds8snr = str(list(ds8.children)[4])
ds8snr = ds8snr[4:-8]

upstreamtable = list(p1.children)[13]
upstreamtable = list(upstreamtable.children)[1]
upstreamtable = list(upstreamtable.children)[3]
upstreamtable = list(upstreamtable.children)[1]


us1pwr = str(list(upstreamtable.children)[3])
us1pwr = us1pwr[4:-10]

upstreamtable = list(upstreamtable.children)[7]

us2pwr = str(list(upstreamtable.children)[3])
us2pwr = us2pwr[4:-10]

upstreamtable = list(upstreamtable.children)[7]

us3pwr = str(list(upstreamtable.children)[3])
us3pwr = us3pwr[4:-10]

statustabel = list(p1.children)[19]

interfaceparamstable = list(p1.children)[23]

print("Upstream 1 power: " + us1pwr + " dBmV")
print("Upstream 2 power: " + us2pwr + " dBmV")
print("Upstream 3 power: " + us3pwr + " dBmV")
print("-----------------------------")
print("Downstream 1 power: " + ds1pwr + " dBmV")
print("Downstream 2 power: " + ds2pwr + " dBmV")
print("Downstream 3 power: " + ds3pwr + " dBmV")
print("Downstream 4 power: " + ds4pwr + " dBmV")
print("Downstream 5 power: " + ds5pwr + " dBmV")
print("Downstream 6 power: " + ds6pwr + " dBmV")
print("Downstream 7 power: " + ds7pwr + " dBmV")
print("Downstream 8 power: " + ds8pwr + " dBmV")
print("-----------------------------")
print("Downstream 1 SnR: " + ds1snr + " dB")
print("Downstream 2 SnR: " + ds2snr + " dB")
print("Downstream 3 SnR: " + ds3snr + " dB")
print("Downstream 4 SnR: " + ds4snr + " dB")
print("Downstream 5 SnR: " + ds5snr + " dB")
print("Downstream 6 SnR: " + ds6snr + " dB")
print("Downstream 7 SnR: " + ds7snr + " dB")
print("Downstream 8 SnR: " + ds8snr + " dB")