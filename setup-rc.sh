#!/bin/bash
cp ddns-update /usr/bin/ | echo
chmod 744 /usr/bin/ddns-update | echo
cp -n ddns-update.openrcservice /etc/init.d/ | echo
mv /etc/init.d/ddns-update.openrcservice /etc/init.d/ddns-update.service | echo
chmod 744 /etc/init.d/ddns-update.service
cp -n ddns-update.conf /etc/ | echo
rc-update add ddns-update.service boot
echo Done!
echo update your config file at /etc/ddns-update.conf and start the service
echo To start the service run the following command:
echo rc-service ddns-update.service start
