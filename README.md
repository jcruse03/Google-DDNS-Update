# Google-DDNS-Update
Simple Google Domains DDNS Public IP Updater

A simple tool that keeps dynamic dns records updated
on Google Domains.

## -------Installation--------

## ---Linux---

This will start ddns-update.py at boot and run it as a daemon.

*If updating or reinstalling follow steps 1-4. Your /etc/ddns-update.conf file will not be modified.*
1. Download and extract or clone the repo.
2. cd into the directory where you extracted the repo.
3. Update permissions of setup.sh.
```bash
$ sudo chmod 744 setup.sh
```
4. Run setup.sh with sudo.
```bash
$ sudo ./setup.sh
```
*The downloaded repo files are no longer needed at this point and can be deleted.*

*If updating or reinstalling you are done.*

5. Edit the config file at /etc/ddns-update.conf
  You must have at least 1 ddns synthetic record already set up on google domains. 
  Your credentials will be found in each individual record. Click the dropdown arrow then click 'view credentials'.
  Each record should be on a single line with each element seperated by a single space in the following format.
```bash
subdomain.domain.com google-ddns-username google-ddns-password
```  
```bash
$ sudo nano /etc/ddns-update.conf
```
6. Configure systemd.
```bash
$ sudo systemctl daemon-reload
$ sudo systemctl enable ddns-update.service
$ sudo systemctl start ddns-update.service
```

You should now have ddns-update.py running as a daemon and it will start at boot.

The downloaded repo and files can be deleted.

You can check the status of the service with:
```bash
$ sudo systemctl status ddns-update.service
```

If you edit /etc/ddns-update.conf after the initial setup just make sure to restart the service.
```bash
$ sudo systemctl stop ddns-update.service
$ sudo systemctl start ddns-update.service
```

You can also view the log file at /var/log/ddns-update.log or using tail.
```bash
$ tail -f /var/log/ddns-update.log
```


## ---Mac OSX---

This will start ddns-update.py at boot and run it as a daemon.

*If updating or reinstalling follow steps 1-4 and see reloading the service at the end. Your /etc/ddns-update.conf file will not be modified.*
1. Download and extract or clone the repo.
2. cd into the directory where you extracted the repo.
3. Run mac-setup.sh with sudo.
```bash
$ sudo ./mac-setup.sh
```
*The downloaded repo files are no longer needed at this point and can be deleted.*

*If updating or reinstalling go to step 5. Your /etc/ddns-update.conf has no been modified.*

4. Edit the config file at /etc/ddns-update.conf
  You must have at least 1 ddns synthetic record already set up on google domains. 
  Your credentials will be found in each individual record. Click the dropdown arrow then click 'view credentials'.
  Each record should be on a single line with each element seperated by a single space in the following format.
```bash
subdomain.domain.com google-ddns-username google-ddns-password
```  
```bash
$ sudo nano /etc/ddns-update.conf
```
5. Configure launchctl.
*Fresh install just start the service.*
```bash
$ sudo launchctl load /Library/LaunchDaemons/ddns-update.plist
```

*For update or reinstall restart the service.*
```bash
$ sudo launchctl unload /Library/LaunchDaemons/ddns-update.plist
$ sudo launchctl load /Library/LaunchDaemons/ddns-update.plist
```

You should now have ddns-update.py running as a daemon and it will start at boot.

The downloaded repo and files can be deleted.


If you edit /etc/ddns-update.conf after the initial setup just make sure to restart the service.
```bash
$ sudo launchctl unload /Library/LaunchDaemons/ddns-update.plist
$ sudo launchctl load /Library/LaunchDaemons/ddns-update.plist
```

You can also view the log file at /var/log/ddns-update.log or using tail.
```bash
$ tail -f /var/log/ddns-update.log
```

