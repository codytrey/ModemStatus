#! /bin/bash

source virtenv/bin/activate

i=0
while true; do
    python ModemStatus/Examples/Update_All/update_all.py /tmp/modemstatus/modem.db
    sleep $PERIOD
    if [[ $i == 5 ]]; then
        python ModemStatus/Examples/Graph_Stats.py /tmp/modemstatus/modem.db
        i=0
    else:
        i=$((i+1)
done