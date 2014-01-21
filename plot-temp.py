import matplotlib.pyplot as plt
import numpy as np

FILE = "temp.log"

# Logging intervall in seconds
LOGGING_INTERVALL = 60

x = []
y = []

with open(FILE) as f:
    for line in f:
        x.append(int(line.split(" ")[0]))
        y.append(float(line.split(" ")[1].strip("\n")))

# Let's see where we have time gaps and mark them as possible shutdowns
index_of_shutdowns= []
tmp = x[0]
for i, time in enumerate(x[1:]):
    if tmp + LOGGING_INTERVALL + 5 < time:
        # Possible shutdown before timepoint x[i+1]
        index_of_shutdowns.append(i+1)
    tmp = time

# Create new x and y-axis where every shutdown are two 0 values on the y-axis
x_new = []
y_new = []
time = 0
last_shutdown = 0

for shutdown in index_of_shutdowns:
    for y_value in y[:shutdown]:
        x_new.append(time)
        time += 1
        y_new.append(y_value)
    # Insert a vertical line to represent a possible shutdown
    y_new.append(np.mean(y_new))
    x_new.append(time)
    plt.axvline(time, ymin=0, ymax=1)
    time += 1
    last_shutdown = shutdown

# Now we got everything until the last shutdown
# Lets add everything from the last shutdown to now
for y_value in y[last_shutdown:]:
    x_new.append(time)
    time += 1
    y_new.append(y_value)

# Only plot the last 24 hours
plt.plot(x_new[-1440:], y_new[-1440:])
plt.xlabel("time")
plt.ylabel("temperature")
plt.show()
