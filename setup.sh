#!/bin/bash
systemctl stop ddns-update.service
cp ddns-update.py /usr/bin/ | echo
cp -n ddns-update.service /lib/systemd/system/ | echo
cp -n ddns-update.conf /etc/ | echo
systemctl start ddns-update.service
echo Done!
