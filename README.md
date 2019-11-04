SystemMonitor
====================================

SystemMonitor is a project to store metrics like CPU or network usage from a system like the Raspberry Pi. The script was written and tested in Python 3.7.4.

[![Build status](https://ci.appveyor.com/api/projects/status/557yvbhg4q3bqxjm?svg=true)](https://ci.appveyor.com/project/SeppPenner/systemmonitor)
[![GitHub issues](https://img.shields.io/github/issues/SeppPenner/SystemMonitor.svg)](https://github.com/SeppPenner/SystemMonitor/issues)
[![GitHub forks](https://img.shields.io/github/forks/SeppPenner/SystemMonitor.svg)](https://github.com/SeppPenner/SystemMonitor/network)
[![GitHub stars](https://img.shields.io/github/stars/SeppPenner/SystemMonitor.svg)](https://github.com/SeppPenner/SystemMonitor/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://raw.githubusercontent.com/SeppPenner/SystemMonitor/master/License.txt)
[![Known Vulnerabilities](https://snyk.io/test/github/SeppPenner/SystemMonitor/badge.svg)](https://snyk.io/test/github/SeppPenner/SystemMonitor) 

# Steps to use this project:
1. Make sure to install Python and Pip correctly
2. Set the execute flags:

```bash
chmod +x install.sh
chmod +x run.sh
chmod +x monitor.py
```

3. Install all required pip package dependencies with:

```bash
pip install -r requirements.txt
```

4. Setup a MySQL database server and run the scripts `SetupProcedures.sql` and `SetupTables.sql` inside the database.

5. Adjust your settings in the [monitor.py](https://github.com/SeppPenner/SystemMonitor/blob/master/monitor.py) file:

```python
databaseUser = 'default'
databasePassword = 'asdf'
databaseName = 'SystemMonitor'
hostAddress = '192.168.2.2'
databasePort = 3307
```

6. Probably run this script in a cronjob:
```bash
sudo crontab -e
```

and add e.g. the line

```bash
* * * * * /usr/bin/python3 /home/SystemMonitor/monitor.py
```

to execute the script every minute.

# For more information see:
* https://github.com/giampaolo/psutil/
* https://psutil.readthedocs.io/en/latest/#memory

Change history
--------------

* **Version 1.0.0.1 (2019-09-29)** : Updated python version, updated requirements.
* **Version 1.0.0.0 (2019-03-03)** : 1.0 release.
