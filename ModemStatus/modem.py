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
        self.p2 = None
        self.p2_updatetime = None
        self.soup = None
        self.soup2 = None
        self.downstreamttalbe = None
        self.upstreamtable = None
        if dbfile is None:
            self.db = ModemDB(str(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "modem.db")))
        else:
            self.db = ModemDB(dbfile)

    def cm_state_cgi(self):
        r = requests.get(self.url + "cm_state_cgi")
        self.soup2 = BeautifulSoup(r.content, 'html.parser')
        html = list(self.soup2.children)[2]
        body = list(html.children)[3]
        wrapper = list(body.children)[1]
        info = list(wrapper.children)[5]
        self.p2 = list(info.children)[1]
        self.p2_updatetime = datetime.datetime.now()

    def cm_statetbl(self):
        if self.p2_updatetime is None or datetime.datetime.now() - self.p2_updatetime > datetime.timedelta(minutes=5):
            self.cm_state_cgi()

        status_table = list(self.p2.children)[7]
        status_table = list(status_table.children)[1]

        downstream_scanning = list(status_table.children)[1]
        downstream_scanning = str(str(list(downstream_scanning.children)[3]).split('>')[1]).split('<')[0]

        downstream_ranging = list(status_table.children)[3]
        downstream_ranging = str(str(list(downstream_ranging.children)[3]).split('>')[1]).split('<')[0]

        upstream_ranging = list(status_table.children)[5]
        upstream_ranging = str(str(list(upstream_ranging.children)[3]).split('>')[1]).split('<')[0]

        dhcp = list(status_table.children)[7]
        dhcp = str(str(list(dhcp.children)[3]).split('>')[1]).split('<')[0]

        tftp = list(status_table.children)[9]
        tftp = str(str(list(tftp.children)[3]).split('>')[1]).split('<')[0]

        data_reg = list(status_table.children)[11]
        data_reg = str(str(list(data_reg.children)[3]).split('>')[1]).split('<')[0]

        ToD = list(self.p2.children)[13]
        ToD = list(ToD.children)[1]
        ToD = list(ToD.children)[1]
        ToD = str(str(list(ToD.children)[3]).split('>')[1]).split('<')[0]

        BPI_status = list(self.p2.children)[19]
        BPI_status = list(BPI_status.children)[1]
        BPI_status = list(BPI_status.children)[1]
        BPI_status = str(str(list(BPI_status.children)[3]).split('>')[1]).split('<')[0]

    def status_cgi(self):
        r = requests.get(self.url + "status_cgi")
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
            ds1pwr = "0.0"
            ds1snr = "0.0"
        try:
            ds2 = list(downstreamtable.children)[4]
            ds2pwr = str(list(ds2.children)[3])[4:-10]
            ds2snr = str(list(ds2.children)[4])[4:-8]
        except:
            ds2pwr = "0.0"
            ds2snr = "0.0"
        try:
            ds3 = list(downstreamtable.children)[5]
            ds3pwr = str(list(ds3.children)[3])[4:-10]
            ds3snr = str(list(ds3.children)[4])[4:-8]
        except:
            ds3pwr = "0.0"
            ds3snr = "0.0"

        try:
            ds4 = list(downstreamtable.children)[6]
            ds4pwr = str(list(ds4.children)[3])[4:-10]
            ds4snr = str(list(ds4.children)[4])[4:-8]
        except:
            ds4pwr = "0.0"
            ds4snr = "0.0"

        try:
            ds5 = list(downstreamtable.children)[7]
            ds5pwr = str(list(ds5.children)[3])[4:-10]
            ds5snr = str(list(ds5.children)[4])[4:-8]
        except:
            ds5pwr = "0.0"
            ds5snr = "0.0"

        try:
            ds6 = list(downstreamtable.children)[8]
            ds6pwr = str(list(ds6.children)[3])[4:-10]
            ds6snr = str(list(ds6.children)[4])[4:-8]
        except:
            ds6pwr = "0.0"
            ds6snr = "0.0"

        try:
            ds7 = list(downstreamtable.children)[9]
            ds7pwr = str(list(ds7.children)[3])[4:-10]
            ds7snr = str(list(ds7.children)[4])[4:-8]
        except:
            ds7pwr = "0.0"
            ds7snr = "0.0"

        try:
            ds8 = list(downstreamtable.children)[10]
            ds8pwr = str(list(ds8.children)[3])[4:-10]
            ds8snr = str(list(ds8.children)[4])[4:-8]
        except:
            ds8pwr = "0.0"
            ds8snr = "0.0"
        self.db.update_downstream(ds1pwr, ds1snr, ds2pwr, ds2snr, ds3pwr, ds3snr, ds4pwr, ds4snr, ds5pwr,
                                  ds5snr, ds6pwr, ds6snr, ds7pwr, ds7snr, ds8pwr, ds8snr,
                                  datetime.datetime.fromtimestamp(time.time(), datetime.timezone.utc).timestamp())
        #                         datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

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
                    us3pwr = "0.0"

            except:
                us2pwr = "0.0"
                us3pwr = "0.0"

        except:
            us1pwr = "0.0"
            us2pwr = "0.0"
            us3pwr = "0.0"
        self.db.update_upstream(us1pwr, us2pwr, us3pwr,
                                datetime.datetime.fromtimestamp(time.time(), datetime.timezone.utc).timestamp())
        #                       datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

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
                              datetime.datetime.fromtimestamp(time.time(), datetime.timezone.utc).timestamp())
        #                     datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

    def update_all(self):
        self.statustbl()
        self.upstreamtbl()
        self.downstreamtbl()
