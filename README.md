# Readme
Useful if you want to know if there is a correlation between your computer dying all the time and the temperature of your cpu.
plot-temp.py will show a graph of the temperature of the last 24 hours. Vertical lines represent time gaps which could be interpreted as shutdowns.

## Creating a cronjob
Logging the temperature every minute (every _minute_ is mandatory if you want plot-temp.py to work correctly):

    crontab -e
And then append `*/1 * * * * python /absolute/path/to/temp-log/log-temp.py` to your cronjob file and save it.

## Configure
The constant `FILE` in log-temp.py has to be an _absolute_ path to your Logfile. Otherwise the cronjob will not find it.
