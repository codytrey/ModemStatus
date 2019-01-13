import sqlite3
import os


class ModemDB:
    def __init__(self, file):
        if os.path.isfile(file):
            self.conn = sqlite3.connect(file)
        else:
            self.conn = sqlite3.connect(file)
            c = self.conn.cursor()
            c.execute('''CREATE TABLE downstream (ds1pwr text, ds1snr text,
            ds2pwr text, ds2snr text, ds3pwr text, ds3snr text, ds4pwr text, ds4snr text,
            ds5pwr text, ds5snr text, ds6pwr text, ds6snr text, ds7pwr text, ds7snr text,
            ds8pwr text, ds8snr text, date integer)''')
            c.execute('''CREATE TABLE upstream (us1pwr text, us2pwr text, us3pwr text, date integer)''')
            c.execute('''CREATE TABLE status (uptime text, cable_if_enabled text, cable_if_state text, date integer)''')
            self.conn.commit()

    def update_status(self, uptime, ifenabled, ifstate, date):
        v = (uptime, ifenabled, ifstate, date,)
        c = self.conn.cursor()
        c.execute("INSERT INTO status VALUES (?, ?, ?, ?)", v)
        self.conn.commit()

    def update_upstream(self, us1pwr, us2pwr, us3pwr, date):
        v = (us1pwr, us2pwr, us3pwr, date,)
        c = self.conn.cursor()
        c.execute("INSERT INTO upstream VALUES (?, ?, ?, ?)", v)
        self.conn.commit()

    def update_downstream(self, ds1pwr, ds1snr, ds2pwr, ds2snr, ds3pwr, ds3snr, ds4pwr, ds4snr, ds5pwr, ds5snr, ds6pwr, ds6snr, ds7pwr, ds7snr, ds8pwr, ds8snr, date):
        v = (ds1pwr, ds1snr, ds2pwr, ds2snr, ds3pwr, ds3snr, ds4pwr, ds4snr, ds5pwr, ds5snr, ds6pwr, ds6snr, ds7pwr, ds7snr, ds8pwr, ds8snr, date,)
        c = self.conn.cursor()
        c.execute("INSERT INTO downstream VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", v)
        self.conn.commit()

    def __del__(self):
        self.conn.close()
