#! /bin/bash

source virtenv/bin/activate

while true; do
    python ModemStatus/Examples/Update_All/update_all.py /tmp/modem.db
    sleep $PERIOD
done