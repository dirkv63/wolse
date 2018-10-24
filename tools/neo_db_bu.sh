#!/usr/bin/env bash
source /opt/envs/flrun/bin/activate
python3 neo_action.py -a stop
python3 stop_webserver.py
python3 neo_bu.py
python3 neo_action.py -a start
sleep 60
python3 ../wolse.py &