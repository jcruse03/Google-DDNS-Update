# Google-DDNS-Update
Simple Google Domains DDNS Public IP Updater

A simple tool that keeps a dynamic dns record updated
on Google Domains. It checks for a change in your public ip at an
interval TICKTIME and if it sees a change an update request is sent
to Google Domains.

-------installation---------

---All---
1. Download the repo. Make sure ddns-update.py is where you want it permanently.
2. Edit the user config section of ddns-update.py. You will need a ddns synthetic
record already set up on google domains. Your credentials will be found in each individual 
record. Do not set TICKTIME too low or you will cause repeated duplicate requests 
to google domains as dns servers need time to update.

---Linux---
  
This will start ddns-update.py at boot and run it as a daemon.

1. Update permissions of ddns-update.py.
```bash
$ sudo chmod 755 /path-to/ddns-update.py
```
2. Edit path to ddns-update.py in the ddns-update.service file on the line beginning with
"ExecStart" in the ddns-update.service file.
ie: "ExecStart=/usr/bin/python3 /path-to/ddns-update.py"
3. Move or copy ddns-update.service to /lib/systemd/system/
```bash
$ sudo mv /path-to/ddns-update.service /lib/systemd/system/
```
4. Update permissions of ddns-update.service.
```bash
$ sudo chmod 644 /lib/systemd/system/ddns-update.service
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
