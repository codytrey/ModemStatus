import requests
import time
import datetime
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

try:
    ds1 = list(downstreamtable.children)[3]
    ds1pwr = str(list(ds1.children)[3])
    ds1pwr = ds1pwr[4:-10]
    ds1snr = str(list(ds1.children)[4])
    ds1snr = ds1snr[4:-8]
except:
    ds1pwr = ""
    ds1snr = ""

try:
    ds2 = list(downstreamtable.children)[4]
    ds2pwr = str(list(ds2.children)[3])
    ds2pwr = ds2pwr[4:-10]
    ds2snr = str(list(ds2.children)[4])
    ds2snr = ds2snr[4:-8]
except:
    ds2pwr = ""
    ds2snr = ""

try:
    ds3 = list(downstreamtable.children)[5]
    ds3pwr = str(list(ds3.children)[3])
    ds3pwr = ds3pwr[4:-10]
    ds3snr = str(list(ds3.children)[4])
    ds3snr = ds3snr[4:-8]
except:
    ds3pwr = ""
    ds3snr = ""

try:
    ds4 = list(downstreamtable.children)[6]
    ds4pwr = str(list(ds4.children)[3])
    ds4pwr = ds4pwr[4:-10]
    ds4snr = str(list(ds4.children)[4])
    ds4snr = ds4snr[4:-8]
except:
    ds4pwr = ""
    ds4snr = ""

try:
    ds5 = list(downstreamtable.children)[7]
    ds5pwr = str(list(ds5.children)[3])
    ds5pwr = ds5pwr[4:-10]
    ds5snr = str(list(ds5.children)[4])
    ds5snr = ds5snr[4:-8]
except:
    ds5pwr = ""
    ds5snr = ""

try:
    ds6 = list(downstreamtable.children)[8]
    ds6pwr = str(list(ds6.children)[3])
    ds6pwr = ds6pwr[4:-10]
    ds6snr = str(list(ds6.children)[4])
    ds6snr = ds6snr[4:-8]
except:
    ds6pwr = ""
    ds6snr = ""

try:
    ds7 = list(downstreamtable.children)[9]
    ds7pwr = str(list(ds7.children)[3])
    ds7pwr = ds7pwr[4:-10]
    ds7snr = str(list(ds7.children)[4])
    ds7snr = ds7snr[4:-8]
except:
    ds7pwr = ""
    ds7snr = ""

try:
    ds8 = list(downstreamtable.children)[10]
    ds8pwr = str(list(ds8.children)[3])
    ds8pwr = ds8pwr[4:-10]
    ds8snr = str(list(ds8.children)[4])
    ds8snr = ds8snr[4:-8]
except:
    ds8pwr = ""
    ds8snr = ""

upstreamtable = list(p1.children)[13]
upstreamtable = list(upstreamtable.children)[1]
upstreamtable = list(upstreamtable.children)[3]
upstreamtable = list(upstreamtable.children)[1]

try:
    us1pwr = str(list(upstreamtable.children)[3])
    us1pwr = us1pwr[4:-10]

    upstreamtable = list(upstreamtable.children)[7]

    try:
        us2pwr = str(list(upstreamtable.children)[3])
        us2pwr = us2pwr[4:-10]

        upstreamtable = list(upstreamtable.children)[7]

        try:
            us3pwr = str(list(upstreamtable.children)[3])
            us3pwr = us3pwr[4:-10]

        except:
            us3pwr = ""

    except:
        us2pwr = ""
        us3pwr = ""

except:
    us1pwr = ""
    us2pwr = ""
    us3pwr = ""


statustabel = list(p1.children)[19]
statustabel = list(statustabel.children)[1]

uptime = list(statustabel.children)[0]
uptime = str(list(uptime.children)[1])
uptime = uptime[4:-5]

interfaceparamstable = list(soup.children)[3]

cable_if_enabled = str(list(interfaceparamstable.children)[2])
cable_if_enabled = cable_if_enabled[4:-5]

cable_if_state = str(list(interfaceparamstable.children)[4])
cable_if_state = cable_if_state[4:-5]

cable_if_speed = str(list(interfaceparamstable.children)[6])
cable_if_speed = cable_if_speed[4:-5]

cable_if_mac = str(list(interfaceparamstable.children)[8])
cable_if_mac = cable_if_mac[4:-5]

print("Upstream 1 power: " + us1pwr + " dBmV")
if len(us2pwr) > 0:
    print("Upstream 2 power: " + us2pwr + " dBmV")
if len(us3pwr) > 0:
    print("Upstream 3 power: " + us3pwr + " dBmV")
print("-----------------------------")
print("Downstream 1 power: " + ds1pwr + " dBmV")
if len(ds2pwr) > 0:
    print("Downstream 2 power: " + ds2pwr + " dBmV")
if len(ds3pwr) > 0:
    print("Downstream 3 power: " + ds3pwr + " dBmV")
if len(ds4pwr) > 0:
    print("Downstream 4 power: " + ds4pwr + " dBmV")
if len(ds5pwr) > 0:
    print("Downstream 5 power: " + ds5pwr + " dBmV")
if len(ds6pwr) > 0:
    print("Downstream 6 power: " + ds6pwr + " dBmV")
if len(ds7pwr) > 0:
    print("Downstream 7 power: " + ds7pwr + " dBmV")
if len(ds8pwr) > 0:
    print("Downstream 8 power: " + ds8pwr + " dBmV")
print("-----------------------------")
print("Downstream 1 SnR: " + ds1snr + " dB")
if len(ds2snr) > 0:
    print("Downstream 2 SnR: " + ds2snr + " dB")
if len(ds3snr) > 0:
    print("Downstream 3 SnR: " + ds3snr + " dB")
if len(ds4snr) > 0:
    print("Downstream 4 SnR: " + ds4snr + " dB")
if len(ds5snr) > 0:
    print("Downstream 5 SnR: " + ds5snr + " dB")
if len(ds6snr) > 0:
    print("Downstream 6 SnR: " + ds6snr + " dB")
if len(ds7snr) > 0:
    print("Downstream 7 SnR: " + ds7snr + " dB")
if len(ds8snr) > 0:
    print("Downstream 8 SnR: " + ds8snr + " dB")
print("-----------------------------")
print("Uptime: " + uptime)
print("Cable Interface Enable: " + cable_if_enabled)
print("Cable Interface State: " + cable_if_state)
print("Cable Interface Speed: " + cable_if_speed)
print("Cable Interface MAC Address: " + cable_if_mac)
print("Date Time: " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
