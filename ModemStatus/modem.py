import requests
import time
import datetime
import json
import os
from bs4 import BeautifulSoup
from .exeptions import InvalidVendor
from .db import ModemDB


def url_for_vendor(vendor, ip):

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"modem_vendors.json"), 'r') as f:
        vendor_list = json.load(f)
    if vendor in vendor_list["supported_list"]:
        for i in vendor_list["vendor_details"]:
            if i['name'] == vendor:
                return i['proto'] + '://' + ip + i['uri']
    else:
        raise InvalidVendor("Vendor " + vendor + " is unknown and not yet supported.")


class Modem:
    def __init__(self, ip, vendor, dbfile=None):
        self.ip = ip
        self.vendor = vendor
        self.url = url_for_vendor(self.vendor, self.ip)
        self.p1 = None
        self.p1_updatetime = None
        self.soup = None
        self.downstreamttalbe = None
        self.upstreamtable = None
        if dbfile is None:
            self.db = ModemDB(str(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "modem.db")))
        else:
            self.db = ModemDB(dbfile)

    def status_cgi(self):
        r = requests.get("http://192.168.100.1/cgi-bin/status_cgi")
        self.soup = BeautifulSoup(r.content, 'html.parser')
        html = list(self.soup.children)[2]
        body = list(html.children)[3]
        wrapper = list(body.children)[1]
        info = list(wrapper.children)[5]
        self.p1 = list(info.children)[1]
        self.p1_updatetime = datetime.datetime.now()

    def downstreamtbl(self):
        if self.p1_updatetime is None or datetime.datetime.now() - self.p1_updatetime > datetime.timedelta(minutes=5):
            self.status_cgi()
        downstreamtable = list(self.p1.children)[7]
        downstreamtable = list(downstreamtable.children)[1]
        try:
            ds1 = list(downstreamtable.children)[3]
            ds1pwr = str(list(ds1.children)[3])[4:-10]
            ds1snr = str(list(ds1.children)[4])[4:-8]
        except:
            ds1pwr = ""
            ds1snr = ""
        try:
            ds2 = list(downstreamtable.children)[4]
            ds2pwr = str(list(ds2.children)[3])[4:-10]
            ds2snr = str(list(ds2.children)[4])[4:-8]
        except:
            ds2pwr = ""
            ds2snr = ""
        try:
            ds3 = list(downstreamtable.children)[5]
            ds3pwr = str(list(ds3.children)[3])[4:-10]
            ds3snr = str(list(ds3.children)[4])[4:-8]
        except:
            ds3pwr = ""
            ds3snr = ""

        try:
            ds4 = list(downstreamtable.children)[6]
            ds4pwr = str(list(ds4.children)[3])[4:-10]
            ds4snr = str(list(ds4.children)[4])[4:-8]
        except:
            ds4pwr = ""
            ds4snr = ""

        try:
            ds5 = list(downstreamtable.children)[7]
            ds5pwr = str(list(ds5.children)[3])[4:-10]
            ds5snr = str(list(ds5.children)[4])[4:-8]
        except:
            ds5pwr = ""
            ds5snr = ""

        try:
            ds6 = list(downstreamtable.children)[8]
            ds6pwr = str(list(ds6.children)[3])[4:-10]
            ds6snr = str(list(ds6.children)[4])[4:-8]
        except:
            ds6pwr = ""
            ds6snr = ""

        try:
            ds7 = list(downstreamtable.children)[9]
            ds7pwr = str(list(ds7.children)[3])[4:-10]
            ds7snr = str(list(ds7.children)[4])[4:-8]
        except:
            ds7pwr = ""
            ds7snr = ""

        try:
            ds8 = list(downstreamtable.children)[10]
            ds8pwr = str(list(ds8.children)[3])[4:-10]
            ds8snr = str(list(ds8.children)[4])[4:-8]
        except:
            ds8pwr = ""
            ds8snr = ""
        self.db.update_downstream(ds1pwr, ds1snr, ds2pwr, ds2snr, ds3pwr, ds3snr, ds4pwr, ds4snr, ds5pwr,
                                  ds5snr, ds6pwr, ds6snr, ds7pwr, ds7snr, ds8pwr, ds8snr,
                                  datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

    def upstreamtbl(self):
        if self.p1_updatetime is None or datetime.datetime.now() - self.p1_updatetime > datetime.timedelta(minutes=5):
            self.status_cgi()
        self.upstreamtable = list(self.p1.children)[13]
        self.upstreamtable = list(self.upstreamtable.children)[1]
        self.upstreamtable = list(self.upstreamtable.children)[3]
        self.upstreamtable = list(self.upstreamtable.children)[1]

        try:
            us1pwr = str(list(self.upstreamtable.children)[3])
            us1pwr = us1pwr[4:-10]

            self.upstreamtable = list(self.upstreamtable.children)[7]

            try:
                us2pwr = str(list(self.upstreamtable.children)[3])
                us2pwr = us2pwr[4:-10]

                self.upstreamtable = list(self.upstreamtable.children)[7]

                try:
                    us3pwr = str(list(self.upstreamtable.children)[3])
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
        self.db.update_upstream(us1pwr, us2pwr, us3pwr,
                                datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

    def statustbl(self):
        if self.p1_updatetime is None or datetime.datetime.now() - self.p1_updatetime > datetime.timedelta(minutes=5):
            self.status_cgi()
        statustabel = list(self.p1.children)[19]
        statustabel = list(statustabel.children)[1]

        uptime = list(statustabel.children)[0]
        uptime = str(list(uptime.children)[1])
        uptime = uptime[4:-5]

        interfaceparamstable = list(self.soup.children)[3]

        cable_if_enabled = str(list(interfaceparamstable.children)[2])
        cable_if_enabled = cable_if_enabled[4:-5]

        cable_if_state = str(list(interfaceparamstable.children)[4])
        cable_if_state = cable_if_state[4:-5]

        self.db.update_status(uptime, cable_if_enabled, cable_if_state,
                              datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

    def update_all(self):
        self.statustbl()
        self.upstreamtbl()
        self.downstreamtbl()
