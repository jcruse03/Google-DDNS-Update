# Google-DDNS-Update
Simple Google Domains DDNS Public IP Updater

A simple tool that keeps dynamic dns records updated
on Google Domains.

-------installation---------
---Linux---
This will start ddns-update.py at boot and run it as a daemon.
*If updating or reinstalling see below.*
1. Download and extract the repo.
2. cd into the directory where you extracted the repo.
3. Update permissions of setup.sh.
```bash
$ sudo chmod 755 setup.sh
```
4. Run setup.sh with sudo.
```bash
$ sudo ./setup.sh
```
(the downloaded repo files are no longer needed at this point and can be deleted)
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

If you update /etc/ddns-update.conf after the initial setup just make sure to restart the service.
```bash
$ sudo systemctl stop ddns-update.service
$ sudo systemctl start ddns-update.service
```

You can also view the log file at /var/log/ddns-update.log

------Updating/reinstalling------
*Your config file at /etc/ddns-update.conf will not be modified*
1. Follow steps 1-3 in the installation section.
2. Stop the service if it is running.
```bash
$ sudo systemctl stop ddns-update.service
```
3. Run setup.sh with sudo.
```bash
$ sudo ./setup.sh
```
4. Start the service back up.
```bash
$ sudo systemctl start ddns-update.service
```
