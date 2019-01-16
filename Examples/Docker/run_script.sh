#! /bin/bash

source virtenv/bin/activate

pushd /tmp/modemstatus

i=0
while true; do
    python /tmp/update_all.py /tmp/modemstatus/modem.db
    sleep $PERIOD
    ((i=i+1))
    if [ $i == 5 ]; then
        python /tmp/graph_stats.py /tmp/modemstatus/modem.db
        i=0
    fi
done

popd