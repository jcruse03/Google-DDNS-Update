#!/bin/bash
rc-service ddns-update.service stop
cp ddns-update /usr/bin/ | echo
chmod 744 /usr/bin/ddns-update | echo
cp -n ddns-update.openrcservice /etc/init.d/ | echo
mv /etc/init.d/ddns-update.openrcservice /etc/init.d/ddns-update.service | echo
cp -n ddns-update.conf /etc/ | echo
rc-service ddns-update.service start | echo
echo Done!