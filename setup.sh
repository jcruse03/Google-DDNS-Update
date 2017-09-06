#!/bin/bash
cp ddns-update.py /usr/bin/ | echo
cp ddns-update.service /lib/systemd/system/ | echo
cp -n ddns-update.conf /etc/ | echo
