#!/bin/bash
cp ddns-update.py /usr/bin/ | echo
cp ddns-update.service /lib/systemd/system/ | echo
cp ddns-update.conf /etc/ | echo