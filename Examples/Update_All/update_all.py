from ModemStatus import modem
import sys

if len(sys.argv) == 2:
    dbfile = sys.argv[1]
elif len(sys.argv) < 2:
    dbfile = None
else:
    print("Expects 0 or 1 positional arguments")
    exit(2)

if dbfile is None:
    m = modem.Modem('192.168.100.1', 'arris')
else:
    m = modem.Modem('192.168.100.1', 'arris', dbfile)

m.update_all()
