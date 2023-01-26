#!/bin/bash

port=(20 21 8728)

for i in "${port[@]}"
do :
masscan 192.168.0.0/24 -p$i -oJ ./$i.json --max-rate 1000 --open-only
if [$port == 8728]
then 
python3 ./mikrotik.py
fi


done
