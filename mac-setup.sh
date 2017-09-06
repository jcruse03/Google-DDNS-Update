#!/bin/bash
cp ddns-update.py /usr/local/bin/ | echo
cp -n ddns-update.plist /Library/LaunchDaemons/ | echo
cp -n ddns-update.conf /etc/ | echo
echo Done!
