# Readme
Useful if you want to know if there is a correlation between your computer dying all the time and the temperature of your cpu.

## Creating a cronjob
Logging the temperature every minute:

    crontab -e
And then append `*/1 * * * * python /absolute/path/to/temp-log/log-temp.py` to your cronjob file and save it.

## Configure
The constant `FILE` in log-temp.py has to be an _absolute_ path to your Logfile. Otherwise the cronjob will not find it.
