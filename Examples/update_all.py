from ModemStatus import modem

m = modem.Modem('192.168.100.1', 'arris')
m.update_all()
