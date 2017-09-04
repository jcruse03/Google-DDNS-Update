# Google-DDNS-Update
Simple Google Domains DDNS Public IP Updater

A simple tool that keeps dynamic dns records updated
on Google Domains. It checks for a change in your public ip at an
interval and if it sees a change an update request is sent
to Google Domains.

-------installation---------

---All---
1. Download and extract the repo.

---Linux---
  
This will start ddns-update.py at boot and run it as a daemon.
1. cd into the directory where you extracted the repo.
2. Update permissions of setup.sh.
```bash
$ sudo chmod 755 setup.sh
```
3. Run setup.sh with sudo.
```bash
$ sudo setup.sh
```
4. Edit the ddns-update.conf file in /etc/ 
  You must have a ddns synthetic record already set up on google domains. 
  Your credentials will be found in each individual record. Click the dropdown arrow then clcik 'view credentials'.
  Each record should be on a single line with each element seperated by a single space.
```bash
subdomain.domain.com google-ddns-username google-ddns-password
```  
```bash
$ sudo nano /etc/ddns-update.conf
```
5. Configure systemd.
```bash
$ sudo systemctl daemon-reload
$ sudo systemctl enable ddns-update.service
$ sudo systemctl start ddns-update.service
```

You should now have ddns-update.py running as a daemon and it will start at boot.
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

