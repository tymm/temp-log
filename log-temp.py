from subprocess import Popen, PIPE
from shlex import split
import re
import time

FILE = "temp.log"

def get_temp():
    command = "acpi -t"
    r = Popen(split(command), stdout=PIPE).communicate()[0]
    # Just look for the first temperature
    return re.search("(?<=0: ok, )\d+.\d", r).group(0)

with open(FILE, "a") as f:
    f.write(str(int(time.time())) + " " + get_temp() + "\n")
