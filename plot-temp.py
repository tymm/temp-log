import matplotlib.pyplot as plt

FILE = "temp.log"

x = []
y = []

with open(FILE) as f:
    for line in f:
        x.append(line.split(" ")[0])
        y.append(line.split(" ")[1])

plt.plot(x,y, "ro")
plt.xlabel("time")
plt.ylabel("temperature")
plt.show()
