#!/bin/bash
launchctl stop /Library/LaunchDaemons/ddns-update.plist | echo
cp ddns-update.py /usr/local/bin/ | echo
cp -n ddns-update.plist /Library/LaunchDaemons/ | echo
cp -n ddns-update.conf /etc/ | echo
launchctl start /Library/LaunchDaemons/ddns-update.plist | echo
echo Done!
